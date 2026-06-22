"""Deterministic figure generation and the shared chart theme/style helpers.

Figure metadata, the design tokens and color families, and every ``_write_*``
generator live here. Heavy plotting dependencies (matplotlib, seaborn, numpy)
are imported lazily inside the functions that need them, exactly as in the
original module, so importing this submodule stays cheap.
"""

from __future__ import annotations

import textwrap
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from .paths import COVER_IMAGE_MIRROR_PATH, COVER_IMAGE_NAME, _project_root
from .rows import (
    GroupSummary,
    SkillRow,
    _group_ids,
    _group_title,
)


@dataclass(frozen=True)
class FigureMetadata:
    filename: str
    source: str
    reader_question: str
    semantic_labels: tuple[str, ...]
    mirrored: bool = False


FIGURES = (
    FigureMetadata(
        "cogsecskills_taxonomy_counts.png",
        "../output/figures/cogsecskills_taxonomy_counts.png",
        "How are skills distributed across the seven taxonomy groups?",
        ("Taxonomy", "skill counts", "share"),
    ),
    FigureMetadata(
        "cogsecskills_skill_grid.png",
        "../output/figures/cogsecskills_skill_grid.png",
        "Can the reader scan all 100 skills as one compact library surface?",
        ("100 skills", "library atlas", "group"),
    ),
    FigureMetadata(
        "cogsecskills_verb_heatmap.png",
        "../output/figures/cogsecskills_verb_heatmap.png",
        "Which groups exercise which neutral tool verbs most often?",
        ("verb", "heatmap", "group"),
    ),
    FigureMetadata(
        "cogsecskills_ageint_network.png",
        "../output/figures/cogsecskills_ageint_network.png",
        "How do skill groups connect to AGEINT teaching topics?",
        ("AGEINT", "teaching", "topic"),
    ),
    FigureMetadata(
        "cogsecskills_plan_build_teach_flow.png",
        "../output/figures/cogsecskills_plan_build_teach_flow.png",
        "How do plan, build, teach, validation, and manuscript generation fit together?",
        ("Plan", "Build", "Teach", "Run"),
    ),
    FigureMetadata(
        "cogsecskills_reference_density.png",
        "../output/figures/cogsecskills_reference_density.png",
        "Which groups carry the deepest declared source-reference backing per skill?",
        ("Reference Density", "references", "metadata"),
    ),
    FigureMetadata(
        "cogsecskills_harness_contract.png",
        "../output/figures/cogsecskills_harness_contract.png",
        "Does each group maintain configured harness adapter coverage?",
        ("Harness Contract", "adapter", "coverage"),
    ),
    FigureMetadata(
        COVER_IMAGE_NAME,
        "../output/figures/cogsecskills_cover_installation.png",
        "How does a reader install CogSecSkills from GitHub into an agent harness?",
        ("GitHub", "install", "harness"),
        mirrored=True,
    ),
)
FIGURE_NAMES = tuple(figure.filename for figure in FIGURES)

FIGURE_DPI = 240
TITLE_SIZE = 23
SUBTITLE_SIZE = 15
AXIS_LABEL_SIZE = 14
TICK_LABEL_SIZE = 13
ANNOTATION_SIZE = 13
CELL_LABEL_SIZE = 14
SMALL_LABEL_SIZE = 11.5
CAPTION_LABEL_SIZE = 14
COVER_PANEL_TITLE_SIZE = 23
COVER_COMMAND_SIZE = 15.2
COVER_LABEL_SIZE = 18.5
COVER_FLOW_TITLE_SIZE = 20
COVER_STAT_VALUE_SIZE = 38
COVER_STAT_LABEL_SIZE = 16.2

FIGURE_SIZES = {
    "taxonomy_counts": (16.2, 9.2),
    "skill_grid": (18.4, 18.2),
    "verb_heatmap": (17.4, 9.4),
    "ageint_network": (19.0, 10.6),
    "plan_build_teach_flow": (18.4, 8.8),
    "reference_density": (16.2, 9.2),
    "harness_contract": (18.4, 8.0),
    "cover_installation": (17.2, 9.2),
}

