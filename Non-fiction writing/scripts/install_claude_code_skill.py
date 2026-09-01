#!/usr/bin/env python3
"""Install the Zinsser Style Guardian skill into a Claude Code skills directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "zinsser-style-guardian"
SKILL_ROOT = ROOT / "plugins" / SKILL_NAME / "skills" / SKILL_NAME
DEFAULT_TARGET = Path.home() / ".claude" / "skills"
INCLUDED_TOP_LEVEL = {"SKILL.md", "references"}


def copy_skill(target_root: Path, *, force: bool) -> Path:
    if not (SKILL_ROOT / "SKILL.md").is_file():
        raise FileNotFoundError(f"Missing source skill at {SKILL_ROOT}")

    target = target_root.expanduser().resolve() / SKILL_NAME
    if target.exists():
        if not force:
            raise FileExistsError(f"{target} already exists. Re-run with --force to replace it.")
        shutil.rmtree(target)

    target.mkdir(parents=True, exist_ok=True)
    for item_name in sorted(INCLUDED_TOP_LEVEL):
        source = SKILL_ROOT / item_name
        destination = target / item_name
        if source.is_dir():
            shutil.copytree(source, destination)
        elif source.is_file():
            shutil.copy2(source, destination)
        else:
            raise FileNotFoundError(f"Missing expected skill item: {source}")
    return target


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        type=Path,
        default=DEFAULT_TARGET,
        help="Claude Code skills parent directory. Defaults to ~/.claude/skills.",
    )
    parser.add_argument("--force", action="store_true", help="Replace an existing installed copy.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        target = copy_skill(args.target, force=args.force)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
