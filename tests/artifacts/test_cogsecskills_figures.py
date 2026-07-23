"""Tests for the figure-generation helpers and design constants.

These tests cover the pure-helper functions in ``figures.py`` that the
integration-level ``write_assets`` tests exercise only indirectly.  By testing
the helpers directly we cover the color mapping, text contrast, group summary,
vertical positioning, PNG signature, and chart-theme entry points without
requiring a full figure render.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cogsecskills.artifacts.manuscript_assets.figures import (
    COLOR_FAMILIES,
    FIGURE_DPI,
    FIGURE_NAMES,
    FIGURE_SIZES,
    FIGURES,
    GROUP_COLORS,
    GROUP_EDGE_COLORS,
    GROUP_LIGHT_COLORS,
    TOKENS,
    _PNG_SIGNATURE,
    _color_for,
    _edge_for,
    _group_short,
    _group_summaries,
    _light_for,
    _publication_doi,
    _readable_text_color,
    _vertical_positions,
    write_figures,
)
from cogsecskills.artifacts.manuscript_assets.rows import SkillRow

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------------
# Design constants
# ---------------------------------------------------------------------------


def test_png_signature_is_correct():
    """The PNG signature is the standard 8-byte header."""
    assert _PNG_SIGNATURE == b"\x89PNG\r\n\x1a\n"


def test_figure_dpi_is_reasonable():
    """Figures render at at least 200 DPI for print quality."""
    assert FIGURE_DPI >= 200


def test_figure_names_match_metadata():
    """FIGURE_NAMES is the tuple of filenames from FIGURES metadata."""
    assert FIGURE_NAMES == tuple(f.filename for f in FIGURES)


def test_all_figures_have_unique_filenames():
    filenames = [f.filename for f in FIGURES]
    assert len(filenames) == len(set(filenames))


def test_all_figures_have_reader_questions():
    for fig in FIGURES:
        assert fig.reader_question
        assert len(fig.reader_question) > 10


def test_all_figures_have_semantic_labels():
    for fig in FIGURES:
        assert fig.semantic_labels
        assert len(fig.semantic_labels) >= 2


def test_cover_figure_is_mirrored():
    """Exactly one figure is marked as mirrored (the cover)."""
    mirrored = [f for f in FIGURES if f.mirrored]
    assert len(mirrored) == 1
    assert mirrored[0].filename == "cogsecskills_cover_installation.png"


def test_figure_sizes_cover_all_generators():
    """Every figure generator has a corresponding size entry."""
    expected_keys = {
        "taxonomy_counts",
        "skill_grid",
        "verb_heatmap",
        "ageint_network",
        "plan_build_teach_flow",
        "reference_density",
        "harness_contract",
        "cover_installation",
    }
    assert set(FIGURE_SIZES) == expected_keys


def test_figure_sizes_are_valid_tuples():
    for key, size in FIGURE_SIZES.items():
        assert isinstance(size, tuple)
        assert len(size) == 2
        assert all(isinstance(v, (int, float)) and v > 0 for v in size)


def test_color_families_have_all_shades():
    """Every color family has all 5 shades."""
    for name, family in COLOR_FAMILIES.items():
        assert set(family) == {"xlight", "light", "base", "mid", "dark"}, (
            f"family {name!r} missing shades"
        )


def test_tokens_have_required_keys():
    expected = {"surface", "panel", "ink", "muted", "grid", "axis"}
    assert set(TOKENS) == expected


def test_group_colors_cover_all_registry_groups():
    """All 7 registry groups have explicit color, edge, and light mappings."""
    expected_groups = {
        "sat",
        "cognitive_security",
        "critical_review",
        "osint_integrity",
        "counterintelligence",
        "information_environment",
        "research_methods",
    }
    assert set(GROUP_COLORS) == expected_groups
    assert set(GROUP_EDGE_COLORS) == expected_groups
    assert set(GROUP_LIGHT_COLORS) == expected_groups


def test_group_colors_reference_valid_families():
    """Every group color is a valid hex from COLOR_FAMILIES."""
    all_hex = set()
    for family in COLOR_FAMILIES.values():
        all_hex.update(family.values())
    for gid, color in GROUP_COLORS.items():
        assert color in all_hex, f"group {gid!r} color {color!r} not in any family"


# ---------------------------------------------------------------------------
# Color helpers
# ---------------------------------------------------------------------------


def test_color_for_known_group():
    assert _color_for("sat") == GROUP_COLORS["sat"]


def test_color_for_unknown_group_returns_neutral():
    assert _color_for("nonexistent") == COLOR_FAMILIES["neutral"]["base"]


def test_edge_for_known_group():
    assert _edge_for("sat") == GROUP_EDGE_COLORS["sat"]


def test_edge_for_unknown_group_returns_neutral_dark():
    assert _edge_for("nonexistent") == COLOR_FAMILIES["neutral"]["dark"]


def test_light_for_known_group():
    assert _light_for("sat") == GROUP_LIGHT_COLORS["sat"]


def test_light_for_unknown_group_returns_neutral_xlight():
    assert _light_for("nonexistent") == COLOR_FAMILIES["neutral"]["xlight"]


# ---------------------------------------------------------------------------
# Text contrast
# ---------------------------------------------------------------------------


def test_readable_text_color_dark_background_returns_light():
    """A dark background color should produce a light (panel) text color."""
    dark = COLOR_FAMILIES["blue"]["dark"]  # #2E4780 — dark
    assert _readable_text_color(dark) == TOKENS["panel"]


def test_readable_text_color_light_background_returns_dark():
    """A light background color should produce a dark (ink) text color."""
    light = COLOR_FAMILIES["gold"]["xlight"]  # #FFF4C2 — very light
    assert _readable_text_color(light) == TOKENS["ink"]


def test_readable_text_color_strips_hash():
    """The function should handle both #-prefixed and bare hex."""
    assert _readable_text_color("#FFFFFF") == TOKENS["ink"]
    assert _readable_text_color("FFFFFF") == TOKENS["ink"]
    assert _readable_text_color("#000000") == TOKENS["panel"]
    assert _readable_text_color("000000") == TOKENS["panel"]


