"""Behavioral quality failures using real source inputs."""

from __future__ import annotations


from tests._support.quality_generated_outputs import (
    SkillSpec,
    SkillTool,
    ToolVerb,
    yaml,
)


def test_validate_skill_missing_adapter_verbs(tmp_path):
    """An adapter that doesn't bind all declared verbs should be flagged."""
    from cogsecskills.quality.validate import validate_skill

    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n  - {verb: write, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# Demo\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nText.\n", encoding="utf-8"
    )
    harness_dir = skills_dir / "harness"
    harness_dir.mkdir()
    # Claude adapter only binds `read`, not `write`
    (harness_dir / "claude.md").write_text(
        "| `read` | tool | note |\n", encoding="utf-8"
    )
    (harness_dir / "codex.md").write_text(
        "| `read` | tool |\n| `write` | tool |\n", encoding="utf-8"
    )
    (harness_dir / "hermes.md").write_text(
        "| `read` | tool |\n| `write` | tool |\n", encoding="utf-8"
    )
    spec = SkillSpec.from_mapping(
        yaml.safe_load((skills_dir / "skill.yaml").read_text(encoding="utf-8"))
    )
    result = validate_skill(spec, skills_dir)
    assert any("does not bind declared tool verbs" in i.message for i in result.errors)


def test_conformance_report_with_load_failures(tmp_path):
    """conformance_report should handle registry/spec load failures gracefully."""
    from cogsecskills.quality.validate import conformance_report

    # tmp_path with no registry: validate_library will catch the error
    report = conformance_report(tmp_path)
    assert report["registry_total"] == 0
    assert report["on_disk_skills"] == 0


def test_validate_skill_unsupported_verbs(tmp_path):
    """A harness that can't realise a verb should be flagged."""
    from cogsecskills.core.harness import check_conformance
    from cogsecskills.quality.validate import validate_skill

    skills_dir = tmp_path / "skills" / "sat" / "demo"
    skills_dir.mkdir(parents=True)
    (skills_dir / "skill.yaml").write_text(
        "id: sat.demo\nname: Demo\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# Demo\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nText.\n", encoding="utf-8"
    )
    harness_dir = skills_dir / "harness"
    harness_dir.mkdir()
    for h in ("claude", "codex", "hermes"):
        (harness_dir / f"{h}.md").write_text(
            "| `read` | tool | note |\n", encoding="utf-8"
        )
    spec = SkillSpec.from_mapping(
        yaml.safe_load((skills_dir / "skill.yaml").read_text(encoding="utf-8"))
    )
    # Pass a harness support map where claude can't realise 'read'
    narrow = {"claude": frozenset()}
    conf = check_conformance(spec, support=narrow, harnesses=("claude",))
    assert conf["claude"].unsupported_verbs == (ToolVerb.READ,)

    # validate_skill exposes the same support seam as check_conformance: a
    # narrower harness support map must fail conformance loudly.
    res = validate_skill(spec, skills_dir, support={"claude": frozenset()})
    assert any("cannot realise verbs" in str(issue.message) for issue in res.errors)


def test_doctor_finds_few_workflow_steps(tmp_path):
    """doctor should warn on skills with fewer than min_workflow_steps."""
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
    # Workflow with only 2 steps (below min_workflow_steps=3)
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nText.\n## Step 2 — T (write)\nText.\n"
        "## Anti-criteria\n- Do not.\n- Do not 2.\n",
        encoding="utf-8",
    )
    harness_dir = skills_dir / "harness"
    harness_dir.mkdir()
    for h in ("claude", "codex", "hermes"):
        (harness_dir / f"{h}.md").write_text(
            "| `read` | tool | note |\n", encoding="utf-8"
        )
    cfg = Config.defaults()
    findings = doctor(tmp_path, cfg)
    assert any("workflow steps" in f["message"] for f in findings)


def test_doctor_finds_missing_references(tmp_path):
    """doctor should warn on implemented skills with no references when require_references is True."""
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
        "  - 'Safe defensive: use to assess defensively.'\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# Demo\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nText.\n## Step 2 — T (reason)\nText.\n## Step 3 — U (write)\nText.\n"
        "## Anti-criteria\n- Do not.\n- Do not 2.\n",
        encoding="utf-8",
    )
    harness_dir = skills_dir / "harness"
    harness_dir.mkdir()
    for h in ("claude", "codex", "hermes"):
        (harness_dir / f"{h}.md").write_text(
            "| `read` | tool | note |\n", encoding="utf-8"
        )
    cfg = Config(require_references=True)
    findings = doctor(tmp_path, cfg)
    assert any("no references" in f["message"] for f in findings)


