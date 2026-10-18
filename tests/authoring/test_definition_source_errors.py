"""Behavioral authoring failures using real source inputs."""

from __future__ import annotations


from tests._support.validation_artifact_sources import (
    pytest,
    yaml,
)


def test_scenarios_route_no_match(tmp_path):
    """A query sharing no tokens with any skill's routing haystack is flagged
    as unrouted: the expected skill is not in the (empty) route matches."""
    from cogsecskills.artifacts.scenarios import check_scenarios

    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.x, name: X, group: sat, status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    # Build a skill on disk so check_scenarios can find the spec
    from cogsecskills.authoring.author import render_definition

    render_definition(
        {
            "id": "sat.x",
            "description": "A skill.",
            "tags": ["test"],
            "triggers": ["defensive use with evidence"],
            "tools": [
                {"verb": "read", "purpose": "p"},
                {"verb": "reason", "purpose": "assess evidence"},
                {"verb": "write", "purpose": "report findings"},
            ],
            "inputs": [{"name": "ctx", "type": "text", "required": True}],
            "outputs": [
                {"name": "product", "type": "md", "description": "the product"}
            ],
            "references": [],
            "workflow_steps": [
                {"verbs": ["read"], "title": "Gather", "text": "Read."},
                {"verbs": ["reason"], "title": "Assess", "text": "Assess."},
                {"verbs": ["write"], "title": "Report", "text": "Write."},
            ],
            "anti_criteria": ["Do not."],
        },
        root=tmp_path,
    )
    # Scenario whose query shares zero tokens with sat.x's routing haystack
    # (name/triggers/tags/summary/group) and with nothing else on disk, while
    # still naming authorized use for the safe_defensive framing check.
    sc = {
        "id": "no-route",
        "group": "sat",
        "kind": "safe_defensive",
        "query": "zzqxzzwvk authorized qqpzwwkx",
        "expected_skill": "sat.x",
        "expected_output_terms": ["product"],
        "required_quality_terms": ["evidence"],
        "expected_response": {
            "required_sections": ["s1", "s2", "s3"],
            "must_include_terms": [
                "evidence",
                "confidence",
                "uncertainty",
                "defensive",
            ],
            "must_exclude_terms": ["x", "y"],
        },
        "expected_answer": {
            "selected_skill": "sat.x",
            "answer_kind": "defensive_output",
            "sections": [
                {
                    "title": "A",
                    "body": "evidence inference gap confidence uncertainty defensive",
                },
                {"title": "B", "body": "evidence"},
                {"title": "C", "body": "evidence"},
            ],
            "rubric_scores": {},
        },
    }
    (tmp_path / "scenarios").mkdir()
    (tmp_path / "scenarios" / "defensive_readiness.yaml").write_text(
        yaml.safe_dump({"scenarios": [sc]}, sort_keys=False), encoding="utf-8"
    )
    findings = check_scenarios(tmp_path)
    assert any(
        "no-route: expected skill sat.x not in top 10 route matches (none)" in f
        for f in findings
    )


def test_load_definitions_missing_id(tmp_path):
    """load_definitions should raise AuthorError for a definition missing id."""
    from cogsecskills.authoring.definitions import AuthorError, load_definitions

    defs_dir = tmp_path / "definitions" / "sat"
    defs_dir.mkdir(parents=True)
    (defs_dir / "bad.yaml").write_text("description: no id\n", encoding="utf-8")
    with pytest.raises(AuthorError, match="missing id"):
        load_definitions(tmp_path)


def test_load_definitions_duplicate_id(tmp_path):
    """load_definitions should raise AuthorError for duplicate definition ids."""
    from cogsecskills.authoring.definitions import AuthorError, load_definitions

    defs_dir = tmp_path / "definitions"
    (defs_dir / "sat").mkdir(parents=True)
    (defs_dir / "cog").mkdir(parents=True)
    content = "id: sat.dup\ndescription: d\n"
    (defs_dir / "sat" / "dup.yaml").write_text(content, encoding="utf-8")
    (defs_dir / "cog" / "dup.yaml").write_text(content, encoding="utf-8")
    with pytest.raises(AuthorError, match="duplicate definition id"):
        load_definitions(tmp_path)


def test_author_slug():
    from cogsecskills.authoring.author import _slug

    assert _slug("sat.demo") == "demo"
    assert (
        _slug("cognitive_security.deepfake_synthetic_media_triage")
        == "deepfake_synthetic_media_triage"
    )


def test_author_require_missing_key():
    from cogsecskills.authoring.author import AuthorError, _require

    with pytest.raises(AuthorError, match="missing required key 'tools'"):
        _require({}, "tools")


def test_author_list_field_fallback():
    from cogsecskills.authoring.author import _list_field

    # Non-string, non-list source falls back
    result = _list_field({"key": 42}, "key", ["default"])
    assert result == ["default"]


def test_author_quality_list_string():
    from cogsecskills.authoring.author import _quality_list

    result = _quality_list({"key": "single string"}, "key")
    assert result == ["single string"]


def test_author_quality_list_empty_string():
    from cogsecskills.authoring.author import _quality_list

    result = _quality_list({"key": ""}, "key")
    assert result == []


def test_author_render_definition_non_mapping(tmp_path):
    """render_definition should raise AuthorError for non-mapping definition."""
    from cogsecskills.authoring.author import AuthorError, render_definition

    with pytest.raises(AuthorError, match="definition must be a mapping"):
        render_definition("notamapping", root=tmp_path)


def test_author_rendered_definition_files_non_mapping(tmp_path):
    """rendered_definition_files should raise AuthorError for non-mapping."""
    from cogsecskills.authoring.author import AuthorError, rendered_definition_files

    with pytest.raises(AuthorError, match="definition must be a mapping"):
        rendered_definition_files([1, 2], root=tmp_path)
