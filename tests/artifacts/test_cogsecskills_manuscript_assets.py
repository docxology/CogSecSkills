"""Tests for generated manuscript supplements and figures."""

from __future__ import annotations

import struct
from pathlib import Path

from cogsecskills.authoring.author import render_definition
from cogsecskills.artifacts.manuscript_assets import (
    CATALOGUE_PATH,
    COVER_COMMAND_SIZE,
    COVER_LABEL_SIZE,
    COVER_PANEL_TITLE_SIZE,
    DATA_CSV_PATH,
    DATA_JSON_PATH,
    FIGURE_NAMES,
    FIGURES,
    GROUP_COLORS,
    MATRIX_PATH,
    check_assets,
    collect_skill_rows,
    render_metadata_matrix,
    render_skill_catalogue,
    write_assets,
)


EXPECTED_FIGURES = (
    "cogsecskills_taxonomy_counts.png",
    "cogsecskills_skill_grid.png",
    "cogsecskills_verb_heatmap.png",
    "cogsecskills_ageint_network.png",
    "cogsecskills_plan_build_teach_flow.png",
    "cogsecskills_reference_density.png",
    "cogsecskills_harness_contract.png",
    "cogsecskills_cover_installation.png",
)

MIN_FIGURE_PIXELS = {
    "cogsecskills_taxonomy_counts.png": (3200, 1800),
    "cogsecskills_skill_grid.png": (3200, 3500),
    "cogsecskills_verb_heatmap.png": (3300, 1800),
    "cogsecskills_ageint_network.png": (3500, 1900),
    "cogsecskills_plan_build_teach_flow.png": (3400, 1600),
    "cogsecskills_reference_density.png": (3200, 1800),
    "cogsecskills_harness_contract.png": (3400, 1400),
    "cogsecskills_cover_installation.png": (3300, 1700),
}


def _seed_registry(root: Path) -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        "  - {id: sat.ach, name: Analysis of Competing Hypotheses, group: sat, "
        "status: implemented, ageint_topic: structured-analytic-techniques, "
        "summary: Score evidence across competing hypotheses.}\n"
        "  - {id: osint_integrity.claim, name: Claim Provenance Verification, "
        "group: osint_integrity, status: implemented, ageint_topic: osint-integrity, "
        "summary: Trace a claim back to a primary source.}\n",
        encoding="utf-8",
    )
    (root / "registry" / "groups.yaml").write_text(
        "groups:\n"
        "  - {id: sat, title: Structured Analytic Techniques}\n"
        "  - {id: osint_integrity, title: OSINT Integrity}\n",
        encoding="utf-8",
    )


def _definition(skill_id: str, *, triggers: list[str], tools: list[dict]) -> dict:
    return {
        "id": skill_id,
        "description": "A concrete defensive analytic routine for the test library.",
        "tags": ["evidence", "defensive"],
        "triggers": triggers,
        "tools": tools,
        "inputs": [
            {
                "name": "case_material",
                "type": "markdown",
                "required": True,
                "description": "materials to inspect",
            }
        ],
        "outputs": [
            {
                "name": "audit_note",
                "type": "markdown",
                "description": "the defensible analytic product",
            }
        ],
        "references": ["docs/ageint/source-a.md", "docs/ageint/source-b.md"],
        "workflow_steps": [
            {"verbs": ["read"], "title": "Gather", "text": "Read the materials."},
            {"verbs": ["reason"], "title": "Assess", "text": "Apply the method."},
            {"verbs": ["write"], "title": "Report", "text": "Write the result."},
        ],
        "anti_criteria": ["Do not invent sources."],
    }


def _library(root: Path, *, harnesses: tuple[str, ...] | None = None) -> None:
    _seed_registry(root)
    render_definition(
        _definition(
            "sat.ach",
            triggers=["compare hypotheses", "diagnose evidence"],
            tools=[
                {"verb": "read", "purpose": "ingest evidence"},
                {"verb": "reason", "purpose": "score hypotheses"},
                {"verb": "write", "purpose": "emit findings"},
            ],
        ),
        root=root,
        harnesses=harnesses,
    )
    render_definition(
        _definition(
            "osint_integrity.claim",
            triggers=["verify claim", "trace provenance"],
            tools=[
                {"verb": "read", "purpose": "inspect supplied material"},
                {"verb": "web", "purpose": "fetch source pages"},
                {"verb": "write", "purpose": "emit provenance note"},
            ],
        ),
        root=root,
        harnesses=harnesses,
    )


def _png_dimensions(data: bytes) -> tuple[int, int]:
    assert data.startswith(b"\x89PNG\r\n\x1a\n")
    return struct.unpack(">II", data[16:24])


def test_collect_skill_rows_derives_metadata(tmp_path):
    _library(tmp_path)
    rows = collect_skill_rows(tmp_path)
    assert [row.id for row in rows] == ["sat.ach", "osint_integrity.claim"]
    assert rows[0].use_when == "compare hypotheses; diagnose evidence"
    assert rows[0].verbs == ("read", "reason", "write")
    assert rows[0].inputs == ("case_material",)
    assert rows[0].outputs == ("audit_note",)
    assert rows[0].references_count == 2
    assert "Analysis of Competing Hypotheses" in rows[0].defensive_boundary
    assert "Analysis of Competing Hypotheses" in rows[0].evidence_discipline
    assert rows[0].confidence_anchor.startswith(
        "High confidence for Analysis of Competing Hypotheses"
    )
    assert "Unsafe:" in rows[0].unsafe_redirect
    assert "Safe defensive:" in rows[0].safe_defensive_pattern
    assert rows[0].source_path == "skills/sat/ach/SKILL.md"


