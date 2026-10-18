from __future__ import annotations

import json
from pathlib import Path

from tests.project_fixtures import copy_project_dirs

import yaml

from cogsecskills.artifacts.evals import check_evals, load_evaluations, write_evals

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _copy_eval_fixture(tmp_path: Path) -> Path:
    return copy_project_dirs(tmp_path, "registry", "skills", "scenarios")


def test_evals_write_and_check_generate_source_markdown_and_json(tmp_path):
    root = _copy_eval_fixture(tmp_path)

    expected_count = len(
        yaml.safe_load((root / "scenarios/defensive_readiness.yaml").read_text())[
            "scenarios"
        ]
    )
    result = write_evals(root)

    assert result["evaluations"] == expected_count
    assert check_evals(root) == []
    assert len(load_evaluations(root)) == expected_count

    markdown = (root / "docs" / "evaluation-readiness.md").read_text(encoding="utf-8")
    payload = json.loads(
        (root / "output" / "data" / "evaluation_readiness.json").read_text(
            encoding="utf-8"
        )
    )
    assert "do not establish independent" in markdown
    assert "live model outputs" in markdown
    assert payload["summary"]["evaluations"] == expected_count
    assert payload["summary"]["measured_score_records"] == 0
    assert "passing_score" not in payload["summary"]
    assert len(payload["evaluations"]) == expected_count


def test_evals_check_detects_missing_forged_score_and_unsafe_fixture(tmp_path):
    root = _copy_eval_fixture(tmp_path)
    write_evals(root)
    source = root / "evals" / "local_output_review.yaml"
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))

    removed = raw["evaluations"].pop()
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("stale offline evaluation source" in finding for finding in findings)
    assert any("missing evaluation fixtures" in finding for finding in findings)

    raw["evaluations"].append(removed)
    raw["evaluations"][0]["rubric_scores"] = {"uncertainty": 1}
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any(
        "authored fixture cannot carry rubric scores" in finding for finding in findings
    )

    del raw["evaluations"][0]["rubric_scores"]
    raw["evaluations"][0]["sections"][0]["body"] += " step-by-step playbook"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("operational misuse phrase" in finding for finding in findings)


def test_cli_evals_write_and_check(tmp_path, capsys):
    from cogsecskills.cli import main

    root = _copy_eval_fixture(tmp_path)
    assert main(["--root", str(root), "evals", "--write"]) == 0
    assert "wrote offline eval fixtures" in capsys.readouterr().out
    assert main(["--root", str(root), "evals", "--check"]) == 0
    assert "offline evaluation fixtures are current" in capsys.readouterr().out