def test_doctor_finds_chain_of_thought(tmp_path):
    """doctor should warn on chain-of-thought wording in negative controls."""
    from cogsecskills.quality.insights import _quality_findings

    spec = SkillSpec(
        id="sat.demo",
        name="Demo",
        group="sat",
        summary="s",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="p"),),
        defensive_boundary="defensive use",
        misuse_redirect="refuse and redirect",
        negative_controls=(
            "Unsafe: chain-of-thought reasoning to exploit. Redirect to safe defensive.",
            "Safe defensive: use to assess defensively.",
        ),
        evidence_requirements=("label evidence and inference",),
        confidence_rubric=("high confidence for Demo",),
        uncertainty_handling=("state unknowns and alternatives",),
        privacy_legal_constraints=("use authorized data for Demo",),
        failure_modes=("Demo failure",),
    )
    findings = _quality_findings(spec, "## Step 1 — S (read)\nText.")
    assert any("chain-of-thought" in f["message"] for f in findings)


def test_doctor_finds_missing_evidence_inference_labels(tmp_path):
    """doctor should warn when evidence_requirements lacks 'evidence' or 'inference'."""
    from cogsecskills.quality.insights import _quality_findings

    spec = SkillSpec(
        id="sat.demo",
        name="Demo",
        group="sat",
        summary="s",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="p"),),
        defensive_boundary="defensive use",
        misuse_redirect="refuse and redirect to safe defensive",
        negative_controls=(
            "Unsafe: refuse and redirect to safe defensive.",
            "Safe defensive: use to assess defensively.",
        ),
        evidence_requirements=(
            "just list observations",
        ),  # Missing "evidence" and "inference"
        confidence_rubric=("high confidence for Demo",),
        uncertainty_handling=("state unknowns and alternatives",),
        privacy_legal_constraints=("use authorized data for Demo",),
        failure_modes=("Demo failure",),
    )
    findings = _quality_findings(spec, "## Step 1 — S (read)\nText.")
    assert any("evidence and inference" in f["message"] for f in findings)


def test_doctor_finds_missing_unknown_alternative_labels():
    """doctor should warn when uncertainty_handling lacks 'unknown' or 'alternative'."""
    from cogsecskills.quality.insights import _quality_findings

    spec = SkillSpec(
        id="sat.demo",
        name="Demo",
        group="sat",
        summary="s",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="p"),),
        defensive_boundary="defensive use",
        misuse_redirect="refuse and redirect to safe defensive",
        negative_controls=(
            "Unsafe: refuse and redirect to safe defensive.",
            "Safe defensive: use to assess defensively.",
        ),
        evidence_requirements=("label evidence and inference",),
        confidence_rubric=("high confidence for Demo",),
        uncertainty_handling=(
            "state what is unclear",
        ),  # Missing "unknown" and "alternative"
        privacy_legal_constraints=("use authorized data for Demo",),
        failure_modes=("Demo failure",),
    )
    findings = _quality_findings(spec, "## Step 1 — S (read)\nText.")
    assert any("unknowns and alternatives" in f["message"] for f in findings)


def test_doctor_finds_sensitive_skill_missing_guardrails():
    """doctor should warn when a sensitive skill lacks privacy/authorized guardrails."""
    from cogsecskills.quality.insights import _quality_findings

    spec = SkillSpec(
        id="cognitive_security.demo",
        name="Demo",
        group="cognitive_security",
        summary="s",
        status="implemented",
        tools=(SkillTool(verb=ToolVerb.READ, purpose="p"),),
        defensive_boundary="defensive use only",
        misuse_redirect="refuse and redirect to safe defensive",
        negative_controls=(
            "Unsafe: refuse and redirect.",
            "Safe defensive: use to assess defensively.",
        ),
        evidence_requirements=("label evidence and inference",),
        confidence_rubric=("high confidence for Demo",),
        uncertainty_handling=("state unknowns and alternatives",),
        privacy_legal_constraints=(
            "use authorized data",
        ),  # Has "authorized" but no "privacy"
        failure_modes=("Demo failure",),
    )
    findings = _quality_findings(spec, "## Step 1 — S (read)\nText.")
    # The sensitive check looks for "refuse", "defensive", "privacy", "authorized"
    # in the lower text of defensive_boundary + misuse_redirect + negative_controls + workflow
    # "privacy" is not in the lower text (only in privacy_legal_constraints, not in lower)
    assert any("sensitive skill" in f["message"] for f in findings)
