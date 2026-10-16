"""Exercise the shipped gateway from outside its checkout."""

import json
from pathlib import Path
import subprocess
import sys


def test_gateway_routes_from_unrelated_directory(tmp_path):
    root = Path(__file__).resolve().parents[2]
    script = root / "integrations/codex/cogsecskills/scripts/library.py"
    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "route",
            "osint_integrity.claim_provenance_verification",
            "--format",
            "json",
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(result.stdout)
    assert (
        payload["matches"][0]["skill_id"]
        == "osint_integrity.claim_provenance_verification"
    )


def test_every_catalogued_skill_is_reachable_by_exact_id():
    from cogsecskills.core.loader import discover_skills
    from cogsecskills.quality.insights import route_query

    root = Path(__file__).resolve().parents[2]
    specs = discover_skills(root)
    assert specs
    for spec in specs:
        assert route_query(spec.id, root=root, limit=1)[0][0].id == spec.id
