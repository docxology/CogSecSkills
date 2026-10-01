"""Orchestration: write all generated assets and check them for drift.

``write_assets`` regenerates Markdown supplements, data exports, and figures
from the live registry; ``check_assets`` compares the on-disk assets against the
canonical expected output and reports any drift.
"""

from __future__ import annotations

from pathlib import Path

from cogsecskills.artifacts.text_outputs import check_text_outputs, write_text_outputs
from cogsecskills.core.locate import resolve_root

from .figures import FIGURE_NAMES, write_figures
from .paths import (
    CATALOGUE_PATH,
    COVER_IMAGE_MIRROR_PATH,
    COVER_IMAGE_NAME,
    DATA_CSV_PATH,
    DATA_JSON_PATH,
    MATRIX_PATH,
)
from .png_probe import (
    duplicate_figure_findings,
    figure_findings,
    read_figure_bytes,
)
from .rows import AssetWriteResult, collect_skill_rows
from .tables import _expected_texts


def write_assets(root: Path | None = None) -> AssetWriteResult:
    """Write generated manuscript supplements, data exports, and figures."""
    base = resolve_root(root)
    rows = collect_skill_rows(base)
    text_outputs = _expected_texts(base)
    write_text_outputs(base, text_outputs)

    figure_paths = write_figures(rows, base)
    return {
        "skills": len(rows),
        "markdown": [str(CATALOGUE_PATH), str(MATRIX_PATH)],
        "data": [str(DATA_JSON_PATH), str(DATA_CSV_PATH)],
        "figures": [str(path.relative_to(base)) for path in figure_paths],
    }


def check_assets(root: Path | None = None) -> list[str]:
    """Return drift findings for generated manuscript assets."""
    base = resolve_root(root)
    findings = check_text_outputs(base, _expected_texts(base))

    figures_dir = base / "output" / "figures"
    figure_bytes: dict[str, bytes] = {}
    for name in FIGURE_NAMES:
        figure_rel = f"output/figures/{name}"
        data = read_figure_bytes(figures_dir / name)
        if data is None:
            findings.append(f"missing generated figure: {figure_rel}")
            continue
        figure_bytes[figure_rel] = data
        findings.extend(figure_findings(figure_rel, data))
    findings.extend(duplicate_figure_findings(figure_bytes))
    cover_path = figures_dir / COVER_IMAGE_NAME
    mirror_path = base / COVER_IMAGE_MIRROR_PATH
    if not mirror_path.is_file():
        findings.append(
            f"missing generated cover image mirror: {COVER_IMAGE_MIRROR_PATH}"
        )
    elif cover_path.is_file() and mirror_path.read_bytes() != cover_path.read_bytes():
        findings.append(
            f"stale generated cover image mirror: {COVER_IMAGE_MIRROR_PATH}"
        )
    return findings
