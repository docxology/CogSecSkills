"""Live conformance test over the REAL CogSecSkills library on disk.

This is the machine-checkable meaning of "multiharness, equally validated for
Claude Code, Codex, and Hermes": every on-disk skill must load, validate, and
conform to all three harnesses, and the registry/disk catalogue must be
coherent. It runs against the actual ``skills/`` tree and ``registry/``, not a
fixture — so adding a malformed skill breaks the build.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cogsecskills.harness import HARNESSES, check_conformance
from cogsecskills.loader import discover_skills
from cogsecskills.registry import load_registry
from cogsecskills.validate import validate_library

#: The real project root (this file lives at <root>/tests/).
ROOT = Path(__file__).resolve().parents[1]


def test_registry_enumerates_one_hundred_areas():
    registry = load_registry(ROOT)
    assert len(registry) == 100, "the catalogue is defined as 100 skill areas"


def test_registry_groups_match_group_definitions():
    registry = load_registry(ROOT)
    defined = set(registry.groups)
    used = {e.group for e in registry.entries}
    assert used <= defined, f"entries use undefined groups: {used - defined}"


def test_every_implemented_entry_has_on_disk_skill():
    registry = load_registry(ROOT)
    on_disk = {s.id for s in discover_skills(ROOT)}
    for entry in registry.by_status("implemented"):
        assert entry.id in on_disk, f"{entry.id} is implemented but absent on disk"


def test_at_least_eight_exemplars_built():
    on_disk = discover_skills(ROOT)
    assert len(on_disk) >= 8, "expected at least the 8 seed exemplar skills"


def test_library_validates_clean():
    result = validate_library(ROOT)
    messages = "\n".join(
        f"  {i.severity}: {i.skill_id}: {i.message}" for i in result.issues
    )
    assert result.ok, f"library validation found errors:\n{messages}"


@pytest.mark.parametrize("spec", discover_skills(ROOT), ids=lambda s: s.id)
def test_each_on_disk_skill_is_multiharness(spec):
    confs = check_conformance(spec)
    assert set(confs) == set(HARNESSES)
    for harness, conf in confs.items():
        assert conf.has_adapter, f"{spec.id} missing {harness} adapter declaration"
        assert not conf.unsupported_verbs, (
            f"{spec.id}: {harness} cannot realise {conf.unsupported_verbs}"
        )


@pytest.mark.parametrize("spec", discover_skills(ROOT), ids=lambda s: s.id)
def test_each_skill_companion_files_exist(spec):
    """Every declared harness adapter + workflow + SKILL.md exists on disk."""
    # Locate the skill directory by id.
    from cogsecskills.loader import SPEC_FILENAME, load_skill, skill_dir, skills_root

    directory = None
    for candidate in skills_root(ROOT).rglob(SPEC_FILENAME):
        if load_skill(candidate).id == spec.id:
            directory = skill_dir(candidate)
            break
    assert directory is not None
    assert (directory / "SKILL.md").is_file()
    assert (directory / spec.workflow).is_file()
    for harness in HARNESSES:
        rel = spec.harness[harness]
        assert (directory / rel).is_file(), f"{spec.id}: missing {rel}"
