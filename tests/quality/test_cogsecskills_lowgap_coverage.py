"""Coverage tests for remaining low-gap modules.

dashboard.py (98.64%), figures.py (98.35%), rows.py (98.29%),
tables.py (99.05%), evals.py (99.27%).
"""

from __future__ import annotations

import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_rows_group_title_fallback():
    """rows.py line 123: _group_title with group_id not in rows."""
    from cogsecskills.artifacts.manuscript_assets.rows import _group_title, SkillRow

    rows = [
        SkillRow(
            id="sat.demo",
            name="Demo",
            group="sat",
            group_title="SAT",
            status="implemented",
            functionality="s",
            use_when="u",
            ageint_topic="t",
            verbs=("read",),
            inputs=("ctx",),
            outputs=("out",),
            tags=("tag",),
            harnesses=("claude",),
            references_count=1,
            defensive_boundary="b",
            evidence_discipline="e",
            confidence_anchor="c",
            unsafe_redirect="u",
            safe_defensive_pattern="s",
            source_path="p",
        )
    ]
    assert _group_title(rows, "nonexistent") == "nonexistent"


def test_tables_latex_escape_backslash():
    """tables.py line 55: _latex_escape with backslash."""
    from cogsecskills.artifacts.manuscript_assets.tables import _latex_escape

    result = _latex_escape("path\\to\\file")
    assert "textbackslash" in result


def test_evals_check_missing_generated_json(tmp_path):
    """evals.py lines 386-387: check_evals missing generated JSON file."""
    from cogsecskills.artifacts.evals import write_evals, check_evals, EVALS_JSON_PATH

    for d in ("registry", "skills", "scenarios"):
        shutil.copytree(PROJECT_ROOT / d, tmp_path / d)
    write_evals(tmp_path)
    (tmp_path / EVALS_JSON_PATH).unlink()
    findings = check_evals(tmp_path)
    assert any("missing generated evaluation file" in f for f in findings)


def test_dashboard_verified_state_absent(tmp_path):
    """dashboard.py line 60->68: _verified_state with no TODO file."""
    from cogsecskills.artifacts.dashboard import _verified_state

    result = _verified_state(tmp_path)
    assert result == []


def test_dashboard_verified_state_present(tmp_path):
    """dashboard.py: _verified_state with a present Verified State section."""
    from cogsecskills.artifacts.dashboard import _verified_state

    (tmp_path / "TODO.md").write_text(
        "# TODO\n\n## Verified State (v1.6.0)\n\n"
        "- Gate 1: ok\n- Gate 2: ok\n\n## Next\n\n- Work\n",
        encoding="utf-8",
    )
    result = _verified_state(tmp_path)
    assert len(result) == 2
    assert "Gate 1: ok" in result[0]


def test_figures_publication_doi_present(tmp_path):
    """figures.py line 1444->1455: cover DOI truthy branch."""
    from cogsecskills.artifacts.manuscript_assets.figures import _publication_doi

    config_dir = tmp_path / "manuscript"
    config_dir.mkdir()
    (config_dir / "config.yaml").write_text(
        "publication:\n  doi: 10.5281/zenodo.20804585\n", encoding="utf-8"
    )
    result = _publication_doi(tmp_path)
    assert result == "10.5281/zenodo.20804585"
