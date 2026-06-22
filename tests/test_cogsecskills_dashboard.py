"""Tests for generated quality dashboard outputs."""

from __future__ import annotations

import json
import shutil
from copy import deepcopy
from pathlib import Path

from cogsecskills.artifacts.dashboard import _dashboard_payload, _payload_findings
from cogsecskills.artifacts.dashboard import check_dashboard, write_dashboard


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _copy_dashboard_fixture(tmp_path: Path) -> Path:
    for dirname in ("registry", "skills", "scenarios", "examples", "evals"):
        shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    shutil.copy2(PROJECT_ROOT / "TODO.md", tmp_path / "TODO.md")
    return tmp_path


def test_dashboard_write_and_check_on_repo_shaped_fixture(tmp_path):
    root = _copy_dashboard_fixture(tmp_path)

    result = write_dashboard(root)

    assert result["skills"] == 100
    assert result["scenarios"] == 28
    assert result["examples"] == 100
    assert check_dashboard(root) == []

    markdown = (root / "docs" / "quality-dashboard.md").read_text(encoding="utf-8")
    html = (root / "docs" / "quality-dashboard.html").read_text(encoding="utf-8")
    payload = json.loads(
        (root / "output" / "data" / "quality_dashboard.json").read_text(
            encoding="utf-8"
        )
    )
    assert "# CogSecSkills Quality Dashboard" in markdown
    assert "<title>CogSecSkills Quality Dashboard</title>" in html
    assert "data-skill-id=" in html
    assert "not field validation or live runtime certification" in html
    assert "Evidence Ladder" in html
    assert "Quality capsule" in html
    assert "Answer kinds" in html
    assert "Source" in html
    assert "not field validation" in markdown
    assert payload["summary"]["skills"] == 100
    assert payload["summary"]["groups"] == 7
    assert payload["summary"]["expected_answers"] == 28
    assert payload["summary"]["worked_examples"] == 100
    assert payload["summary"]["offline_evaluations"] == 28
    assert len(payload["skills"]) == 100
    assert len(payload["worked_examples"]) == 100
    assert len(payload["offline_evaluations"]) == 28
    assert len({row["group"] for row in payload["skills"]}) == 7
    assert all("claim_boundary_status" in row for row in payload["skills"])
    assert all("worked_example_id" in row for row in payload["skills"])
    assert all("expected_answer_kinds" in row for row in payload["skills"])
    assert all("evaluation_scenario_ids" in row for row in payload["skills"])
    assert all("quality_capsule" in row for row in payload["skills"])
    assert all("source_path" in row for row in payload["skills"])
    assert "Boundary" in html
    assert "Evidence" in html
    assert "Confidence" in html
    assert "Safe pattern" in html


def test_dashboard_json_and_markdown_cover_all_scenarios(tmp_path):
    root = _copy_dashboard_fixture(tmp_path)
    write_dashboard(root)

    markdown = (root / "docs" / "quality-dashboard.md").read_text(encoding="utf-8")
    html = (root / "docs" / "quality-dashboard.html").read_text(encoding="utf-8")
    payload = json.loads(
        (root / "output" / "data" / "quality_dashboard.json").read_text(
            encoding="utf-8"
        )
    )
    scenario_ids = {scenario["id"] for scenario in payload["scenarios"]}
    assert len(scenario_ids) == 28
    for scenario_id in scenario_ids:
        assert f"`{scenario_id}`" in markdown
        assert scenario_id in html
    assert "Evidence Ladder" in markdown
    assert "Evidence Ladder" in html
    assert "Worked example" in markdown
    assert "Skill worked examples" in html
    assert "Offline output review" in markdown
    assert "Offline output review" in html
    assert "local deterministic fixture only" in html
    assert html.count("data-skill-id=") == 100


def test_dashboard_check_detects_missing_and_stale_outputs(tmp_path):
    root = _copy_dashboard_fixture(tmp_path)
    write_dashboard(root)

    md_path = root / "docs" / "quality-dashboard.md"
    md_path.write_text(md_path.read_text(encoding="utf-8") + "\nmanual drift\n")
    findings = check_dashboard(root)
    assert any("stale generated dashboard file" in finding for finding in findings)

    data_path = root / "output" / "data" / "quality_dashboard.json"
    data_path.unlink()
    findings = check_dashboard(root)
    assert any("missing generated dashboard file" in finding for finding in findings)

    write_dashboard(root)
    html_path = root / "docs" / "quality-dashboard.html"
    html_path.write_text(
        html_path.read_text(encoding="utf-8").replace("Claim Boundary", "Drift"),
        encoding="utf-8",
    )
    findings = check_dashboard(root)
    assert any("stale generated dashboard file" in finding for finding in findings)


def test_dashboard_payload_findings_report_each_quality_gate(tmp_path):
    root = _copy_dashboard_fixture(tmp_path)
    payload = _dashboard_payload(root)

    broken = deepcopy(payload)
    broken["summary"]["skills"] = 99
    broken["summary"]["groups"] = 6
    broken["summary"]["scenarios"] = 27
    broken["summary"]["worked_examples"] = 99
    broken["summary"]["offline_evaluations"] = 1
    broken["summary"]["expected_answers"] = 1
    broken["summary"]["scenario_summary_consistent"] = False
    broken["verified_state"] = []
    broken["scenarios"] = broken["scenarios"][:-1]
    covered_index = next(
        index for index, row in enumerate(broken["skills"]) if row["scenario_ids"]
    )
    broken["skills"][0]["quality_capsule_present"] = False
    broken["skills"][1]["worked_example_id"] = ""
    broken["skills"][covered_index]["evaluation_scenario_ids"] = []
    broken["skills"][3]["selected_skill_consistent"] = False
    broken["skills"][4]["claim_boundary_status"] = "unbounded"

    findings = "\n".join(_payload_findings(broken))

    for expected in (
        "expected 100 skills",
        "expected 7 groups",
        "expected 28 scenario fixtures",
        "expected 100 worked examples",
        "offline evaluation fixtures do not match",
        "not every scenario has an expected answer",
        "one or more skills are missing a quality capsule",
        "one or more skills are missing a worked example",
        "one or more scenario-covered skills lack eval fixtures",
        "one or more scenario selected-skill checks are inconsistent",
        "scenario summary does not match dashboard scenario rows",
        "one or more skills are missing a local claim boundary",
        "verified-state lines are missing",
    ):
        assert expected in findings

    duplicated = deepcopy(payload)
    duplicated["scenarios"][1]["id"] = duplicated["scenarios"][0]["id"]
    assert "scenario ids are missing or duplicated" in "\n".join(
        _payload_findings(duplicated)
    )


def test_cli_dashboard_write_and_check(tmp_path, capsys):
    from cogsecskills.cli import main

    root = _copy_dashboard_fixture(tmp_path)
    assert main(["--root", str(root), "dashboard", "--write"]) == 0
    assert "wrote quality dashboard" in capsys.readouterr().out
    assert main(["--root", str(root), "dashboard", "--check"]) == 0
    assert "quality dashboard is current" in capsys.readouterr().out
