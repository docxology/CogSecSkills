"""Design tokens for the generated manuscript figures.

Sizes, DPI, palettes, and the per-group color families shared by every figure
generator. Pure data with no imports, so both the helpers and the panels can
depend on it without creating a cycle.
"""

from __future__ import annotations

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
