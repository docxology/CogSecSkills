"""Shared filesystem boundaries for declarative identifiers and output paths."""

from __future__ import annotations

import re
from collections.abc import Sequence
from pathlib import Path


def validate_component(value: object, label: str) -> str:
    """Return a portable single path component or raise ``ValueError``.

    Harness names, groups, and slugs become output filenames. Keep their
    vocabulary independent of the host's path separator and reject traversal
    before any directory creation or overwrite.
    """
    if not isinstance(value, str) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9_-]*", value
    ):
        raise ValueError(f"{label} must be a safe non-empty path component")
    return value


def validate_harnesses(values: object) -> tuple[str, ...]:
    """Validate and normalize a non-empty, unique sequence of harness names."""
    if not isinstance(values, Sequence) or isinstance(values, (str, bytes)):
        raise ValueError("'harnesses' must be a non-empty list or tuple")
    if not values:
        raise ValueError("'harnesses' must be a non-empty list or tuple")
    cleaned = tuple(
        value.strip() if isinstance(value, str) else value for value in values
    )
    if not any(cleaned):
        raise ValueError("'harnesses' resolved to empty after cleaning")
    names = tuple(validate_component(value, "harness name") for value in cleaned)
    if len(names) != len(set(names)):
        raise ValueError("'harnesses' must not contain duplicate names")
    return names


def skill_components(skill_id: str, group: str) -> tuple[str, str]:
    """Return the path-safe group and slug for an id agreeing with its group."""
    validate_component(group, "skill group")
    prefix = f"{group}."
    if not skill_id.startswith(prefix):
        raise ValueError(f"skill id must be '<group>.<slug>' using group {group!r}")
    return group, validate_component(skill_id[len(prefix) :], "skill slug")


def contained_path(directory: Path, declared: str | Path) -> Path:
    """Resolve a relative path that remains physically inside ``directory``.

    Lexical traversal and symlinks pointing outside the boundary are rejected.
    Return the lexical path so reports and generated-file keys remain stable.
    """
    relative = Path(declared)
    candidate = directory / relative
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or not candidate.resolve().is_relative_to(directory.resolve())
    ):
        raise ValueError(f"path {str(declared)!r} must stay inside {directory}")
    return candidate
