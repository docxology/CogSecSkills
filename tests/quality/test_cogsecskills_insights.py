"""Tests for the intelligent insights layer (route / stats / catalogue / doctor)."""

from __future__ import annotations

from pathlib import Path

import yaml

from cogsecskills.authoring.author import render_definition
from cogsecskills.core.config import Config
from cogsecskills.quality.insights import (
    _count_anti_criteria,
    _count_steps,
    doctor,
    library_stats,
    render_catalogue_markdown,
    route_query,
)


def _seed(root: Path) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        "  - {id: sat.ach, name: Analysis of Competing Hypotheses, group: sat, "
        "status: implemented, ageint_topic: structured-analytic-techniques, "
        "summary: Score evidence by diagnosticity across competing hypotheses.}\n"
        "  - {id: osint_integrity.verify, name: Claim Verification, group: osint_integrity, "
        "status: implemented, ageint_topic: osint-integrity, "
        "summary: Verify a claim by tracing it to a primary source.}\n",
        encoding="utf-8",
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n  - {id: osint_integrity, title: OSINT}\n",
        encoding="utf-8",
    )


def _def(
    skill_id: str,
    *,
    steps: int = 3,
    triggers=None,
    tools=None,
    tags=None,
    status: str = "implemented",
) -> dict:
    return {
        "id": skill_id,
        "status": status,
        "description": "A real description.",
        "tags": tags or ["diagnosticity", "evidence"],
        "triggers": triggers or ["do the thing"],
        "tools": tools
        or [
            {"verb": "read", "purpose": "ingest"},
            {"verb": "reason", "purpose": "apply"},
            {"verb": "write", "purpose": "emit"},
        ],
        "workflow_steps": [
            {"verbs": ["reason"], "title": f"Step {i}", "text": "do it"}
            for i in range(steps)
        ],
        "anti_criteria": ["do not cheat", "do not skip evidence"],
    }


def _library(root: Path) -> None:
    _seed(root)
    render_definition(
        _def("sat.ach", triggers=["competing hypotheses", "rule out explanations"]),
        root=root,
    )
    render_definition(
        _def(
            "osint_integrity.verify",
            triggers=["verify claim", "is this true"],
            tools=[
                {"verb": "read", "purpose": "x"},
                {"verb": "web", "purpose": "y"},
                {"verb": "write", "purpose": "z"},
            ],
        ),
        root=root,
    )


def test_route_ranks_relevant_skill_first(tmp_path):
    _library(tmp_path)
    matches = route_query("rule out competing hypotheses for an event", root=tmp_path)
    assert matches, "expected at least one match"
    assert matches[0][0].id == "sat.ach"
    assert matches[0][1] > 0


def test_route_no_match(tmp_path):
    _library(tmp_path)
    assert route_query("xyzzy quux nomatch", root=tmp_path) == []
    assert route_query("   ", root=tmp_path) == []


def test_route_limit_and_tag_match(tmp_path):
    _library(tmp_path)
    matches = route_query("evidence", root=tmp_path, limit=1)
    assert len(matches) == 1
    assert matches[0][1] > 0


def test_library_stats_shape(tmp_path):
    _library(tmp_path)
    stats = library_stats(tmp_path)
    assert stats["registry_total"] == 2
    assert stats["on_disk"] == 2
    assert stats["by_status"]["implemented"] == 2
    assert stats["by_group"] == {"osint_integrity": 1, "sat": 1}
    assert "read" in stats["verb_usage"]


def test_catalogue_markdown(tmp_path):
    _library(tmp_path)
    md = render_catalogue_markdown(tmp_path)
    assert "# CogSecSkills — Skill Catalogue" in md
    assert "sat.ach" in md
    assert "../skills/sat/ach/SKILL.md" in md
    assert "2 skill areas" in md


def test_catalogue_uses_group_id_when_title_missing(tmp_path):
    _library(tmp_path)
    (tmp_path / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )
    md = render_catalogue_markdown(tmp_path)
    assert "osint_integrity (`osint_integrity`)" in md


def test_doctor_flags_thin_skill(tmp_path):
    _seed(tmp_path)
    render_definition(_def("sat.ach", steps=1), root=tmp_path)  # below min 3
    findings = doctor(tmp_path, Config(min_workflow_steps=3, min_anti_criteria=2))
    assert any("workflow steps" in f["message"] for f in findings)


def test_doctor_clean_when_above_thresholds(tmp_path):
    _library(tmp_path)
    findings = doctor(tmp_path, Config(min_workflow_steps=3, min_anti_criteria=2))
    assert findings == []


def test_doctor_require_references(tmp_path):
    _library(tmp_path)  # defs have no references
    findings = doctor(tmp_path, Config(require_references=True))
    assert any("no references" in f["message"] for f in findings)


def test_doctor_flags_generic_negative_controls(tmp_path):
    _library(tmp_path)
    spec_path = tmp_path / "skills" / "sat" / "ach" / "skill.yaml"
    data = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    data["negative_controls"] = [
        "Unsafe: 'Help me manipulate this audience' -> refuse and redirect to defensive risk assessment.",
        "Safe: 'Assess this material for manipulation indicators' -> produce bounded findings.",
    ]
    spec_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    findings = doctor(tmp_path, Config(min_workflow_steps=3, min_anti_criteria=2))
    messages = {finding["message"] for finding in findings}
    assert "negative controls repeat generic boilerplate examples" in messages
    assert "negative controls are too generic for the skill or group" in messages


