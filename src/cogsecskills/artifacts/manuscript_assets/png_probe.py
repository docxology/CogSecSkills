"""Dependency-free PNG inspection for the generated-figure drift gate.

``check_assets`` compares generated Markdown byte-for-byte, but figures cannot be
compared that way: matplotlib PNG output is not reproducible across matplotlib,
freetype, and OS versions, so an exact-bytes gate would flap across the CI
Python matrix rather than catch real breakage.

The checks here are the strongest ones that stay deterministic regardless of
rendering environment:

* **Header validity** — the file really is a PNG.
* **Pixel floor** — read straight from the IHDR chunk, so a thumbnail or a
  collapsed canvas is rejected.
* **Byte floor** — a blank figure at the project's 240 DPI compresses to roughly
  37 KB, while the smallest real figure is over 300 KB. The floor sits between
  those, well clear of both.
* **Mutual distinctness** — enforced by the caller. No two generated figures may
  be byte-identical, which is what catches one figure being written over
  another.

Reading IHDR directly keeps PyYAML the runner's only runtime dependency; the
``figures`` extra (matplotlib/numpy/seaborn) stays needed only for *writing*
figures, never for verifying them.
"""

from __future__ import annotations

import struct
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# A blank 16x9 canvas at FIGURE_DPI=240 is ~37 KB; the smallest committed figure
# is ~305 KB. 100 KB separates them with margin on both sides.
MIN_FIGURE_BYTES = 100_000

# Every committed figure is at least 3339x1728 px. 1000 px on a side rejects
# thumbnails and collapsed canvases without tracking exact layout dimensions,
# which shift with font metrics and tight-bbox cropping.
MIN_FIGURE_PIXELS = 1_000

# Byte offsets of the IHDR width/height fields in a well-formed PNG.
_IHDR_DIMENSIONS = slice(16, 24)


def png_dimensions(data: bytes) -> tuple[int, int] | None:
    """Return ``(width, height)`` from a PNG's IHDR chunk, or ``None`` if unreadable."""
    if not data.startswith(PNG_SIGNATURE) or len(data) < _IHDR_DIMENSIONS.stop:
        return None
    width, height = struct.unpack(">II", data[_IHDR_DIMENSIONS])
    return width, height


def figure_findings(rel_path: str, data: bytes) -> list[str]:
    """Return drift findings for one generated figure's bytes.

    ``rel_path`` is used only to label findings, so callers can report a path
    that reads the same way as the rest of ``check_assets`` output.
    """
    findings: list[str] = []
    dimensions = png_dimensions(data)
    if dimensions is None:
        findings.append(f"invalid generated figure: {rel_path}")
        return findings

    width, height = dimensions
    if width < MIN_FIGURE_PIXELS or height < MIN_FIGURE_PIXELS:
        findings.append(
            f"undersized generated figure: {rel_path} "
            f"({width}x{height}px, minimum {MIN_FIGURE_PIXELS}px per side)"
        )
    if len(data) < MIN_FIGURE_BYTES:
        findings.append(
            f"near-empty generated figure: {rel_path} "
            f"({len(data)} bytes, minimum {MIN_FIGURE_BYTES})"
        )
    return findings


def duplicate_figure_findings(figures: dict[str, bytes]) -> list[str]:
    """Return findings for figures whose bytes are identical to another figure.

    Distinct figures answer distinct reader questions, so identical bytes mean
    one figure was written over another — the failure the size and header checks
    cannot see, because the wrong image is still a perfectly valid PNG.
    """
    by_digest: dict[bytes, list[str]] = {}
    for rel_path, data in figures.items():
        by_digest.setdefault(data, []).append(rel_path)

    findings: list[str] = []
    for shared in by_digest.values():
        if len(shared) > 1:
            joined = ", ".join(sorted(shared))
            findings.append(f"duplicate generated figures (identical bytes): {joined}")
    return sorted(findings)


def read_figure_bytes(path: Path) -> bytes | None:
    """Return ``path``'s bytes, or ``None`` when it is not a readable file."""
    if not path.is_file():
        return None
    return path.read_bytes()
