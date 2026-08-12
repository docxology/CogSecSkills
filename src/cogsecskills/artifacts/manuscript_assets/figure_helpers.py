"""Shared drawing, theming, and summarising helpers for the figure panels.

Every ``_write_*`` panel in ``figure_panels`` draws through these, which is what
keeps the eight figures visually consistent. Heavy plotting imports stay inside
the functions so importing this module remains cheap.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from .figure_theme import (
    AXIS_LABEL_SIZE,
    COLOR_FAMILIES,
    FIGURE_DPI,
    GROUP_COLORS,
    GROUP_EDGE_COLORS,
    GROUP_LIGHT_COLORS,
    SUBTITLE_SIZE,
    TICK_LABEL_SIZE,
    TITLE_SIZE,
    TOKENS,
)
from .paths import _project_root
from .rows import GroupSummary, SkillRow, _group_ids, _group_title


def _save(fig, path: Path) -> Path:
    fig.savefig(
        path, dpi=FIGURE_DPI, bbox_inches="tight", facecolor=fig.get_facecolor()
    )
    import matplotlib.pyplot as plt

    plt.close(fig)
    return path


def _use_chart_theme() -> None:
    import seaborn as sns

    sns.set_theme(
        style="whitegrid",
        rc={
            "figure.facecolor": TOKENS["surface"],
            "figure.edgecolor": "none",
            "savefig.facecolor": TOKENS["surface"],
            "savefig.edgecolor": "none",
            "axes.facecolor": TOKENS["panel"],
            "axes.edgecolor": TOKENS["axis"],
            "axes.labelcolor": TOKENS["ink"],
            "axes.grid": True,
            "axes.labelsize": AXIS_LABEL_SIZE,
            "grid.color": TOKENS["grid"],
            "grid.linewidth": 0.8,
            "font.size": TICK_LABEL_SIZE,
            "font.family": "sans-serif",
            "font.sans-serif": [
                "Aptos",
                "Inter",
                "Segoe UI",
                "DejaVu Sans",
                "Arial",
                "sans-serif",
            ],
            "font.monospace": [
                "SF Mono",
                "Menlo",
                "Consolas",
                "DejaVu Sans Mono",
                "monospace",
            ],
            "patch.linewidth": 1.0,
            "xtick.labelsize": TICK_LABEL_SIZE,
            "ytick.labelsize": TICK_LABEL_SIZE,
        },
    )


def _add_chart_header(
    fig,
    ax,
    title: str,
    subtitle: str,
    *,
    title_width: int = 76,
    subtitle_width: int = 118,
    top: float = 0.84,
) -> None:
    from matplotlib.lines import Line2D

    title = textwrap.fill(str(title).strip(), width=title_width)
    subtitle = textwrap.fill(str(subtitle).strip(), width=subtitle_width)
    title_lines = title.count("\n") + 1
    subtitle_lines = subtitle.count("\n") + 1
    adjusted_top = max(
        0.58, top - 0.035 * (title_lines - 1) - 0.024 * (subtitle_lines - 1)
    )
    fig.subplots_adjust(top=adjusted_top)
    left = ax.get_position().x0
    fig.text(
        left,
        0.985,
        title,
        ha="left",
        va="top",
        fontsize=TITLE_SIZE,
        fontweight="semibold",
        color=TOKENS["ink"],
        linespacing=1.08,
    )
    fig.text(
        left,
        0.93 - 0.041 * (title_lines - 1),
        subtitle,
        ha="left",
        va="top",
        fontsize=SUBTITLE_SIZE,
        color=TOKENS["muted"],
        linespacing=1.18,
    )
    accent_x = max(0.012, left - 0.012)
    accent_bottom = max(0.86, 0.925 - 0.041 * (title_lines - 1))
    fig.add_artist(
        Line2D(
            [accent_x, accent_x],
            [accent_bottom, 0.985],
            color=COLOR_FAMILIES["blue"]["mid"],
            linewidth=2.0,
            solid_capstyle="round",
            transform=fig.transFigure,
        )
    )
    ax.set_title("")


def _style_axes(ax, *, grid_axis: str = "x") -> None:
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(TOKENS["axis"])
        ax.spines[side].set_linewidth(1.0)
    ax.tick_params(colors=TOKENS["muted"], labelsize=TICK_LABEL_SIZE, length=0)
    ax.xaxis.label.set_color(TOKENS["muted"])
    ax.yaxis.label.set_color(TOKENS["muted"])
    if grid_axis == "x":
        ax.grid(axis="x", color=TOKENS["grid"], linewidth=0.8)
        ax.grid(axis="y", visible=False)
    elif grid_axis == "y":
        ax.grid(axis="y", color=TOKENS["grid"], linewidth=0.8)
        ax.grid(axis="x", visible=False)
    else:
        ax.grid(False)


def _color_for(group_id: str) -> str:
    return GROUP_COLORS.get(group_id, COLOR_FAMILIES["neutral"]["base"])


def _edge_for(group_id: str) -> str:
    return GROUP_EDGE_COLORS.get(group_id, COLOR_FAMILIES["neutral"]["dark"])


def _light_for(group_id: str) -> str:
    return GROUP_LIGHT_COLORS.get(group_id, COLOR_FAMILIES["neutral"]["xlight"])


def _publication_doi(root: Path | None = None) -> str:
    """Return ``publication.doi`` from the manuscript config, or "" if unset.

    The cover figure surfaces the archived DOI once a release reserves it; until
    then the field is empty and the cover simply omits the DOI line.
    """
    import yaml

    config_path = _project_root(root) / "manuscript" / "config.yaml"
    try:
        data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return ""
    publication = data.get("publication") or {}
    return str(publication.get("doi") or "").strip()


def _group_short(group_id: str) -> str:
    labels = {
        "sat": "SAT",
        "cognitive_security": "COG",
        "critical_review": "REV",
        "osint_integrity": "OSINT",
        "counterintelligence": "CI",
        "information_environment": "INFO",
        "research_methods": "METHOD",
    }
    return labels.get(group_id, group_id[:6].upper())


def _readable_text_color(hex_color: str) -> str:
    hex_color = hex_color.lstrip("#")
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)
    luminance = (0.2126 * red + 0.7152 * green + 0.0722 * blue) / 255
    return TOKENS["ink"] if luminance > 0.62 else TOKENS["panel"]


def _group_summaries(rows: list[SkillRow]) -> list[GroupSummary]:
    summaries: list[GroupSummary] = []
    for group_id in _group_ids(rows):
        group_rows = [row for row in rows if row.group == group_id]
        references = sum(row.references_count for row in group_rows)
        count = len(group_rows)
        summaries.append(
            {
                "id": group_id,
                "title": _group_title(rows, group_id),
                "count": count,
                "references": references,
                "references_per_skill": references / count if count else 0.0,
            }
        )
    return summaries


def _vertical_positions(
    items, *, top: float = 0.82, bottom: float = 0.18
) -> dict[str, float]:
    ordered = list(items)
    if not ordered:
        return {}
    if len(ordered) == 1:
        return {ordered[0]: (top + bottom) / 2}
    step = (top - bottom) / (len(ordered) - 1)
    return {item: top - index * step for index, item in enumerate(ordered)}
