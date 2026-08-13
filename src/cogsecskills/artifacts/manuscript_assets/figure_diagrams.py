"""Diagram panels: hand-laid figures rather than plotted series.

The library atlas, the AGEINT topic network, the plan/build/teach flow, and the
harness-contract matrix. These position artists on an axes directly, so they
share the theme tokens but little plotting machinery.
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
    _light_for,
    _readable_text_color,
    _save,
    _vertical_positions,
)
from .figure_specs import FIGURE_NAMES
from .figure_theme import (
    ANNOTATION_SIZE,
    CAPTION_LABEL_SIZE,
    CELL_LABEL_SIZE,
    COLOR_FAMILIES,
    FIGURE_SIZES,
    SMALL_LABEL_SIZE,
    TOKENS,
)
from .rows import SkillRow, _group_ids, _group_title


def _write_skill_grid(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.pyplot as plt
    from matplotlib import patches

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


def _write_ageint_network(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.pyplot as plt
    from matplotlib import patches
    from matplotlib.path import Path as MplPath

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
    import matplotlib.pyplot as plt
    from matplotlib import patches

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


def _write_harness_contract(rows: list[SkillRow], figures_dir: Path) -> Path:
    import matplotlib.pyplot as plt
    from matplotlib import patches

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
