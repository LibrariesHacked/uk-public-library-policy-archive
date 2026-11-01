"""Shared helpers for the archive validation scripts.

Kept deliberately small: every check in this repository should be readable by
a single maintainer in a few minutes.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "archive" / "reports"
SCHEMAS_DIR = ROOT / "schemas"

REQUIRED_FILES = ("report.md", "metadata.yaml", "provenance.yaml", "acquisition.yaml")


class _StringDateLoader(yaml.SafeLoader):
    """SafeLoader that keeps ISO dates as strings.

    PyYAML turns unquoted 2026-01-15 into a datetime.date, which would then
    fail the JSON Schema "string" type. Archival dates are text, so keep them
    as written.
    """


_StringDateLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.load(fh, Loader=_StringDateLoader)


def load_yaml_text(text: str):
    return yaml.load(text, Loader=_StringDateLoader)


def report_dirs() -> list[Path]:
    if not REPORTS_DIR.is_dir():
        return []
    return sorted(p for p in REPORTS_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))


FRONT_MATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def split_front_matter(text: str):
    """Return (front_matter_dict_or_None, body_text)."""
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return None, text
    return load_yaml_text(m.group(1)), text[m.end():]


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


class Problems:
    """Collects failures and prints GitHub Actions annotations."""

    def __init__(self, title: str):
        self.title = title
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, message: str):
        self.errors.append(f"{where}: {message}")
        print(f"::error file={where}::{message}")

    def warn(self, where: str, message: str):
        self.warnings.append(f"{where}: {message}")
        print(f"::warning file={where}::{message}")

    def finish(self, checked: int) -> None:
        print(f"\n{self.title}: checked {checked} item(s), "
              f"{len(self.errors)} error(s), {len(self.warnings)} warning(s).")
        sys.exit(1 if self.errors else 0)