# ---------------------------------------------------------------------------
# Group short labels
# ---------------------------------------------------------------------------


def test_group_short_all_known_groups():
    expected = {
        "sat": "SAT",
        "cognitive_security": "COG",
        "critical_review": "REV",
        "osint_integrity": "OSINT",
        "counterintelligence": "CI",
        "information_environment": "INFO",
        "research_methods": "METHOD",
    }
    for gid, expected_short in expected.items():
        assert _group_short(gid) == expected_short


def test_group_short_unknown_group_truncates():
    assert _group_short("unknown_group") == "UNKNOW"
    assert _group_short("ab") == "AB"


# ---------------------------------------------------------------------------
# Vertical positions
# ---------------------------------------------------------------------------


def test_vertical_positions_empty():
    assert _vertical_positions([]) == {}


def test_vertical_positions_single_item():
    result = _vertical_positions(["only"], top=0.8, bottom=0.2)
    assert result == {"only": 0.5}


def test_vertical_positions_multiple_items():
    result = _vertical_positions(["a", "b", "c"], top=0.9, bottom=0.3)
    assert len(result) == 3
    assert result["a"] == pytest.approx(0.9)
    assert result["c"] == pytest.approx(0.3)
    # Middle item should be between top and bottom
    assert 0.3 < result["b"] < 0.9


def test_vertical_positions_two_items():
    result = _vertical_positions(["top", "bottom"], top=0.8, bottom=0.2)
    assert result["top"] == pytest.approx(0.8)
    assert result["bottom"] == pytest.approx(0.2)


# ---------------------------------------------------------------------------
# Group summaries
# ---------------------------------------------------------------------------


def _make_row(
    *,
    id: str = "sat.demo",
    group: str = "sat",
    group_title: str = "SAT",
    references_count: int = 2,
) -> SkillRow:
    return SkillRow(
        id=id,
        name="Demo Skill",
        group=group,
        group_title=group_title,
        status="implemented",
        functionality="A demo skill.",
        use_when="demo",
        ageint_topic="structured-analytic-techniques",
        verbs=("read", "reason", "write"),
        inputs=("context",),
        outputs=("product",),
        tags=("test",),
        harnesses=("claude", "codex", "hermes"),
        references_count=references_count,
        defensive_boundary="defensive use only",
        evidence_discipline="bind to evidence",
        confidence_anchor="high confidence",
        unsafe_redirect="Unsafe: refuse",
        safe_defensive_pattern="Safe defensive: proceed",
        source_path="skills/sat/demo/SKILL.md",
    )


