"""Authored answer keys cannot manufacture independent reviews or ratings."""

from pathlib import Path
import shutil

import pytest
import yaml

from cogsecskills.artifacts.evals import load_evaluations, write_evals
from cogsecskills.artifacts.scenarios import RUBRIC_KEYS

REPOSITORY = Path(__file__).resolve().parents[2]


def fixture_project(root: Path) -> Path:
    (root / "scenarios").mkdir()
    shutil.copy2(
        REPOSITORY / "scenarios/defensive_readiness.yaml",
        root / "scenarios/defensive_readiness.yaml",
    )
    write_evals(root)
    return root / "evals/local_output_review.yaml"


def test_generated_answer_keys_have_no_attached_ratings(tmp_path: Path) -> None:
    path = fixture_project(tmp_path)
    source = yaml.safe_load(path.read_text())
    assert source["evaluations"]
    assert all("rubric_scores" not in row for row in source["evaluations"])
    assert all(
        row["provenance"] == "authored expected-answer fixture"
        for row in source["evaluations"]
    )


def test_fixture_report_records_no_independent_review_or_measured_scores(
    tmp_path: Path,
) -> None:
    fixture_project(tmp_path)
    import json

    report = json.loads(
        (tmp_path / "output/data/evaluation_readiness.json").read_text()
    )
    assert report["summary"]["independent_review_records"] == 0
    assert report["summary"]["measured_score_records"] == 0
    assert "passing_score" not in report["summary"]
    markdown = (tmp_path / "docs/evaluation-readiness.md").read_text()
    assert "reviewed local answers" not in markdown
    assert "Passing score" not in markdown
    assert "vocabulary presence" in markdown


@pytest.mark.parametrize("score", [0, 1, 2])
def test_authored_fixture_rejects_fabricated_rubric_ratings(
    tmp_path: Path, score: int
) -> None:
    path = fixture_project(tmp_path)
    source = yaml.safe_load(path.read_text())
    source["evaluations"][0]["rubric_scores"] = {key: score for key in RUBRIC_KEYS}
    path.write_text(yaml.safe_dump(source, sort_keys=False))
    with pytest.raises(ValueError, match="authored fixture cannot carry rubric scores"):
        load_evaluations(tmp_path)


def test_legacy_review_api_exposes_no_fabricated_scores(tmp_path: Path) -> None:
    fixture_project(tmp_path)
    reviews = load_evaluations(tmp_path)
    assert len(reviews) == len(
        yaml.safe_load((tmp_path / "scenarios/defensive_readiness.yaml").read_text())[
            "scenarios"
        ]
    )
    assert all(review.rubric_scores == {} for review in reviews)


def test_direct_api_cannot_silently_discard_forged_ratings(tmp_path):
    from dataclasses import replace

    from cogsecskills.artifacts.evals import _payload

    root = tmp_path
    fixture_project(root)
    review = load_evaluations(root)[0]
    forged = replace(review, rubric_scores={key: 2 for key in RUBRIC_KEYS})
    with pytest.raises(ValueError, match="authored fixture cannot carry rubric scores"):
        _payload(root, reviews=[forged])
