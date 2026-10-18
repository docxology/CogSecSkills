"""Behavioral artifacts failures using real source inputs."""

from __future__ import annotations


from tests._support.validation_artifact_sources import (
    PROJECT_ROOT,
    pytest,
    shutil,
    yaml,
)


def test_release_metadata_check_rejects_non_mapping_citation(tmp_path):
    """A non-mapping CITATION.cff surfaces a ValueError from the release check."""
    from cogsecskills.artifacts.release_metadata import check_release_metadata

    for f in ("pyproject.toml", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, tmp_path / f)
    (tmp_path / "CITATION.cff").write_text("- just a list\n", encoding="utf-8")
    with pytest.raises(ValueError, match="top level must be a mapping"):
        check_release_metadata(tmp_path)


def test_release_metadata_check_rejects_non_mapping_codemeta(tmp_path):
    """A non-mapping codemeta.json surfaces a ValueError from the release check."""
    from cogsecskills.artifacts.release_metadata import check_release_metadata

    for f in ("pyproject.toml", "CITATION.cff", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, tmp_path / f)
    (tmp_path / "codemeta.json").write_text("[1, 2, 3]\n", encoding="utf-8")
    with pytest.raises(ValueError, match="top level must be a mapping"):
        check_release_metadata(tmp_path)


def test_release_findings_pyproject_license_mismatch(tmp_path):
    """_findings should flag pyproject license mismatch."""
    from cogsecskills.artifacts.release_metadata import _findings, _metadata_payload

    for f in ("pyproject.toml", "CITATION.cff", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, tmp_path / f)
    for d in ("docs", "manuscript", "output", "figures"):
        if (PROJECT_ROOT / d).exists():
            shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    payload = _metadata_payload(tmp_path)
    # Corrupt the pyproject license
    payload["license"]["pyproject"] = "MIT"
    findings = _findings(
        payload, mode="local", runtime_git={"available": True, "dirty": False}
    )
    assert any("pyproject license is not Apache" in f for f in findings)


def test_examples_not_in_registry(tmp_path):
    """Example for a skill not in the registry should be flagged."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_SOURCE_PATH,
        _content_findings,
        load_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    source = tmp_path / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["skill_id"] = "sat.nonexistent_in_registry"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    examples = load_examples(tmp_path)
    findings = _content_findings(tmp_path, examples)
    assert any("not present in registry" in f for f in findings)


def test_examples_repeated_section_titles(tmp_path):
    """Example with repeated section titles should be flagged."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_SOURCE_PATH,
        _content_findings,
        load_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    source = tmp_path / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["sections"][1]["title"] = raw["examples"][0]["sections"][0][
        "title"
    ]
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    examples = load_examples(tmp_path)
    findings = _content_findings(tmp_path, examples)
    assert any("repeats section titles" in f for f in findings)


def test_examples_operational_misuse_in_text(tmp_path):
    """Example with operational misuse phrase should be flagged."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_SOURCE_PATH,
        _content_findings,
        load_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    source = tmp_path / EXAMPLES_SOURCE_PATH
    raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    raw["examples"][0]["sections"][0]["body"] += " step-by-step operational playbook"
    source.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")
    examples = load_examples(tmp_path)
    findings = _content_findings(tmp_path, examples)
    assert any("operational misuse detail" in f for f in findings)


def test_examples_check_missing_generated_json(tmp_path):
    """check_examples should flag missing generated JSON file."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_JSON_PATH,
        check_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    (tmp_path / EXAMPLES_JSON_PATH).unlink()
    findings = check_examples(tmp_path)
    assert any("missing generated examples file" in f for f in findings)


def test_examples_check_stale_generated_md(tmp_path):
    """check_examples should flag stale generated markdown."""
    from cogsecskills.artifacts.examples import (
        EXAMPLES_MD_PATH,
        check_examples,
        write_examples,
    )

    for d in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_examples(tmp_path)
    (tmp_path / EXAMPLES_MD_PATH).write_text("manual edit\n", encoding="utf-8")
    findings = check_examples(tmp_path)
    assert any("stale generated examples file" in f for f in findings)


def test_check_assets_missing_cover_mirror(tmp_path):
    """check_assets should flag a missing cover mirror."""
    from cogsecskills.artifacts.manuscript_assets.assets_io import check_assets
    from cogsecskills.artifacts.manuscript_assets.figures import (
        _PNG_SIGNATURE,
        FIGURE_NAMES,
    )
    from cogsecskills.artifacts.manuscript_assets.paths import (
        CATALOGUE_PATH,
        DATA_CSV_PATH,
        DATA_JSON_PATH,
        MATRIX_PATH,
    )

    (tmp_path / "registry").mkdir(parents=True, exist_ok=True)
    (tmp_path / "registry" / "skills.yaml").write_text("skills: []\n", encoding="utf-8")
    (tmp_path / "registry" / "groups.yaml").write_text("groups: []\n", encoding="utf-8")
    for p in (CATALOGUE_PATH, MATRIX_PATH, DATA_JSON_PATH, DATA_CSV_PATH):
        full = tmp_path / p
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text("dummy", encoding="utf-8")
    fig_dir = tmp_path / "output" / "figures"
    fig_dir.mkdir(parents=True)
    for name in FIGURE_NAMES:
        (fig_dir / name).write_bytes(_PNG_SIGNATURE + b"\x00" * 2000)
    # Don't create the cover mirror — it should be flagged as missing
    findings = check_assets(tmp_path)
    assert any("missing generated cover image mirror" in f for f in findings)


def test_check_evals_stale_source_only(tmp_path):
    """check_evals should flag a stale offline evaluation source."""
    from cogsecskills.artifacts.evals import EVALS_SOURCE_PATH, check_evals, write_evals

    for d in ("registry", "skills", "scenarios"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_evals(tmp_path)
    # Make the valid source noncanonical without introducing a parse failure.
    source = tmp_path / EVALS_SOURCE_PATH
    source.write_text(
        source.read_text(encoding="utf-8") + "# manual edit\n", encoding="utf-8"
    )
    findings = check_evals(tmp_path)
    assert any("stale offline evaluation source" in f for f in findings)
