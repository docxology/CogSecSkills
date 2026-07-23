"""Flattened manuscript skill rows and the small string/group helpers.

This submodule turns the live registry and on-disk skill specifications into
``SkillRow`` records and exposes the lightweight text/grouping helpers shared by
the table and figure renderers.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, TypedDict

from cogsecskills.core.loader import discover_skills
from cogsecskills.core.registry import load_registry
from cogsecskills.core.text_utils import clean_cell

from .paths import _project_root


@dataclass(frozen=True)
class SkillRow:
    """Flattened manuscript metadata for one registry skill row."""

    id: str
    name: str
    group: str
    group_title: str
    status: str
    functionality: str
    use_when: str
    ageint_topic: str
    verbs: tuple[str, ...]
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    tags: tuple[str, ...]
    harnesses: tuple[str, ...]
    references_count: int
    defensive_boundary: str
    evidence_discipline: str
    confidence_anchor: str
    unsafe_redirect: str
    safe_defensive_pattern: str
    source_path: str


class AssetWriteResult(TypedDict):
    skills: int
    markdown: list[str]
    data: list[str]
    figures: list[str]


class GroupSummary(TypedDict):
    id: str
    title: str
    count: int
    references: int
    references_per_skill: float


def _slug(skill_id: str) -> str:
    """Return the slug portion of a ``group.slug`` skill id."""
    return skill_id.split(".", 1)[-1]


# Backward-compat alias for consumers that import `_clean_cell` from rows.
_clean_cell = clean_cell


def _join(values: Iterable[str], *, fallback: str = "none") -> str:
    """Join non-empty values with commas, falling back if none survive."""
    cleaned = [v for v in values if v]
    return ", ".join(cleaned) if cleaned else fallback


def _first(values: Iterable[str], *, fallback: str = "not declared") -> str:
    """Return the first non-empty value, or *fallback* if none."""
    for value in values:
        if value:
            return value
    return fallback


def _first_containing(
    values: Iterable[str], needles: tuple[str, ...], *, fallback: str = "not declared"
) -> str:
    """Return the first value containing all *needles* (case-insensitive)."""
    for value in values:
        lower = value.lower()
        if all(needle in lower for needle in needles):
            return value
    return fallback


def _first_with_prefix(
    values: Iterable[str], prefix: str, *, fallback: str = "not declared"
) -> str:
    """Return the first value starting with *prefix* (case-insensitive)."""
    lower_prefix = prefix.lower()
    for value in values:
        if value.lower().startswith(lower_prefix):
            return value
    return fallback


def _group_ids(rows: Iterable[SkillRow]) -> tuple[str, ...]:
    """Return group ids in first-seen order from the skill rows."""
    seen: set[str] = set()
    ordered: list[str] = []
    for row in rows:
        if row.group not in seen:
            seen.add(row.group)
            ordered.append(row.group)
    return tuple(ordered)


def _group_title(rows: Iterable[SkillRow], group_id: str) -> str:
    """Return the human-readable title for *group_id* from the rows."""
    for row in rows:
        if row.group == group_id:
            return row.group_title
    return group_id


def collect_skill_rows(root: Path | None = None) -> list[SkillRow]:
    """Return manuscript-ready rows, ordered exactly like the registry."""
    base = _project_root(root)
    registry = load_registry(base)
    specs = {spec.id: spec for spec in discover_skills(base)}
    rows: list[SkillRow] = []

    for entry in registry.entries:
        spec = specs.get(entry.id)
        triggers = spec.triggers if spec else ()
        use_when = "; ".join(triggers[:3]) if triggers else entry.name.lower()
        verbs = tuple(sorted(v.value for v in spec.verbs)) if spec else ()
        inputs = tuple(io_item.name for io_item in spec.inputs) if spec else ()
        outputs = tuple(io_item.name for io_item in spec.outputs) if spec else ()
        tags = tuple(spec.tags) if spec else ()
        harnesses = tuple(sorted(spec.harness)) if spec else ()
        references_count = len(spec.references) if spec else 0
        ageint_topic = (
            spec.ageint_topic if spec and spec.ageint_topic else entry.ageint_topic
        )
        rows.append(
            SkillRow(
                id=entry.id,
                name=entry.name,
                group=entry.group,
                group_title=registry.groups.get(entry.group, entry.group),
                status=spec.status if spec else entry.status,
                functionality=spec.summary if spec else entry.summary,
                use_when=use_when,
                ageint_topic=ageint_topic or "unmapped",
                verbs=verbs,
                inputs=inputs,
                outputs=outputs,
                tags=tags,
                harnesses=harnesses,
                references_count=references_count,
                defensive_boundary=spec.defensive_boundary if spec else "not declared",
                evidence_discipline=_first(spec.evidence_requirements if spec else ()),
                confidence_anchor=_first(spec.confidence_rubric if spec else ()),
                unsafe_redirect=_first_with_prefix(
                    spec.negative_controls if spec else (), "unsafe:"
                ),
                safe_defensive_pattern=_first_with_prefix(
                    spec.negative_controls if spec else (), "safe defensive:"
                ),
                source_path=f"skills/{entry.group}/{_slug(entry.id)}/SKILL.md",
            )
        )

    return rows
