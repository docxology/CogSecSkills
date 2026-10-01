"""Real-process regression cases for live-eval preflight and evidence custody."""

from __future__ import annotations

import json
import os
import signal
import shutil
import subprocess
import sys
import time
from dataclasses import replace
from pathlib import Path

import pytest

from cogsecskills.cli import main
from cogsecskills.runtime.models import LiveEvalReport
from cogsecskills.runtime.process import (
    MAX_STREAM_BYTES,
    _kill_process_tree,
    run_process,
)
from cogsecskills.runtime.reporting import write_text_exclusive
from cogsecskills.runtime_eval import run_live_eval
from cogsecskills.runtime_eval import parse_live_eval_yaml, score_transcript
from cogsecskills.artifacts.scenarios import load_scenarios

ROOT = Path(__file__).resolve().parents[2]


def fixture_root(tmp_path: Path) -> Path:
    shutil.copytree(ROOT / "scenarios", tmp_path / "scenarios")
    shutil.copytree(
        ROOT / "skills" / "sat" / "analysis_of_competing_hypotheses",
        tmp_path / "skills" / "sat" / "analysis_of_competing_hypotheses",
    )
    return tmp_path


def test_empty_report_cannot_pass():
    assert not LiveEvalReport("fake", "pinned", "exploratory", (), "out").ok


def test_live_sections_must_be_headings_and_terms_ignore_line_wraps():
    scenario = load_scenarios(ROOT)[0]
    scenario = replace(scenario, expected_output_terms=("wrapped term",))
    text = "\n".join(
        f"## {title}" for title in scenario.expected_response.required_sections
    )
    checks, _ = score_transcript(scenario, text + "\nwrapped\nterm\n")
    assert next(check for check in checks if check.name == "required sections").passed
    assert next(
        check for check in checks if check.name == "expected output terms"
    ).passed
    checks, _ = score_transcript(
        scenario, "Mention " + ", ".join(scenario.expected_response.required_sections)
    )
    assert not next(
        check for check in checks if check.name == "required sections"
    ).passed


def test_longer_skill_id_cannot_supply_skill_fit():
    scenario = load_scenarios(ROOT)[0]
    _, rubric = score_transcript(scenario, scenario.expected_skill + "_other")
    assert rubric["skill_fit"] == 0


@pytest.mark.parametrize(
    "source", ["results: [not-a-mapping]\n", "results: []\nresults: []\n"]
)
def test_live_report_loader_rejects_ambiguous_or_mistyped_results(tmp_path, source):
    report = tmp_path / "report.yaml"
    report.write_text(source)
    with pytest.raises(ValueError):
        parse_live_eval_yaml(report)


@pytest.mark.parametrize("timeout", [0, -1, True, 1.5, "30"])
def test_timeout_is_validated_before_io(tmp_path, timeout):
    with pytest.raises(ValueError, match="positive integer"):
        run_live_eval(tmp_path, harness="fake", timeout_seconds=timeout)
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("harness", ["../escape", "/tmp/escape", "a/b", "a\\b", ""])
def test_harness_name_cannot_escape_output(tmp_path, harness):
    with pytest.raises(ValueError, match="safe non-empty path component"):
        run_live_eval(tmp_path, harness=harness)
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize(
    "template", [(), "echo {prompt}", (1,), (" ", "{prompt}"), ("echo\0", "{prompt}")]
)
def test_invalid_argv_fails_before_io(tmp_path, template):
    with pytest.raises(ValueError, match="argv sequence"):
        run_live_eval(tmp_path, harness="fake", commands={"fake": template})


@pytest.mark.parametrize(
    "template",
    [("{prompt}",), ("{skill_dir}", "{prompt}"), ("echo", "{prompt}{prompt}")],
)
def test_bad_placeholders_fail_before_io(tmp_path, template):
    with pytest.raises(ValueError, match="placeholder"):
        run_live_eval(tmp_path, harness="fake", commands={"fake": template})


