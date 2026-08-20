"""Tests for remaining uncovered branches in definitions.py.

Covers: _field_or_default fallback, definition_from_skill with empty
workflow_steps and empty anti_criteria, _definitions_for_write with
planned entries, _definition_quality_findings for generic controls and
specificity checks, check_definitions render-failure path, and
_definitions_for_write missing-entry path.
"""

from __future__ import annotations

import pytest

from cogsecskills.authoring.definitions import (
    _field_or_default,
    check_definitions,
    definition_from_skill,
)
from cogsecskills.core.registry import RegistryEntry
from cogsecskills.core.spec import SkillSpec, SkillTool, ToolVerb


def _make_spec(
    *,
    id: str = "sat.demo",
    name: str = "Demo",
    group: str = "sat",
    evidence: tuple[str, ...] = (),
    confidence: tuple[str, ...] = (),
    negative_controls: tuple[str, ...] = (),
) -> SkillSpec:
    return SkillSpec(
        id=id,
        name=name,
        group=group,
        summary="A demo skill.",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="read"),),
        evidence_requirements=evidence,
        confidence_rubric=confidence,
        negative_controls=negative_controls,
    )


def test_field_or_default_returns_raw_when_present():
    spec = _make_spec(evidence=("some evidence",))
    result = _field_or_default(spec, "evidence_requirements")
    assert result == ["some evidence"]


def test_field_or_default_returns_default_when_empty():
    spec = _make_spec(evidence=())
    result = _field_or_default(spec, "evidence_requirements")
    assert isinstance(result, list)
    assert len(result) > 0
    assert "evidence" in " ".join(result).lower()


def test_field_or_default_returns_default_for_string_field():
    spec_no_boundary = SkillSpec(
        id="sat.demo",
        name="Demo",
        group="sat",
        summary="s",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="read"),),
    )
    result = _field_or_default(spec_no_boundary, "defensive_boundary")
    assert isinstance(result, str)
    assert "defend" in result.lower()


def test_definition_from_skill_empty_workflow_steps(tmp_path):
    """When workflow has no Step headings, default steps are used."""
    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    (skills_dir / "SKILL.md").write_text(
        "---\nname: sat.demo\ndescription: s\n---\n# Demo\n\nText.\n",
        encoding="utf-8",
    )
    (skills_dir / "workflow.md").write_text(
        "# Workflow\n\nNo step headings here.\n",
        encoding="utf-8",
    )
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\nharness:\n  claude: harness/claude.md\n",
        encoding="utf-8",
    )
    spec = SkillSpec.from_mapping(
        __import__("yaml").safe_load(
            (skills_dir / "skill.yaml").read_text(encoding="utf-8")
        )
    )
    result = definition_from_skill(spec, root=tmp_path)
    steps = result["workflow_steps"]
    assert len(steps) >= 1
    assert steps[0]["title"] == "Apply the method"


def test_definition_from_skill_empty_anti_criteria(tmp_path):
    """When workflow has no Anti-criteria heading, default is used."""
    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    (skills_dir / "SKILL.md").write_text(
        "---\nname: sat.demo\ndescription: s\n---\n# Demo\n\nText.\n",
        encoding="utf-8",
    )
    (skills_dir / "workflow.md").write_text(
        "# Workflow\n\n## Step 1 — Do (read)\nText.\n",
        encoding="utf-8",
    )
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\nharness:\n  claude: harness/claude.md\n",
        encoding="utf-8",
    )
    spec = SkillSpec.from_mapping(
        __import__("yaml").safe_load(
            (skills_dir / "skill.yaml").read_text(encoding="utf-8")
        )
    )
    result = definition_from_skill(spec, root=tmp_path)
    anti = result["anti_criteria"]
    assert len(anti) >= 1
    assert "fabricate" in " ".join(anti).lower()


