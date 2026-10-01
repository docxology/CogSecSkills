"""Discover and load skills from disk.

Skills live under ``<project>/skills/<group>/<slug>/`` and are identified by a
``skill.yaml`` file. This module turns that on-disk tree into validated
:class:`~cogsecskills.core.spec.SkillSpec` objects, and resolves the conventional
companion files (``SKILL.md`` for Claude Code, ``workflow.md``, and the
per-harness adapters under ``harness/``).
"""

from __future__ import annotations

from pathlib import Path

import yaml

from cogsecskills.core.locate import resolve_root
from cogsecskills.core.paths import contained_path
from cogsecskills.core.spec import SkillSpec, SpecError
from cogsecskills.core.yaml_io import read_yaml

#: Filename that marks a directory as a skill.
SPEC_FILENAME = "skill.yaml"

#: Default project-relative location of the skills tree.
SKILLS_DIRNAME = "skills"


def skills_root(root: Path | None = None) -> Path:
    """Return the path to the ``skills/`` directory."""
    base = resolve_root(root)
    return base / SKILLS_DIRNAME


def load_skill(spec_path: Path) -> SkillSpec:
    """Parse and validate a single ``skill.yaml`` at ``spec_path``."""
    spec_path = Path(spec_path)
    if not spec_path.is_file():
        raise FileNotFoundError(f"no skill spec at {spec_path}")
    try:
        raw = read_yaml(spec_path)
    except ValueError as exc:
        if isinstance(exc.__cause__, yaml.YAMLError):
            raise SpecError(
                f"{spec_path}: invalid YAML: {exc.__cause__}"
            ) from exc.__cause__
        raise SpecError(str(exc)) from exc
    try:
        return SkillSpec.from_mapping(raw)
    except SpecError as exc:
        raise SpecError(f"{spec_path}: {exc}") from exc


def discover_skills(root: Path | None = None) -> list[SkillSpec]:
    """Discover every skill under the ``skills/`` tree, sorted by id.

    Returns an empty list when the tree does not exist yet (a fresh scaffold),
    so callers never need to special-case bootstrap.
    """
    tree = skills_root(root)
    if not tree.is_dir():
        return []
    specs: list[SkillSpec] = []
    seen: set[str] = set()
    for spec_path in sorted(tree.rglob(SPEC_FILENAME)):
        try:
            contained_path(
                resolve_root(root), spec_path.relative_to(resolve_root(root))
            )
            contained_path(tree, spec_path.relative_to(tree))
        except (ValueError, OSError, RuntimeError) as exc:
            raise SpecError(f"unsafe skill source {spec_path}: {exc}") from exc
        spec = load_skill(spec_path)
        if spec.id in seen:
            raise SpecError(f"duplicate on-disk skill id {spec.id!r}")
        seen.add(spec.id)
        specs.append(spec)
    return sorted(specs, key=lambda s: s.id)


def skill_dir(spec_path: Path) -> Path:
    """Return the directory containing a skill spec."""
    return Path(spec_path).resolve().parent
