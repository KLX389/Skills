#!/usr/bin/env python3
"""Build a Claude-compatible ZIP archive for the Zinsser Style Guardian skill."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "zinsser-style-guardian"
SKILL_ROOT = ROOT / "plugins" / SKILL_NAME / "skills" / SKILL_NAME
DEFAULT_OUTPUT = ROOT / "dist" / f"{SKILL_NAME}-claude-skill.zip"
EXCLUDED_TOP_LEVEL = {"agents", "__pycache__"}


def read_frontmatter(skill_md: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", skill_md, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md must start with YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def validate_skill_root() -> None:
    skill_md_path = SKILL_ROOT / "SKILL.md"
    if not skill_md_path.is_file():
        raise FileNotFoundError(f"Missing {skill_md_path}")

    metadata = read_frontmatter(skill_md_path.read_text(encoding="utf-8"))
    name = metadata.get("name")
    description = metadata.get("description", "")
    if name != SKILL_NAME:
        raise ValueError(f"SKILL.md name must be {SKILL_NAME!r}, got {name!r}")
    if len(description) > 200:
        raise ValueError("Claude skill description must be 200 characters or fewer")
    if SKILL_ROOT.name != name:
        raise ValueError("Skill directory name must match SKILL.md name")


def iter_skill_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted(SKILL_ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(SKILL_ROOT)
        if rel.parts and rel.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        if any(part == "__pycache__" for part in rel.parts):
            continue
        if path.suffix == ".pyc":
            continue
        files.append(path)
    return files


def build_archive(output: Path) -> Path:
    validate_skill_root()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in iter_skill_files():
            rel = path.relative_to(SKILL_ROOT)
            archive.write(path, str(Path(SKILL_NAME) / rel))
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output ZIP path. Defaults to dist/zinsser-style-guardian-claude-skill.zip.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output = build_archive(args.output.expanduser().resolve())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
