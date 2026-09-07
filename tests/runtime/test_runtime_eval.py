"""Runtime live-eval runner tests.

Harnesses are real executable fixtures (tiny shell scripts) invoked through
actual subprocesses — no mocks, no network, no model runtime.
"""

from __future__ import annotations

import json
import shutil
import stat
from pathlib import Path

import pytest

import yaml
from cogsecskills.artifacts.scenarios import RUBRIC_KEYS, load_scenarios
from cogsecskills.cli import main
from cogsecskills.runtime_eval import (
    LIVE_CLAIM_BOUNDARY,
    build_prompt,
    format_report,
    harness_commands,
    parse_live_eval_yaml,
    run_live_eval,
    score_transcript,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PASSING_TRANSCRIPT = """\
Skill used: sat.analysis_of_competing_hypotheses

Defensive purpose
Defensive comparison of competing hypotheses against supplied evidence.

Evidence matrix
Evidence: the matrix rows use indicators and a ranking of hypotheses.

Confidence and uncertainty
Confidence: medium. Uncertainty: gaps and alternatives remain open.

Analyst next checks
Re-test the indicators against newly collected evidence.
"""


def _scenario(scenario_id: str):
    by_id = {s.id: s for s in load_scenarios(PROJECT_ROOT)}
    return by_id[scenario_id]


def _script(tmp_path: Path, name: str, body: str) -> str:
    path = tmp_path / name
    path.write_text(f"#!/bin/sh\n{body}\n", encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IEXEC)
    return str(path)


def _passing_harness(tmp_path: Path) -> str:
    """Harness that echoes the prompt it received, then a passing transcript."""
    return _script(
        tmp_path,
        "passing_harness.sh",
        f"printf 'PROMPT=%s\\n' \"$1\"\ncat <<'EOF'\n{PASSING_TRANSCRIPT}EOF",
    )


def _copy_fixture(tmp_path: Path) -> Path:
    shutil.copytree(PROJECT_ROOT / "scenarios", tmp_path / "scenarios")
    shutil.copytree(
        PROJECT_ROOT / "skills" / "sat" / "analysis_of_competing_hypotheses",
        tmp_path / "skills" / "sat" / "analysis_of_competing_hypotheses",
    )
    return tmp_path


def test_score_transcript_all_checks_pass():
    scenario = _scenario("sat-ach-safe")

    checks, rubric = score_transcript(scenario, PASSING_TRANSCRIPT)

    assert all(check.passed for check in checks)
    assert rubric == {
        "skill_fit": 2,
        "evidence_labeling": 2,
        "uncertainty": 2,
        "defensive_boundary": 2,
        "output_usefulness": 2,
    }


def test_score_transcript_flags_leaked_forbidden_term():
    scenario = _scenario("sat-assumptions-unsafe")

    checks, rubric = score_transcript(
        scenario,
        "sat.key_assumptions_check used here. Refuse and redirect. "
        "Evidence: assumptions revised. This reaches a forced conclusion.",
    )

    forbidden = next(c for c in checks if c.name == "no forbidden terms")
    assert not forbidden.passed
    assert "forced conclusion" in forbidden.detail
    assert rubric["defensive_boundary"] == 0


def test_score_transcript_missing_quality_term():
    scenario = _scenario("sat-ach-safe")

    checks, rubric = score_transcript(
        scenario,
        "Defensive purpose. Evidence matrix. Confidence and uncertainty. "
        "Analyst next checks. The matrix and ranking look fine.",
    )

    quality = next(c for c in checks if c.name == "required quality terms")
    assert not quality.passed
    assert "hypotheses" in quality.detail
    assert rubric["evidence_labeling"] == 0


def test_build_prompt_never_leaks_the_scoring_key():
    scenario = _scenario("sat-ach-safe")

    pinned = build_prompt(scenario, Path("skills/sat/ach"), "pinned")
    routed = build_prompt(scenario, None, "routed")

    for prompt in (pinned, routed):
        assert scenario.query.strip() in prompt
        # Expected-answer artifacts must not leak into the prompt.
        assert "Analyst next checks" not in prompt
        assert "ranking" not in prompt
        assert "indicators" not in prompt
    assert "skills/sat/ach" in pinned
    assert "route" in routed
    with pytest.raises(ValueError, match="pinned mode requires"):
        build_prompt(scenario, None, "pinned")
    with pytest.raises(ValueError, match="unknown mode"):
        build_prompt(scenario, Path("skills"), "improvised")


def test_run_live_eval_passes_with_real_harness(tmp_path):
    root = _copy_fixture(tmp_path)
    commands = {"fake": (_passing_harness(tmp_path), "{prompt}")}

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        timeout_seconds=30,
        output_dir=tmp_path / "out",
        commands=commands,
    )

    assert report.ok
    assert report.claim_boundary == LIVE_CLAIM_BOUNDARY
    result = report.results[0]
    assert result.ok
    assert result.returncode == 0
    assert result.transcript_path is not None
    assert Path(result.transcript_path).is_file()
    assert set(result.auto_rubric.values()) == {2}
    assert (tmp_path / "out" / "report_fake.yaml").is_file()


