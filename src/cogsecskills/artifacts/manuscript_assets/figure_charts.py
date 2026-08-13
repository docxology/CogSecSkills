"""Quantitative chart panels: bars and a verb heatmap.

Each reads the collected skill rows and reports a distribution — counts by
group, verb usage by group, declared reference density. Metadata density, not
effectiveness; the manuscript captions say so explicitly.
"""

from __future__ import annotations

import textwrap
from collections import Counter
from pathlib import Path

from .figure_helpers import (
    _add_chart_header,
    _color_for,
    _edge_for,
    _group_short,
    _group_summaries,
    _readable_text_color,
    _save,
    _style_axes,
)
from .figure_specs import FIGURE_NAMES
from .figure_theme import (
    ANNOTATION_SIZE,
    CAPTION_LABEL_SIZE,
    CELL_LABEL_SIZE,
    COLOR_FAMILIES,
    FIGURE_SIZES,
    SMALL_LABEL_SIZE,
    TICK_LABEL_SIZE,
    TOKENS,
)
from .rows import SkillRow, _group_ids, _group_title


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
