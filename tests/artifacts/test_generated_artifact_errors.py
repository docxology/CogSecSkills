"""Behavioral artifacts failures using real source inputs."""

from __future__ import annotations


from tests._support.quality_generated_outputs import (
    Path,
)


def test_check_assets_invalid_figure(tmp_path):
    """check_assets should flag a figure that is not a valid PNG."""
    from cogsecskills.artifacts.manuscript_assets.assets_io import check_assets
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
    from cogsecskills.artifacts.manuscript_assets.figures import (
        COVER_IMAGE_MIRROR_PATH,
        COVER_IMAGE_NAME,
        FIGURE_NAMES,
    )

    for name in FIGURE_NAMES:
        if name == COVER_IMAGE_NAME:
            # Create an invalid file (not PNG)
            (fig_dir / name).write_bytes(b"not a png")
        else:
            (fig_dir / name).write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 2000)

    # Create a valid cover mirror
    mirror = tmp_path / COVER_IMAGE_MIRROR_PATH
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 2000)

    findings = check_assets(tmp_path)
    assert any("invalid generated figure" in f for f in findings)


def test_check_assets_stale_cover_mirror(tmp_path):
    """check_assets should flag a stale cover mirror."""
    from cogsecskills.artifacts.manuscript_assets.assets_io import check_assets
    from cogsecskills.artifacts.manuscript_assets.paths import (
        CATALOGUE_PATH,
        COVER_IMAGE_MIRROR_PATH,
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
    from cogsecskills.artifacts.manuscript_assets.figures import (
        _PNG_SIGNATURE,
        FIGURE_NAMES,
    )

    for name in FIGURE_NAMES:
        (fig_dir / name).write_bytes(_PNG_SIGNATURE + b"\x00" * 2000)

    mirror = tmp_path / COVER_IMAGE_MIRROR_PATH
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_bytes(b"different content")

    findings = check_assets(tmp_path)
    assert any("stale generated cover image mirror" in f for f in findings)


def test_check_evals_stale_source_and_generated(tmp_path):
    """check_evals should flag both stale source and stale generated files."""
    import shutil

    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    for d in ("registry", "skills", "scenarios"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)

    from cogsecskills.artifacts.evals import (
        EVALS_MD_PATH,
        check_evals,
        write_evals,
    )

    write_evals(tmp_path)
    # Corrupt the generated markdown only (source stays valid so load_evaluations works)
    (tmp_path / EVALS_MD_PATH).write_text("manual edit\n", encoding="utf-8")

    findings = check_evals(tmp_path)
    assert any("stale generated evaluation file" in f for f in findings)