def test_routed_template_cannot_reveal_expected_skill(tmp_path):
    with pytest.raises(ValueError, match="only supported in pinned"):
        run_live_eval(
            tmp_path,
            harness="fake",
            mode="routed",
            commands={"fake": ("echo", "{skill_dir}", "{prompt}")},
        )


def test_missing_later_pinned_skill_prevents_all_invocations(tmp_path):
    root = fixture_root(tmp_path)
    marker = root / "invoked"
    script = root / "harness.py"
    script.write_text(f"from pathlib import Path\nPath({str(marker)!r}).touch()\n")
    with pytest.raises(ValueError, match="pinned mode requires"):
        run_live_eval(
            root,
            harness="fake",
            scenario_ids=("sat-ach-safe", "sat-assumptions-unsafe"),
            commands={"fake": (sys.executable, str(script), "{prompt}")},
        )
    assert not marker.exists()
    assert not (root / ".live-evals").exists()


def test_duplicate_selection_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="duplicate ids"):
        run_live_eval(
            fixture_root(tmp_path),
            harness="fake",
            scenario_ids=("sat-ach-safe", "sat-ach-safe"),
            commands={"fake": (sys.executable, "-c", "print('noise')", "{prompt}")},
        )


@pytest.mark.parametrize("missing", ["SKILL.md", "workflow.md", "harness/codex.md"])
def test_missing_selected_skill_document_prevents_invocation(tmp_path, missing):
    root = fixture_root(tmp_path)
    (root / "skills" / "sat" / "analysis_of_competing_hypotheses" / missing).unlink()
    with pytest.raises(ValueError, match="selected skill is invalid"):
        run_live_eval(
            root,
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            commands={"fake": (sys.executable, "-c", "print('noise')", "{prompt}")},
        )
    assert not (root / ".live-evals").exists()


@pytest.mark.parametrize(
    "filename",
    ["fake/sat-ach-safe.txt", "fake/sat-ach-safe.stderr.txt", "report_fake.yaml"],
)
@pytest.mark.parametrize("inside_output", [False, True])
def test_late_receipt_symlink_cannot_overwrite_existing_file(
    tmp_path, filename, inside_output
):
    root = fixture_root(tmp_path)
    sentinel = root / ("out" if inside_output else "") / "preserve"
    sentinel.parent.mkdir(exist_ok=True)
    sentinel.write_text("original")
    planted = root / "out" / filename
    code = f"from pathlib import Path; Path({str(planted)!r}).symlink_to({str(sentinel)!r}); import sys; print('noise'); print('diagnostic', file=sys.stderr)"
    with pytest.raises((FileExistsError, ValueError)):
        run_live_eval(
            root,
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            output_dir=root / "out",
            commands={"fake": (sys.executable, "-c", code, "{prompt}")},
        )
    assert sentinel.read_text() == "original"


def test_late_harness_directory_symlink_is_rejected(tmp_path):
    root = fixture_root(tmp_path)
    outside = root.parent / (root.name + "-outside")
    outside.mkdir()
    output = root / "out"
    code = f"from pathlib import Path; folder = Path({str(output / 'fake')!r}); folder.rmdir(); folder.symlink_to({str(outside)!r}, target_is_directory=True); print('noise')"
    with pytest.raises(ValueError, match="must stay inside"):
        run_live_eval(
            root,
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            output_dir=output,
            commands={"fake": (sys.executable, "-c", code, "{prompt}")},
        )
    assert list(outside.iterdir()) == []


def test_late_output_root_symlink_cannot_redefine_boundary(tmp_path):
    root = fixture_root(tmp_path)
    outside = root.parent / (root.name + "-outside")
    (outside / "fake").mkdir(parents=True)
    output = root / "out"
    code = f"from pathlib import Path; folder = Path({str(output)!r}); folder.rename({str(root / 'oldout')!r}); folder.symlink_to({str(outside)!r}, target_is_directory=True); print('noise')"
    with pytest.raises(ValueError, match="boundary was replaced"):
        run_live_eval(
            root,
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            output_dir=output,
            commands={"fake": (sys.executable, "-c", code, "{prompt}")},
        )
    assert list((outside / "fake").iterdir()) == []


