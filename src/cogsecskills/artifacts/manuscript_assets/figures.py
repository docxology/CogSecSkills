"""Figure generation entry point.

The figure code is split by concern — :mod:`figure_specs` (the registry),
:mod:`figure_theme` (design tokens), :mod:`figure_helpers` (shared drawing), and
:mod:`figure_charts`, :mod:`figure_diagrams`, and :mod:`figure_cover`
(one function per figure). This module keeps the
``write_figures`` orchestrator and re-exports the names those modules previously
exposed from here, so importers and tests are unaffected by the split.
"""

from __future__ import annotations

from pathlib import Path

from .figure_helpers import (
    _add_chart_header,
    _color_for,
    _edge_for,
    _group_short,
    _group_summaries,
    _light_for,
    _publication_doi,
    _readable_text_color,
    _save,
    _style_axes,
    _use_chart_theme,
    _vertical_positions,
)
from .figure_charts import (
    _write_reference_density,
    _write_taxonomy_counts,
    _write_verb_heatmap,
)
from .figure_cover import _write_cover_installation
from .figure_diagrams import (
    _write_ageint_network,
    _write_harness_contract,
    _write_plan_build_teach_flow,
    _write_skill_grid,
)
from .figure_specs import FIGURES, FIGURE_NAMES, FigureMetadata
from .figure_theme import (
    ANNOTATION_SIZE,
    AXIS_LABEL_SIZE,
    CAPTION_LABEL_SIZE,
    CELL_LABEL_SIZE,
    COLOR_FAMILIES,
    COVER_COMMAND_SIZE,
    COVER_FLOW_TITLE_SIZE,
    COVER_LABEL_SIZE,
    COVER_PANEL_TITLE_SIZE,
    COVER_STAT_LABEL_SIZE,
    COVER_STAT_VALUE_SIZE,
    FIGURE_DPI,
    FIGURE_SIZES,
    GROUP_COLORS,
    GROUP_EDGE_COLORS,
    GROUP_LIGHT_COLORS,
    SMALL_LABEL_SIZE,
    SUBTITLE_SIZE,
    TICK_LABEL_SIZE,
    TITLE_SIZE,
    TOKENS,
    _PNG_SIGNATURE,
)
from .paths import COVER_IMAGE_MIRROR_PATH, COVER_IMAGE_NAME, _project_root
from .rows import SkillRow


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


__all__ = [
    "ANNOTATION_SIZE",
    "AXIS_LABEL_SIZE",
    "CAPTION_LABEL_SIZE",
    "CELL_LABEL_SIZE",
    "COLOR_FAMILIES",
    "COVER_COMMAND_SIZE",
    "COVER_FLOW_TITLE_SIZE",
    "COVER_LABEL_SIZE",
    "COVER_PANEL_TITLE_SIZE",
    "COVER_STAT_LABEL_SIZE",
    "COVER_STAT_VALUE_SIZE",
    "FIGURES",
    "FIGURE_DPI",
    "FIGURE_NAMES",
    "FIGURE_SIZES",
    "FigureMetadata",
    "GROUP_COLORS",
    "GROUP_EDGE_COLORS",
    "GROUP_LIGHT_COLORS",
    "SMALL_LABEL_SIZE",
    "SUBTITLE_SIZE",
    "TICK_LABEL_SIZE",
    "TITLE_SIZE",
    "TOKENS",
    "_PNG_SIGNATURE",
    "_add_chart_header",
    "_color_for",
    "_edge_for",
    "_group_short",
    "_group_summaries",
    "_light_for",
    "_publication_doi",
    "_readable_text_color",
    "_save",
    "_style_axes",
    "_use_chart_theme",
    "_vertical_positions",
    "_write_ageint_network",
    "_write_cover_installation",
    "_write_harness_contract",
    "_write_plan_build_teach_flow",
    "_write_reference_density",
    "_write_skill_grid",
    "_write_taxonomy_counts",
    "_write_verb_heatmap",
    "write_figures",
]