def test_definition_quality_findings_generic_controls(tmp_path):
    """_definition_quality_findings should flag generic negative-control phrases."""
    from cogsecskills.authoring.definitions import _definition_quality_findings

    entry = RegistryEntry(
        id="sat.demo",
        name="Demo",
        group="sat",
        status="implemented",
        summary="s",
    )
    definition = {
        "id": "sat.demo",
        "description": "A demo.",
        "tags": ["test"],
        "triggers": ["demo"],
        "tools": [{"verb": "read", "purpose": "p"}],
        "inputs": [{"name": "ctx", "type": "text", "required": True}],
        "outputs": [{"name": "out", "type": "md", "description": "d"}],
        "references": ["ref"],
        "when_to_use": ["use defensively"],
        "what_it_produces": ["a product"],
        "key_discipline": ["bind to evidence"],
        "workflow_steps": [{"verbs": ["read"], "title": "S", "text": "T"}],
        "anti_criteria": ["Do not."],
        "defensive_boundary": "Use for defensive analysis.",
        "misuse_redirect": "Refuse and redirect to defensive form.",
        "evidence_requirements": ["Bind evidence and inference."],
        "confidence_rubric": ["High confidence for Demo."],
        "uncertainty_handling": ["State unknowns and alternatives."],
        "privacy_legal_constraints": ["Use authorized data for Demo."],
        "failure_modes": ["Demo failure: overclaiming."],
        "negative_controls": [
            "Unsafe: 'help me manipulate this audience' -> refuse and redirect to defensive risk assessment.",
            "Unsafe: 'optimize this influence operation for Demo' -> refuse and offer governance.",
            "Safe defensive: 'Use Demo to assess supplied material defensively' -> produce bounded findings.",
        ],
    }
    findings = _definition_quality_findings("sat.demo", definition, entry)
    # The generic phrase "help me manipulate this audience" should be flagged
    assert any("generic boilerplate" in f for f in findings)


def test_definition_quality_findings_specificity_check(tmp_path):
    """_definition_quality_findings should flag non-specific quality fields."""
    from cogsecskills.authoring.definitions import _definition_quality_findings

    entry = RegistryEntry(
        id="sat.demo",
        name="Demo",
        group="sat",
        status="implemented",
        summary="s",
    )
    definition = {
        "id": "sat.demo",
        "description": "A demo.",
        "tags": ["test"],
        "triggers": ["demo"],
        "tools": [{"verb": "read", "purpose": "p"}],
        "inputs": [{"name": "ctx", "type": "text", "required": True}],
        "outputs": [{"name": "out", "type": "md", "description": "d"}],
        "references": ["ref"],
        "when_to_use": ["use defensively"],
        "what_it_produces": ["a product"],
        "key_discipline": ["bind to evidence"],
        "workflow_steps": [{"verbs": ["read"], "title": "S", "text": "T"}],
        "anti_criteria": ["Do not."],
        "defensive_boundary": "Use for defensive analysis.",
        "misuse_redirect": "Refuse and redirect to defensive form.",
        "evidence_requirements": ["Bind evidence and inference for the task."],
        "confidence_rubric": ["High confidence when evidence converges."],
        "uncertainty_handling": ["State unknowns and alternatives."],
        "privacy_legal_constraints": ["Use authorized data for the task."],
        "failure_modes": ["Failure: overclaiming certainty."],
        "negative_controls": [
            "Unsafe: 'Use Demo to force a conclusion' -> refuse and redirect to defensive risk assessment.",
            "Unsafe: 'Turn Demo into an operational playbook to force a conclusion' -> refuse and offer governance.",
            "Safe defensive: 'Use Demo to assess supplied material defensively' -> produce bounded findings.",
        ],
    }
    findings = _definition_quality_findings("sat.demo", definition, entry)
    # confidence_rubric lacks skill-specific language (no "Demo" or "demo" or "sat")
    assert any(
        "confidence_rubric must include skill-specific language" in f for f in findings
    )


