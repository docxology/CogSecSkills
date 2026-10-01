"""Behavioral edge-case branches across the quality and artifact surfaces.

Covers: validate.py (warnings vs errors, declared-path escape rejection),
release_metadata (non-mapping metadata files, license mismatch findings),
examples (not-in-registry, repeated-titles, operational misuse, drift checks),
scenarios (zero-overlap routing, malformed fixtures), definitions (missing and
duplicate ids), author helpers and rendering, insights (doctor findings),
dashboard verified-state parsing, evals drift, and assets_io cover mirrors.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

from cogsecskills.core.spec import SkillSpec, SkillTool, ToolVerb

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# === validate.py: warn/error severities and declared-path escape rejection ===


def test_validation_result_warn():
    """ValidationResult.warn should append a warning-severity issue."""
    from cogsecskills.quality.validate import SEVERITY_WARNING, ValidationResult

    result = ValidationResult()
    result.warn("sat.demo", "test warning")
    assert len(result.warnings) == 1
    assert result.warnings[0].severity == SEVERITY_WARNING
    assert result.ok is True  # warnings don't affect ok


def test_validation_result_error():
    """ValidationResult.error should append an error-severity issue."""
    from cogsecskills.quality.validate import SEVERITY_ERROR, ValidationResult

    result = ValidationResult()
    result.error("sat.demo", "test error")
    assert len(result.errors) == 1
    assert result.errors[0].severity == SEVERITY_ERROR
    assert result.ok is False


def _spec_with_harness_path(skills_dir, declared_path: str) -> SkillSpec:
    """Build a minimal spec whose claude adapter points at ``declared_path``."""
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        f"harness:\n  claude: {declared_path}\n",
        encoding="utf-8",
    )
    return SkillSpec.from_mapping(
        yaml.safe_load((skills_dir / "skill.yaml").read_text(encoding="utf-8"))
    )


def test_validate_skill_rejects_escaping_adapter_path(tmp_path):
    """A declared adapter path escaping the skill dir is an error, never a read."""
    from cogsecskills.quality.validate import validate_skill

    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    spec = _spec_with_harness_path(skills_dir, "../../outside/adapter.md")
    result = validate_skill(spec, skills_dir)
    assert any("must stay inside" in i.message for i in result.errors)
    assert not result.ok


def test_validate_skill_rejects_absolute_adapter_path(tmp_path):
    """A declared absolute adapter path is an error, never a read."""
    from cogsecskills.quality.validate import validate_skill

    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    spec = _spec_with_harness_path(skills_dir, "/etc/adapter.md")
    result = validate_skill(spec, skills_dir)
    assert any("must stay inside" in i.message for i in result.errors)
    assert not result.ok


# === release_metadata: malformed metadata files surface ValueError ===


def test_release_metadata_check_rejects_non_mapping_citation(tmp_path):
    """A non-mapping CITATION.cff surfaces a ValueError from the release check."""
    from cogsecskills.artifacts.release_metadata import check_release_metadata

    for f in ("pyproject.toml", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, tmp_path / f)
    (tmp_path / "CITATION.cff").write_text("- just a list\n", encoding="utf-8")
    with pytest.raises(ValueError, match="top level must be a mapping"):
        check_release_metadata(tmp_path)


def test_release_metadata_check_rejects_non_mapping_codemeta(tmp_path):
    """A non-mapping codemeta.json surfaces a ValueError from the release check."""
    from cogsecskills.artifacts.release_metadata import check_release_metadata

    for f in ("pyproject.toml", "CITATION.cff", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, tmp_path / f)
    (tmp_path / "codemeta.json").write_text("[1, 2, 3]\n", encoding="utf-8")
    with pytest.raises(ValueError, match="top level must be a mapping"):
        check_release_metadata(tmp_path)


def test_release_findings_pyproject_license_mismatch(tmp_path):
    """_findings should flag pyproject license mismatch."""
    from cogsecskills.artifacts.release_metadata import _findings, _metadata_payload

    for f in ("pyproject.toml", "CITATION.cff", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, tmp_path / f)
    for d in ("docs", "manuscript", "output", "figures"):
        if (PROJECT_ROOT / d).exists():
            shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    payload = _metadata_payload(tmp_path)
    # Corrupt the pyproject license
    payload["license"]["pyproject"] = "MIT"
    findings = _findings(
        payload, mode="local", runtime_git={"available": True, "dirty": False}
    )
    assert any("pyproject license is not Apache" in f for f in findings)


# === examples: not-in-registry, rendered-missing, provenance, repeated-titles ===


def test_examples_not_in_registry(tmp_path):
    """Example for a skill not in the registry should be flagged."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_SOURCE_PATH,
        _content_findings,
        load_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    source = tmp_path / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["skill_id"] = "sat.nonexistent_in_registry"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    examples = load_examples(tmp_path)
    findings = _content_findings(tmp_path, examples)
    assert any("not present in registry" in f for f in findings)


