"""CLI behavior tests for the tightened command surface.

Covers: the ``scenarios --check`` flag is optional (catalogue convention), the
``report`` command checks the configured harness set, ``eval-live`` exits 1 on
a failed setup, ``catalogue --output`` creates missing parent directories, and
the shared validation printer used by ``validate``/``doctor``.
"""

from __future__ import annotations

import json
from pathlib import Path

from cogsecskills.authoring.author import render_definition
from cogsecskills.cli import build_parser, main


def _seed_registry(root: Path) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        "  - {id: sat.demo, name: Demo Technique, group: sat, status: stub, "
        "summary: A demo technique.}\n",
        encoding="utf-8",
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n  - {id: sat, title: SAT}\n", encoding="utf-8"
    )


def _narrow_harnesses(root: Path) -> None:
    """Limit the harness set to the one adapter the fixture declares.

    The renderer always marks authored skills ``implemented``, so also lower the
    doctor quality bar below what the minimal fixture ships (3 steps, 1
    anti-criterion) to keep these tests focused on the printing paths.
    """
    (root / "cogsecskills.yaml").write_text(
        "harnesses: [claude]\n"
        "quality:\n"
        "  min_workflow_steps: 1\n"
        "  min_anti_criteria: 1\n",
        encoding="utf-8",
    )


def _good_def() -> dict:
    return {
        "id": "sat.demo",
        "description": "A real description of the demo technique.",
        "tools": [
            {"verb": "read", "purpose": "ingest the inputs"},
            {"verb": "reason", "purpose": "apply the technique"},
            {"verb": "write", "purpose": "emit the product"},
        ],
        "workflow_steps": [
            {"verbs": ["read"], "title": "Gather", "text": "Collect the inputs."},
            {"verbs": ["reason", "write"], "title": "Analyse", "text": "Do the work."},
            {"verbs": ["write"], "title": "Emit", "text": "Write the product out."},
        ],
        "anti_criteria": ["Do not skip the evidence step."],
    }


# --- scenarios: --check is optional (catalogue convention) ----------------------


def test_scenarios_check_flag_is_optional():
    parser = build_parser()
    args = parser.parse_args(["scenarios"])
    assert args.check is False
    args_with_check = parser.parse_args(["scenarios", "--check"])
    assert args_with_check.check is True


def test_scenarios_without_check_reports_findings(tmp_path, capsys):
    rc = main(["--root", str(tmp_path), "scenarios"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "scenario issue(s)" in out


def test_scenarios_check_flag_reports_findings(tmp_path, capsys):
    rc = main(["--root", str(tmp_path), "scenarios", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "scenario issue(s)" in out


# --- report: checks the configured harness set ---------------------------------


def test_report_uses_configured_harnesses(tmp_path, capsys):
    _seed_registry(tmp_path)
    (tmp_path / "cogsecskills.yaml").write_text(
        "harnesses: [claude]\n", encoding="utf-8"
    )
    render_definition(_good_def(), root=tmp_path, harnesses=("claude",))

    rc = main(["--root", str(tmp_path), "report"])
    payload = json.loads(capsys.readouterr().out)
    assert rc == 0
    assert payload["ok"] is True
    assert payload["errors"] == 0


def test_report_defaults_flag_missing_adapters(tmp_path, capsys):
    """Without a narrowed config, report checks the full default harness set."""
    _seed_registry(tmp_path)
    render_definition(_good_def(), root=tmp_path, harnesses=("claude",))

    rc = main(["--root", str(tmp_path), "report"])
    payload = json.loads(capsys.readouterr().out)
    assert rc == 0  # report always exits 0; the JSON carries the verdict
    assert payload["ok"] is False
    assert payload["errors"] > 0


# --- eval-live: failed setup exits 1 --------------------------------------------


def test_eval_live_failure_exits_one(tmp_path):
    # No scenarios fixture on this root: run_live_eval raises ValueError, which
    # the CLI must convert to exit code 1 (not 2).
    rc = main(["--root", str(tmp_path), "eval-live", "--harness", "claude"])
    assert rc == 1


# --- catalogue --output: creates missing parents --------------------------------


def test_catalogue_output_creates_parent_directories(tmp_path):
    _seed_registry(tmp_path)
    target = tmp_path / "deep" / "nested" / "catalogue.md"
    rc = main(
        [
            "--root",
            str(tmp_path),
            "catalogue",
            "--markdown",
            "--output",
            str(target),
        ]
    )
    assert rc == 0
    assert target.is_file()
    assert target.read_text(encoding="utf-8").startswith("# CogSecSkills")


# --- shared validation printer ---------------------------------------------------


def test_validate_text_output_prints_issues_and_summary(tmp_path, capsys):
    _seed_registry(tmp_path)
    _narrow_harnesses(tmp_path)
    render_definition(_good_def(), root=tmp_path)
    workflow = tmp_path / "skills" / "sat" / "demo" / "workflow.md"
    workflow.unlink()

    rc = main(["--root", str(tmp_path), "validate"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "ERROR" in out
    assert "missing workflow document" in out
    assert out.rstrip().endswith("1 error(s), 0 warning(s)")


def test_validate_text_output_clean_tree(tmp_path, capsys):
    _seed_registry(tmp_path)
    _narrow_harnesses(tmp_path)
    render_definition(_good_def(), root=tmp_path)

    rc = main(["--root", str(tmp_path), "validate"])
    out = capsys.readouterr().out
    assert rc == 0
    assert out.rstrip().endswith("0 error(s), 0 warning(s)")


def test_doctor_text_output_shares_validation_printer(tmp_path, capsys):
    """doctor prints the same issue lines plus quality findings."""
    _seed_registry(tmp_path)
    _narrow_harnesses(tmp_path)
    render_definition(_good_def(), root=tmp_path)

    rc = main(["--root", str(tmp_path), "doctor"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "validation: 0 error(s)" in out
