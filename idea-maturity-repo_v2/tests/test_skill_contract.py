#!/usr/bin/env python3
"""Contract tests for the idea-maturity skill package.

The skill is Markdown-only, so these tests guard the behaviors that are easy to
break during editing: packaging, routing references, enum contracts, and the
main methodological invariants.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "idea-maturity"
SKILL_ROOT = PLUGIN_ROOT / "skills" / "idea-maturity"
REFERENCE_ROOT = SKILL_ROOT / "reference"
CLAUDE_ZIP_SCRIPT = ROOT / "scripts" / "build_claude_skill_zip.py"

PRIMARY_REFERENCES = {
    "input-triage.md",
    "block-problem.md",
    "block-relevance.md",
    "block-intent.md",
    "phase-hypotheses.md",
    "phase-worth.md",
}

SUPPORT_REFERENCES = {
    "template-spec.md",
    "mandate-systems.md",
    "edge-cases-and-workflows.md",
    "facilitation.md",
    "example-briefing.md",
    "glossary.md",
}

ENUMS = {
    "mandate": {"discretionary", "obligatory", "maintenance"},
    "form": {"observation", "complaint", "problem_claim", "solution_request", "hypothesis", "assignment"},
    "block_status": {"open", "partial", "complete", "not_applicable"},
    "evidence": {"unknown", "assumed", "reported", "observed", "validated"},
    "test_type": {"data_check", "fake_door", "prototype", "wizard_of_oz", "full_build_test", "other"},
    "candidate_type": {"build", "test"},
    "judgement": {"build", "test", "defer", "drop"},
}

STALE_TERMS = {
    ".claude-plugin",
    "stage-1-problem-evidence.md",
    "stage-2-problem-size.md",
    "stage-3-solution-fit.md",
    "stage-4-buildability.md",
    "stage-5-targets-and-priority.md",
    "example-card.md",
    "Use whenever someone presents something to work on",
}


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
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def validate_json_file(path: Path, errors: list[str]) -> dict:
    try:
        payload = json.loads(read(path))
    except Exception as exc:  # pragma: no cover - printed by test runner
        errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return {}
    require(isinstance(payload, dict), f"{path.relative_to(ROOT)} must contain a JSON object", errors)
    return payload if isinstance(payload, dict) else {}


def main() -> int:
    errors: list[str] = []

    skill_md_path = SKILL_ROOT / "SKILL.md"
    require(skill_md_path.is_file(), "SKILL.md exists", errors)
    skill_md = read(skill_md_path)
    frontmatter = parse_frontmatter(skill_md)
    require(frontmatter.get("name") == "idea-maturity", "frontmatter name is idea-maturity", errors)
    description = frontmatter.get("description", "")
    require(0 < len(description) <= 1024, "description is present and <= 1024 chars", errors)
    require("ordinary implementation requests" in description, "description has an invocation boundary", errors)

    all_references = PRIMARY_REFERENCES | SUPPORT_REFERENCES
    for filename in sorted(all_references):
        require((REFERENCE_ROOT / filename).is_file(), f"reference/{filename} exists", errors)
        require(f"reference/{filename}" in skill_md, f"SKILL.md routes to reference/{filename}", errors)

    linked_refs = set(re.findall(r"reference/([a-z0-9-]+\.md)", skill_md))
    require(linked_refs <= all_references, f"SKILL.md only links known references: {linked_refs - all_references}", errors)

    readme = read(ROOT / "README.md")
    changelog = read(ROOT / "CHANGELOG.md")
    combined_public_docs = "\n".join([readme, skill_md, changelog])
    for stale in STALE_TERMS:
        require(stale not in combined_public_docs, f"stale term removed: {stale}", errors)

    template = read(REFERENCE_ROOT / "template-spec.md")
    for enum_name, values in ENUMS.items():
        line = next((line for line in template.splitlines() if line.startswith(enum_name + " ")), "")
        require(line, f"enum {enum_name} is documented", errors)
        for value in values:
            require(value in line, f"enum {enum_name} includes {value}", errors)

    relevance = read(REFERENCE_ROOT / "block-relevance.md")
    require("stage 2 remains blocking" in relevance, "unknown stage-2 values remain blocking", errors)
    require("unknown -> measure first" in relevance, "stage 2 uses explicit measurement wording", errors)

    intent = read(REFERENCE_ROOT / "block-intent.md")
    require("The threshold is not the same as the user-near target" in intent, "target and worth threshold are separated", errors)
    require("threshold is `not_applicable`" in intent, "obligatory worth threshold is not_applicable", errors)

    hypotheses = read(REFERENCE_ROOT / "phase-hypotheses.md")
    require("eligible for stage 5 worth assessment" in hypotheses, "build candidate does not equal build approval", errors)
    require("confidence <= assumed" in hypotheses, "test/build candidate rule is explicit", errors)

    require("input.raw_statement" in skill_md and "problem.reformulated_from" in skill_md, "solution-free exceptions are explicit", errors)

    require("### Claude App" in readme, "README documents Claude App installation", errors)
    require("Customize > Skills > + > Upload skill" in readme, "README includes Claude upload path", errors)
    require(".claude/skills" in readme, "README documents Claude Code project-local install", errors)
    require(CLAUDE_ZIP_SCRIPT.is_file(), "Claude ZIP build script exists", errors)

    if CLAUDE_ZIP_SCRIPT.is_file():
        spec = importlib.util.spec_from_file_location("build_claude_skill_zip", CLAUDE_ZIP_SCRIPT)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "idea-maturity-claude-skill.zip"
            module.build_zip(output)
            require(output.is_file(), "Claude ZIP was created", errors)
            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())
            require("idea-maturity/SKILL.md" in names, "Claude ZIP contains top-level idea-maturity/SKILL.md", errors)
            require("idea-maturity/reference/block-intent.md" in names, "Claude ZIP contains references", errors)
            require(all(name.startswith("idea-maturity/") for name in names), "Claude ZIP has one top-level skill folder", errors)

    plugin = validate_json_file(PLUGIN_ROOT / ".codex-plugin" / "plugin.json", errors)
    require(plugin.get("name") == "idea-maturity", "plugin manifest name matches", errors)
    require(plugin.get("skills") == "./skills/", "plugin manifest points to skills directory", errors)
    require((PLUGIN_ROOT / "skills").is_dir(), "plugin skills path exists", errors)

    marketplace = validate_json_file(ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    entries = marketplace.get("plugins", []) if isinstance(marketplace.get("plugins"), list) else []
    idea_entries = [entry for entry in entries if isinstance(entry, dict) and entry.get("name") == "idea-maturity"]
    require(len(idea_entries) == 1, "marketplace has exactly one idea-maturity entry", errors)
    if idea_entries:
        require(idea_entries[0].get("source", {}).get("path") == "./plugins/idea-maturity", "marketplace source path is correct", errors)

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: idea-maturity skill contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