TOKENS = {
    "surface": "#FCFCFD",
    "panel": "#FFFFFF",
    "ink": "#1F2430",
    "muted": "#6F768A",
    "grid": "#E6E8F0",
    "axis": "#D7DBE7",
}

COLOR_FAMILIES = {
    "blue": {
        "xlight": "#EAF1FE",
        "light": "#CEDFFE",
        "base": "#A3BEFA",
        "mid": "#5477C4",
        "dark": "#2E4780",
    },
    "gold": {
        "xlight": "#FFF4C2",
        "light": "#FFEA8F",
        "base": "#FFE15B",
        "mid": "#B8A037",
        "dark": "#736422",
    },
    "orange": {
        "xlight": "#FFEDDE",
        "light": "#FFBDA1",
        "base": "#F0986E",
        "mid": "#CC6F47",
        "dark": "#804126",
    },
    "olive": {
        "xlight": "#D8ECBD",
        "light": "#BEEB96",
        "base": "#A3D576",
        "mid": "#71B436",
        "dark": "#386411",
    },
    "pink": {
        "xlight": "#FCDAD6",
        "light": "#F5BACC",
        "base": "#F390CA",
        "mid": "#BD569B",
        "dark": "#8A3A6F",
    },
    "neutral": {
        "xlight": "#F4F5F7",
        "light": "#E2E5EA",
        "base": "#C5CAD3",
        "mid": "#7A828F",
        "dark": "#464C55",
    },
}

GROUP_COLORS = {
    "sat": COLOR_FAMILIES["blue"]["base"],
    "cognitive_security": COLOR_FAMILIES["orange"]["base"],
    "critical_review": COLOR_FAMILIES["pink"]["base"],
    "osint_integrity": COLOR_FAMILIES["olive"]["base"],
    "counterintelligence": COLOR_FAMILIES["gold"]["base"],
    "information_environment": COLOR_FAMILIES["blue"]["light"],
    "research_methods": COLOR_FAMILIES["neutral"]["base"],
}

GROUP_EDGE_COLORS = {
    "sat": COLOR_FAMILIES["blue"]["dark"],
    "cognitive_security": COLOR_FAMILIES["orange"]["dark"],
    "critical_review": COLOR_FAMILIES["pink"]["dark"],
    "osint_integrity": COLOR_FAMILIES["olive"]["dark"],
    "counterintelligence": COLOR_FAMILIES["gold"]["dark"],
    "information_environment": COLOR_FAMILIES["blue"]["mid"],
    "research_methods": COLOR_FAMILIES["neutral"]["dark"],
}

GROUP_LIGHT_COLORS = {
    "sat": COLOR_FAMILIES["blue"]["xlight"],
    "cognitive_security": COLOR_FAMILIES["orange"]["xlight"],
    "critical_review": COLOR_FAMILIES["pink"]["xlight"],
    "osint_integrity": COLOR_FAMILIES["olive"]["xlight"],
    "counterintelligence": COLOR_FAMILIES["gold"]["xlight"],
    "information_environment": COLOR_FAMILIES["blue"]["xlight"],
    "research_methods": COLOR_FAMILIES["neutral"]["xlight"],
}

_PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def write_figures(rows: list[SkillRow], root: Path | None = None) -> list[Path]:
    """Write deterministic PNG figures under ``output/figures``."""
    base = _project_root(root)
    figures_dir = base / "output" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    import matplotlib

    matplotlib.use("Agg")
    _use_chart_theme()

    paths = [
        _write_taxonomy_counts(rows, figures_dir),
        _write_skill_grid(rows, figures_dir),
        _write_verb_heatmap(rows, figures_dir),
        _write_ageint_network(rows, figures_dir),
        _write_plan_build_teach_flow(figures_dir),
        _write_reference_density(rows, figures_dir),
        _write_harness_contract(rows, figures_dir),
        _write_cover_installation(rows, figures_dir),
    ]
    cover_mirror = base / COVER_IMAGE_MIRROR_PATH
    cover_mirror.parent.mkdir(parents=True, exist_ok=True)
    cover_mirror.write_bytes((figures_dir / COVER_IMAGE_NAME).read_bytes())
    return paths


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


