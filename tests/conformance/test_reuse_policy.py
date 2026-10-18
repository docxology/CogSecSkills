"""Real YAML policy cases: field-specific allowances never exempt controls."""

import subprocess
import sys

import pytest
import yaml

from cogsecskills.authoring.definitions import (
    _reused_negative_control_findings,
    _reused_quality_field_findings,
    load_definitions,
)
from cogsecskills.core.quality_constants import REUSED_QUALITY_FIELDS


@pytest.mark.parametrize("field", REUSED_QUALITY_FIELDS)
def test_shared_quality_policy_is_field_specific_and_normalized(tmp_path, field):
    source = tmp_path / "definitions/sat"
    source.mkdir(parents=True)
    for slug in ["first", "second"]:
        (source / f"{slug}.yaml").write_text(
            yaml.safe_dump(
                {
                    "id": f"sat.{slug}",
                    field: ["  Authorized data only.  "],
                    "negative_controls": ["A shared control"],
                }
            ),
            encoding="utf-8",
        )
    definitions = load_definitions(tmp_path)
    forbidden = _reused_quality_field_findings(definitions, allowed_shared_items={})
    assert len(forbidden) == 1
    assert f"{field} entry reused" in forbidden[0]
    assert "sat.first" in forbidden[0] and "sat.second" in forbidden[0]
    assert (
        _reused_quality_field_findings(
            definitions, allowed_shared_items={field: {"AUTHORIZED DATA ONLY."}}
        )
        == []
    )
    other = next(name for name in REUSED_QUALITY_FIELDS if name != field)
    assert (
        _reused_quality_field_findings(
            definitions, allowed_shared_items={other: {"authorized data only."}}
        )
        == forbidden
    )
    # Negative controls have no shared-item escape hatch, even when a quality
    # statement has an explicit field-scoped allowance.
    controls = _reused_negative_control_findings(definitions)
    assert len(controls) == 1
    assert "negative_control entry reused" in controls[0]


def test_nonexistent_root_cli_fails_with_source_path_without_traceback(tmp_path):
    root = tmp_path / "does-not-exist"
    result = subprocess.run(
        [sys.executable, "-m", "cogsecskills", "--root", str(root), "report"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "no registry" in result.stderr
    assert str(root / "registry/skills.yaml") in result.stderr
    assert "Traceback" not in result.stderr
