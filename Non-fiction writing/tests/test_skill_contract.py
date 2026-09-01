#!/usr/bin/env python3
"""Contract tests for the Zinsser Style Guardian skill package."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "zinsser-style-guardian"
SKILL_ROOT = PLUGIN_ROOT / "skills" / "zinsser-style-guardian"
REFERENCES = {
    "style-rules.md",
    "output-modes.md",
    "editing-checklist.md",
}
PLACEHOLDERS = {"[TO" + "DO:", "TO" + "DO", "Local " + "developer", "Help me " + "use"}
MODE_TERMS = {"nur Feedback", "direkt überarbeiten", "Diagnose", "Überarbeiteter Text", "Wichtigste Änderungen"}
STYLE_TERMS = {"Klar. Knapp. Aktiv. Menschlich.", "nominalizations", "passive", "concrete", "human"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def parse_frontmatter(skill_md: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", skill_md, re.DOTALL)
    if not match:
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(read(path))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return {}
    require(isinstance(value, dict), f"{path.relative_to(ROOT)} must contain a JSON object", errors)
    return value if isinstance(value, dict) else {}


def run_command(command: list[str], errors: list[str]) -> subprocess.CompletedProcess[str] | None:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        errors.append("command failed: " + " ".join(command) + "\n" + result.stderr + result.stdout)
        return None
    return result


def validate_claude_zip(errors: list[str]) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        output = Path(tmp_dir) / "zinsser-style-guardian.zip"
        run_command([sys.executable, str(ROOT / "scripts" / "build_claude_skill_zip.py"), "--output", str(output)], errors)
        if not output.is_file():
            errors.append("Claude ZIP was not created")
            return
        with zipfile.ZipFile(output) as archive:
            names = set(archive.namelist())
        require("zinsser-style-guardian/SKILL.md" in names, "Claude ZIP contains skill folder and SKILL.md", errors)
        require("zinsser-style-guardian/references/style-rules.md" in names, "Claude ZIP contains references", errors)
        require(not any(name.startswith("SKILL.md") for name in names), "Claude ZIP does not put files at archive root", errors)
        require(not any("/agents/" in name for name in names), "Claude ZIP excludes Codex-only agents metadata", errors)


def validate_claude_code_installer(errors: list[str]) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        target_parent = Path(tmp_dir) / "skills"
        run_command(
            [
                sys.executable,
                str(ROOT / "scripts" / "install_claude_code_skill.py"),
                "--target",
                str(target_parent),
                "--force",
            ],
            errors,
        )
        installed = target_parent / "zinsser-style-guardian"
        require((installed / "SKILL.md").is_file(), "Claude Code installer copies SKILL.md", errors)
        require((installed / "references" / "output-modes.md").is_file(), "Claude Code installer copies references", errors)
        require(not (installed / "agents").exists(), "Claude Code installer excludes Codex-only agents metadata", errors)


def main() -> int:
    errors: list[str] = []

    skill_md_path = SKILL_ROOT / "SKILL.md"
    require(skill_md_path.is_file(), "SKILL.md exists", errors)
    skill_md = read(skill_md_path)
    frontmatter = parse_frontmatter(skill_md)
    require(frontmatter.get("name") == "zinsser-style-guardian", "frontmatter name matches skill directory", errors)
    description = frontmatter.get("description", "")
    require(0 < len(description) <= 200, "description is present and Claude-compatible", errors)
    require("non-fiction prose" in description, "description states invocation domain", errors)
    require("avoid for fiction" in description, "description states a routing boundary", errors)

    for filename in REFERENCES:
        require((SKILL_ROOT / "references" / filename).is_file(), f"references/{filename} exists", errors)
        require(f"references/{filename}" in skill_md, f"SKILL.md links references/{filename}", errors)

    package_text = "\n".join(read(path) for path in [skill_md_path, ROOT / "README.md", ROOT / "CHANGELOG.md"])
    for placeholder in PLACEHOLDERS:
        require(placeholder not in package_text, f"placeholder removed: {placeholder}", errors)
    for term in MODE_TERMS:
        require(term in package_text, f"output mode term is documented: {term}", errors)
    for term in STYLE_TERMS:
        require(term in package_text, f"style invariant is documented: {term}", errors)

    style_rules = read(SKILL_ROOT / "references" / "style-rules.md")
    require("Do not force active voice" in style_rules, "active voice has accuracy guardrail", errors)
    require("without inventing an actor" in style_rules, "missing actor guardrail is explicit", errors)
    require("Replace official fog with plain phrasing" in style_rules, "bureaucratic language rule is explicit", errors)

    checklist = read(SKILL_ROOT / "references" / "editing-checklist.md")
    require("no new facts" in checklist, "factual preservation is a final check", errors)

    plugin = load_json(PLUGIN_ROOT / ".codex-plugin" / "plugin.json", errors)
    require(plugin.get("name") == "zinsser-style-guardian", "plugin manifest name matches", errors)
    require(plugin.get("skills") == "./skills/", "plugin manifest points to skills", errors)
    interface = plugin.get("interface", {}) if isinstance(plugin.get("interface"), dict) else {}
    require(interface.get("displayName") == "Zinsser Style Guardian", "plugin display name is set", errors)
    require(len(interface.get("defaultPrompt", [])) == 3, "plugin has three starter prompts", errors)

    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    entries = marketplace.get("plugins", []) if isinstance(marketplace.get("plugins"), list) else []
    entries = [entry for entry in entries if isinstance(entry, dict) and entry.get("name") == "zinsser-style-guardian"]
    require(len(entries) == 1, "marketplace has one zinsser-style-guardian entry", errors)
    if entries:
        require(entries[0].get("source", {}).get("path") == "./plugins/zinsser-style-guardian", "marketplace path matches plugin", errors)
        require(entries[0].get("policy", {}).get("installation") == "AVAILABLE", "marketplace install policy is available", errors)

    validate_claude_zip(errors)
    validate_claude_code_installer(errors)

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: zinsser-style-guardian skill contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