def _write_taxonomy_counts(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.pyplot as plt

    summaries = sorted(
        _group_summaries(rows),
        key=lambda item: (-int(item["count"]), str(item["title"])),
    )
    total = sum(int(item["count"]) for item in summaries) or 1
    labels = [textwrap.fill(str(item["title"]), width=28) for item in summaries]
    counts = [int(item["count"]) for item in summaries]
    colors = [_color_for(str(item["id"])) for item in summaries]
    edges = [_edge_for(str(item["id"])) for item in summaries]

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["taxonomy_counts"])
    y_positions = list(range(len(summaries)))
    bars = ax.barh(y_positions, counts, color=colors, edgecolor=edges, linewidth=1.3)
    ax.set_yticks(y_positions, labels)
    ax.set_xlabel("Implemented skills")
    ax.set_xlim(0, (max(counts) if counts else 1) + 14)
    ax.invert_yaxis()
    _style_axes(ax, grid_axis="x")

    for bar, item in zip(bars, summaries):
        count = int(item["count"])
        share = count / total
        references = int(item["references"])
        density = float(item["references_per_skill"])
        label = (
            f"{count} skills | {share:.0%} | {references} refs | {density:.1f}/skill"
        )
        ax.text(
            count + 0.7,
            bar.get_y() + bar.get_height() / 2,
            label,
            ha="left",
            va="center",
            fontsize=ANNOTATION_SIZE,
            color=TOKENS["ink"],
        )
        ax.text(
            0.5,
            bar.get_y() + bar.get_height() / 2,
            _group_short(str(item["id"])),
            ha="left",
            va="center",
            fontsize=SMALL_LABEL_SIZE,
            fontweight="bold",
            color=_readable_text_color(_color_for(str(item["id"]))),
        )

    ax.text(
        0.99,
        0.045,
        f"Total: {total} implemented skills across {len(summaries)} groups",
        transform=ax.transAxes,
        ha="right",
        va="center",
        fontsize=CAPTION_LABEL_SIZE,
        color=TOKENS["muted"],
    )

    _add_chart_header(
        fig,
        ax,
        "Taxonomy concentration across seven skill groups",
        "Largest groups appear first; direct labels report skill count, library share, declared references, and reference metadata density.",
    )
    return _save(fig, figures_dir / FIGURE_NAMES[0])