def test_examples_repeated_section_titles(tmp_path):
    """Example with repeated section titles should be flagged."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_SOURCE_PATH,
        _content_findings,
        load_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    source = tmp_path / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["sections"][1]["title"] = raw["examples"][0]["sections"][0][
        "title"
    ]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    examples = load_examples(tmp_path)
    findings = _content_findings(tmp_path, examples)
    assert any("repeats section titles" in f for f in findings)


def test_examples_operational_misuse_in_text(tmp_path):
    """Example with operational misuse phrase should be flagged."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_SOURCE_PATH,
        _content_findings,
        load_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    source = tmp_path / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["sections"][0]["body"] += " step-by-step operational playbook"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    examples = load_examples(tmp_path)
    findings = _content_findings(tmp_path, examples)
    assert any("operational misuse detail" in f for f in findings)


def test_examples_check_missing_generated_json(tmp_path):
    """check_examples should flag missing generated JSON file."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_JSON_PATH,
        check_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    (tmp_path / EXAMPLES_JSON_PATH).unlink()
    findings = check_examples(tmp_path)
    assert any("missing generated examples file" in f for f in findings)


def test_examples_check_stale_generated_md(tmp_path):
    """check_examples should flag stale generated markdown."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_MD_PATH,
        check_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    (tmp_path / EXAMPLES_MD_PATH).write_text("manual edit\n", encoding="utf-8")
    findings = check_examples(tmp_path)
    assert any("stale generated examples file" in f for f in findings)


# === scenarios: route no-match, not-implemented, workflow-missing, too-few-steps ===


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
            "rubric_scores": {
                k: 2
                for k in (
                    "skill_fit",
                    "evidence_labeling",
                    "uncertainty",
                    "defensive_boundary",
                    "output_usefulness",
                )
            },
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


# === definitions: load_definitions missing-id and duplicate ===


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


# === author: _slug, _require, _list_field, _quality_list edge cases ===


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


# === insights: doctor anti-criteria and empty-quality-field ===


def test_doctor_finds_few_anti_criteria(tmp_path):
    """doctor should warn on skills with fewer than min_anti_criteria."""
    from cogsecskills.core.config import Config
    from cogsecskills.quality.insights import doctor

    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "skills.yaml").write_text(
        "skills:\n  - {id: sat.demo, name: Demo, group: sat, "
        "status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n"
        "defensive_boundary: 'defensive use'\n"
        "misuse_redirect: 'refuse and redirect'\n"
        "evidence_requirements: ['label evidence and inference']\n"
        "confidence_rubric: ['high confidence for Demo']\n"
        "uncertainty_handling: ['state unknowns and alternatives']\n"
        "privacy_legal_constraints: ['use authorized data for Demo']\n"
        "failure_modes: ['Demo failure']\n"
        "negative_controls:\n"
        "  - 'Unsafe: refuse and redirect to safe defensive.'\n"
        "  - 'Safe defensive: use to assess defensively.'\n"
        "references: ['ref']\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# Demo\n", encoding="utf-8")
    # Workflow with only 1 anti-criteria (below min_anti_criteria=2)
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nText.\n## Step 2 — T (reason)\nText.\n## Step 3 — U (write)\nText.\n"
        "## Anti-criteria\n- Do not.\n",
        encoding="utf-8",
    )
    harness_dir = skills_dir / "harness"
    harness_dir.mkdir()
    for h in ("claude", "codex", "hermes"):
        (harness_dir / f"{h}.md").write_text(
            "| `read` | tool | note |\n", encoding="utf-8"
        )
    findings = doctor(tmp_path, Config.defaults())
    assert any("anti-criteria" in f["message"] for f in findings)


