"""Shared deterministic text artifact writing and drift diagnostics."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from cogsecskills.core.paths import contained_path


def write_text_outputs(base: Path, outputs: Mapping[Path, str]) -> None:
    """Write each declared artifact after its expected content is collected."""
    destinations = {
        contained_path(base, rel_path): text for rel_path, text in outputs.items()
    }
    for path, text in destinations.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def check_text_outputs(
    base: Path, outputs: Mapping[Path, str], *, label: str = "generated file"
) -> list[str]:
    """Compare artifacts with readable UTF-8 source text, reporting read failures."""
    findings = []
    for rel_path, expected in outputs.items():
        try:
            path = contained_path(base, rel_path)
        except (ValueError, OSError, RuntimeError) as exc:
            findings.append(f"unsafe {label}: {rel_path} ({exc})")
            continue
        if not path.is_file():
            findings.append(f"missing {label}: {rel_path}")
            continue
        try:
            actual = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            findings.append(f"unreadable {label}: {rel_path} ({exc})")
            continue
        if actual != expected:
            findings.append(f"stale {label}: {rel_path}")
    return findings
