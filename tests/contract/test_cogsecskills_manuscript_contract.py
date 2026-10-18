"""Contract tests for the authored manuscript surfaces."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT = PROJECT_ROOT / "docs" / "manuscript"


BIB_KEY_RE = re.compile(r"^@(?!comment\b)\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
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


def _section_headings(paths: list[Path]) -> dict[str, tuple[str, str]]:
    inventory = {}
    anchors = set()
    for path in paths:
        text = re.sub(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", "", _read(path))
        headings = re.findall(r"^# +(.+)$", text, re.MULTILINE)
        if len(headings) != 1:
            raise ValueError(f"{path.name}: requires exactly one H1")
        match = re.fullmatch(r"(.+?)\s+\{#(sec:[a-z][a-z0-9_-]*)\}", headings[0])
        if match is None:
            raise ValueError(f"{path.name}: H1 requires a section anchor")
        title, anchor = match.groups()
        if anchor in anchors:
            raise ValueError(f"{path.name}: duplicate section anchor {anchor}")
        anchors.add(anchor)
        inventory[path.name] = (title, anchor)
    return inventory


def test_manuscript_sections_have_one_h1_with_unique_anchor():
    paths = sorted(
        path
        for path in MANUSCRIPT.glob("*.md")
        if re.match(r"(?:[0-9]{2}|S[0-9]{2})_", path.name)
    )
    inventory = _section_headings(paths)
    assert {"00_abstract.md", "99_references.md"} <= inventory.keys()
    anchors = {anchor for _, anchor in inventory.values()}
    referenced = {
        anchor
        for path in paths
        for anchor in re.findall(r"@(sec:[a-z][a-z0-9_-]*)", _read(path))
    }
    assert referenced <= anchors


def test_heading_contract_accepts_copy_edits_and_ignores_code_examples(tmp_path):
    first = tmp_path / "00_first.md"
    first.write_text(
        "# A revised reader-facing title {#sec:first}\n\n```markdown\n# Example only\n```\n",
        encoding="utf-8",
    )
    assert _section_headings([first]) == {
        "00_first.md": ("A revised reader-facing title", "sec:first")
    }


@pytest.mark.parametrize(
    "text",
    [
        "No heading\n",
        "# One {#sec:one}\n# Two {#sec:two}\n",
        "# A heading without an anchor\n",
    ],
)
def test_heading_contract_rejects_missing_or_ambiguous_structure(tmp_path, text):
    path = tmp_path / "00_invalid.md"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError, match="requires"):
        _section_headings([path])


def test_heading_contract_rejects_shared_anchors(tmp_path):
    paths = [tmp_path / "00_one.md", tmp_path / "01_two.md"]
    for path in paths:
        path.write_text(f"# {path.stem} {{#sec:duplicate}}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate section anchor"):
        _section_headings(paths)


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
    # Current source version and historical archive identity are separate.
    from cogsecskills import __version__

    assert config["paper"]["version"] == __version__
    assert re.fullmatch(r"10\.5281/zenodo\.\d+", config["publication"]["doi"])
    if config["publication"].get("version_doi"):
        assert re.fullmatch(
            r"10\.5281/zenodo\.\d+", config["publication"]["version_doi"]
        )
    prior = config["publication"]["prior_archive"]
    assert prior["version"] == "1.0.0"
    assert re.fullmatch(r"10\.5281/zenodo\.\d+", prior["version_doi"])
    cover_path = (MANUSCRIPT / config["paper"]["cover"]["image"]).resolve()
    assert (
        cover_path
        == (PROJECT_ROOT / "figures/cogsecskills_cover_installation.png").resolve()
    )
    assert cover_path.is_file()
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
            r"\\begin\{equation\}(.*?)\\end\{equation\}", text, re.DOTALL
        ):
            assert "\\label{" in match.group(1)


def test_figure_captions_are_interpretive_and_name_sources():
    for figure_name in BODY_FIGURE_NAMES:
        matches = []
        for source in MANUSCRIPT.glob("*.md"):
            for caption, target in re.findall(
                rf"!\[([^\]]*{re.escape(figure_name)}[^\]]*)\]\(([^)\n]+)\)",
                _read(source),
            ):
                matches.append((source, caption, target))
        assert matches, figure_name
        caption = matches[0][1]
        assert len(caption) >= 120
        assert "does not" in caption
        for source, _, target in matches:
            resolved = (source.parent / target).resolve()
            expected = (PROJECT_ROOT / "output" / "figures" / figure_name).resolve()
            assert resolved == expected, (source, target)
            assert resolved.is_file(), (source, target)


def test_release_manifest_records_provenance_surfaces():
    text = _read(MANUSCRIPT / "S02_release_manifest.md")
    assert "Supplemental Local Release and Render Manifest" in text
    assert "https://github.com/docxology/CogSecSkills" in text
    assert "Apache-2.0" in text
    assert "Source revision" in text
    assert "Verification Gates" in text
    publication = yaml.safe_load(_read(MANUSCRIPT / "config.yaml"))["publication"]
    assert publication["doi"] in text
    assert publication["prior_archive"]["version_doi"] in text
    assert publication["prior_archive"]["concept_doi"] in text
    assert publication["doi"] != publication["prior_archive"]["concept_doi"]
    cff = yaml.safe_load(_read(PROJECT_ROOT / "CITATION.cff"))
    codemeta = json.loads(_read(PROJECT_ROOT / "codemeta.json"))
    assert cff["doi"] == codemeta["identifier"] == publication["doi"]
    assert "Software archive" in text
    assert "Historical manuscript archive" in text
    if publication.get("version_doi"):
        assert publication["version_doi"] in text
    else:
        assert "unavailable" in text


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
    assert "one authored local worked example per skill" in text
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