def _write_skill_grid(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.patches as patches
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["skill_grid"])
    for index, row in enumerate(rows):
        col = index % 10
        row_pos = 9 - (index // 10)
        rect = patches.Rectangle(
            (col, row_pos),
            1,
            1,
            facecolor=_color_for(row.group),
            edgecolor="white",
            linewidth=0.8,
        )
        ax.add_patch(rect)
        ax.text(
            col + 0.5,
            row_pos + 0.58,
            f"{index + 1}",
            ha="center",
            va="center",
            color=_readable_text_color(_color_for(row.group)),
            fontsize=12.4,
            fontweight="bold",
        )
        ax.text(
            col + 0.5,
            row_pos + 0.32,
            _group_short(row.group),
            ha="center",
            va="center",
            color=_readable_text_color(_color_for(row.group)),
            fontsize=8.5,
            alpha=0.94,
            fontweight="semibold",
        )

    for index, row in enumerate(rows):
        col = index % 10
        row_pos = 9 - (index // 10)
        boundaries = {
            "left": col == 0 or rows[index - 1].group != row.group,
            "right": col == 9
            or index == len(rows) - 1
            or rows[index + 1].group != row.group,
            "top": index < 10 or rows[index - 10].group != row.group,
            "bottom": index + 10 >= len(rows) or rows[index + 10].group != row.group,
        }
        color = _edge_for(row.group)
        if boundaries["left"]:
            ax.plot([col, col], [row_pos, row_pos + 1], color=color, linewidth=2.2)
        if boundaries["right"]:
            ax.plot(
                [col + 1, col + 1], [row_pos, row_pos + 1], color=color, linewidth=2.2
            )
        if boundaries["top"]:
            ax.plot(
                [col, col + 1], [row_pos + 1, row_pos + 1], color=color, linewidth=2.2
            )
        if boundaries["bottom"]:
            ax.plot([col, col + 1], [row_pos, row_pos], color=color, linewidth=2.2)

    ax.set_xlim(-0.58, 10.55)
    span_y = -0.72
    span_height = 0.32
    group_start = 0
    for group_id in _group_ids(rows):
        count = sum(1 for row in rows if row.group == group_id)
        start_x = group_start / 10
        width = count / 10
        ax.add_patch(
            patches.Rectangle(
                (start_x, span_y),
                width,
                span_height,
                facecolor=_color_for(group_id),
                edgecolor=_edge_for(group_id),
                linewidth=1.1,
            )
        )
        start = group_start + 1
        end = group_start + count
        short_label = _group_short(group_id)
        band_label = "METH" if short_label == "METHOD" else short_label
        label = (
            f"{band_label}\n{start}-{end}"
            if width < 0.8
            else f"{short_label} {start}-{end}"
        )
        ax.text(
            start_x + width / 2,
            span_y + span_height / 2,
            label,
            ha="center",
            va="center",
            fontsize=10.2 if width >= 0.8 else 8.0,
            fontweight="semibold",
            color=_readable_text_color(_color_for(group_id)),
            linespacing=0.86,
        )
        center_index = group_start + (count - 1) / 2
        center_row = 9 - int(center_index // 10)
        ax.text(
            -0.42,
            center_row + 0.5,
            f"{short_label}\n{count}",
            ha="center",
            va="center",
            fontsize=11.5,
            fontweight="bold",
            linespacing=0.86,
            color=_edge_for(group_id),
            bbox={
                "boxstyle": "round,pad=0.16,rounding_size=0.05",
                "fc": TOKENS["panel"],
                "ec": _edge_for(group_id),
                "lw": 1.0,
            },
        )
        group_start += count
    ax.text(
        0,
        span_y - 0.22,
        "Source-order group spans",
        ha="left",
        va="center",
        fontsize=SMALL_LABEL_SIZE,
        color=TOKENS["muted"],
    )

    ax.set_ylim(-1.05, 10)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    counts = Counter(row.group for row in rows)
    legend_handles = [
        patches.Patch(
            facecolor=_color_for(gid),
            edgecolor=_edge_for(gid),
            label=f"{_group_title(rows, gid)} ({counts[gid]})",
        )
        for gid in _group_ids(rows)
    ]
    ax.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.03),
        ncol=2,
        frameon=False,
        fontsize=SMALL_LABEL_SIZE + 0.2,
        handlelength=1.1,
        columnspacing=1.4,
    )
    _add_chart_header(
        fig,
        ax,
        "Library atlas of all 100 implemented skills",
        "Each numbered cell is one registry skill in source order; color, short code, and heavy boundaries identify the taxonomy group without relying on a separate lookup.",
        top=0.87,
    )
    return _save(fig, figures_dir / FIGURE_NAMES[1])


def _write_verb_heatmap(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.colors as mcolors
    import matplotlib.pyplot as plt
    import numpy as np

    verbs = ("read", "reason", "write", "search", "web", "ask", "exec", "delegate")
    groups = _group_ids(rows)
    values = np.zeros((len(groups), len(verbs)), dtype=int)
    group_index = {group: index for index, group in enumerate(groups)}
    verb_index = {verb: index for index, verb in enumerate(verbs)}
    for row in rows:
        for verb in row.verbs:
            if verb in verb_index:
                values[group_index[row.group], verb_index[verb]] += 1

    cmap = mcolors.LinearSegmentedColormap.from_list(
        "cogsecskills_blue",
        [
            COLOR_FAMILIES["neutral"]["xlight"],
            COLOR_FAMILIES["blue"]["light"],
            COLOR_FAMILIES["blue"]["base"],
            COLOR_FAMILIES["blue"]["dark"],
        ],
    )

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["verb_heatmap"])
    image = ax.imshow(values, cmap=cmap, vmin=0, vmax=max(int(values.max()), 1))
    ax.set_aspect("auto")
    verb_totals = values.sum(axis=0)
    ax.set_xticks(
        range(len(verbs)),
        [f"{verb}\n{int(total)} uses" for verb, total in zip(verbs, verb_totals)],
        rotation=0,
        ha="center",
    )
    group_counts = Counter(row.group for row in rows)
    y_labels = [
        f"{textwrap.fill(_group_title(rows, group), width=24)}\n{group_counts[group]} skills"
        for group in groups
    ]
    ax.set_yticks(range(len(groups)), y_labels)
    ax.tick_params(
        axis="both", length=0, colors=TOKENS["muted"], labelsize=TICK_LABEL_SIZE
    )
    for y_pos in range(values.shape[0]):
        for x_pos in range(values.shape[1]):
            value = int(values[y_pos, x_pos])
            ax.text(
                x_pos,
                y_pos,
                str(value),
                ha="center",
                va="center",
                color=TOKENS["ink"]
                if value < max(values.max(), 1) / 2
                else TOKENS["panel"],
                fontsize=CELL_LABEL_SIZE + 0.5,
                fontfamily="monospace",
                fontweight="bold",
            )
    ax.set_xticks(np.arange(-0.5, len(verbs), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(groups), 1), minor=True)
    ax.grid(which="minor", color=TOKENS["panel"], linewidth=1.1)
    ax.tick_params(which="minor", bottom=False, left=False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    colorbar = fig.colorbar(image, ax=ax, fraction=0.035, pad=0.03)
    colorbar.set_label(
        "skills declaring verb", color=TOKENS["muted"], fontsize=SMALL_LABEL_SIZE + 1
    )
    colorbar.ax.tick_params(
        labelsize=SMALL_LABEL_SIZE, colors=TOKENS["muted"], length=0
    )
    _add_chart_header(
        fig,
        ax,
        "Harness-neutral tool verb coverage by group",
        "Direct cell labels show how many skills in each group declare each closed-set verb; column labels add library-wide verb totals.",
    )
    return _save(fig, figures_dir / FIGURE_NAMES[2])


def _write_ageint_network(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.patches as patches
    from matplotlib.path import Path as MplPath
    import matplotlib.pyplot as plt

    edge_counts = Counter((row.group, row.ageint_topic) for row in rows)
    groups = _group_ids(rows)
    topics: list[str] = []
    for row in rows:
        if row.ageint_topic not in topics:
            topics.append(row.ageint_topic)

    group_y = _vertical_positions(groups, top=0.78, bottom=0.14)
    topic_y = _vertical_positions(topics, top=0.78, bottom=0.14)
    topic_counts = Counter(row.ageint_topic for row in rows)
    group_counts = Counter(row.group for row in rows)
    max_edge = max(edge_counts.values()) if edge_counts else 1

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["ageint_network"])
    ax.add_patch(
        patches.Rectangle(
            (0.02, 0.08),
            0.34,
            0.78,
            facecolor=COLOR_FAMILIES["neutral"]["xlight"],
            edgecolor="none",
            zorder=0,
        )
    )
    ax.add_patch(
        patches.Rectangle(
            (0.64, 0.08),
            0.34,
            0.78,
            facecolor=COLOR_FAMILIES["neutral"]["xlight"],
            edgecolor="none",
            zorder=0,
        )
    )
    for (group_id, topic), count in edge_counts.items():
        start_y = group_y[group_id]
        end_y = topic_y[topic]
        path = MplPath(
            [
                (0.355, start_y),
                (0.46, start_y),
                (0.54, end_y),
                (0.645, end_y),
            ],
            [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4],
        )
        patch = patches.PathPatch(
            path,
            facecolor="none",
            edgecolor=_color_for(group_id),
            linewidth=2.0 + 7.2 * count / max_edge,
            alpha=0.50,
            capstyle="round",
            zorder=1,
        )
        ax.add_patch(patch)
        ax.text(
            0.5,
            (start_y + end_y) / 2,
            str(count),
            ha="center",
            va="center",
            fontsize=ANNOTATION_SIZE + 0.4,
            fontweight="bold",
            color=TOKENS["ink"],
            bbox={
                "boxstyle": "round,pad=0.22,rounding_size=0.06",
                "fc": TOKENS["panel"],
                "ec": TOKENS["grid"],
                "lw": 0.5,
            },
            zorder=3,
        )

    for group_id in groups:
        y_pos = group_y[group_id]
        box = patches.FancyBboxPatch(
            (0.045, y_pos - 0.052),
            0.29,
            0.104,
            boxstyle="round,pad=0.012,rounding_size=0.018",
            facecolor=_light_for(group_id),
            edgecolor=_edge_for(group_id),
            linewidth=1.2,
            zorder=2,
        )
        ax.add_patch(box)
        ax.text(
            0.190,
            y_pos,
            (
                f"{textwrap.fill(_group_title(rows, group_id), width=23)}\n"
                f"{group_counts[group_id]} skills"
            ),
            ha="center",
            va="center",
            fontsize=12.0,
            color=TOKENS["ink"],
            linespacing=1.08,
            zorder=3,
        )

    for topic in topics:
        y_pos = topic_y[topic]
        box = patches.FancyBboxPatch(
            (0.665, y_pos - 0.052),
            0.30,
            0.104,
            boxstyle="round,pad=0.012,rounding_size=0.018",
            facecolor=COLOR_FAMILIES["neutral"]["xlight"],
            edgecolor=COLOR_FAMILIES["neutral"]["mid"],
            linewidth=1.2,
            zorder=2,
        )
        ax.add_patch(box)
        ax.text(
            0.815,
            y_pos,
            f"{textwrap.fill(topic, width=25)}\n{topic_counts[topic]} skills",
            ha="center",
            va="center",
            fontsize=12.0,
            color=TOKENS["ink"],
            linespacing=1.08,
            zorder=3,
        )

    ax.text(
        0.185,
        0.91,
        "Skill groups",
        ha="center",
        va="center",
        fontsize=CAPTION_LABEL_SIZE + 1,
        fontweight="semibold",
        color=TOKENS["muted"],
    )
    ax.text(
        0.815,
        0.91,
        "AGEINT topics",
        ha="center",
        va="center",
        fontsize=CAPTION_LABEL_SIZE + 1,
        fontweight="semibold",
        color=TOKENS["muted"],
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0.04, 0.98)
    ax.axis("off")
    _add_chart_header(
        fig,
        ax,
        "AGEINT teaching crosswalk from groups to topics",
        "Lane boxes show library groups and AGEINT topics; link widths and badges both report the number of implemented skills in each declared pairing.",
        top=0.84,
    )
    return _save(fig, figures_dir / FIGURE_NAMES[3])


def _write_plan_build_teach_flow(figures_dir: Path) -> Path:
    import matplotlib.patches as patches
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["plan_build_teach_flow"])
    columns = [
        (
            "SOURCE FILES",
            [
                "registry/skills.yaml",
                "definitions/**/*.yaml",
                "docs/ageint/",
                "scenarios/*.yaml",
            ],
            COLOR_FAMILIES["blue"],
        ),
        (
            "GENERATORS",
            [
                "definitions --write",
                "manuscript-assets --write",
                "dashboard --write",
            ],
            COLOR_FAMILIES["orange"],
        ),
        (
            "LOCAL GATES",
            [
                "validate + doctor",
                "definitions --check",
                "scenarios --check",
                "pytest + render",
            ],
            COLOR_FAMILIES["olive"],
        ),
        (
            "READER OUTPUTS",
            [
                "skills/** adapters",
                "quality dashboard",
                "supplements + figures",
                "PDF manuscript",
            ],
            COLOR_FAMILIES["pink"],
        ),
    ]
    x_positions = [0.035, 0.285, 0.535, 0.785]
    widths = [0.180, 0.180, 0.180, 0.165]
    y_base = 0.18
    height = 0.60
    for index, (title, items, family) in enumerate(columns):
        x_pos = x_positions[index]
        width = widths[index]
        ax.add_patch(
            patches.FancyBboxPatch(
                (x_pos, y_base),
                width,
                height,
                boxstyle="round,pad=0.018,rounding_size=0.028",
                facecolor=family["xlight"],
                edgecolor=family["dark"],
                linewidth=1.35,
            )
        )
        ax.text(
            x_pos + width / 2,
            y_base + height - 0.075,
            title,
            ha="center",
            va="center",
            fontsize=CAPTION_LABEL_SIZE + 1,
            fontweight="bold",
            color=family["dark"],
        )
        for item_index, item in enumerate(items):
            y_pos = y_base + height - 0.165 - item_index * 0.105
            ax.add_patch(
                patches.FancyBboxPatch(
                    (x_pos + 0.022, y_pos - 0.033),
                    width - 0.044,
                    0.066,
                    boxstyle="round,pad=0.006,rounding_size=0.014",
                    facecolor=TOKENS["panel"],
                    edgecolor=family["light"],
                    linewidth=0.9,
                )
            )
            ax.text(
                x_pos + width / 2,
                y_pos,
                item,
                ha="center",
                va="center",
                fontsize=12.4,
                color=TOKENS["ink"],
                fontfamily="monospace" if "/" in item or "*" in item else "sans-serif",
            )
        if index < len(columns) - 1:
            ax.annotate(
                "",
                xy=(x_positions[index + 1] - 0.030, y_base + height / 2),
                xytext=(x_pos + width + 0.024, y_base + height / 2),
                arrowprops=dict(
                    arrowstyle="-|>",
                    color=family["dark"],
                    lw=2.2,
                    shrinkA=0,
                    shrinkB=0,
                    mutation_scale=21,
                ),
            )

    lane_labels = [
        ("PLAN", 0.035, COLOR_FAMILIES["blue"]),
        ("BUILD", 0.282, COLOR_FAMILIES["orange"]),
        ("TEACH", 0.530, COLOR_FAMILIES["olive"]),
        ("RUN", 0.777, COLOR_FAMILIES["pink"]),
    ]
    for label, x_pos, family in lane_labels:
        ax.text(
            x_pos,
            0.105,
            label,
            ha="left",
            va="center",
            fontsize=17,
            fontweight="bold",
            color=family["dark"],
        )
    ax.text(
        0.50,
        0.055,
        "Claim discipline: every reader-facing figure, supplement, dashboard row, and adapter claim is generated from source-owned files and checked before rendering.",
        ha="center",
        va="center",
        fontsize=CAPTION_LABEL_SIZE,
        color=TOKENS["muted"],
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.94)
    ax.axis("off")
    _add_chart_header(
        fig,
        ax,
        "Plan, Build, Teach flow into checked manuscript assets",
        "The pipeline moves left to right from source files through deterministic generators and local gates into skills, dashboards, figures, and the rendered manuscript.",
        top=0.83,
    )
    return _save(fig, figures_dir / FIGURE_NAMES[4])


def _write_reference_density(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.pyplot as plt

    summaries = sorted(
        _group_summaries(rows),
        key=lambda item: (
            item["references_per_skill"],
            item["references"],
            item["title"],
        ),
    )
    labels = [textwrap.fill(str(item["title"]), width=24) for item in summaries]
    densities = [float(item["references_per_skill"]) for item in summaries]
    max_density = max(densities) if densities else 1.0

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["reference_density"])
    y_positions = list(range(len(summaries)))
    for y_pos, item, density in zip(y_positions, summaries, densities):
        group_id = str(item["id"])
        ax.barh(
            y_pos,
            density,
            facecolor=_color_for(group_id),
            edgecolor=_edge_for(group_id),
            linewidth=1.2,
            alpha=0.78,
            height=0.62,
        )
        ax.text(
            density + 0.08,
            y_pos,
            f"{density:.1f} refs/skill  {int(item['references'])} total",
            ha="left",
            va="center",
            fontsize=ANNOTATION_SIZE,
            color=TOKENS["ink"],
        )
        ax.text(
            max(0.08, min(density * 0.45, max_density - 0.10)),
            y_pos,
            _group_short(group_id),
            ha="center",
            va="center",
            fontsize=SMALL_LABEL_SIZE,
            fontweight="bold",
            color=_readable_text_color(_color_for(group_id)),
        )

    ax.set_yticks(y_positions, labels)
    ax.set_xlabel("Declared references per implemented skill")
    ax.set_xlim(0, max_density + 1.9)
    _style_axes(ax, grid_axis="x")
    _add_chart_header(
        fig,
        ax,
        "Reference density by taxonomy group",
        "Bars show declared references per implemented skill and labels add total references; this is metadata density, not evidence quality or field validity.",
    )
    return _save(fig, figures_dir / FIGURE_NAMES[5])


def _write_harness_contract(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.patches as patches
    import matplotlib.pyplot as plt

    groups = _group_ids(rows)
    harnesses = tuple(
        sorted({harness for row in rows for harness in row.harnesses})
    ) or (
        "claude",
        "codex",
        "hermes",
    )
    group_rows = {
        group: [row for row in rows if row.group == group] for group in groups
    }
    total_skills = len(rows)

    fig, ax = plt.subplots(figsize=FIGURE_SIZES["harness_contract"])
    for y_index, harness in enumerate(reversed(harnesses)):
        row_covered = sum(1 for row in rows if harness in row.harnesses)
        row_full = row_covered == total_skills and total_skills > 0
        for x_index, group_id in enumerate(groups):
            covered = sum(1 for row in group_rows[group_id] if harness in row.harnesses)
            total = len(group_rows[group_id])
            full = covered == total and total > 0
            rect = patches.FancyBboxPatch(
                (x_index, y_index),
                0.92,
                0.80,
                boxstyle="round,pad=0.012,rounding_size=0.035",
                facecolor=_light_for(group_id)
                if full
                else COLOR_FAMILIES["orange"]["xlight"],
                edgecolor=_edge_for(group_id)
                if full
                else COLOR_FAMILIES["orange"]["dark"],
                linewidth=1.2,
            )
            ax.add_patch(rect)
            ax.text(
                x_index + 0.46,
                y_index + 0.48,
                "OK" if full else "GAP",
                ha="center",
                va="center",
                fontsize=CELL_LABEL_SIZE + 1,
                fontweight="bold",
                color=TOKENS["ink"],
            )
            ax.text(
                x_index + 0.46,
                y_index + 0.24,
                f"{covered}/{total}",
                ha="center",
                va="center",
                fontsize=SMALL_LABEL_SIZE,
                fontfamily="monospace",
                color=TOKENS["muted"],
            )
        badge = patches.FancyBboxPatch(
            (len(groups) + 0.15, y_index),
            0.98,
            0.80,
            boxstyle="round,pad=0.012,rounding_size=0.035",
            facecolor=COLOR_FAMILIES["olive"]["xlight"]
            if row_full
            else COLOR_FAMILIES["orange"]["xlight"],
            edgecolor=COLOR_FAMILIES["olive"]["dark"]
            if row_full
            else COLOR_FAMILIES["orange"]["dark"],
            linewidth=1.2,
        )
        ax.add_patch(badge)
        ax.text(
            len(groups) + 0.64,
            y_index + 0.48,
            "ALL" if row_full else "GAP",
            ha="center",
            va="center",
            fontsize=CELL_LABEL_SIZE + 1,
            fontweight="bold",
            color=TOKENS["ink"],
        )
        ax.text(
            len(groups) + 0.64,
            y_index + 0.24,
            f"{row_covered}/{total_skills}",
            ha="center",
            va="center",
            fontsize=SMALL_LABEL_SIZE,
            fontfamily="monospace",
            color=TOKENS["muted"],
        )

    ax.set_xlim(-0.05, len(groups) + 1.25)
    ax.set_ylim(-0.05, len(harnesses) + 0.05)
    ax.set_xticks(
        [index + 0.46 for index in range(len(groups))] + [len(groups) + 0.64],
        [
            textwrap.fill(
                _group_title(rows, group),
                width=18,
                break_long_words=False,
            )
            for group in groups
        ]
        + ["All\nskills"],
    )
    ax.set_yticks(
        [index + 0.38 for index in range(len(harnesses))],
        [harness for harness in reversed(harnesses)],
    )
    ax.xaxis.tick_top()
    ax.tick_params(axis="both", length=0, labelsize=12.0, colors=TOKENS["muted"])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    default_harnesses = ("claude", "codex", "hermes")
    if harnesses == default_harnesses:
        title = "Harness Contract: default Claude, Codex, and Hermes coverage"
    else:
        title = "Harness Contract: configured adapter coverage"
    subtitle = (
        f"Configured harness set: {', '.join(harnesses)}. "
        "Each cell reports skills declaring that harness adapter over skills in the group; "
        "the right column checks whole-library structural coverage."
    )
    _add_chart_header(
        fig,
        ax,
        title,
        subtitle,
        top=0.78,
    )
    return _save(fig, figures_dir / FIGURE_NAMES[6])


def _write_cover_installation(rows: list[SkillRow], figures_dir: Path) -> Path:
    import textwrap

    import matplotlib.patches as patches
    import matplotlib.pyplot as plt

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
