"""Tests for the dependency-free PNG checks behind the generated-figure gate.

PNG bytes are synthesised here rather than rendered with matplotlib: the checks
under test read only the signature and the IHDR width/height, so a hand-built
header exercises them exactly while keeping these tests deterministic and
independent of the optional ``figures`` extra.
"""

from __future__ import annotations

import struct

from cogsecskills.artifacts.manuscript_assets.png_probe import (
    MIN_FIGURE_BYTES,
    MIN_FIGURE_PIXELS,
    PNG_SIGNATURE,
    duplicate_figure_findings,
    figure_findings,
    png_dimensions,
    read_figure_bytes,
)


def _png(width: int, height: int, *, size: int = MIN_FIGURE_BYTES) -> bytes:
    """Build PNG bytes whose IHDR reports ``width`` x ``height``, padded to ``size``."""
    header = PNG_SIGNATURE + struct.pack(">I", 13) + b"IHDR"
    header += struct.pack(">II", width, height)
    return header + b"\x00" * max(0, size - len(header))


def test_png_dimensions_reads_ihdr():
    assert png_dimensions(_png(3339, 1728)) == (3339, 1728)


def test_png_dimensions_rejects_non_png():
    assert png_dimensions(b"GIF89a" + b"\x00" * 100) is None


def test_png_dimensions_rejects_truncated_header():
    assert png_dimensions(PNG_SIGNATURE + b"\x00" * 4) is None


def test_figure_findings_accepts_a_realistic_figure():
    assert figure_findings("output/figures/a.png", _png(3339, 1728)) == []


def test_figure_findings_flags_a_non_png():
    findings = figure_findings("output/figures/a.png", b"not a png at all")
    assert findings == ["invalid generated figure: output/figures/a.png"]


def test_figure_findings_flags_undersized_dimensions():
    small = MIN_FIGURE_PIXELS - 1
    findings = figure_findings("output/figures/a.png", _png(small, 2000))
    assert len(findings) == 1
    assert "undersized generated figure" in findings[0]
    assert f"{small}x2000px" in findings[0]


def test_figure_findings_flags_a_near_empty_figure():
    # A blank canvas is a valid, correctly-sized PNG that simply compresses small.
    findings = figure_findings(
        "output/figures/a.png", _png(3339, 1728, size=MIN_FIGURE_BYTES - 1)
    )
    assert len(findings) == 1
    assert "near-empty generated figure" in findings[0]


def test_figure_findings_can_report_both_problems():
    findings = figure_findings("output/figures/a.png", _png(10, 10, size=500))
    assert len(findings) == 2


def test_duplicate_findings_empty_when_all_figures_differ():
    figures = {"a.png": _png(3000, 2000), "b.png": _png(3100, 2000)}
    assert duplicate_figure_findings(figures) == []


def test_duplicate_findings_detect_one_figure_written_over_another():
    # The failure the old size/header gate could not see: a perfectly valid PNG
    # that happens to be the wrong image.
    shared = _png(3000, 2000)
    figures = {"taxonomy.png": shared, "heatmap.png": shared, "grid.png": _png(1, 1)}
    findings = duplicate_figure_findings(figures)
    assert len(findings) == 1
    assert "heatmap.png, taxonomy.png" in findings[0]


def test_duplicate_findings_are_sorted_for_stable_output():
    figures = {
        "b.png": _png(2000, 2000),
        "a.png": _png(2000, 2000),
        "d.png": _png(3000, 3000),
        "c.png": _png(3000, 3000),
    }
    assert duplicate_figure_findings(figures) == sorted(
        duplicate_figure_findings(figures)
    )
    assert len(duplicate_figure_findings(figures)) == 2


def test_read_figure_bytes_round_trips_a_real_file(tmp_path):
    path = tmp_path / "figure.png"
    payload = _png(3000, 2000)
    path.write_bytes(payload)
    assert read_figure_bytes(path) == payload


def test_read_figure_bytes_returns_none_for_missing_file(tmp_path):
    assert read_figure_bytes(tmp_path / "absent.png") is None


def test_read_figure_bytes_returns_none_for_a_directory(tmp_path):
    directory = tmp_path / "figures"
    directory.mkdir()
    assert read_figure_bytes(directory) is None
