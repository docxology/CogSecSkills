"""Live conformance test over the REAL CogSecSkills library on disk.

This is the machine-checkable meaning of "multiharness, equally validated":
every on-disk skill must load, validate, and conform to every configured
harness. The real project defaults to Claude Code, Codex, and Hermes, and the
registry/disk catalogue must be coherent. It runs against the actual
``skills/`` tree and ``registry/``, not a fixture — so adding a malformed skill
breaks the build.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import pytest

from cogsecskills.author import QUALITY_FIELDS
from cogsecskills.definitions import (
    check_definitions,
    definition_path,
    load_definitions,
)
from cogsecskills.harness import HARNESSES, check_conformance
from cogsecskills.insights import GENERIC_NEGATIVE_CONTROL_PHRASES
from cogsecskills.loader import (
    SPEC_FILENAME,
    discover_skills,
    load_skill,
    skill_dir,
    skills_root,
)
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


def test_every_registry_entry_has_canonical_definition():
    registry = load_registry(ROOT)
    for entry in registry.entries:
        assert definition_path(entry.id, ROOT).is_file(), (
            f"{entry.id} lacks canonical definition"
        )


def _specificity_tokens(entry) -> set[str]:
    ignored = {"analysis", "review", "assessment"}
    text = f"{entry.name} {entry.id.split('.', 1)[1].replace('_', ' ')} {entry.summary}"
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower()) if len(token) >= 5
    } - ignored


def _quality_item_is_specific(entry, item: str) -> bool:
    lower = item.lower()
    if entry.name.lower() in lower:
        return True
    slug_phrase = entry.id.split(".", 1)[1].replace("_", " ").lower()
    if slug_phrase in lower:
        return True
    return any(token in lower for token in _specificity_tokens(entry))


def test_canonical_definitions_have_specific_quality_controls():
    registry = load_registry(ROOT)
    entries = {entry.id: entry for entry in registry.entries}
    definitions = load_definitions(ROOT)
    for skill_id, definition in definitions.items():
        entry = entries[skill_id]
        negative = "\n".join(definition["negative_controls"]).lower()
        evidence = "\n".join(definition["evidence_requirements"]).lower()
        uncertainty = "\n".join(definition["uncertainty_handling"]).lower()
        workflow_text = "\n".join(
            f"{step.get('title', '')} {step.get('text', '')}"
            for step in definition["workflow_steps"]
        ).lower()
        assert "unsafe" in negative, f"{skill_id}: missing unsafe negative control"
        assert "safe" in negative, f"{skill_id}: missing safe negative control"
        assert "defensive" in negative, f"{skill_id}: missing defensive safe example"
        assert "evidence" in evidence, f"{skill_id}: missing evidence label"
        assert "inference" in evidence, f"{skill_id}: missing inference label"
        assert "unknown" in uncertainty, f"{skill_id}: missing unknowns discipline"
        assert "alternative" in uncertainty, (
            f"{skill_id}: missing alternatives discipline"
        )
        assert not any(
            phrase in negative for phrase in GENERIC_NEGATIVE_CONTROL_PHRASES
        ), f"{skill_id}: generic negative-control boilerplate survived"
        specificity_tokens = _specificity_tokens(entry)
        slug_phrase = entry.id.split(".", 1)[1].replace("_", " ").lower()
        assert (
            entry.name.lower() in negative
            or slug_phrase in negative
            or entry.group in negative
            or any(token in negative for token in specificity_tokens)
        ), f"{skill_id}: negative controls are not skill- or group-specific"
        assert entry.group in workflow_text or any(
            token in workflow_text for token in specificity_tokens
        ), f"{skill_id}: workflow is not skill- or group-specific"
        for field in (
            "confidence_rubric",
            "evidence_requirements",
            "privacy_legal_constraints",
            "failure_modes",
        ):
            values = definition[field]
            assert any(
                _quality_item_is_specific(entry, str(item)) for item in values
            ), f"{skill_id}: {field} lacks skill-specific language"


def test_negative_control_sets_are_not_reused_across_corpus():
    definitions = load_definitions(ROOT)
    normalized = Counter(
        "\n".join(definition["negative_controls"]).lower()
        for definition in definitions.values()
    )
    reused = [text for text, count in normalized.items() if count > 1]
    assert reused == []


def test_individual_negative_controls_are_not_reused_across_corpus():
    definitions = load_definitions(ROOT)
    normalized = Counter(
        " ".join(str(item).lower().split())
        for definition in definitions.values()
        for item in definition["negative_controls"]
    )
    reused = [text for text, count in normalized.items() if count > 1]
    assert reused == []


def test_core_quality_entries_are_not_reused_across_corpus():
    definitions = load_definitions(ROOT)
    for field in (
        "confidence_rubric",
        "evidence_requirements",
        "privacy_legal_constraints",
    ):
        normalized = Counter(
            " ".join(str(item).lower().split())
            for definition in definitions.values()
            for item in definition[field]
        )
        reused = [text for text, count in normalized.items() if count > 1]
        assert reused == [], f"{field} reused entries: {reused[:5]}"


def test_canonical_definitions_match_rendered_skills():
    findings = check_definitions(ROOT)
    assert findings == []


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


@pytest.mark.parametrize("spec", discover_skills(ROOT), ids=lambda s: s.id)
def test_each_skill_has_quality_fields_and_negative_controls(spec):
    for field in QUALITY_FIELDS:
        value = getattr(spec, field)
        assert value, f"{spec.id}: missing {field}"
    negative = "\n".join(spec.negative_controls).lower()
    assert "unsafe" in negative, f"{spec.id}: negative controls lack unsafe example"
    assert "redirect" in negative, f"{spec.id}: negative controls lack redirect"


@pytest.mark.parametrize("spec", discover_skills(ROOT), ids=lambda s: s.id)
def test_workflow_step_verbs_are_declared(spec):
    directory = None
    for candidate in skills_root(ROOT).rglob(SPEC_FILENAME):
        if load_skill(candidate).id == spec.id:
            directory = skill_dir(candidate)
            break
    assert directory is not None
    workflow = (directory / spec.workflow).read_text(encoding="utf-8")
    declared = {verb.value for verb in spec.verbs}
    used: set[str] = set()
    for match in re.finditer(r"^## Step \d+ [—-] .*?\(([^)]*)\)", workflow, re.M):
        used.update(part.strip() for part in match.group(1).split(",") if part.strip())
    assert used, f"{spec.id}: no tagged workflow step verbs"
    assert used <= declared, (
        f"{spec.id}: workflow uses undeclared verbs {used - declared}"
    )


def test_generated_harness_adapters_do_not_request_chain_of_thought():
    for path in (ROOT / "skills").glob("*/*/harness/*.md"):
        assert "chain-of-thought" not in path.read_text(encoding="utf-8").lower()
