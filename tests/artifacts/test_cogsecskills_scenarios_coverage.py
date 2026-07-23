"""Coverage tests for scenarios.py remaining uncovered lines.

Lines 369, 493, 504, 508, 519, 558, 562.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from cogsecskills.artifacts.scenarios import check_scenarios
from cogsecskills.authoring.author import render_definition

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _seed(root: Path) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        "  - {id: sat.x, name: X, group: sat, status: implemented, summary: s}\n",
        encoding="utf-8",
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


def _render_skill(root: Path) -> None:
    render_definition(
        {
            "id": "sat.x",
            "description": "A skill.",
            "tags": ["test"],
            "triggers": ["defensive use with evidence"],
            "tools": [{"verb": "read", "purpose": "p"}],
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
        root=root,
    )


def _safe_sc() -> dict:
    return {
        "id": "sc-safe",
        "group": "sat",
        "kind": "safe_defensive",
        "query": "defensive use with evidence",
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


def _write(root: Path, scenarios: list[dict]) -> None:
    (root / "scenarios").mkdir(parents=True, exist_ok=True)
    (root / "scenarios" / "defensive_readiness.yaml").write_text(
        yaml.safe_dump({"scenarios": scenarios}, sort_keys=False),
        encoding="utf-8",
    )


def test_unsafe_missing_unsafe_keyword(tmp_path):
    """Line 369: unsafe scenario without 'unsafe' or 'misuse' in query."""
    _seed(tmp_path)
    _render_skill(tmp_path)
    sc = _safe_sc()
    sc["kind"] = "unsafe_redirect"
    sc["query"] = "force a conclusion and redirect"
    sc["expected_answer"]["answer_kind"] = "refusal_redirect"
    sc["expected_response"]["required_sections"] = [
        "Refusal and redirect",
        "Safe alternative",
        "Evidence",
        "Confidence",
    ]
    sc["expected_response"]["must_include_terms"] = [
        "refuse",
        "redirect",
        "safe",
        "evidence",
        "confidence",
        "uncertainty",
    ]
    sc["expected_answer"]["sections"][0]["body"] = (
        "refuse redirect safe evidence inference gap confidence uncertainty"
    )
    _write(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("must name unsafe or misuse framing" in f for f in findings)


def test_spec_not_implemented(tmp_path):
    """Line 504: scenario pointing to a non-implemented skill."""
    _seed(tmp_path)
    # Create a stub skill (status=stub, not implemented)
    skills_dir = tmp_path / "skills" / "sat" / "x"
    skills_dir.mkdir(parents=True)
    (skills_dir / "skill.yaml").write_text(
        "id: sat.x\nname: X\ngroup: sat\nsummary: s\nstatus: stub\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# X\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nT.\n## Step 2 — T (reason)\nT.\n## Step 3 — U (write)\nT.\n"
        "## Anti-criteria\n- Do not.\n- Do not 2.\n",
        encoding="utf-8",
    )
    (skills_dir / "harness").mkdir()
    for h in ("claude", "codex", "hermes"):
        (skills_dir / "harness" / f"{h}.md").write_text(
            "| `read` | t | n |\n", encoding="utf-8"
        )
    sc = _safe_sc()
    _write(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("is not implemented" in f for f in findings)


def test_workflow_missing(tmp_path):
    """Line 508: skill directory has no workflow.md."""
    _seed(tmp_path)
    skills_dir = tmp_path / "skills" / "sat" / "x"
    skills_dir.mkdir(parents=True)
    (skills_dir / "skill.yaml").write_text(
        "id: sat.x\nname: X\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# X\n", encoding="utf-8")
    # No workflow.md!
    (skills_dir / "harness").mkdir()
    for h in ("claude", "codex", "hermes"):
        (skills_dir / "harness" / f"{h}.md").write_text(
            "| `read` | t | n |\n", encoding="utf-8"
        )
    sc = _safe_sc()
    _write(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("workflow missing" in f for f in findings)


def test_workflow_too_few_steps(tmp_path):
    """Line 519: workflow with fewer than 3 steps."""
    _seed(tmp_path)
    skills_dir = tmp_path / "skills" / "sat" / "x"
    skills_dir.mkdir(parents=True)
    (skills_dir / "skill.yaml").write_text(
        "id: sat.x\nname: X\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# X\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nT.\n## Step 2 — T (write)\nT.\n"
        "## Anti-criteria\n- Do not.\n- Do not 2.\n",
        encoding="utf-8",
    )
    (skills_dir / "harness").mkdir()
    for h in ("claude", "codex", "hermes"):
        (skills_dir / "harness" / f"{h}.md").write_text(
            "| `read` | t | n |\n", encoding="utf-8"
        )
    sc = _safe_sc()
    _write(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("fewer than 3 steps" in f for f in findings)


def test_adapter_missing(tmp_path):
    """Line 558: harness adapter file missing."""
    _seed(tmp_path)
    skills_dir = tmp_path / "skills" / "sat" / "x"
    skills_dir.mkdir(parents=True)
    (skills_dir / "skill.yaml").write_text(
        "id: sat.x\nname: X\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness:\n  claude: harness/claude.md\n  codex: harness/codex.md\n  hermes: harness/hermes.md\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# X\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nT.\n## Step 2 — T (r)\nT.\n## Step 3 — U (w)\nT.\n"
        "## Anti-criteria\n- Do not.\n- Do not 2.\n",
        encoding="utf-8",
    )
    (skills_dir / "harness").mkdir()
    # Only create codex and hermes adapters — claude is missing
    for h in ("codex", "hermes"):
        (skills_dir / "harness" / f"{h}.md").write_text(
            "| `read` | t | n |\n", encoding="utf-8"
        )
    sc = _safe_sc()
    _write(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("harness adapter" in f and "missing" in f for f in findings)


def test_no_adapters_declared(tmp_path):
    """Line 562: spec with empty harness map."""
    _seed(tmp_path)
    skills_dir = tmp_path / "skills" / "sat" / "x"
    skills_dir.mkdir(parents=True)
    (skills_dir / "skill.yaml").write_text(
        "id: sat.x\nname: X\ngroup: sat\nsummary: s\nstatus: implemented\n"
        "tools:\n  - {verb: read, purpose: p}\n"
        "harness: {}\n",
        encoding="utf-8",
    )
    (skills_dir / "SKILL.md").write_text("# X\n", encoding="utf-8")
    (skills_dir / "workflow.md").write_text(
        "# W\n\n## Step 1 — S (read)\nT.\n## Step 2 — T (r)\nT.\n## Step 3 — U (w)\nT.\n"
        "## Anti-criteria\n- Do not.\n- Do not 2.\n",
        encoding="utf-8",
    )
    sc = _safe_sc()
    _write(tmp_path, [sc])
    findings = check_scenarios(tmp_path)
    assert any("declares no adapters" in f for f in findings)
