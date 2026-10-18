"""Behavioral quality failures using real source inputs."""

from __future__ import annotations


from tests._support.validation_artifact_sources import (
    SkillSpec,
    SkillTool,
    ToolVerb,
    _spec_with_harness_path,
)


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