def test_doctor_finds_empty_quality_field(tmp_path):
    """doctor should warn on skills with empty quality fields."""
    from cogsecskills.quality.insights import _quality_findings

    spec = SkillSpec(
        id="sat.demo",
        name="Demo",
        group="sat",
        summary="s",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="p"),),
        defensive_boundary="",  # empty
        misuse_redirect="refuse and redirect to safe defensive",
        negative_controls=(
            "Unsafe: refuse and redirect to safe defensive.",
            "Safe defensive: use to assess defensively.",
        ),
        evidence_requirements=("label evidence and inference",),
        confidence_rubric=("high confidence for Demo",),
        uncertainty_handling=("state unknowns and alternatives",),
        privacy_legal_constraints=("use authorized data for Demo",),
        failure_modes=("Demo failure",),
    )
    findings = _quality_findings(spec, "## Step 1 — S (read)\nText.")
    assert any(
        "missing quality field: defensive_boundary" in f["message"] for f in findings
    )


def test_doctor_finds_missing_unsafe_redirect():
    """doctor should warn when negative controls lack unsafe/redirect coverage."""
    from cogsecskills.quality.insights import _quality_findings

    spec = SkillSpec(
        id="sat.demo",
        name="Demo",
        group="sat",
        summary="s",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="p"),),
        defensive_boundary="defensive use",
        misuse_redirect="just say no",
        negative_controls=(
            "Always be careful.",  # No "unsafe" or "redirect"
            "Safe defensive: use to assess defensively.",
        ),
        evidence_requirements=("label evidence and inference",),
        confidence_rubric=("high confidence for Demo",),
        uncertainty_handling=("state unknowns and alternatives",),
        privacy_legal_constraints=("use authorized data for Demo",),
        failure_modes=("Demo failure",),
    )
    findings = _quality_findings(spec, "## Step 1 — S (read)\nText.")
    assert any("unsafe redirect coverage" in f["message"] for f in findings)


# === assets_io: missing cover mirror ===


def test_check_assets_missing_cover_mirror(tmp_path):
    """check_assets should flag a missing cover mirror."""
    from cogsecskills.artifacts.manuscript_assets.assets_io import check_assets
    from cogsecskills.artifacts.manuscript_assets.figures import (
        _PNG_SIGNATURE,
        FIGURE_NAMES,
    )
    from cogsecskills.artifacts.manuscript_assets.paths import (
        CATALOGUE_PATH,
        DATA_CSV_PATH,
        DATA_JSON_PATH,
        MATRIX_PATH,
    )

    (tmp_path / "registry").mkdir(parents=True, exist_ok=True)
    (tmp_path / "registry" / "skills.yaml").write_text("skills: []\n", encoding="utf-8")
    (tmp_path / "registry" / "groups.yaml").write_text("groups: []\n", encoding="utf-8")
    for p in (CATALOGUE_PATH, MATRIX_PATH, DATA_JSON_PATH, DATA_CSV_PATH):
        full = tmp_path / p
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text("dummy", encoding="utf-8")
    fig_dir = tmp_path / "output" / "figures"
    fig_dir.mkdir(parents=True)
    for name in FIGURE_NAMES:
        (fig_dir / name).write_bytes(_PNG_SIGNATURE + b"\x00" * 2000)
    # Don't create the cover mirror — it should be flagged as missing
    findings = check_assets(tmp_path)
    assert any("missing generated cover image mirror" in f for f in findings)


# === evals: check_evals with stale source only ===


def test_check_evals_stale_source_only(tmp_path):
    """check_evals should flag a stale offline evaluation source."""
    from cogsecskills.artifacts.evals import EVALS_SOURCE_PATH, check_evals, write_evals

    for d in ("registry", "skills", "scenarios"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_evals(tmp_path)
    # Make the valid source noncanonical without introducing a parse failure.
    source = tmp_path / EVALS_SOURCE_PATH
    source.write_text(
        source.read_text(encoding="utf-8") + "# manual edit\n", encoding="utf-8"
    )
    findings = check_evals(tmp_path)
    assert any("stale offline evaluation source" in f for f in findings)