def test_render_supplements_include_skill_metadata(tmp_path):
    _library(tmp_path)
    rows = collect_skill_rows(tmp_path)
    catalogue = render_skill_catalogue(rows)
    matrix = render_metadata_matrix(rows)
    assert "Supplemental 100-Skill Catalogue" in catalogue
    assert "Use when" in catalogue
    assert "Quality capsule" in catalogue
    assert "Unsafe redirect:" in catalogue
    assert "Safe defensive:" in catalogue
    assert "Claim Provenance Verification" in catalogue
    assert r"\begin{longtable}" in catalogue
    assert r"p{0.455\linewidth}" in catalogue
    assert r"\scriptsize" in catalogue
    assert r"Source: skills/\allowbreak{}osint\_\allowbreak{}integrity/" in catalogue
    assert "Supplemental Skill Metadata and Figure Matrix" in matrix
    assert "Tool Verb Usage By Group" in matrix
    assert "Quality Capsule Coverage" in matrix
    assert "`hermes` | 2" in matrix
    assert "cogsecskills_reference_density.png" in matrix
    assert "cogsecskills_harness_contract.png" in matrix
    assert "cogsecskills_cover_installation.png" in matrix


def test_figure_inventory_is_exact():
    assert FIGURE_NAMES == EXPECTED_FIGURES
    assert tuple(figure.filename for figure in FIGURES) == EXPECTED_FIGURES
    assert all(figure.reader_question for figure in FIGURES)
    assert all(figure.semantic_labels for figure in FIGURES)
    assert [figure.filename for figure in FIGURES if figure.mirrored] == [
        "cogsecskills_cover_installation.png"
    ]


def test_cover_readability_constants_are_pdf_first():
    assert COVER_COMMAND_SIZE >= 20
    assert COVER_LABEL_SIZE >= 16
    assert COVER_PANEL_TITLE_SIZE >= 30


def test_live_group_palette_covers_registry_groups():
    rows = collect_skill_rows(Path.cwd())
    groups = {row.group for row in rows}
    assert groups <= set(GROUP_COLORS)


def test_write_assets_creates_markdown_data_and_figures(tmp_path):
    _library(tmp_path)
    result = write_assets(tmp_path)
    assert result["skills"] == 2
    for rel_path in (CATALOGUE_PATH, MATRIX_PATH, DATA_JSON_PATH, DATA_CSV_PATH):
        assert (tmp_path / rel_path).is_file()
    for name in FIGURE_NAMES:
        data = (tmp_path / "output" / "figures" / name).read_bytes()
        assert data.startswith(b"\x89PNG\r\n\x1a\n")
        assert len(data) > 1000
        width, height = _png_dimensions(data)
        min_width, min_height = MIN_FIGURE_PIXELS[name]
        assert width >= min_width
        assert height >= min_height
    cover = (
        tmp_path / "output" / "figures" / "cogsecskills_cover_installation.png"
    ).read_bytes()
    assert (
        tmp_path / "figures" / "cogsecskills_cover_installation.png"
    ).read_bytes() == cover
    cover_width, cover_height = _png_dimensions(cover)
    assert 1.65 <= cover_width / cover_height <= 1.95


def test_custom_harness_flows_into_matrix_and_harness_figure(tmp_path):
    _library(tmp_path, harnesses=("claude", "codex", "hermes", "gemini"))
    rows = collect_skill_rows(tmp_path)
    assert all("gemini" in row.harnesses for row in rows)

    matrix = render_metadata_matrix(rows)
    assert "`gemini` | 2" in matrix

    write_assets(tmp_path)
    figure = tmp_path / "output" / "figures" / "cogsecskills_harness_contract.png"
    width, height = _png_dimensions(figure.read_bytes())
    min_width, min_height = MIN_FIGURE_PIXELS["cogsecskills_harness_contract.png"]
    assert width >= min_width
    assert height >= min_height


def test_check_assets_detects_missing_and_stale_files(tmp_path):
    _library(tmp_path)
    findings = check_assets(tmp_path)
    assert any("missing generated file" in finding for finding in findings)
    assert any("missing generated figure" in finding for finding in findings)

    write_assets(tmp_path)
    assert check_assets(tmp_path) == []

    path = tmp_path / CATALOGUE_PATH
    path.write_text(
        path.read_text(encoding="utf-8") + "\nmanual edit\n", encoding="utf-8"
    )
    assert check_assets(tmp_path) == [f"stale generated file: {CATALOGUE_PATH}"]


def test_cli_manuscript_assets_write_and_check(tmp_path, capsys):
    from cogsecskills.cli import main

    _library(tmp_path)
    assert main(["--root", str(tmp_path), "manuscript-assets", "--check"]) == 1
    assert "DRIFT" in capsys.readouterr().out
    assert main(["--root", str(tmp_path), "manuscript-assets", "--write"]) == 0
    assert "2 markdown, 2 data, 8 figures" in capsys.readouterr().out
    assert main(["--root", str(tmp_path), "manuscript-assets", "--check"]) == 0
    assert "manuscript assets are current" in capsys.readouterr().out