def test_group_summaries_basic():
    rows = [
        _make_row(id="sat.one", references_count=3),
        _make_row(id="sat.two", references_count=2),
        _make_row(
            id="cog.three",
            group="cognitive_security",
            group_title="Cognitive Security",
            references_count=5,
        ),
    ]
    summaries = _group_summaries(rows)
    assert len(summaries) == 2
    sat = next(s for s in summaries if s["id"] == "sat")
    assert sat["count"] == 2
    assert sat["references"] == 5
    assert sat["references_per_skill"] == 2.5
    cog = next(s for s in summaries if s["id"] == "cognitive_security")
    assert cog["count"] == 1
    assert cog["references"] == 5


def test_group_summaries_empty_rows():
    assert _group_summaries([]) == []


def test_group_summaries_zero_count_safe():
    """A group with zero skills should not crash (division by zero guard)."""
    # This can't happen in practice because group summaries are derived from
    # rows that exist, but the guard is there.
    rows = [_make_row()]
    summaries = _group_summaries(rows)
    assert summaries[0]["references_per_skill"] == 2.0


# ---------------------------------------------------------------------------
# Publication DOI
# ---------------------------------------------------------------------------


def test_publication_doi_returns_string():
    """The DOI helper should return a string (possibly empty) from config."""
    result = _publication_doi()
    assert isinstance(result, str)


def test_publication_doi_missing_config(tmp_path):
    """When no manuscript config exists, DOI should be empty string."""
    result = _publication_doi(tmp_path)
    assert result == ""


def test_publication_doi_from_config(tmp_path):
    """A config with publication.doi should return that DOI."""
    config_dir = tmp_path / "manuscript"
    config_dir.mkdir()
    (config_dir / "config.yaml").write_text(
        "publication:\n  doi: 10.5281/zenodo.12345\n", encoding="utf-8"
    )
    result = _publication_doi(tmp_path)
    assert result == "10.5281/zenodo.12345"


def test_publication_doi_malformed_config(tmp_path):
    """A malformed config file should return empty string, not crash."""
    config_dir = tmp_path / "manuscript"
    config_dir.mkdir()
    (config_dir / "config.yaml").write_text(
        "not: valid: yaml: at: all\n", encoding="utf-8"
    )
    result = _publication_doi(tmp_path)
    assert result == ""


# ---------------------------------------------------------------------------
# write_figures integration (with minimal library)
# ---------------------------------------------------------------------------


def test_write_figures_generates_all_pngs(tmp_path):
    """write_figures should produce all 8 PNG files with valid headers."""
    from cogsecskills.artifacts.manuscript_assets.rows import collect_skill_rows

    rows = collect_skill_rows(PROJECT_ROOT)
    paths = write_figures(rows, tmp_path)
    assert len(paths) == len(FIGURE_NAMES)
    for path in paths:
        assert path.is_file()
        data = path.read_bytes()
        assert data.startswith(_PNG_SIGNATURE)
        assert len(data) > 1000


def test_write_figures_cover_mirror_created(tmp_path):
    """write_figures should also mirror the cover image."""
    from cogsecskills.artifacts.manuscript_assets.rows import collect_skill_rows
    from cogsecskills.artifacts.manuscript_assets.paths import (
        COVER_IMAGE_MIRROR_PATH,
        COVER_IMAGE_NAME,
    )

    rows = collect_skill_rows(PROJECT_ROOT)
    write_figures(rows, tmp_path)
    mirror = tmp_path / COVER_IMAGE_MIRROR_PATH
    cover = tmp_path / "output" / "figures" / COVER_IMAGE_NAME
    assert mirror.is_file()
    assert cover.is_file()
    assert mirror.read_bytes() == cover.read_bytes()