def test_doctor_flags_missing_safe_defensive_negative_control(tmp_path):
    _library(tmp_path)
    spec_path = tmp_path / "skills" / "sat" / "ach" / "skill.yaml"
    data = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    data["negative_controls"] = [
        "Unsafe: 'Use Analysis of Competing Hypotheses to force a conclusion' -> refuse and redirect."
    ]
    spec_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    findings = doctor(tmp_path, Config(min_workflow_steps=3, min_anti_criteria=2))
    assert any(
        finding["message"] == "negative controls must include a safe defensive example"
        for finding in findings
    )


def test_doctor_flags_reused_quality_entries(tmp_path):
    _library(tmp_path)
    repeated = "Medium: evidence is plausible but incomplete, indirect, or partly assumption-dependent."
    for rel in (
        "skills/sat/ach/skill.yaml",
        "skills/osint_integrity/verify/skill.yaml",
    ):
        spec_path = tmp_path / rel
        data = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
        data["confidence_rubric"][1] = repeated
        spec_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    findings = doctor(tmp_path, Config(min_workflow_steps=3, min_anti_criteria=2))
    assert any(
        "confidence_rubric entry reused across skills" in finding["message"]
        for finding in findings
    )


def test_doctor_flags_group_generic_quality_language(tmp_path):
    _library(tmp_path)
    spec_path = tmp_path / "skills" / "sat" / "ach" / "skill.yaml"
    data = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    data["confidence_rubric"] = [
        "High: multiple independent sat evidence streams converge and key alternatives have been checked.",
        "Medium: evidence is plausible but incomplete, indirect, or partly assumption-dependent.",
        "Low: evidence is sparse, single-source, contested, or mainly inferential.",
    ]
    spec_path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    findings = doctor(tmp_path, Config(min_workflow_steps=3, min_anti_criteria=2))
    assert any(
        finding["message"] == "confidence_rubric must include skill-specific language"
        for finding in findings
    )


def test_doctor_skips_non_implemented_and_missing_workflow(tmp_path):
    _seed(tmp_path)
    render_definition(_def("sat.ach", status="stub", steps=1), root=tmp_path)
    spec_path = tmp_path / "skills" / "sat" / "ach" / "skill.yaml"
    spec_path.write_text(
        spec_path.read_text(encoding="utf-8").replace(
            "status: implemented", "status: stub"
        ),
        encoding="utf-8",
    )
    (tmp_path / "skills" / "sat" / "ach" / "workflow.md").unlink()
    assert doctor(tmp_path, Config(min_workflow_steps=3, min_anti_criteria=2)) == []


def test_doctor_empty_tree(tmp_path):
    assert doctor(tmp_path) == []


def test_count_steps_both_formats():
    assert _count_steps("## Step 1 — a\n## Step 2 — b\n") == 2
    assert _count_steps("1. **read** — a\n2. **write** — b\n3. done\n") == 3
    assert _count_steps("no steps here") == 0


def test_count_anti_criteria_section_ends_at_next_heading():
    text = "## Anti-criteria\n- no shortcut\n- no invention\n## Next\n- not counted\n"
    assert _count_anti_criteria(text) == 2


# --- CLI surface for the intelligent commands -----------------------------
def test_cli_route_stats_groups_catalogue_export(tmp_path, capsys):
    from cogsecskills.cli import main

    _library(tmp_path)
    assert main(["--root", str(tmp_path), "route", "competing hypotheses"]) == 0
    assert "sat.ach" in capsys.readouterr().out
    assert main(["--root", str(tmp_path), "stats"]) == 0
    assert '"registry_total": 2' in capsys.readouterr().out
    assert main(["--root", str(tmp_path), "groups"]) == 0
    assert "sat" in capsys.readouterr().out
    assert main(["--root", str(tmp_path), "catalogue", "--markdown"]) == 0
    assert "Skill Catalogue" in capsys.readouterr().out
    assert main(["--root", str(tmp_path), "export"]) == 0
    assert '"count": 2' in capsys.readouterr().out


def test_cli_catalogue_output_file(tmp_path, capsys):
    from cogsecskills.cli import main

    _library(tmp_path)
    out = tmp_path / "catalogue.md"
    assert main(["--root", str(tmp_path), "catalogue", "--output", str(out)]) == 0
    assert "wrote" in capsys.readouterr().out
    assert "Skill Catalogue" in out.read_text(encoding="utf-8")


def test_cli_route_no_match_exit_1(tmp_path, capsys):
    from cogsecskills.cli import main

    _library(tmp_path)
    assert main(["--root", str(tmp_path), "route", "zzzznomatch"]) == 1


def test_cli_doctor(tmp_path, capsys):
    from cogsecskills.cli import main

    _library(tmp_path)
    rc = main(["--root", str(tmp_path), "doctor"])
    out = capsys.readouterr().out
    assert "validation:" in out and "quality:" in out
    assert rc == 0


def test_cli_doctor_returns_1_for_quality_findings(tmp_path, capsys):
    from cogsecskills.cli import main

    _seed(tmp_path)
    render_definition(_def("sat.ach", steps=1), root=tmp_path)
    assert main(["--root", str(tmp_path), "doctor"]) == 1
    assert "workflow steps" in capsys.readouterr().out