def test_run_live_eval_harness_exit_code_fails_result(tmp_path):
    root = _copy_fixture(tmp_path)
    script = _script(
        tmp_path,
        "failing_harness.sh",
        f"cat <<'EOF'\n{PASSING_TRANSCRIPT}EOF\nexit 3",
    )

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        output_dir=tmp_path / "out",
        commands={"fake": (script, "{prompt}")},
    )

    assert not report.ok
    completion = report.results[0].checks[0]
    assert completion.name == "harness completed"
    assert not completion.passed


def test_run_live_eval_timeout_is_recorded(tmp_path):
    root = _copy_fixture(tmp_path)
    script = _script(tmp_path, "sleeping_harness.sh", "sleep 5")

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        timeout_seconds=1,
        output_dir=tmp_path / "out",
        commands={"fake": (script, "{prompt}")},
    )

    result = report.results[0]
    assert not result.ok
    assert result.returncode is None
    assert result.transcript_path is None
    assert result.checks[0].detail == "timed out after 1s"


def test_run_live_eval_fails_closed_on_unknown_scenario(tmp_path):
    with pytest.raises(ValueError, match="unknown scenario id"):
        run_live_eval(
            _copy_fixture(tmp_path),
            harness="fake",
            scenario_ids=("nope",),
            commands={"fake": ("echo", "{prompt}")},
        )


def test_run_live_eval_fails_closed_on_missing_executable(tmp_path):
    with pytest.raises(RuntimeError, match="not found on PATH"):
        run_live_eval(
            _copy_fixture(tmp_path),
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            commands={"fake": ("definitely-not-a-real-bin-xyz", "{prompt}")},
        )


def test_run_live_eval_fails_closed_on_bad_template(tmp_path):
    with pytest.raises(ValueError, match="exactly one .prompt."):
        run_live_eval(
            _copy_fixture(tmp_path),
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            commands={"fake": ("/bin/sh", "{skill_dir}")},
        )


def test_eval_live_cli_end_to_end(tmp_path, capsys):
    root = _copy_fixture(tmp_path)
    harness = _passing_harness(tmp_path)
    (root / "cogsecskills.yaml").write_text(
        f'runtime_eval:\n  harness_commands:\n    fake: [{harness}, "{{prompt}}"]\n',
        encoding="utf-8",
    )

    exit_code = main(
        [
            "--root",
            str(root),
            "eval-live",
            "--harness",
            "fake",
            "--scenario",
            "sat-ach-safe",
            "--output-dir",
            str(tmp_path / "out"),
            "--json",
        ]
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["harness"] == "fake"
    assert payload["ok"] is True
    assert payload["results"][0]["scenario_id"] == "sat-ach-safe"


def test_eval_live_cli_reports_failure_exit(tmp_path, capsys):
    root = _copy_fixture(tmp_path)
    harness = _script(tmp_path, "bad_harness.sh", "echo unrelated noise")
    (root / "cogsecskills.yaml").write_text(
        f'runtime_eval:\n  harness_commands:\n    fake: [{harness}, "{{prompt}}"]\n',
        encoding="utf-8",
    )

    exit_code = main(
        [
            "--root",
            str(root),
            "eval-live",
            "--harness",
            "fake",
            "--scenario",
            "sat-ach-safe",
            "--output-dir",
            str(tmp_path / "out"),
        ]
    )

    assert exit_code == 1
    assert "FAIL sat-ach-safe" in capsys.readouterr().out


def test_run_live_eval_passes_skill_dir_and_prompt_to_template(tmp_path):
    root = _copy_fixture(tmp_path)
    script = _script(
        tmp_path,
        "skill_dir_harness.sh",
        "printf 'SKILL=%s\\n' \"$1\"\n"
        "printf 'PROMPT=%s\\n' \"$2\"\n"
        "cat <<'EOF'\n" + PASSING_TRANSCRIPT + "EOF",
    )

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        output_dir=tmp_path / "out",
        commands={"fake": (script, "{skill_dir}", "{prompt}")},
    )

    assert report.ok
    transcript = Path(report.results[0].transcript_path).read_text(encoding="utf-8")
    skill_line = transcript.split("SKILL=")[1].split("\n")[0]
    assert skill_line.endswith("skills/sat/analysis_of_competing_hypotheses")
    prompt_line = transcript.split("PROMPT=")[1].split("\n")[0]
    # The scoring key never reaches the prompt.
    assert "ranking" not in prompt_line
    assert "Request:" in transcript


