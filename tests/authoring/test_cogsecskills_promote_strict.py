"""Tests for strict id matching in ``promote_to_implemented``.

A requested id with no stub/planned registry entry must raise ``AuthorError``
listing the unmatched ids — silently skipping a typo'd or already-implemented
id would leave the registry disagreeing with the just-rendered skills.
"""

from __future__ import annotations

import pytest

from cogsecskills.authoring.author import AuthorError, promote_to_implemented


def _seed_registry(root, *, status: str = "stub") -> None:
    (root / "registry").mkdir(parents=True, exist_ok=True)
    (root / "registry" / "skills.yaml").write_text(
        "skills:\n"
        f"  - {{id: sat.demo, name: Demo Technique, group: sat, status: {status}, "
        "summary: A demo technique.}\n",
        encoding="utf-8",
    )


def test_promote_unmatched_id_raises_authorerror(tmp_path):
    _seed_registry(tmp_path)
    with pytest.raises(AuthorError, match="no stub/planned registry entry matched"):
        promote_to_implemented(["sat.nope"], root=tmp_path)


def test_promote_error_names_only_unmatched_ids(tmp_path):
    _seed_registry(tmp_path)
    with pytest.raises(AuthorError) as exc_info:
        promote_to_implemented(["sat.demo", "sat.typo"], root=tmp_path)
    message = str(exc_info.value)
    assert "sat.typo" in message
    assert "sat.demo" not in message


def test_promote_unmatched_leaves_registry_unchanged(tmp_path):
    _seed_registry(tmp_path)
    with pytest.raises(AuthorError):
        promote_to_implemented(["sat.nope"], root=tmp_path)
    text = (tmp_path / "registry" / "skills.yaml").read_text(encoding="utf-8")
    assert "status: stub" in text
    assert "status: implemented" not in text


def test_promote_already_implemented_id_is_unmatched(tmp_path):
    _seed_registry(tmp_path, status="implemented")
    with pytest.raises(AuthorError, match="sat.demo"):
        promote_to_implemented(["sat.demo"], root=tmp_path)


def test_promote_matching_stub_still_flips_status(tmp_path):
    _seed_registry(tmp_path)
    changed = promote_to_implemented(["sat.demo"], root=tmp_path)
    assert changed == 1
    text = (tmp_path / "registry" / "skills.yaml").read_text(encoding="utf-8")
    assert "status: implemented" in text
    assert "status: stub" not in text
