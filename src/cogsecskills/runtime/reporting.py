"""Live-report formatting and local persistence."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

from cogsecskills.runtime.models import LiveEvalReport
from cogsecskills.core.yaml_io import read_yaml
from cogsecskills.core.paths import contained_path


def write_text_exclusive(
    path: Path, text: str, *, boundary: Path | None = None
) -> None:
    """Create a receipt once without following a planted file/parent symlink.

    POSIX writes are anchored to an opened parent-directory descriptor. Recheck
    containment after harness execution; a conflicting path fails rather than
    overwriting previous evidence or a symlink target.
    """
    if boundary is not None:
        # The runner freezes an absolute, resolved output boundary before
        # invocation. Re-resolving a replaced boundary must not redefine trust.
        boundary = boundary.absolute()
        if boundary.resolve() != boundary:
            raise ValueError("live-eval output boundary was replaced by a symlink")
        contained_path(boundary, path.relative_to(boundary))
    if os.name == "posix":
        parent_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            descriptor = os.open(
                path.name,
                os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                0o600,
                dir_fd=parent_fd,
            )
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(text)
        finally:
            os.close(parent_fd)
    else:
        with path.open("x", encoding="utf-8") as stream:
            stream.write(text)


def write_report(
    report: LiveEvalReport, path: Path, *, boundary: Path | None = None
) -> None:
    """Persist the YAML report next to the transcripts."""
    path.parent.mkdir(parents=True, exist_ok=True)
    write_text_exclusive(
        path,
        yaml.safe_dump(report.to_dict(), sort_keys=False, allow_unicode=True),
        boundary=boundary,
    )


def format_report(report: LiveEvalReport) -> str:
    """Human-readable summary with the claim boundary footer."""
    lines = [
        f"live eval: harness={report.harness} mode={report.mode}",
        f"claim boundary: {report.claim_boundary}",
        "",
    ]
    for result in report.results:
        passed = sum(1 for check in result.checks if check.passed)
        status = "PASS" if result.ok else "FAIL"
        lines.append(
            f"{status} {result.scenario_id} ({passed}/{len(result.checks)} checks)"
        )
        for check in result.checks:
            marker = "ok" if check.passed else "MISS"
            lines.append(f"  [{marker}] {check.name}: {check.detail}")
        rubric = ", ".join(f"{k}={v}" for k, v in result.auto_rubric.items())
        lines.append(f"  mechanical rubric screening: {rubric}")
    total = len(report.results)
    failures = sum(1 for result in report.results if not result.ok)
    lines.append("")
    lines.append(
        f"{total - failures}/{total} scenarios passed mechanical screening; "
        f"transcripts under {report.output_dir}"
    )
    return "\n".join(lines)


def parse_live_eval_yaml(path: Path) -> list[dict[str, Any]]:
    """Load a persisted YAML live-eval report (helper for reviewers)."""
    raw = read_yaml(path)
    if (
        not isinstance(raw, dict)
        or not isinstance(raw.get("results"), list)
        or not all(isinstance(row, dict) for row in raw["results"])
    ):
        raise ValueError(f"{path}: expected a live-eval report mapping")
    return raw["results"]