def test_duplicate_skill_ids_are_rejected(tmp_path):
    root = fixture_root(tmp_path)
    shutil.copytree(root / "skills" / "sat", root / "skills" / "duplicate")
    with pytest.raises(ValueError, match="duplicate skill id"):
        run_live_eval(
            root,
            harness="fake",
            scenario_ids=("sat-ach-safe",),
            commands={"fake": (sys.executable, "-c", "print('noise')", "{prompt}")},
        )


def test_explicit_output_is_never_overwritten(tmp_path):
    root = fixture_root(tmp_path)
    options = {
        "harness": "fake",
        "scenario_ids": ("sat-ach-safe",),
        "output_dir": root / "out",
        "commands": {"fake": (sys.executable, "-c", "print('noise')", "{prompt}")},
    }
    run_live_eval(root, **options)
    report_path = root / "out" / "report_fake.yaml"
    original = report_path.read_bytes()
    with pytest.raises(ValueError, match="already exists"):
        run_live_eval(root, **options)
    assert report_path.read_bytes() == original


def test_default_run_directories_are_unique(tmp_path):
    root = fixture_root(tmp_path)
    options = {
        "harness": "fake",
        "scenario_ids": ("sat-ach-safe",),
        "commands": {"fake": (sys.executable, "-c", "print('noise')", "{prompt}")},
    }
    first = run_live_eval(root, **options)
    second = run_live_eval(root, **options)
    assert first.output_dir != second.output_dir
    assert Path(first.output_dir).is_dir()


def test_harness_runs_at_resolved_root(tmp_path):
    root = fixture_root(tmp_path)
    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        commands={
            "fake": (sys.executable, "-c", "import os; print(os.getcwd())", "{prompt}")
        },
    )
    assert Path(report.results[0].transcript_path).read_text().strip() == str(
        root.resolve()
    )


def test_prompt_echo_cannot_supply_expected_skill(tmp_path):
    root = fixture_root(tmp_path)
    report = run_live_eval(
        root,
        harness="fake",
        scenario_ids=("sat-ach-safe",),
        commands={
            "fake": (sys.executable, "-c", "import sys; print(sys.argv[1])", "{prompt}")
        },
    )
    assert report.results[0].auto_rubric["skill_fit"] == 0


def test_process_spawn_failure_is_a_failed_result(tmp_path):
    result = run_process([str(tmp_path / "missing")], cwd=tmp_path, timeout_seconds=1)
    assert result.returncode is None
    assert "could not start harness" in result.failure


@pytest.mark.skipif(os.name != "posix", reason="POSIX signal and group semantics")
def test_process_cleanup_is_safe_after_group_has_exited(tmp_path):
    process = subprocess.Popen([sys.executable, "-c", "pass"], start_new_session=True)
    assert process.wait(timeout=3) == 0
    _kill_process_tree(process)


