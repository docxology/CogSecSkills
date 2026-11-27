"""Finite replay of the manuscript's synthetic source-record fixtures."""

from pathlib import Path

import pytest

from cogsecskills.core.yaml_io import read_yaml


def test_static_source_record_preserves_attribution(tmp_path: Path) -> None:
    record = tmp_path / "record.yaml"
    record.write_text(
        "claim: The museum catalogue lists a ceramic bowl.\n"
        "source: Synthetic accession card A-17\n",
        encoding="utf-8",
    )
    expected = {
        "claim": "The museum catalogue lists a ceramic bowl.",
        "source": "Synthetic accession card A-17",
    }
    assert read_yaml(record) == expected
    assert read_yaml(record) == expected


def test_static_source_record_rejects_conflicting_attribution(tmp_path: Path) -> None:
    record = tmp_path / "conflicting.yaml"
    record.write_text(
        "claim: The museum catalogue lists a ceramic bowl.\n"
        "source: Synthetic accession card A-17\n"
        "source: Synthetic accession card B-32\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate mapping key 'source'") as excinfo:
        read_yaml(record)
    assert str(record) in str(excinfo.value)
