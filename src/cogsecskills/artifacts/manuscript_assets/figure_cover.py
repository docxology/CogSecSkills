"""The title-page installation cover.

Kept apart from the body panels: it is the largest single panel, it owns the
COVER_* type scale that nothing else uses, and it is the one figure mirrored
outside ``output/figures`` for the manuscript title page.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from .figure_helpers import (
    _edge_for,
    _group_short,
    _group_summaries,
    _light_for,
    _publication_doi,
    _readable_text_color,
    _save,
)
from .figure_theme import (
    COLOR_FAMILIES,
    COVER_COMMAND_SIZE,
    COVER_FLOW_TITLE_SIZE,
    COVER_LABEL_SIZE,
    COVER_PANEL_TITLE_SIZE,
    COVER_STAT_LABEL_SIZE,
    COVER_STAT_VALUE_SIZE,
    FIGURE_SIZES,
    TOKENS,
)
from .paths import COVER_IMAGE_NAME
from .rows import SkillRow, _group_ids


def _write_cover_installation(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.pyplot as plt
    from matplotlib import patches

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["cover_installation"])
    fig.subplots_adjust(left=0.006, right=0.994, top=0.992, bottom=0.015)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor(TOKENS["surface"])

    total_skills = len(rows)
    groups = _group_ids(rows)
    harnesses = tuple(
        sorted({harness for row in rows for harness in row.harnesses})
    ) or (
        "claude",
        "codex",
        "hermes",
    )
    default_harnesses = ("claude", "codex", "hermes")

    def box(
        x: float,
        y: float,
        w: float,
        h: float,
        *,
        face: str,
        edge: str,
        radius: float = 0.018,
        linewidth: float = 1.05,
    ) -> patches.FancyBboxPatch:
        return patches.FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle=f"round,pad=0.010,rounding_size={radius}",
            facecolor=face,
            edgecolor=edge,
            linewidth=linewidth,
        )

    def label_chip(
        x: float,
        y: float,
        text: str,
        *,
        face: str,
        edge: str,
        text_color: str | None = None,
    ) -> None:
        ax.add_patch(box(x, y, 0.052, 0.032, face=face, edge=edge, radius=0.013))
        ax.text(
            x + 0.026,
            y + 0.016,
            text,
            ha="center",
            va="center",
            fontsize=13.0,
            fontweight="semibold",
            color=text_color or _readable_text_color(face),
        )

    def stat_card(
        idx: int, value: str, label: str, face: str, edge: str, *, y: float = 0.714
    ) -> None:
        stat_w = 0.205
        x = 0.063 + idx * (stat_w + 0.022)
        h = 0.084
        ax.add_patch(box(x, y, stat_w, h, face=face, edge=edge, radius=0.020))
        ax.text(
            x + 0.024,
            y + h / 2,
            value,
            ha="left",
            va="center",
            fontsize=COVER_STAT_VALUE_SIZE,
            fontweight="bold",
            color=TOKENS["ink"],
        )
        ax.text(
            x + 0.108,
            y + h / 2,
            label,
            ha="left",
            va="center",
            fontsize=COVER_STAT_LABEL_SIZE,
            color=TOKENS["muted"],
            linespacing=0.95,
        )

    def command_line(
        x: float,
        y: float,
        text: str,
        *,
        step: str,
        size: float = COVER_COMMAND_SIZE,
    ) -> None:
        label_chip(
            x,
            y - 0.003,
            step,
            face=COLOR_FAMILIES["neutral"]["light"],
            edge=COLOR_FAMILIES["neutral"]["mid"],
            text_color=TOKENS["ink"],
        )
        ax.text(
            x + 0.066,
            y,
            text,
            ha="left",
            va="top",
            fontsize=size,
            color=TOKENS["ink"],
            fontfamily="monospace",
        )

    ax.add_patch(
        box(
            0.030,
            0.045,
            0.940,
            0.910,
            face=TOKENS["panel"],
            edge=TOKENS["grid"],
            radius=0.028,
            linewidth=0.9,
        )
    )
    ax.text(
        0.060,
        0.949,
        "CogSecSkills",
        ha="left",
        va="top",
        fontsize=42,
        fontweight="bold",
        color=TOKENS["ink"],
    )
    # Accent rule under the wordmark to anchor the identity block.
    ax.add_patch(
        patches.Rectangle(
            (0.062, 0.876),
            0.252,
            0.006,
            facecolor=COLOR_FAMILIES["blue"]["mid"],
            edgecolor="none",
        )
    )
    ax.text(
        0.062,
        0.858,
        "A defensive, harness-neutral agent-skill library for cognitive security and analytic tradecraft.",
        ha="left",
        va="top",
        fontsize=15.6,
        color=TOKENS["muted"],
    )
    ax.text(
        0.062,
        0.822,
        "github.com/docxology/CogSecSkills",
        ha="left",
        va="top",
        fontsize=16.5,
        color=COLOR_FAMILIES["blue"]["dark"],
        fontfamily="monospace",
    )
    cover_doi = _publication_doi()
    if cover_doi:
        ax.text(
            0.662,
            0.838,
            f"DOI: {cover_doi}",
            ha="left",
            va="top",
            fontsize=14.5,
            color=COLOR_FAMILIES["blue"]["dark"],
            fontfamily="monospace",
        )
    ax.text(
        0.662,
        0.946,
        "Default adapters: Claude, Codex, Hermes.\n"
        "Optional profiles become structural only\n"
        "after config, regeneration, and validation.",
        ha="left",
        va="top",
        fontsize=14.2,
        color=TOKENS["muted"],
        linespacing=1.16,
    )
    stats = [
        (
            f"{total_skills}",
            "implemented\nskills",
            COLOR_FAMILIES["blue"]["xlight"],
            COLOR_FAMILIES["blue"]["dark"],
        ),
        (
            f"{len(groups)}",
            "taxonomy\ngroups",
            COLOR_FAMILIES["orange"]["xlight"],
            COLOR_FAMILIES["orange"]["dark"],
        ),
        (
            f"{len(default_harnesses)}",
            "default\nharnesses",
            COLOR_FAMILIES["olive"]["xlight"],
            COLOR_FAMILIES["olive"]["dark"],
        ),
        (
            f"{len(harnesses)}",
            "configured\nadapters",
            COLOR_FAMILIES["pink"]["xlight"],
            COLOR_FAMILIES["pink"]["dark"],
        ),
    ]
    for idx, (value, label, face, edge) in enumerate(stats):
        stat_card(idx, value, label, face, edge)

    # Live taxonomy band: name every defensive group with its skill count,
    # so the cover communicates the library's scope, not just its install route.
    ax.text(
        0.060,
        0.706,
        f"Seven defensive taxonomy groups · {total_skills} skills",
        ha="left",
        va="top",
        fontsize=COVER_LABEL_SIZE,
        fontweight="semibold",
        color=TOKENS["ink"],
    )
    summaries = _group_summaries(rows)
    band_x0 = 0.060
    band_w = 0.880
    band_gap = 0.012
    chip_w = (band_w - band_gap * (len(summaries) - 1)) / len(summaries)
    chip_y = 0.580
    chip_h = 0.092
    for gi, summary in enumerate(summaries):
        gid = str(summary["id"])
        gx = band_x0 + gi * (chip_w + band_gap)
        ax.add_patch(
            box(
                gx,
                chip_y,
                chip_w,
                chip_h,
                face=_light_for(gid),
                edge=_edge_for(gid),
                radius=0.015,
                linewidth=1.05,
            )
        )
        ax.text(
            gx + 0.013,
            chip_y + chip_h - 0.013,
            _group_short(gid),
            ha="left",
            va="top",
            fontsize=13.5,
            fontweight="bold",
            color=_edge_for(gid),
        )
        ax.text(
            gx + chip_w - 0.013,
            chip_y + chip_h - 0.011,
            str(summary["count"]),
            ha="right",
            va="top",
            fontsize=18.0,
            fontweight="bold",
            color=TOKENS["ink"],
        )
        title_lines = textwrap.wrap(str(summary["title"]), width=15)[:3]
        ax.text(
            gx + 0.013,
            chip_y + chip_h - 0.043,
            "\n".join(title_lines),
            ha="left",
            va="top",
            fontsize=8.0,
            color=TOKENS["ink"],
            linespacing=1.04,
        )

    ax.add_patch(
        box(
            0.060,
            0.298,
            0.430,
            0.262,
            face=COLOR_FAMILIES["neutral"]["xlight"],
            edge=COLOR_FAMILIES["neutral"]["dark"],
        )
    )
    ax.text(
        0.082,
        0.540,
        "Install and verify",
        ha="left",
        va="top",
        fontsize=COVER_PANEL_TITLE_SIZE,
        fontweight="semibold",
        color=TOKENS["ink"],
    )
    command_line(
        0.082,
        0.476,
        "git clone https://github.com/docxology/CogSecSkills.git",
        step="1",
        size=12.6,
    )
    command_line(0.082, 0.439, "cd CogSecSkills && uv sync", step="2")
    command_line(
        0.082,
        0.402,
        'export PYTHONPATH="src:."',
        step="3",
    )
    command_line(0.082, 0.365, "python -m cogsecskills validate", step="4")

    ax.add_patch(
        box(
            0.510,
            0.298,
            0.430,
            0.262,
            face=COLOR_FAMILIES["blue"]["xlight"],
            edge=COLOR_FAMILIES["blue"]["dark"],
        )
    )
    ax.text(
        0.532,
        0.540,
        "Connect an agent harness",
        ha="left",
        va="top",
        fontsize=COVER_PANEL_TITLE_SIZE,
        fontweight="semibold",
        color=TOKENS["ink"],
    )
    command_line(
        0.532,
        0.476,
        "python -m cogsecskills route",
        step="1",
    )
    command_line(
        0.532,
        0.439,
        "load SKILL.md + workflow.md",
        step="2",
    )
    command_line(
        0.532,
        0.402,
        "load harness/<name>.md",
        step="3",
    )
    command_line(0.532, 0.365, "custom harness: edit config", step="4")

    ax.add_patch(
        box(
            0.060,
            0.108,
            0.880,
            0.172,
            face=TOKENS["panel"],
            edge=TOKENS["axis"],
            radius=0.022,
            linewidth=0.9,
        )
    )
    lane_y = 0.150
    lane_items = [
        (
            "CLONE",
            "public repo",
            COLOR_FAMILIES["blue"]["base"],
            COLOR_FAMILIES["blue"]["dark"],
        ),
        (
            "CHECK",
            "validate gates",
            COLOR_FAMILIES["olive"]["base"],
            COLOR_FAMILIES["olive"]["dark"],
        ),
        (
            "ROUTE",
            "select skill",
            COLOR_FAMILIES["orange"]["base"],
            COLOR_FAMILIES["orange"]["dark"],
        ),
        (
            "LOAD",
            "adapter files",
            COLOR_FAMILIES["gold"]["base"],
            COLOR_FAMILIES["gold"]["dark"],
        ),
        (
            "RUN",
            "bounded output",
            COLOR_FAMILIES["pink"]["base"],
            COLOR_FAMILIES["pink"]["dark"],
        ),
    ]
    ax.text(
        0.082,
        0.268,
        "Source-owned run flow",
        ha="left",
        va="top",
        fontsize=COVER_FLOW_TITLE_SIZE,
        fontweight="semibold",
        color=TOKENS["ink"],
    )
    for idx, (title, label, face, edge) in enumerate(lane_items):
        x = 0.082 + idx * 0.172
        w = 0.140
        ax.add_patch(
            box(
                x,
                lane_y,
                w,
                0.074,
                face=face,
                edge=edge,
                radius=0.018,
            )
        )
        ax.text(
            x + w / 2,
            lane_y + 0.049,
            title,
            ha="center",
            va="center",
            fontsize=18.0,
            fontweight="bold",
            color=_readable_text_color(face),
        )
        ax.text(
            x + w / 2,
            lane_y + 0.020,
            label,
            ha="center",
            va="center",
            fontsize=12.4,
            color=_readable_text_color(face),
            fontfamily="monospace",
        )
        if idx < len(lane_items) - 1:
            ax.annotate(
                "",
                xy=(x + 0.166, lane_y + 0.037),
                xytext=(x + w + 0.008, lane_y + 0.037),
                arrowprops=dict(arrowstyle="-|>", color=TOKENS["muted"], lw=1.9),
            )

    ax.text(
        0.060,
        0.074,
        "Structural claim only: defaults ship; optional profiles require config, regenerated adapters, validation, and runtime review.",
        ha="left",
        va="center",
        fontsize=13.8,
        color=TOKENS["muted"],
    )
    return _save(fig, figures_dir / COVER_IMAGE_NAME)
