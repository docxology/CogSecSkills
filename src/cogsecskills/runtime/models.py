"""Typed results for mechanical live-evaluation screening."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LiveCheck:
    """One deterministic mechanical check against a live transcript."""

    name: str
    passed: bool
    detail: str


@dataclass(frozen=True)
class LiveScenarioResult:
    """Outcome of one live harness invocation for one scenario."""

    scenario_id: str
    harness: str
    mode: str
    ok: bool
    returncode: int | None
    duration_seconds: float
    checks: tuple[LiveCheck, ...]
    auto_rubric: dict[str, int]
    transcript_path: str | None
    stderr_path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "scenario_id": self.scenario_id,
            "harness": self.harness,
            "mode": self.mode,
            "ok": self.ok,
            "returncode": self.returncode,
            "duration_seconds": round(self.duration_seconds, 3),
            "checks": [
                {"name": c.name, "passed": c.passed, "detail": c.detail}
                for c in self.checks
            ],
            "auto_rubric": dict(self.auto_rubric),
            "transcript_path": self.transcript_path,
            "stderr_path": self.stderr_path,
        }


@dataclass(frozen=True)
class LiveEvalReport:
    """Full report for one live-eval invocation."""

    harness: str
    mode: str
    claim_boundary: str
    results: tuple[LiveScenarioResult, ...]
    output_dir: str

    @property
    def ok(self) -> bool:
        return bool(self.results) and all(result.ok for result in self.results)

    def to_dict(self) -> dict[str, Any]:
        return {
            "harness": self.harness,
            "mode": self.mode,
            "claim_boundary": self.claim_boundary,
            "ok": self.ok,
            "output_dir": self.output_dir,
            "results": [result.to_dict() for result in self.results],
        }
