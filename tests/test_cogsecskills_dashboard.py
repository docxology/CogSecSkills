"""Tests for generated quality dashboard outputs."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from cogsecskills.dashboard import check_dashboard, write_dashboard


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
    payload = json.loads(
        (root / "output" / "data" / "quality_dashboard.json").read_text(
            encoding="utf-8"
        )
    )
    assert "# CogSecSkills Quality Dashboard" in markdown
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


def test_dashboard_json_and_markdown_cover_all_scenarios(tmp_path):
    root = _copy_dashboard_fixture(tmp_path)
    write_dashboard(root)

    markdown = (root / "docs" / "quality-dashboard.md").read_text(encoding="utf-8")
    payload = json.loads(
        (root / "output" / "data" / "quality_dashboard.json").read_text(
            encoding="utf-8"
        )
    )
    scenario_ids = {scenario["id"] for scenario in payload["scenarios"]}
    assert len(scenario_ids) == 28
    for scenario_id in scenario_ids:
        assert f"`{scenario_id}`" in markdown
    assert "Evidence Ladder" in markdown
    assert "Worked example" in markdown
    assert "Offline output review" in markdown


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


def test_cli_dashboard_write_and_check(tmp_path, capsys):
    from cogsecskills.cli import main

    root = _copy_dashboard_fixture(tmp_path)
    assert main(["--root", str(root), "dashboard", "--write"]) == 0
    assert "wrote quality dashboard" in capsys.readouterr().out
    assert main(["--root", str(root), "dashboard", "--check"]) == 0
    assert "quality dashboard is current" in capsys.readouterr().out
