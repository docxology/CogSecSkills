"""Tests for the harness-neutral skill spec parsing and validation.

No mocks: every test parses real YAML-shaped dicts and asserts on the resulting
dataclasses, exercising both happy paths and the precise error messages.
"""

from __future__ import annotations

import pytest

from cogsecskills.spec import (
    SKILL_STATUSES,
    SkillIO,
    SkillSpec,
    SkillTool,
    SpecError,
    ToolVerb,
)


def _minimal_mapping(**overrides) -> dict:
    base = {
        "id": "sat.example",
        "name": "Example",
        "group": "sat",
        "summary": "An example skill.",
        "status": "planned",
    }
    base.update(overrides)
    return base


# --- ToolVerb ------------------------------------------------------------
def test_toolverb_coerce_from_string_and_enum():
    assert ToolVerb.coerce("read") is ToolVerb.READ
    assert ToolVerb.coerce("  REASON ") is ToolVerb.REASON
    assert ToolVerb.coerce(ToolVerb.WRITE) is ToolVerb.WRITE


def test_toolverb_coerce_rejects_unknown_and_nonstring():
    with pytest.raises(SpecError, match="unknown tool verb"):
        ToolVerb.coerce("teleport")
    with pytest.raises(SpecError, match="must be a string"):
        ToolVerb.coerce(42)


# --- SkillTool -----------------------------------------------------------
def test_skilltool_from_obj_ok():
    tool = SkillTool.from_obj({"verb": "read", "purpose": "gather inputs"})
    assert tool.verb is ToolVerb.READ
    assert tool.purpose == "gather inputs"


@pytest.mark.parametrize(
    "obj, match",
    [
        (["not", "a", "map"], "must be a mapping"),
        ({"purpose": "x"}, "missing required key 'verb'"),
        ({"verb": "read"}, "missing non-empty 'purpose'"),
        ({"verb": "read", "purpose": "  "}, "missing non-empty 'purpose'"),
    ],
)
def test_skilltool_from_obj_errors(obj, match):
    with pytest.raises(SpecError, match=match):
        SkillTool.from_obj(obj)


# --- SkillIO -------------------------------------------------------------
def test_skillio_defaults_and_required():
    io = SkillIO.from_obj({"name": "evidence"})
    assert io.type == "any" and io.required is False and io.description == ""
    io2 = SkillIO.from_obj(
        {"name": "q", "type": "text", "required": True, "description": "the question"}
    )
    assert io2.required is True and io2.type == "text"


def test_skillio_errors():
    with pytest.raises(SpecError, match="must be a mapping"):
        SkillIO.from_obj("nope")
    with pytest.raises(SpecError, match="missing non-empty 'name'"):
        SkillIO.from_obj({"type": "text"})


# --- SkillSpec -----------------------------------------------------------
def test_skillspec_minimal_defaults():
    spec = SkillSpec.from_mapping(_minimal_mapping())
    assert spec.status == "planned"
    assert spec.version == "0.1.0"
    assert spec.workflow == "workflow.md"
    assert spec.verbs == frozenset()
    assert spec.is_implemented is False


def test_skillspec_full_roundtrip():
    spec = SkillSpec.from_mapping(
        _minimal_mapping(
            status="implemented",
            tags=["a", "b", "  "],
            triggers="single trigger",
            tools=[
                {"verb": "read", "purpose": "p1"},
                {"verb": "write", "purpose": "p2"},
            ],
            inputs=[{"name": "x", "required": True}],
            outputs=[{"name": "y"}],
            references=["r1"],
            harness={"claude": "harness/claude.md"},
        )
    )
    assert spec.is_implemented
    assert spec.tags == ("a", "b")  # blank stripped
    assert spec.triggers == ("single trigger",)
    assert spec.verbs == {ToolVerb.READ, ToolVerb.WRITE}
    assert spec.inputs[0].required is True
    assert spec.harness["claude"] == "harness/claude.md"


@pytest.mark.parametrize("missing", ["id", "name", "group", "summary"])
def test_skillspec_missing_required(missing):
    data = _minimal_mapping()
    data[missing] = "   "
    with pytest.raises(SpecError, match=f"key {missing!r} must be a non-empty string"):
        SkillSpec.from_mapping(data)


@pytest.mark.parametrize("bad", [0, False, [], None, {"x": 1}])
def test_skillspec_required_field_wrong_type_rejected(bad):
    # str() coercion would silently turn 0/[]/None into "0"/"[]"/"None".
    data = _minimal_mapping(id=bad)
    with pytest.raises(SpecError, match="key 'id' must be a non-empty string"):
        SkillSpec.from_mapping(data)


def test_skillspec_status_must_be_string():
    with pytest.raises(SpecError, match="field 'status' must be a string"):
        SkillSpec.from_mapping(_minimal_mapping(status=3))


def test_skillio_required_must_be_bool():
    # The string "false" is truthy — coercion would invert required semantics.
    with pytest.raises(SpecError, match="field 'required' must be a boolean"):
        SkillIO.from_obj({"name": "x", "required": "false"})


def test_skillspec_list_items_must_be_strings():
    with pytest.raises(SpecError, match="items must be strings"):
        SkillSpec.from_mapping(_minimal_mapping(tags=[0, False]))


def test_skillspec_bad_status_and_type():
    with pytest.raises(SpecError, match="status 'bogus' invalid"):
        SkillSpec.from_mapping(_minimal_mapping(status="bogus"))
    with pytest.raises(SpecError, match="must be a mapping at top level"):
        SkillSpec.from_mapping(["not", "a", "mapping"])


def test_skillspec_bad_harness_and_list_fields():
    with pytest.raises(SpecError, match="field 'harness' must be a mapping"):
        SkillSpec.from_mapping(_minimal_mapping(harness=["claude"]))
    with pytest.raises(SpecError, match="must be a string or list of strings"):
        SkillSpec.from_mapping(_minimal_mapping(tags=123))


def test_all_statuses_accepted():
    for status in SKILL_STATUSES:
        spec = SkillSpec.from_mapping(_minimal_mapping(status=status))
        assert spec.status == status
