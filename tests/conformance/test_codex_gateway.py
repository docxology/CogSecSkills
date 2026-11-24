"""Exercise real discovery, handoff, and setup failures through the shipped gateway."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
GATEWAY_PATH = Path("integrations/codex/cogsecskills/scripts/library.py")
CLI_PATH = Path("src/cogsecskills/cli.py")
SKILL_ID = "osint_integrity.claim_provenance_verification"


def run_gateway(script, cwd, *args):
    env = {**os.environ, "PATH": "", "PYTHONPATH": str(cwd)}
    return subprocess.run(
        [sys.executable, "-B", str(script), *args],
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        timeout=35,
        check=False,
    )


def test_gateway_handoff_through_symlink_from_unrelated_directory(tmp_path):
    gateway = tmp_path / "linked-skill"
    gateway.symlink_to((ROOT / GATEWAY_PATH).parent.parent, target_is_directory=True)
    script = gateway / "scripts/library.py"
    (tmp_path / "cogsecskills.py").write_text(
        "raise SystemExit('wrong runner imported')"
    )

    route = run_gateway(script, tmp_path, "route", SKILL_ID, "--format", "json")
    assert route.returncode == 0, route.stderr
    match = json.loads(route.stdout)["matches"][0]
    assert set(match) == {"skill_id", "name", "group", "score"}
    assert match["skill_id"] == SKILL_ID

    show = run_gateway(script, tmp_path, "show", match["skill_id"])
    assert show.returncode == 0, show.stderr
    spec = json.loads(show.stdout)
    assert spec["id"] == SKILL_ID and spec["status"] == "implemented"
    assert spec["summary"] and spec["triggers"] and spec["inputs"]

    skill_dir = ROOT / "skills" / Path(*SKILL_ID.split("."))
    assert "workflow.md" in (skill_dir / "SKILL.md").read_text()
    workflow = (skill_dir / "workflow.md").read_text()
    assert "Claim Provenance Verification" in workflow
    assert spec["harness"]["codex"] == "harness/codex.md"
    adapter = (skill_dir / spec["harness"]["codex"]).read_text()
    assert sorted(re.findall(r"(?m)^\| `([a-z]+)` \|", adapter)) == spec["verbs"]


def test_gateway_empty_route_and_browse(tmp_path):
    script = ROOT / GATEWAY_PATH
    query = "and the of"
    route = run_gateway(script, tmp_path, "route", query, "--format", "json")
    assert route.returncode == 0, route.stderr
    assert json.loads(route.stdout) == {"query": query, "matches": [], "count": 0}
    text = run_gateway(script, tmp_path, "route", query)
    assert text.returncode == 1
    assert "no skill matches" in text.stdout

    listing = run_gateway(
        script,
        tmp_path,
        "list",
        "--group",
        "osint_integrity",
        "--limit",
        "1",
        "--format",
        "json",
    )
    assert listing.returncode == 0, listing.stderr
    data = json.loads(listing.stdout)
    assert data["total"] == 100 and data["count"] == len(data["skills"]) == 1
    assert data["skills"][0]["group"] == "osint_integrity"


def test_gateway_preserves_cli_argument_and_unknown_skill_errors(tmp_path):
    script = ROOT / GATEWAY_PATH
    invalid = run_gateway(script, tmp_path, "route", "test", "--limit", "-1")
    assert invalid.returncode == 2 and "--limit" in invalid.stderr
    override = run_gateway(script, tmp_path, "list", "--root", str(tmp_path))
    assert (
        override.returncode == 2 and "unrecognized arguments: --root" in override.stderr
    )
    unknown = run_gateway(script, tmp_path, "show", "missing.skill")
    assert unknown.returncode == 1
    assert "unknown skill id: missing.skill" in unknown.stdout


def copy_minimal_corpus(root):
    registry = Path("registry/skills.yaml")
    skill = Path("skills/osint_integrity/claim_provenance_verification/skill.yaml")
    for path in (registry, skill):
        (root / path).parent.mkdir(parents=True)
        shutil.copyfile(ROOT / path, root / path)


@pytest.fixture
def unprepared_gateway(tmp_path):
    script = tmp_path / GATEWAY_PATH
    script.parent.mkdir(parents=True)
    shutil.copyfile(ROOT / GATEWAY_PATH, script)
    return script


@pytest.mark.parametrize(
    "args", [(), ("definitions", "--check"), ("eval-live",), ("--root", ".", "list")]
)
def test_gateway_refuses_commands_before_validating_checkout(
    unprepared_gateway, tmp_path, args
):
    result = run_gateway(unprepared_gateway, tmp_path, *args)
    assert result.returncode == 2 and "expected route, list, or show" in result.stderr
    assert result.stdout == ""
    assert not (tmp_path / ".venv").exists()


def test_gateway_missing_checkout_and_environment(unprepared_gateway, tmp_path):
    result = run_gateway(unprepared_gateway, tmp_path, "list")
    assert result.returncode == 1 and "checkout not found" in result.stderr

    cli = tmp_path / CLI_PATH
    cli.parent.mkdir(parents=True)
    shutil.copyfile(ROOT / CLI_PATH, cli)
    result = run_gateway(
        unprepared_gateway, tmp_path, "route", "claim", "--format", "json"
    )
    assert result.returncode == 1 and "checkout is incomplete" in result.stderr
    assert result.stdout == ""

    copy_minimal_corpus(tmp_path)
    result = run_gateway(unprepared_gateway, tmp_path, "list")
    assert result.returncode == 1
    assert (
        "Python environment is missing" in result.stderr
        and "uv sync --locked" in result.stderr
    )
    assert not (tmp_path / ".venv").exists()


def test_gateway_missing_dependency_in_real_empty_venv(unprepared_gateway, tmp_path):
    shutil.copytree(ROOT / "src/cogsecskills", tmp_path / "src/cogsecskills")
    copy_minimal_corpus(tmp_path)
    subprocess.run(
        [sys.executable, "-B", "-m", "venv", "--without-pip", str(tmp_path / ".venv")],
        timeout=20,
        check=True,
    )
    result = run_gateway(unprepared_gateway, tmp_path, "list")
    assert result.returncode == 1
    assert "missing yaml" in result.stderr and "uv sync --locked" in result.stderr
    assert "Traceback" not in result.stderr


def test_every_catalogued_skill_is_reachable_by_exact_id():
    from cogsecskills.core.loader import discover_skills
    from cogsecskills.quality.insights import route_query

    specs = discover_skills(ROOT)
    assert specs
    for spec in specs:
        assert route_query(spec.id, root=ROOT, limit=1)[0][0].id == spec.id