@pytest.mark.skipif(os.name != "posix", reason="POSIX signal and group semantics")
def test_interrupt_cleans_up_real_harness_process(tmp_path):
    ready = tmp_path / "ready"
    survived = tmp_path / "survived"
    worker = f"from pathlib import Path; import time; Path({str(ready)!r}).touch(); time.sleep(2); Path({str(survived)!r}).touch(); time.sleep(10)"
    wrapper_code = (
        "from pathlib import Path; from cogsecskills.runtime.process import run_process; "
        f"run_process([{sys.executable!r}, '-c', {worker!r}], cwd=Path({str(tmp_path)!r}), timeout_seconds=30)"
    )
    wrapper = subprocess.Popen(
        [sys.executable, "-c", wrapper_code],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    try:
        deadline = time.monotonic() + 3
        while (
            not ready.exists()
            and wrapper.poll() is None
            and time.monotonic() < deadline
        ):
            time.sleep(0.05)
        assert ready.exists()
        wrapper.send_signal(signal.SIGINT)
        _, stderr = wrapper.communicate(timeout=3)
        assert wrapper.returncode != 0
        assert b"KeyboardInterrupt" in stderr
        time.sleep(2.1)
        assert not survived.exists()
    finally:
        if wrapper.poll() is None:
            wrapper.kill()
            wrapper.communicate(timeout=3)


def test_standalone_receipt_write_is_exclusive(tmp_path):
    path = tmp_path / "receipt.txt"
    write_text_exclusive(path, "first")
    with pytest.raises(FileExistsError):
        write_text_exclusive(path, "second")
    assert path.read_text() == "first"


@pytest.mark.skipif(os.name != "posix", reason="process-group cleanup is POSIX")
def test_timeout_kills_real_descendant_and_preserves_output(tmp_path):
    marker = tmp_path / "child-survived"
    child_code = f"import time; from pathlib import Path; time.sleep(2); Path({str(marker)!r}).touch()"
    parent_code = (
        "import subprocess, sys, time; "
        f"subprocess.Popen([sys.executable, '-c', {child_code!r}]); "
        "print('partial answer', flush=True); print('diagnostic', file=sys.stderr, flush=True); time.sleep(10)"
    )
    result = run_process(
        [sys.executable, "-c", parent_code], cwd=tmp_path, timeout_seconds=1
    )
    assert result.failure == "timed out after 1s"
    assert result.returncode is None
    assert result.duration_seconds < 2
    assert result.stdout == "partial answer\n"
    assert result.stderr == "diagnostic\n"
    time.sleep(1.3)
    assert not marker.exists()


def test_inherited_output_handles_do_not_extend_parent_deadline(tmp_path):
    parent_code = "import subprocess, sys; subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(1)']); print('done')"
    result = run_process(
        [sys.executable, "-c", parent_code], cwd=tmp_path, timeout_seconds=1
    )
    assert result.returncode == 0
    assert result.failure is None
    assert result.duration_seconds < 0.8


@pytest.mark.skipif(os.name != "posix", reason="process-group cleanup is POSIX")
def test_successful_harness_cannot_leave_ordinary_descendant_running(tmp_path):
    survived = tmp_path / "survived"
    worker = f"import time; from pathlib import Path; time.sleep(1); Path({str(survived)!r}).touch()"
    parent = f"import subprocess, sys; subprocess.Popen([sys.executable, '-c', {worker!r}]); print('answer')"
    result = run_process(
        [sys.executable, "-c", parent], cwd=tmp_path, timeout_seconds=5
    )
    assert result.returncode == 0
    assert result.failure is None
    assert result.stdout == "answer\n"
    time.sleep(1.3)
    assert not survived.exists()


@pytest.mark.parametrize("stream", ["stdout", "stderr"])
def test_large_output_cannot_pass_or_exhaust_capture_memory(tmp_path, stream):
    code = f"import sys; sys.{stream}.buffer.write(b'x' * {MAX_STREAM_BYTES + 1})"
    result = run_process([sys.executable, "-c", code], cwd=tmp_path, timeout_seconds=10)
    assert result.returncode == 0
    assert "output exceeded" in result.failure
    assert len(getattr(result, stream)) == MAX_STREAM_BYTES


def test_invalid_utf8_is_preserved_as_decoding_replacement(tmp_path):
    result = run_process(
        [sys.executable, "-c", "import sys; sys.stdout.buffer.write(b'\\xff')"],
        cwd=tmp_path,
        timeout_seconds=5,
    )
    assert result.stdout == "\ufffd"


@pytest.mark.parametrize("command", ["list", "route"])
def test_negative_cli_limits_are_usage_errors(command):
    args = [command] + (["query"] if command == "route" else []) + ["--limit", "-1"]
    with pytest.raises(SystemExit) as exc:
        main(args)
    assert exc.value.code == 2


def test_cli_malformed_config_produces_diagnostic_without_traceback(tmp_path, capsys):
    (tmp_path / "cogsecskills.yaml").write_text("quality: not-a-mapping\n")
    assert main(["--root", str(tmp_path), "doctor"]) == 1
    assert "must be a mapping" in capsys.readouterr().err


def test_cli_limit_zero_is_empty_json(capsys):
    assert main(["list", "--limit", "0", "--format", "json"]) == 0
    assert json.loads(capsys.readouterr().out)["skills"] == []
