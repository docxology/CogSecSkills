"""The skill registry — the enumerated catalogue of all skill areas.

``registry/skills.yaml`` enumerates every skill area in the CogSecSkills library
(the full ~100-area taxonomy), independent of whether each area has been
implemented on disk yet. The registry is the *plan*; the ``skills/`` tree is the
*build*. The validation gates cross-check the two so the catalogue can never
silently drift from what actually ships.

``registry/groups.yaml`` defines the workflow subfolders (the groups) each skill
belongs to.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cogsecskills.core.locate import project_root

import yaml

from cogsecskills.core.spec import SKILL_STATUSES, SpecError


def _project_root() -> Path:
    return project_root()


def registry_path(root: Path | None = None) -> Path:
    base = Path(root) if root is not None else _project_root()
    return base / "registry" / "skills.yaml"


def groups_path(root: Path | None = None) -> Path:
    base = Path(root) if root is not None else _project_root()
    return base / "registry" / "groups.yaml"


@dataclass(frozen=True)
class RegistryEntry:
    """One catalogue row: a planned-or-built skill area."""

    id: str
    name: str
    group: str
    status: str
    summary: str
    ageint_topic: str = ""

    @classmethod
    def from_obj(cls, obj: object) -> "RegistryEntry":
        if not isinstance(obj, dict):
            raise SpecError(
                f"registry entry must be a mapping, got {type(obj).__name__}"
            )
        for key in ("id", "name", "group", "summary"):
            if not str(obj.get(key, "")).strip():
                raise SpecError(f"registry entry missing required key {key!r}: {obj!r}")
        status = str(obj.get("status", "planned")).strip().lower()
        if status not in SKILL_STATUSES:
            raise SpecError(
                f"registry entry {obj['id']!r} has invalid status {status!r}"
            )
        return cls(
            id=str(obj["id"]).strip(),
            name=str(obj["name"]).strip(),
            group=str(obj["group"]).strip(),
            status=status,
            summary=str(obj["summary"]).strip(),
            ageint_topic=str(obj.get("ageint_topic", "")).strip(),
        )


@dataclass(frozen=True)
class SkillRegistry:
    """The full catalogue plus the group definitions."""

    entries: tuple[RegistryEntry, ...]
    groups: dict[str, str]

    def __len__(self) -> int:
        return len(self.entries)

    @property
    def ids(self) -> tuple[str, ...]:
        return tuple(e.id for e in self.entries)

    def by_group(self, group: str) -> tuple[RegistryEntry, ...]:
        return tuple(e for e in self.entries if e.group == group)

    def by_status(self, status: str) -> tuple[RegistryEntry, ...]:
        return tuple(e for e in self.entries if e.status == status)

    def get(self, skill_id: str) -> RegistryEntry | None:
        for entry in self.entries:
            if entry.id == skill_id:
                return entry
        return None

    def status_counts(self) -> dict[str, int]:
        counts = {status: 0 for status in SKILL_STATUSES}
        for entry in self.entries:
            counts[entry.status] += 1
        return counts


def load_registry(root: Path | None = None) -> SkillRegistry:
    """Load and validate ``registry/skills.yaml`` + ``registry/groups.yaml``."""
    skills_file = registry_path(root)
    if not skills_file.is_file():
        raise FileNotFoundError(f"no registry at {skills_file}")
    raw = yaml.safe_load(skills_file.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict) or "skills" not in raw:
        raise SpecError(f"{skills_file}: expected top-level mapping with 'skills' key")
    entries = tuple(RegistryEntry.from_obj(item) for item in raw["skills"])

    seen: set[str] = set()
    for entry in entries:
        if entry.id in seen:
            raise SpecError(f"duplicate registry id {entry.id!r}")
        seen.add(entry.id)

    groups: dict[str, str] = {}
    groups_file = groups_path(root)
    if groups_file.is_file():
        graw = yaml.safe_load(groups_file.read_text(encoding="utf-8")) or {}
        if not isinstance(graw, dict):
            raise SpecError(f"{groups_file}: expected a top-level mapping")
        for item in graw.get("groups", []):
            if not isinstance(item, dict) or not str(item.get("id", "")).strip():
                raise SpecError(
                    f"{groups_file}: each group must be a mapping with a non-empty 'id'"
                )
            gid = str(item["id"]).strip()
            groups[gid] = str(item.get("title", gid)).strip() or gid

    return SkillRegistry(entries=entries, groups=groups)
