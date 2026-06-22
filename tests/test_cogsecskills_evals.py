from __future__ import annotations

import json
import shutil
from pathlib import Path

import yaml

from cogsecskills.artifacts.evals import check_evals, load_evaluations, write_evals


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _copy_eval_fixture(tmp_path: Path) -> Path:
    for dirname in ("registry", "skills", "scenarios"):
        shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    return tmp_path


def test_evals_write_and_check_generate_source_markdown_and_json(tmp_path):
    root = _copy_eval_fixture(tmp_path)

    result = write_evals(root)

    assert result["evaluations"] == 28
    assert check_evals(root) == []
    assert len(load_evaluations(root)) == 28

    markdown = (root / "docs" / "evaluation-readiness.md").read_text(encoding="utf-8")
    payload = json.loads(
        (root / "output" / "data" / "evaluation_readiness.json").read_text(
            encoding="utf-8"
        )
    )
    assert "not live model outputs" in markdown
    assert payload["summary"]["evaluations"] == 28
    assert payload["summary"]["passing_score"] == 2
    assert len(payload["evaluations"]) == 28


def test_evals_check_detects_missing_low_score_and_unsafe_fixture(tmp_path):
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
    raw["evaluations"][0]["rubric_scores"]["uncertainty"] = 1
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    findings = check_evals(root)
    assert any("rubric uncertainty must be 2" in finding for finding in findings)

    raw["evaluations"][0]["rubric_scores"]["uncertainty"] = 2
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
