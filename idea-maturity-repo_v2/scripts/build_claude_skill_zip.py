#!/usr/bin/env python3
"""Build a Claude custom skill upload ZIP for idea-maturity."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "idea-maturity"
SKILL_ROOT = ROOT / "plugins" / "idea-maturity" / "skills" / SKILL_NAME
DEFAULT_OUTPUT = ROOT / "dist" / "idea-maturity-claude-skill.zip"

EXCLUDED_PARTS = {"__pycache__", ".DS_Store"}


def iter_skill_files() -> list[Path]:
    if not SKILL_ROOT.is_dir():
        raise FileNotFoundError(f"Skill folder not found: {SKILL_ROOT}")
    skill_md = SKILL_ROOT / "SKILL.md"
    if not skill_md.is_file():
        raise FileNotFoundError(f"Missing required SKILL.md: {skill_md}")
    files: list[Path] = []
    for path in sorted(SKILL_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        files.append(path)
    return files


def validate_skill_name() -> None:
    skill_md = SKILL_ROOT / "SKILL.md"
    frontmatter = skill_md.read_text(encoding="utf-8").split("---", 2)
    if len(frontmatter) < 3 or f"name: {SKILL_NAME}" not in frontmatter[1]:
        raise ValueError(f"SKILL.md frontmatter must declare name: {SKILL_NAME}")
    if SKILL_ROOT.name != SKILL_NAME:
        raise ValueError(f"Skill folder must be named {SKILL_NAME}")


def build_zip(output: Path = DEFAULT_OUTPUT) -> Path:
    validate_skill_name()
    files = iter_skill_files()
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            relative = path.relative_to(SKILL_ROOT)
            archive.write(path, Path(SKILL_NAME) / relative)
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a Claude upload ZIP for the idea-maturity skill.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output ZIP path. Default: {DEFAULT_OUTPUT.relative_to(ROOT)}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output = build_zip(args.output)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