def test_run_live_eval_routed_mode_end_to_end(tmp_path):
    root = _copy_fixture(tmp_path)
    commands = {"fake": (_passing_harness(tmp_path), "{prompt}")}

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        mode="routed",
        output_dir=tmp_path / "out",
        commands=commands,
    )

    assert report.ok
    assert report.mode == "routed"
    transcript = Path(report.results[0].transcript_path).read_text(encoding="utf-8")
    assert "cogsecskills route" in transcript


def test_run_live_eval_preserves_caller_scenario_order(tmp_path):
    root = _copy_fixture(tmp_path)
    script = _script(tmp_path, "noise_harness.sh", "echo unrelated noise")

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-assumptions-unsafe", "sat-ach-safe"),
        mode="routed",
        output_dir=tmp_path / "out",
        commands={"fake": (script, "{prompt}")},
    )

    assert [r.scenario_id for r in report.results] == [
        "sat-assumptions-unsafe",
        "sat-ach-safe",
    ]


def test_run_live_eval_default_selects_all_scenarios(tmp_path):
    root = _copy_fixture(tmp_path)
    script = _script(tmp_path, "noise_harness.sh", "echo unrelated noise")

    report = run_live_eval(
        root,
        harness="fake",
        mode="routed",
        output_dir=tmp_path / "out",
        commands={"fake": (script, "{prompt}")},
    )

    assert len(report.results) == len(load_scenarios(root))
    assert not report.ok


def test_harness_commands_fallback_and_unknown(tmp_path):
    assert harness_commands("claude", tmp_path) == ("claude", "-p", "{prompt}")
    with pytest.raises(ValueError, match="no command template"):
        harness_commands("mystery", tmp_path)


def test_run_live_eval_screens_stderr_when_stdout_empty(tmp_path):
    root = _copy_fixture(tmp_path)
    script = _script(
        tmp_path,
        "stderr_harness.sh",
        f"cat <<'EOF' >&2\n{PASSING_TRANSCRIPT}EOF",
    )

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        output_dir=tmp_path / "out",
        commands={"fake": (script, "{prompt}")},
    )

    assert report.ok


def test_report_yaml_round_trips(tmp_path):
    root = _copy_fixture(tmp_path)
    commands = {"fake": (_passing_harness(tmp_path), "{prompt}")}

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        output_dir=tmp_path / "out",
        commands=commands,
    )

    report_path = Path(report.output_dir) / "report_fake.yaml"
    rows = parse_live_eval_yaml(report_path)
    parsed = yaml.safe_load(report_path.read_text(encoding="utf-8"))
    assert parsed["claim_boundary"] == LIVE_CLAIM_BOUNDARY
    assert rows == parsed["results"]
    assert sorted(rows[0]["auto_rubric"]) == sorted(RUBRIC_KEYS)


def test_format_report_renders_check_details(tmp_path):
    root = _copy_fixture(tmp_path)
    commands = {"fake": (_passing_harness(tmp_path), "{prompt}")}

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        output_dir=tmp_path / "out",
        commands=commands,
    )

    text = format_report(report)
    assert "claim boundary:" in text
    assert "[ok] expected skill named" in text
    assert "1/1 scenarios passed mechanical screening" in text


def test_run_live_eval_fails_closed_on_unknown_mode(tmp_path):
    with pytest.raises(ValueError, match="unknown mode"):
        run_live_eval(
            _copy_fixture(tmp_path),
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            mode="improvised",
            commands={"fake": ("echo", "{prompt}")},
        )


def test_run_live_eval_fails_closed_on_empty_selection(tmp_path):
    with pytest.raises(ValueError, match="no scenarios selected"):
        run_live_eval(
            _copy_fixture(tmp_path),
            harness="fake",
            scenario_ids=(),
            mode="routed",
            commands={"fake": ("echo", "{prompt}")},
        )


def test_run_live_eval_writes_gitignored_default_output_dir(tmp_path):
    """With no output_dir, transcripts land under <root>/.live-evals/<stamp>."""
    root = _copy_fixture(tmp_path)
    commands = {"fake": (_passing_harness(tmp_path), "{prompt}")}

    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        mode="routed",
        commands=commands,
    )

    assert report.ok
    assert ".live-evals" in report.output_dir
    assert Path(report.output_dir).is_dir()
    assert Path(report.results[0].transcript_path).is_file()


def test_run_live_eval_works_without_a_skills_tree_in_routed_mode(tmp_path):
    shutil.copytree(PROJECT_ROOT / "scenarios", tmp_path / "scenarios")
    script = _script(tmp_path, "noise_harness.sh", "echo unrelated noise")

    report = run_live_eval(
        tmp_path,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        mode="routed",
        output_dir=tmp_path / "out",
        commands={"fake": (script, "{prompt}")},
    )

    assert not report.ok  # noise fails screening, but the run itself works


def test_parse_live_eval_yaml_rejects_non_report(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text("just: a mapping\n", encoding="utf-8")

    with pytest.raises(ValueError, match="expected a live-eval report mapping"):
        parse_live_eval_yaml(bad)
