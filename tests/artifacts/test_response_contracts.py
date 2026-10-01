"""Real-source regressions for answer contracts and strict fixture loading."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest
import yaml

from cogsecskills.artifacts.dashboard import check_dashboard
from cogsecskills.artifacts.evals import (
    EVALS_SOURCE_PATH,
    check_evals,
    load_evaluations,
    write_evals,
)
from cogsecskills.artifacts.examples import (
    EXAMPLES_SOURCE_PATH,
    check_examples,
    load_examples,
    write_examples,
)
from cogsecskills.artifacts.release_metadata import _has_doi, _metadata_payload
from cogsecskills.artifacts.response_contract import response_contract_findings
from cogsecskills.artifacts.text_outputs import check_text_outputs, write_text_outputs
from cogsecskills.artifacts.scenarios import (
    AnswerSection,
    _as_text_list,
    check_scenarios,
    load_scenarios,
)
from cogsecskills.core.yaml_io import read_yaml
from tests.artifacts.test_cogsecskills_scenarios import _library

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _update(path: Path, mutate) -> None:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    mutate(raw)
    path.write_text(yaml.safe_dump(raw, sort_keys=False), encoding="utf-8")


def test_response_contract_normalizes_case_and_line_wraps():
    sections = [AnswerSection("Evidence   Table", "Source\n evidence is bounded.")]
    assert (
        response_contract_findings(
            sections,
            required_sections=["evidence table"],
            must_include_terms=["source evidence"],
            must_exclude_terms=["invented evidence"],
            label="answer",
        )
        == []
    )


@pytest.mark.parametrize(
    ("field", "term", "message"),
    [
        ("required_sections", "Missing section", "required response section"),
        ("must_include_terms", "absent marker", "required response term"),
        ("must_exclude_terms", "supplied evidence", "excluded response term"),
    ],
)
def test_scenario_answer_enforces_its_declared_contract(tmp_path, field, term, message):
    _library(tmp_path)
    source = tmp_path / "scenarios/defensive_readiness.yaml"

    def change(raw):
        raw["scenarios"][0]["expected_response"][field].append(term)

    _update(source, change)
    assert any(message in finding for finding in check_scenarios(tmp_path))


def test_excluded_term_cannot_supply_a_required_quality_term(tmp_path):
    _library(tmp_path)
    source = tmp_path / "scenarios/defensive_readiness.yaml"

    def change(raw):
        contract = raw["scenarios"][0]["expected_response"]
        contract["required_sections"] = ["Defensive purpose", "Results", "Limits"]
        contract["must_include_terms"] = ["defensive", "matrix", "hypotheses", "gap"]
        contract["must_exclude_terms"] = ["confidence", "evidence", "uncertainty"]

    _update(source, change)
    findings = check_scenarios(tmp_path)
    assert any("expected response term 'evidence' is missing" in f for f in findings)
    assert any("excluded response term 'confidence' is present" in f for f in findings)


def test_contradictory_response_contract_is_reported(tmp_path):
    _library(tmp_path)
    source = tmp_path / "scenarios/defensive_readiness.yaml"
    _update(
        source,
        lambda raw: raw["scenarios"][0]["expected_response"][
            "must_exclude_terms"
        ].append("evidence"),
    )
    assert any(
        "expected response excludes required term 'evidence'" in finding
        for finding in check_scenarios(tmp_path)
    )


def test_evaluation_count_follows_the_source_scenarios(tmp_path):
    _library(tmp_path)
    write_evals(tmp_path)
    assert len(load_evaluations(tmp_path)) == 4
    assert check_evals(tmp_path) == []


def test_evaluation_cannot_satisfy_contract_with_metadata(tmp_path):
    _library(tmp_path)
    source = tmp_path / "scenarios/defensive_readiness.yaml"
    _update(
        source,
        lambda raw: raw["scenarios"][0]["expected_response"][
            "must_include_terms"
        ].append("reviewed local fixture"),
    )
    write_evals(tmp_path)
    findings = check_evals(tmp_path)
    assert any(
        "required response term 'reviewed local fixture' is missing" in f
        for f in findings
    )


def test_example_request_cannot_supply_answer_output_or_evidence(tmp_path):
    for dirname in ("registry", "skills", "examples"):
        shutil.copytree(PROJECT_ROOT / dirname, tmp_path / dirname)
    source = tmp_path / EXAMPLES_SOURCE_PATH

    def change(raw):
        example = raw["examples"][0]
        example["request"] = "defensive evidence inference gap confidence uncertainty"
        example["sections"] = [
            {"title": f"Section {i}", "body": "No reviewed result."} for i in range(3)
        ]

    _update(source, change)
    write_examples(tmp_path)
    findings = check_examples(tmp_path)
    assert any("example term 'evidence' is missing" in f for f in findings)
    assert any("does not name a declared output" in f for f in findings)


@pytest.mark.parametrize("field", ["id", "group", "query", "expected_skill"])
@pytest.mark.parametrize("value", [None, False, 42, {"nested": "text"}])
def test_scenario_scalar_fields_require_actual_text(tmp_path, field, value):
    _library(tmp_path)
    source = tmp_path / "scenarios/defensive_readiness.yaml"
    _update(source, lambda raw: raw["scenarios"][0].__setitem__(field, value))
    with pytest.raises(ValueError, match=f"{field} must be a non-empty string"):
        load_scenarios(tmp_path)


@pytest.mark.parametrize("value", [[None], [False], [42], [{"term": "evidence"}]])
def test_scenario_term_lists_reject_non_text_members(value):
    with pytest.raises(ValueError, match="list of strings"):
        _as_text_list(value, field="terms")


@pytest.mark.parametrize("surface", ["scenario", "evaluation"])
def test_boolean_cannot_be_a_rubric_integer(tmp_path, surface):
    _library(tmp_path)
    if surface == "scenario":
        source = tmp_path / "scenarios/defensive_readiness.yaml"
        key, load = "scenarios", load_scenarios
        score_field = "expected_answer"
    else:
        write_evals(tmp_path)
        source = tmp_path / EVALS_SOURCE_PATH
        key, load = "evaluations", load_evaluations
        score_field = None

    def change(raw):
        row = raw[key][0]
        if score_field:
            row = row[score_field]
        row["rubric_scores"]["skill_fit"] = True

    _update(source, change)
    with pytest.raises(ValueError, match="rubric_scores.skill_fit must be"):
        load(tmp_path)


@pytest.mark.parametrize(
    "text",
    [
        "key: first\nkey: last\n",
        "outer:\n  key: first\n  key: last\n",
        "base: &base {key: first}\nmerged: {<<: *base, key: last}\n",
        "[unclosed\n",
        "? [unhashable, mapping, key]\n: value\n",
    ],
)
def test_yaml_rejects_ambiguous_or_malformed_source(tmp_path, text):
    source = tmp_path / "source.yaml"
    source.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError, match="cannot read YAML"):
        read_yaml(source)


def test_yaml_allows_unambiguous_aliases_and_scalar_values(tmp_path):
    source = tmp_path / "source.yaml"
    source.write_text("base: &base {key: value}\ncopy: *base\n", encoding="utf-8")
    assert read_yaml(source) == {"base": {"key": "value"}, "copy": {"key": "value"}}


@pytest.mark.parametrize("failure", ["missing", "non_utf8"])
def test_yaml_read_failures_are_source_labelled(tmp_path, failure):
    source = tmp_path / "source.yaml"
    if failure == "non_utf8":
        source.write_bytes(b"\xff")
    with pytest.raises(ValueError, match="source.yaml: cannot read YAML"):
        read_yaml(source)


@pytest.mark.parametrize(
    ("relpath", "check"),
    [
        (Path("scenarios/defensive_readiness.yaml"), check_scenarios),
        (EXAMPLES_SOURCE_PATH, check_examples),
        (EVALS_SOURCE_PATH, check_evals),
    ],
)
def test_fixture_check_reports_yaml_errors_without_tracebacks(tmp_path, relpath, check):
    _library(tmp_path)
    write_evals(tmp_path)
    path = tmp_path / relpath
    path.parent.mkdir(exist_ok=True)
    path.write_text("key: [unclosed\n", encoding="utf-8")
    assert any("cannot read YAML" in finding for finding in check(tmp_path))


def test_evaluation_check_reports_invalid_scenario_source(tmp_path):
    _library(tmp_path)
    write_evals(tmp_path)
    (tmp_path / "scenarios/defensive_readiness.yaml").write_text(
        "key: [unclosed\n", encoding="utf-8"
    )
    assert any("cannot read YAML" in finding for finding in check_evals(tmp_path))


@pytest.mark.parametrize(
    "metadata",
    [
        {"doi": "release 10. next"},
        {"identifier": "https://example.invalid/10.1234/archive"},
        {"identifiers": [{"type": "doi"}]},
        {"identifiers": [{"type": "doi", "value": ""}]},
        {"doi": "10.1234/"},
        {"doi": 10.1234},
        {"doi": "10.1234/has spaces"},
    ],
)
def test_doi_detection_requires_an_identifier_value(metadata):
    assert not _has_doi(metadata)


@pytest.mark.parametrize(
    "value",
    ["10.1234/archive", "doi:10.1234/archive", "https://doi.org/10.1234/archive"],
)
def test_doi_detection_accepts_bounded_declared_forms(value):
    assert _has_doi({"doi": value})


def test_release_report_bounds_doi_to_a_metadata_declaration():
    payload = _metadata_payload(PROJECT_ROOT)
    assert payload["archive"]["status"] == "declared"
    assert payload["archive"]["resolution_checked"] is False
    archive_claim = next(
        row for row in payload["claim_matrix"] if row["claim"] == "Public archive DOI"
    )
    assert "external archive not checked" in archive_claim["status"]
    assert "contain no DOI" not in archive_claim["evidence"]


def test_generated_answers_preserve_actual_source_sections(tmp_path):
    _library(tmp_path)
    write_evals(tmp_path)
    payload = json.loads(
        (tmp_path / "output/data/evaluation_readiness.json").read_text(encoding="utf-8")
    )
    assert payload["evaluations"][0]["sections"] == [
        {"title": section.title, "body": section.body}
        for section in load_scenarios(tmp_path)[0].expected_answer.sections
    ]


def test_examples_load_duplicate_keys_reports_source(tmp_path):
    path = tmp_path / EXAMPLES_SOURCE_PATH
    path.parent.mkdir()
    path.write_text("examples: []\nexamples: []\n", encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate mapping key 'examples'"):
        load_examples(tmp_path)


def test_evaluation_check_reports_non_utf8_source(tmp_path):
    _library(tmp_path)
    write_evals(tmp_path)
    (tmp_path / EVALS_SOURCE_PATH).write_bytes(b"\xff")
    assert any("cannot read YAML" in finding for finding in check_evals(tmp_path))


def test_text_artifact_checks_report_all_drift_states(tmp_path):
    outputs = {
        Path("data/current.txt"): "current\n",
        Path("data/stale.txt"): "expected\n",
        Path("data/unreadable.txt"): "valid UTF-8\n",
        Path("data/missing.txt"): "missing\n",
    }
    write_text_outputs(tmp_path, outputs)
    (tmp_path / "data/stale.txt").write_text("changed\n", encoding="utf-8")
    (tmp_path / "data/unreadable.txt").write_bytes(b"\xff")
    (tmp_path / "data/missing.txt").unlink()
    findings = check_text_outputs(tmp_path, outputs)
    assert len(findings) == 3
    assert "stale generated file: data/stale.txt" in findings
    assert any("unreadable generated file: data/unreadable.txt" in f for f in findings)
    assert "missing generated file: data/missing.txt" in findings


@pytest.mark.parametrize("name", ["markdown", "data"])
def test_eval_check_reports_corrupt_generated_text(tmp_path, name):
    _library(tmp_path)
    result = write_evals(tmp_path)
    (tmp_path / result[name]).write_bytes(b"\xff")
    assert any(
        "unreadable generated evaluation file" in f for f in check_evals(tmp_path)
    )


def test_dashboard_check_reports_malformed_source(tmp_path):
    _library(tmp_path)
    (tmp_path / "scenarios/defensive_readiness.yaml").write_text(
        "key: [unclosed\n", encoding="utf-8"
    )
    assert any("cannot read YAML" in f for f in check_dashboard(tmp_path))


def test_text_outputs_reject_external_symlink_before_any_write(tmp_path):
    root = tmp_path / "root"
    outside = tmp_path / "outside"
    root.mkdir()
    outside.mkdir()
    (outside / "private.txt").write_text("original\n", encoding="utf-8")
    (root / "redirect").symlink_to(outside, target_is_directory=True)
    outputs = {
        Path("first.txt"): "must not be written\n",
        Path("redirect/private.txt"): "must not overwrite\n",
    }
    with pytest.raises(ValueError, match="must stay inside"):
        write_text_outputs(root, outputs)
    assert not (root / "first.txt").exists()
    assert (outside / "private.txt").read_text(encoding="utf-8") == "original\n"
    findings = check_text_outputs(root, outputs)
    assert any("unsafe generated file: redirect/private.txt" in f for f in findings)


def test_eval_source_symlink_cannot_overwrite_an_external_file(tmp_path):
    root = tmp_path / "root"
    outside = tmp_path / "outside.yaml"
    _library(root)
    outside.write_text("private sentinel\n", encoding="utf-8")
    source = root / EVALS_SOURCE_PATH
    source.parent.mkdir()
    source.symlink_to(outside)
    with pytest.raises(ValueError, match="must stay inside"):
        write_evals(root)
    assert outside.read_text(encoding="utf-8") == "private sentinel\n"
    assert not (root / "docs/evaluation-readiness.md").exists()


def test_unsafe_eval_mirror_cannot_partially_rewrite_the_source(tmp_path):
    root = tmp_path / "root"
    outside = tmp_path / "outside"
    _library(root)
    write_evals(root)
    source = root / EVALS_SOURCE_PATH
    original = source.read_bytes()
    (root / "output/data").rename(root / "original-data")
    outside.mkdir()
    (root / "output/data").symlink_to(outside, target_is_directory=True)
    _update(
        root / "scenarios/defensive_readiness.yaml",
        lambda raw: raw["scenarios"][0]["expected_answer"]["sections"][0].__setitem__(
            "body", "Changed prospective answer evidence."
        ),
    )
    with pytest.raises(ValueError, match="must stay inside"):
        write_evals(root)
    assert source.read_bytes() == original
    assert list(outside.iterdir()) == []
