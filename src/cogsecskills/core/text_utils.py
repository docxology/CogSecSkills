"""Shared text utilities for artifact generators.

Several artifact modules (``evals``, ``examples``, ``rows``) need the same
small string helpers: collapsing whitespace, escaping pipe characters for
Markdown tables, and validating non-empty string fields from parsed YAML.
Centralizing them here prevents the copies from drifting.
"""

from __future__ import annotations

from pathlib import Path

import yaml


def yaml_scalar(value: str) -> str:
    """Render a single-line YAML-safe scalar, quoting only when required.

    Used for frontmatter emitted into generated files (``SKILL.md`` and
    scaffolds). Plain text stays plain; values containing YAML-significant
    characters (``: ``, ``#``, quotes, leading indicators) are quoted so
    strict YAML parsers accept the emitted frontmatter.
    """
    return (
        yaml.safe_dump(value, width=10**6, allow_unicode=True)
        .removesuffix("...\n")
        .strip()
    )


def clean_cell(value: object) -> str:
    """Collapse whitespace and escape pipe characters for Markdown table cells."""
    text = " ".join(str(value).split())
    return text.replace("|", r"\|")


def as_text(value: object, *, field: str, path: Path) -> str:
    """Return a validated non-empty string from a parsed YAML mapping.

    Raises :class:`ValueError` if *value* is not a string or is empty.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{path}: {field} must be a non-empty string")
    return value.strip()