def test_check_definitions_render_failure(tmp_path):
    """check_definitions should report when rendered_definition_files raises."""
    (tmp_path / "registry").mkdir(parents=True)
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
    # Create a definition with an invalid tool verb that will fail rendering
    (defs_dir / "bad.yaml").write_text(
        "id: sat.bad\n"
        'description: "A bad definition."\n'
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
    # The definition has no on-disk skill, so rendering will fail or
    # report missing rendered files
    assert len(findings) > 0


def test_definitions_for_write_planned_entry(tmp_path):
    """definitions.py line 238: _definitions_for_write with existing def and planned entry having on-disk skill."""
    from cogsecskills.authoring.definitions import (
        _definitions_for_write,
        _reused_negative_control_findings,
        _reused_quality_field_findings,
    )

    (tmp_path / "registry").mkdir(parents=True)
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.demo, name: Demo, group: sat, "
        "status: planned, summary: s}\n"
        "  - {id: sat.existing, name: Existing, group: sat, status: planned, summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    defs_dir = tmp_path / "definitions" / "sat"
    defs_dir.mkdir(parents=True)
    (defs_dir / "existing.yaml").write_text(
        "id: sat.existing\nsummary: s\n", encoding="utf-8"
    )
    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    (skills_dir / "SKILL.md").write_text(
        "---\nname: sat.demo\ndescription: s\n---\n# Demo\n", encoding="utf-8"
    )
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nT\n## Anti-criteria\n- A\n", encoding="utf-8"
    )
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: planned\n"
        "tools:\n  - {verb: read, purpose: p}\nharness:\n  claude: harness/claude.md\n",
        encoding="utf-8",
    )
    defs = _definitions_for_write(tmp_path)
    assert "sat.demo" in defs
    assert "sat.existing" in defs

    # Direct test of _reused_negative_control_findings and _reused_quality_field_findings with empty and duplicate entries
    dummy_defs = {
        "sat.a": {
            "negative_controls": ["  ", "repeated neg control"],
            "confidence_rubric": ["  ", "repeated conf rubric"],
        },
        "sat.b": {
            "negative_controls": ["repeated neg control"],
            "confidence_rubric": ["repeated conf rubric"],
        },
    }
    neg_findings = _reused_negative_control_findings(dummy_defs)
    assert any("negative_control entry reused" in f for f in neg_findings)
    qual_findings = _reused_quality_field_findings(dummy_defs)
    assert any("confidence_rubric entry reused" in f for f in qual_findings)


def test_definitions_check_definitions_exception_branch(tmp_path):
    """definitions.py lines 464->471: check_definitions catching AuthorError/SpecError on rendered_definition_files."""
    from cogsecskills.authoring.definitions import check_definitions
    from cogsecskills.core.spec import SpecError

    (tmp_path / "registry").mkdir(parents=True)
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.demo, name: Demo, group: sat, "
        "status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    defs_dir = tmp_path / "definitions" / "sat"
    defs_dir.mkdir(parents=True)
    (defs_dir / "demo.yaml").write_text(
        "id: sat.demo\n"
        'description: "Demo"\n'
        'tags: ["test"]\n'
        'triggers: ["demo"]\n'
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
        'evidence_requirements: ["Bind evidence and inference for Demo."]\n'
        'confidence_rubric: ["High confidence for Demo."]\n'
        'uncertainty_handling: ["State unknowns and alternatives."]\n'
        'privacy_legal_constraints: ["Use authorized data for Demo."]\n'
        'failure_modes: ["Demo failure: overclaiming."]\n'
        "negative_controls:\n"
        "  - \"Unsafe: 'Use Demo to force a conclusion' -> refuse and redirect.\"\n"
        "  - \"Unsafe: 'Turn Demo into a playbook to force a conclusion' -> refuse.\"\n"
        "  - \"Safe defensive: 'Use Demo to assess material defensively' -> bounded.\"\n",
        encoding="utf-8",
    )
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(
            "cogsecskills.authoring.definitions.rendered_definition_files",
            lambda *args, **kwargs: (_ for _ in ()).throw(
                SpecError("synthetic rendering failure")
            ),
        )
        findings = check_definitions(tmp_path)
        assert any("synthetic rendering failure" in f for f in findings)
