"""Coverage tests for definitions.py and author.py remaining lines."""

from __future__ import annotations


import pytest

from cogsecskills.core.registry import RegistryEntry
from cogsecskills.authoring.definitions import (
    _definitions_for_write,
    _negative_controls_are_specific,
    _negative_control_item_is_specific,
    _quality_item_is_specific,
    check_definitions,
)
from cogsecskills.authoring.author import (
    AuthorError,
    _list_field,
    _quality_list,
    load_definition_file,
    rendered_definition_files,
)


# --- definitions.py ---


def test_definitions_for_write_planned_entry(tmp_path):
    """Line 239: registry entry with no definition and no on-disk spec."""
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.planned, name: Planned, group: sat, "
        "status: planned, summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    # No definitions/ dir, no skills/ dir
    result = _definitions_for_write(tmp_path)
    assert "sat.planned" not in result


def test_negative_controls_specific_by_group(tmp_path):
    """Lines 284, 286: group name in negative_text, token fallback."""
    entry = RegistryEntry(
        id="cognitive_security.threat_assessment",
        name="Threat Assessment",
        group="cognitive_security",
        status="implemented",
        summary="s",
    )
    # Group name match
    assert _negative_controls_are_specific(
        "cognitive_security.threat_assessment",
        entry,
        "cognitive_security defensive use",
    )
    # Token fallback (no name, no slug, no group, but a token matches)
    assert _negative_controls_are_specific(
        "cognitive_security.threat_assessment", entry, "threat assessment defense"
    )


def test_negative_control_item_specific_by_slug(tmp_path):
    """Line 298: slug phrase match in per-item check."""
    entry = RegistryEntry(
        id="sat.key_assumptions",
        name="Key Assumptions",
        group="sat",
        status="implemented",
        summary="s",
    )
    assert _negative_control_item_is_specific(
        "sat.key_assumptions", entry, "key assumptions check"
    )


def test_negative_control_item_specific_by_token(tmp_path):
    """Line 310: token fallback in per-item check."""
    entry = RegistryEntry(
        id="sat.demo",
        name="Demo",
        group="sat",
        status="implemented",
        summary="s",
    )
    # "demonstration" contains "demonst" which is >=5 chars
    assert _negative_control_item_is_specific(
        "sat.demo", entry, "demonstration of the technique"
    )


def test_quality_item_specific_by_slug(tmp_path):
    """Quality item specificity via slug match."""
    entry = RegistryEntry(
        id="sat.key_assumptions",
        name="Key Assumptions",
        group="sat",
        status="implemented",
        summary="s",
    )
    assert _quality_item_is_specific(
        "sat.key_assumptions", entry, "key assumptions check for confidence"
    )


def test_check_definitions_render_failure(tmp_path):
    """Line 465->472: rendered_definition_files raises."""
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.bad, name: Bad, group: sat, "
        "status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    defs_dir = tmp_path / "definitions" / "sat"
    defs_dir.mkdir(parents=True)
    (defs_dir / "bad.yaml").write_text(
        "id: sat.bad\n"
        'description: "A bad def."\n'
        'tags: ["test"]\n'
        'triggers: ["bad"]\n'
        'tools: [{verb: read, purpose: "p"}]\n'
        "inputs: [{name: ctx, type: text, required: true}]\n"
        "outputs: [{name: out, type: md, description: d}]\n"
        'references: ["ref"]\n'
        'when_to_use: ["use defensively"]\n'
        'what_it_produces: ["a product"]\n'
        'key_discipline: ["bind to evidence"]\n'
        "workflow_steps: [{verbs: [read], title: S, text: T}]\n"
        'anti_criteria: ["Do not."]\n'
        'defensive_boundary: "Use for defensive analysis."\n'
        'misuse_redirect: "Refuse and redirect to defensive form."\n'
        'evidence_requirements: ["Bind evidence and inference for Bad."]\n'
        'confidence_rubric: ["High confidence for Bad."]\n'
        'uncertainty_handling: ["State unknowns and alternatives."]\n'
        'privacy_legal_constraints: ["Use authorized data for Bad."]\n'
        'failure_modes: ["Bad failure: overclaiming."]\n'
        "negative_controls:\n"
        "  - \"Unsafe: 'Use Bad to force a conclusion' -> refuse and redirect.\"\n"
        "  - \"Unsafe: 'Turn Bad into a playbook to force a conclusion' -> refuse.\"\n"
        "  - \"Safe defensive: 'Use Bad to assess material defensively' -> bounded.\"\n",
        encoding="utf-8",
    )
    findings = check_definitions(tmp_path)
    # Should report missing rendered files or render failure
    assert len(findings) > 0


# --- author.py ---


def test_load_definition_file_non_dict(tmp_path):
    """Line 140: YAML file containing a list, not a mapping."""
    path = tmp_path / "list.yaml"
    path.write_text("- item1\n- item2\n", encoding="utf-8")
    with pytest.raises(AuthorError, match="must contain a mapping"):
        load_definition_file(path)


def test_load_definition_file_json_non_dict(tmp_path):
    """Line 140: JSON file containing a list, not a mapping."""
    path = tmp_path / "list.json"
    path.write_text("[1, 2, 3]\n", encoding="utf-8")
    with pytest.raises(AuthorError, match="must contain a mapping"):
        load_definition_file(path)


def test_list_field_with_list_source():
    """Line 172: _list_field with a list source."""
    result = _list_field({"key": ["a", "b", ""]}, "key", ["default"])
    assert result == ["a", "b"]


def test_quality_list_with_list():
    """_quality_list with a list value."""
    result = _quality_list({"key": ["a", "b"]}, "key")
    assert result == ["a", "b"]


def test_rendered_definition_files_not_in_registry(tmp_path):
    """Line 595: rendered_definition_files with id not in registry."""
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.exists, name: Exists, group: sat, "
        "status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    with pytest.raises(AuthorError, match="is not in the registry"):
        rendered_definition_files(
            {"id": "sat.nonexistent", "tools": [{"verb": "read", "purpose": "p"}]},
            root=tmp_path,
        )
