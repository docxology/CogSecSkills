"""Authored name-free software controls, not independent routing evaluation."""

from pathlib import Path
import re

import pytest
import yaml

from cogsecskills.core.loader import discover_skills
from cogsecskills.quality.insights import route_query

ROOT = Path(__file__).resolve().parents[2]
SOURCE = yaml.safe_load((ROOT / "tests/fixtures/routing_paraphrases.yaml").read_text())


@pytest.mark.parametrize("probe", SOURCE["probes"], ids=lambda probe: probe["id"])
@pytest.mark.parametrize(
    "prefix",
    ["", "A chart and a table may help present the result, but the actual task is: "],
    ids=["paraphrase", "distractor"],
)
def test_name_free_task_retains_its_intended_candidate(probe, prefix):
    specs = {spec.id: spec for spec in discover_skills(ROOT)}
    expected = specs[probe["expected_skill"]]
    query = prefix + probe["query"]
    assert expected.id not in query
    for phrase in [expected.name, *expected.triggers]:
        assert not re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", query, re.I)
    matches = route_query(query, ROOT, limit=10)
    assert expected.id in [spec.id for spec, _ in matches]
    assert all(type(score) is int and score > 0 for _, score in matches)


@pytest.mark.parametrize("query", ["and the of", "qxzv blrpt", "?!..."])
def test_noninformative_query_does_not_select_a_skill(query):
    assert route_query(query, ROOT) == []


def test_explicit_identifier_survives_grammatical_token_filter(tmp_path):
    directory = tmp_path / "skills/and/of"
    directory.mkdir(parents=True)
    (directory / "skill.yaml").write_text(
        "id: and.of\nname: And Of\ngroup: and\nsummary: A declared catalogue record.\nstatus: planned\n",
        encoding="utf-8",
    )
    matches = route_query(" AND.OF ", tmp_path)
    assert [spec.id for spec, _ in matches] == ["and.of"]
    assert matches[0][1] > 0
