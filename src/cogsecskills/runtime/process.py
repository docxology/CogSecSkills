"""Bounded real subprocess execution for the opt-in harness runner.

File-backed streams avoid pipe deadlocks when a harness forks a child. POSIX
cleanup kills the process group so ordinary descendants cannot outlive a run.
"""

from __future__ import annotations

import os
import signal
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

MAX_STREAM_BYTES = 4 * 1024 * 1024


@dataclass(frozen=True)
class ProcessResult:
    stdout: str
    stderr: str
    returncode: int | None
    duration_seconds: float
    failure: str | None = None


def _kill_process_tree(process: subprocess.Popen) -> None:
    if os.name == "posix":
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    else:
        process.kill()
    process.wait()


def run_process(argv: list[str], *, cwd: Path, timeout_seconds: int) -> ProcessResult:
    """Execute argv without a shell and preserve bounded diagnostic output.

    The timeout bounds the direct process. On POSIX its session's process group is
    also killed; Windows currently guarantees cleanup of the direct process only.
    """
    started = time.monotonic()
    failure = None
    returncode: int | None = None
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        try:
            process = subprocess.Popen(
                argv,
                cwd=cwd,
                stdout=stdout,
                stderr=stderr,
                start_new_session=True,
            )
        except OSError as exc:
            return ProcessResult(
                "",
                "",
                None,
                time.monotonic() - started,
                f"could not start harness: {exc}",
            )
        try:
            returncode = process.wait(timeout=timeout_seconds)
            if os.name == "posix":
                _kill_process_tree(process)
        except subprocess.TimeoutExpired:
            _kill_process_tree(process)
            failure = f"timed out after {timeout_seconds}s"
        except BaseException:
            _kill_process_tree(process)
            raise
        stdout.seek(0)
        stderr.seek(0)
        raw_stdout = stdout.read(MAX_STREAM_BYTES + 1)
        raw_stderr = stderr.read(MAX_STREAM_BYTES + 1)
    if len(raw_stdout) > MAX_STREAM_BYTES or len(raw_stderr) > MAX_STREAM_BYTES:
        failure = (
            failure or f"harness output exceeded {MAX_STREAM_BYTES} bytes per stream"
        )
    return ProcessResult(
        raw_stdout[:MAX_STREAM_BYTES].decode("utf-8", errors="replace"),
        raw_stderr[:MAX_STREAM_BYTES].decode("utf-8", errors="replace"),
        returncode,
        time.monotonic() - started,
        failure,
    )
