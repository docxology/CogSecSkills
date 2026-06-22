"""Discover and load skills from disk.

Skills live under ``<project>/skills/<group>/<slug>/`` and are identified by a
``skill.yaml`` file. This module turns that on-disk tree into validated
:class:`~cogsecskills.spec.SkillSpec` objects, and resolves the conventional
companion files (``SKILL.md`` for Claude Code, ``workflow.md``, and the
per-harness adapters under ``harness/``).
"""

from __future__ import annotations

from pathlib import Path

import yaml

from cogsecskills.core.spec import SkillSpec, SpecError

#: Filename that marks a directory as a skill.
SPEC_FILENAME = "skill.yaml"

#: Default project-relative location of the skills tree.
SKILLS_DIRNAME = "skills"


def _project_root() -> Path:
    """Best-effort project root (the directory that contains ``skills/``).

    The package lives at ``<root>/src/cogsecskills/``; the skills tree at
    ``<root>/skills/``. We resolve relative to this file so the loader works
    regardless of the caller's working directory.
    """
    return Path(__file__).resolve().parents[3]


def skills_root(root: Path | None = None) -> Path:
    """Return the path to the ``skills/`` directory."""
    base = Path(root) if root is not None else _project_root()
    return base / SKILLS_DIRNAME


def load_skill(spec_path: Path) -> SkillSpec:
    """Parse and validate a single ``skill.yaml`` at ``spec_path``."""
    spec_path = Path(spec_path)
    if not spec_path.is_file():
        raise FileNotFoundError(f"no skill spec at {spec_path}")
    try:
        raw = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise SpecError(f"{spec_path}: invalid YAML: {exc}") from exc
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
    for spec_path in sorted(tree.rglob(SPEC_FILENAME)):
        specs.append(load_skill(spec_path))
    return sorted(specs, key=lambda s: s.id)


def skill_dir(spec_path: Path) -> Path:
    """Return the directory containing a skill spec."""
    return Path(spec_path).resolve().parent
