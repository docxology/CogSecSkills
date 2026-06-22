"""Contract tests for the authored manuscript surfaces."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT = PROJECT_ROOT / "manuscript"


BIB_KEY_RE = re.compile(r"^@(?!comment\b)\w+\s*\{\s*([^,\s]+)\s*,", re.M)
CITATION_BLOCK_RE = re.compile(r"\[[^\]]*@[^]]+\]")
CITATION_KEY_RE = re.compile(r"@([A-Za-z][A-Za-z0-9_:-]*)")


REQUIRED_BIB_KEYS = {
    "sandve2013reproducible",
    "wilkinson2016fair",
    "smith2016softwareCitation",
    "ageint2026",
    "cogsecskills2026software",
    "heuer1999psychology",
    "heuerPherson2019structured",
    "delbecq1971groupProcess",
    "klein2007premortem",
    "roozenbeek2022inoculation",
    "wineburg2019lateralReading",
    "ukmod2023jdp200",
    "wardleDerakhshan2017informationDisorder",
    "vosoughi2018spread",
    "lewandowsky2012misinformationCorrection",
    "ferrara2016socialBots",
    "lazer2018fakeNews",
    "mirskyLee2021deepfakes",
    "yao2022react",
    "schick2023toolformer",
    "c2pa2026spec",
    "woolleyHoward2017computationalPropaganda",
    "bradshawHoward2019globalDisinformation",
    "kent1964estimativeProbability",
}

EXPECTED_FIGURE_NAMES = {
    "cogsecskills_taxonomy_counts.png",
    "cogsecskills_skill_grid.png",
    "cogsecskills_verb_heatmap.png",
    "cogsecskills_ageint_network.png",
    "cogsecskills_plan_build_teach_flow.png",
    "cogsecskills_reference_density.png",
    "cogsecskills_harness_contract.png",
    "cogsecskills_cover_installation.png",
}

BODY_FIGURE_NAMES = EXPECTED_FIGURE_NAMES - {"cogsecskills_cover_installation.png"}

FORMALISM_FILES = (
    "02_system_context.md",
    "03_methods.md",
)

EXPECTED_MANUSCRIPT_H1S = (
    ("00_abstract.md", "Abstract", "sec:abstract"),
    ("01_introduction.md", "Library Purpose and Reader Map", "sec:introduction"),
    (
        "02_system_context.md",
        "Source Boundary and Harness-Neutral Skill Contract",
        "sec:system_context",
    ),
    (
        "03_methods.md",
        "Source-Owned Authoring and Manuscript Generation",
        "sec:methods",
    ),
    (
        "04_artifacts_and_evidence.md",
        "Evidence Surfaces, Generated Views, and Claim Discipline",
        "sec:artifacts_evidence",
    ),
    (
        "05_reproducibility.md",
        "Reproducibility and Render Gates",
        "sec:reproducibility",
    ),
    (
        "06_limitations_and_next_steps.md",
        "Evidence Boundaries, Defensive Governance, and Next Steps",
        "sec:limitations_next_steps",
    ),
    (
        "S01_source_surface.md",
        "Supplemental Claim-Provenance Source Map",
        "sec:source_surface",
    ),
    (
        "S02_release_manifest.md",
        "Supplemental Local Release and Render Manifest",
        "sec:release_manifest",
    ),
    (
        "S10_skill_catalogue.md",
        "Supplemental 100-Skill Catalogue",
        "sec:supplemental_skill_catalogue",
    ),
    (
        "S11_skill_metadata_matrix.md",
        "Supplemental Skill Metadata and Figure Matrix",
        "sec:supplemental_skill_metadata_matrix",
    ),
    (
        "98_symbols_glossary.md",
        "Symbols and Skill-System Glossary",
        "sec:symbols_glossary",
    ),
    ("99_references.md", "References", "sec:references"),
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _bib_keys() -> set[str]:
    return set(BIB_KEY_RE.findall(_read(MANUSCRIPT / "references.bib")))


def _citation_keys() -> set[str]:
    keys: set[str] = set()
    for path in MANUSCRIPT.glob("*.md"):
        if path.name.startswith(("S10_", "S11_")):
            continue
        for block in CITATION_BLOCK_RE.findall(_read(path)):
            keys.update(CITATION_KEY_RE.findall(block))
    return keys


def test_references_bib_has_verified_non_placeholder_entries():
    text = _read(MANUSCRIPT / "references.bib")
    keys = _bib_keys()
    assert "Bibliography placeholder" not in text
    assert "Add real BibTeX" not in text
    assert REQUIRED_BIB_KEYS <= keys
    assert len(keys) >= len(REQUIRED_BIB_KEYS)


def test_manuscript_h1_inventory_is_informative_and_stable():
    seen: list[tuple[str, str, str]] = []
    for filename, _, _ in EXPECTED_MANUSCRIPT_H1S:
        text = _read(MANUSCRIPT / filename)
        match = re.search(r"^#\s+(.+?)\s+\{#([^}]+)\}", text, re.M)
        assert match, filename
        seen.append((filename, match.group(1), match.group(2)))
    assert tuple(seen) == EXPECTED_MANUSCRIPT_H1S


def test_manuscript_citations_resolve_to_references_bib():
    citation_keys = _citation_keys()
    assert citation_keys
    assert citation_keys <= _bib_keys()


def test_references_section_is_not_an_author_reminder():
    text = _read(MANUSCRIPT / "99_references.md").lower()
    assert "add references later" not in text
    assert "add real bibtex" not in text
    assert "placeholder" not in text
    assert "{#refs}" in text


def test_reproducibility_paths_are_portable():
    text = _read(MANUSCRIPT / "05_reproducibility.md")
    assert "/Users/4d/" not in text
    assert "${PROJECT_ROOT}" in text
    assert "${TEMPLATE_ROOT}" in text
    assert "python -m cogsecskills definitions --write" in text
    assert "python -m cogsecskills definitions --check" in text
    assert "python -m cogsecskills scenarios --check" in text
    assert "eight `output/figures/*.png` manuscript figures" in text


def test_manuscript_config_exposes_repository_and_license_metadata():
    config = yaml.safe_load(_read(MANUSCRIPT / "config.yaml"))
    assert config["publication"]["github_repository"] == (
        "https://github.com/docxology/CogSecSkills"
    )
    assert config["metadata"]["license"] == "Apache-2.0"
    assert config["publication"]["doi"] == ""
    assert config["publication"]["version_doi"] == ""
    assert config["paper"]["cover"]["image"] == (
        "../figures/cogsecskills_cover_installation.png"
    )
    assert "Install" in config["paper"]["cover"]["alt"]


def test_reference_density_definition_is_formal_and_bounded():
    text = _read(MANUSCRIPT / "03_methods.md")
    assert "declared references per implemented skill" in text
    assert "d_g :=" in text
    assert "metadata density, not evidence quality" in text


def test_formal_contract_names_configured_harness_set():
    text = _read(MANUSCRIPT / "02_system_context.md")
    assert "H_0 :=" in text
    assert "H_{\\mathrm{cfg}}" in text
    assert "\\operatorname{dom}(A_s)=H_{\\mathrm{cfg}}" in text
    assert "V_s \\subseteq B_{s,h}" in text


def test_formalism_uses_labeled_equations_without_inline_math_hazards():
    raw_math_symbols = set("∈⊂⊆≥≤→←↔∀∃∧∨¬∪∩")
    for filename in FORMALISM_FILES:
        text = _read(MANUSCRIPT / filename)
        assert "\\[" not in text
        assert "\\]" not in text
        assert "\\(" not in text
        assert "\\)" not in text
        assert "\\texttt{" not in text
        assert not (set(text) & raw_math_symbols)
        for match in re.finditer(
            r"\\begin\{equation\}(.*?)\\end\{equation\}", text, re.S
        ):
            assert "\\label{" in match.group(1)


def test_figure_captions_are_interpretive_and_name_sources():
    manuscript_text = "\n".join(_read(path) for path in MANUSCRIPT.glob("*.md"))
    for figure_name in BODY_FIGURE_NAMES:
        matches = re.findall(
            rf"!\[([^\]]*{re.escape(figure_name)}[^\]]*)\]"
            rf"\(\.\./output/figures/{re.escape(figure_name)}\)",
            manuscript_text,
        )
        assert matches, figure_name
        caption = matches[0]
        assert len(caption) >= 120
        assert "does not" in caption


def test_release_manifest_records_provenance_surfaces():
    text = _read(MANUSCRIPT / "S02_release_manifest.md")
    assert "Supplemental Local Release and Render Manifest" in text
    assert "https://github.com/docxology/CogSecSkills" in text
    assert "Apache-2.0" in text
    assert "Source revision" in text
    assert "Verification Gates" in text
    assert "Archive DOI | unavailable" in text


def test_manuscript_docs_include_release_manifest_and_full_figure_set():
    readme = _read(MANUSCRIPT / "README.md")
    syntax = _read(MANUSCRIPT / "SYNTAX.md")
    for text in (readme, syntax):
        assert "S02_release_manifest.md" in text
        assert "cogsecskills_reference_density.png" in text
        assert "cogsecskills_harness_contract.png" in text
        assert "cogsecskills_cover_installation.png" in text


def test_abstract_points_to_github_installation_and_harness_install():
    text = _read(MANUSCRIPT / "00_abstract.md")
    assert "github.com/docxology/CogSecSkills" in text
    assert "install" in text.lower()
    assert "agent harness" in text.lower()


def test_manuscript_describes_skill_quality_audit_contract():
    text = _read(MANUSCRIPT / "04_artifacts_and_evidence.md")
    assert "Skill Quality Audit" in text
    assert "definitions --check" in text
    assert "doctor" in text
    assert "negative controls" in text
    assert "safe defensive request pattern" in text
    assert "generic boilerplate" in text
    assert "confidence-rubric" in text
    assert "privacy/legal" in text
    assert "evidence and inference" in text
    assert "unknowns and credible alternatives" in text


def test_manuscript_describes_scenario_readiness_gate():
    text = _read(MANUSCRIPT / "04_artifacts_and_evidence.md")
    assert "Evidence Ladder and Scenario Readiness Gate" in text
    assert "scenarios/defensive_readiness.yaml" in text
    assert "python -m cogsecskills scenarios --check" in text
    assert "28 curated fixtures" in text
    assert "python -m cogsecskills examples --check" in text
    assert "one reviewed local worked example per skill" in text
    assert "expected defensive response shape" in text
    assert "do not ask Claude, Codex, Hermes" in text
    assert "live runtime" in text


def test_docs_expose_scenario_gate():
    docs = {
        "README.md": _read(PROJECT_ROOT / "README.md"),
        "docs/README.md": _read(PROJECT_ROOT / "docs" / "README.md"),
        "docs/cli.md": _read(PROJECT_ROOT / "docs" / "cli.md"),
        "docs/harness-installation.md": _read(
            PROJECT_ROOT / "docs" / "harness-installation.md"
        ),
    }
    for name, text in docs.items():
        assert "scenarios --check" in text, name


def test_manuscript_integrates_scholarship_without_overclaiming():
    combined = "\n".join(_read(path) for path in MANUSCRIPT.glob("*.md"))
    assert "harness-neutral agent-interface" in combined
    assert "information disorder" in combined
    assert "Comparative Scholarship Map" in combined
    assert "LLM reasoning/action and tool-use systems" in combined
    assert "does not support" in combined
    assert "field effectiveness" in combined


def test_manuscript_has_no_pasted_review_citation_artifacts():
    combined = "\n".join(_read(path) for path in MANUSCRIPT.glob("*.md"))
    forbidden = (
        "filecite",
        "turn0",
        "turn1",
        "turn2",
        "academia",
        "",
        "Priority annotated bibliography",
        "Section-by-section integration plan",
    )
    for needle in forbidden:
        assert needle not in combined


def test_docs_do_not_call_generated_skill_yaml_the_source_of_truth():
    stale_phrase = (
        "skill"
        + ".yaml          # harness-neutral spec — the "
        + "single"
        + " source of truth"
    )
    source_files = (
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "docs" / "architecture.md",
        PROJECT_ROOT / "docs" / "skill-contract.md",
        PROJECT_ROOT / "src" / "cogsecskills" / "core" / "spec.py",
    )
    for path in source_files:
        text = _read(path)
        assert stale_phrase not in text, path
    assert "definitions/<group>/<slug>.yaml" in _read(PROJECT_ROOT / "README.md")
    assert "canonical YAML under ``definitions/`` owns" in _read(
        PROJECT_ROOT / "src" / "cogsecskills" / "core" / "spec.py"
    )
