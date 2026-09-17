"""Regression tests: explicit YAML nulls must never beat a spec field default.

``str(...)`` coercion turns an explicit ``null`` (or a numeric scalar) into the
strings ``"None"`` / ``"5"``, which are truthy and therefore silently replace
the declared default. Every optional text field must demand a real string.
"""

from __future__ import annotations

import pytest
import yaml

from cogsecskills.core.spec import SkillSpec, SpecError


def _base_mapping() -> dict:
    """A minimal valid skill mapping (only the four required keys)."""
    return {
        "id": "sat.demo",
        "name": "Demo Technique",
        "group": "sat",
        "summary": "A demo technique.",
    }


def _from_yaml(text: str) -> SkillSpec:
    return SkillSpec.from_mapping(yaml.safe_load(text))


def test_explicit_null_version_falls_back_to_default():
    data = _base_mapping() | {"version": None}
    spec = SkillSpec.from_mapping(data)
    assert spec.version == "0.1.0"


def test_explicit_null_description_is_empty():
    data = _base_mapping() | {"description": None}
    spec = SkillSpec.from_mapping(data)
    assert spec.description == ""


def test_explicit_null_version_via_real_yaml():
    # Parse actual YAML so the None reaches from_mapping exactly as a loader
    # would deliver it.
    spec = _from_yaml(
        "id: sat.demo\n"
        "name: Demo Technique\n"
        "group: sat\n"
        "summary: A demo technique.\n"
        "version: null\n"
    )
    assert spec.version == "0.1.0"


def test_explicit_null_description_via_real_yaml():
    spec = _from_yaml(
        "id: sat.demo\n"
        "name: Demo Technique\n"
        "group: sat\n"
        "summary: A demo technique.\n"
        "description: null\n"
    )
    assert spec.description == ""


@pytest.mark.parametrize(
    ("key", "default"),
    [
        ("ageint_topic", ""),
        ("defensive_boundary", ""),
        ("misuse_redirect", ""),
        ("workflow", "workflow.md"),
    ],
)
def test_explicit_null_optional_text_fields_use_defaults(key: str, default: str):
    data = _base_mapping() | {key: None}
    spec = SkillSpec.from_mapping(data)
    assert getattr(spec, key) == default


def test_numeric_version_never_coerces():
    """``version: 5`` must fall back to the default, not become the string "5"."""
    data = _base_mapping() | {"version": 5}
    spec = SkillSpec.from_mapping(data)
    assert spec.version == "0.1.0"


def test_numeric_workflow_never_coerces():
    data = _base_mapping() | {"workflow": 7}
    spec = SkillSpec.from_mapping(data)
    assert spec.workflow == "workflow.md"


def test_empty_string_version_falls_back_to_default():
    data = _base_mapping() | {"version": "  "}
    spec = SkillSpec.from_mapping(data)
    assert spec.version == "0.1.0"


def test_valid_strings_still_parse_and_strip():
    data = _base_mapping() | {"version": " 1.2.3 ", "description": " Real text. "}
    spec = SkillSpec.from_mapping(data)
    assert spec.version == "1.2.3"
    assert spec.description == "Real text."


def test_harness_null_path_is_rejected_not_coerced():
    """``harness: {claude: null}`` previously became the path string "None"."""
    data = _base_mapping() | {"harness": {"claude": None}}
    with pytest.raises(SpecError, match="harness.*string paths"):
        SkillSpec.from_mapping(data)


def test_harness_non_string_key_is_rejected():
    data = _base_mapping() | {"harness": {1: "harness/claude.md"}}
    with pytest.raises(SpecError, match="harness.*string paths"):
        SkillSpec.from_mapping(data)


def test_harness_valid_mapping_round_trips():
    data = _base_mapping() | {"harness": {"claude": " harness/claude.md "}}
    spec = SkillSpec.from_mapping(data)
    assert spec.harness == {"claude": "harness/claude.md"}


# --- io entries: same null-coercion class --------------------------------------


def test_io_null_name_is_rejected_not_coerced():
    """`name: null` previously became the string "None", passing the check."""
    data = _base_mapping() | {"inputs": [{"name": None, "type": "file"}]}
    with pytest.raises(SpecError, match="io entry missing non-empty 'name'"):
        SkillSpec.from_mapping(data)


def test_io_null_type_falls_back_to_any():
    data = _base_mapping() | {"inputs": [{"name": "report", "type": None}]}
    spec = SkillSpec.from_mapping(data)
    assert spec.inputs[0].type == "any"


def test_io_null_description_is_empty():
    data = _base_mapping() | {"inputs": [{"name": "report", "description": None}]}
    spec = SkillSpec.from_mapping(data)
    assert spec.inputs[0].description == ""


def test_io_numeric_type_never_coerces():
    data = _base_mapping() | {"inputs": [{"name": "report", "type": 7}]}
    spec = SkillSpec.from_mapping(data)
    assert spec.inputs[0].type == "any"


def test_io_valid_strings_still_parse():
    data = _base_mapping() | {
        "inputs": [{"name": " report ", "type": " file ", "description": " d "}],
    }
    spec = SkillSpec.from_mapping(data)
    assert spec.inputs[0].name == "report"
    assert spec.inputs[0].type == "file"
    assert spec.inputs[0].description == "d"


# --- tool entries: same null-coercion class ------------------------------------


def test_tool_null_purpose_is_rejected_not_coerced():
    data = _base_mapping() | {"tools": [{"verb": "read", "purpose": None}]}
    with pytest.raises(SpecError, match="missing non-empty 'purpose'"):
        SkillSpec.from_mapping(data)


def test_tool_purpose_still_strips():
    data = _base_mapping() | {
        "tools": [{"verb": "read", "purpose": " ingest inputs "}],
    }
    spec = SkillSpec.from_mapping(data)
    assert spec.tools[0].purpose == "ingest inputs"
