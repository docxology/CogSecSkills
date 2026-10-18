"""Behavioral authoring failures using real source inputs."""

from __future__ import annotations


from tests._support.cli_artifact_inputs import (
    PROJECT_ROOT,
    _ROW,
    _copy_fixture,
    _seed_registry,
    main,
    shutil,
)


def test_cli_list_group_with_no_matches(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "list", "--group", "nonexistent"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 of 1 skill areas" in out


def test_cli_list_status_with_no_matches(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "list", "--status", "implemented"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 of 1 skill areas" in out


def test_cli_list_limit_zero(tmp_path, capsys):
    _seed_registry(tmp_path, _ROW)
    rc = main(["--root", str(tmp_path), "list", "--limit", "0"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 of 1 skill areas" in out


def test_cli_dashboard_check_with_drift(tmp_path, capsys):
    root = _copy_fixture(
        tmp_path, "registry", "skills", "scenarios", "examples", "evals"
    )
    from cogsecskills.artifacts.dashboard import write_dashboard

    write_dashboard(root)
    # Corrupt a dashboard file to trigger drift
    (root / "docs" / "quality-dashboard.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "dashboard", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "DASHBOARD" in out
    assert "dashboard issue(s)" in out


def test_cli_examples_check_with_drift(tmp_path, capsys):
    root = _copy_fixture(tmp_path, "registry", "skills", "examples")
    from cogsecskills.artifacts.examples import write_examples

    write_examples(root)
    (root / "docs" / "skill-worked-examples.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "examples", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "EXAMPLES" in out
    assert "worked example issue(s)" in out


def test_cli_evals_check_with_drift(tmp_path, capsys):
    root = _copy_fixture(tmp_path, "registry", "skills", "scenarios")
    from cogsecskills.artifacts.evals import write_evals

    write_evals(root)
    (root / "docs" / "evaluation-readiness.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "evals", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "EVALS" in out
    assert "offline eval issue(s)" in out


def test_cli_release_metadata_check_with_drift(tmp_path, capsys):
    root = tmp_path
    for f in ("pyproject.toml", "CITATION.cff", "codemeta.json", "LICENSE"):
        shutil.copy2(PROJECT_ROOT / f, root / f)
    for d in ("docs", "manuscript", "output", "figures"):
        if (PROJECT_ROOT / d).exists():
            shutil.copytree(PROJECT_ROOT / d, root / d)
    from cogsecskills.artifacts.release_metadata import write_release_metadata

    write_release_metadata(root)
    (root / "docs" / "release-claim-matrix.md").write_text(
        "manual edit\n", encoding="utf-8"
    )
    rc = main(["--root", str(root), "release-metadata", "--check"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "RELEASE" in out
    assert "release metadata issue(s)" in out


def test_cli_author_batch_with_bad_def(tmp_path, capsys):
    _seed_registry(
        tmp_path,
        "  - {id: sat.good, name: Good, group: sat, status: implemented, summary: s}",
        "  - {id: sat.bad, name: Bad, group: sat, status: implemented, summary: s}",
    )
    # Create a _def.json with a bad verb
    skill_dir = tmp_path / "skills" / "sat" / "bad"
    skill_dir.mkdir(parents=True)
    (skill_dir / "_def.json").write_text(
        '{"id": "sat.bad", "tools": [{"verb": "badverb", "purpose": "p"}], '
        '"workflow_steps": [{"verbs": ["reason"], "title": "S", "text": "T"}], '
        '"anti_criteria": ["Do not."]}',
        encoding="utf-8",
    )
    rc = main(["--root", str(tmp_path), "author-batch", "--keep-defs"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "FAIL" in out
