"""Command-line interface for the CogSecSkills runner.

Thin orchestrator over the library API. All logic lives in the sibling modules;
this file only parses arguments, calls them, and prints results.

Usage::

    python -m cogsecskills list [--group G] [--status S]
    python -m cogsecskills show <skill-id>
    python -m cogsecskills validate
    python -m cogsecskills report
    python -m cogsecskills route "free text need" [--limit N]
    python -m cogsecskills catalogue --markdown [--output docs/skill_catalogue.md]
    python -m cogsecskills doctor
    python -m cogsecskills definitions --write|--check
    python -m cogsecskills scenarios --check
    python -m cogsecskills examples --write|--check
    python -m cogsecskills evals --write|--check
    python -m cogsecskills dashboard --write|--check
    python -m cogsecskills release-metadata --write|--check
    python -m cogsecskills manuscript-assets --write|--check
    python -m cogsecskills scaffold <skill-id> [--root PATH]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .author import author_batch, load_definition_file, render_definition
from .config import load_config
from .dashboard import check_dashboard, write_dashboard
from .definitions import check_definitions, write_definitions
from .evals import check_evals, write_evals
from .examples import check_examples, write_examples
from .insights import (
    doctor,
    library_stats,
    render_catalogue_markdown,
    route_query,
)
from . import __version__
from .loader import discover_skills
from .manuscript_assets import check_assets, write_assets
from .registry import load_registry
from .release_metadata import check_release_metadata, write_release_metadata
from .scenarios import check_scenarios, scenario_summary
from .scaffold import scaffold_skill
from .spec import SkillSpec
from .validate import conformance_report, validate_library


def _cmd_list(args: argparse.Namespace) -> int:
    registry = load_registry(args.root)
    rows = registry.entries
    if args.group:
        rows = tuple(e for e in rows if e.group == args.group)
    if args.status:
        rows = tuple(e for e in rows if e.status == args.status)
    for entry in rows:
        print(f"{entry.status:11}  {entry.id:48}  {entry.name}")
    print(
        f"\n{len(rows)} of {len(registry)} skill areas "
        f"({', '.join(f'{k}={v}' for k, v in registry.status_counts().items())})"
    )
    return 0


def _cmd_show(args: argparse.Namespace) -> int:
    for spec in discover_skills(args.root):
        if spec.id == args.skill_id:
            print(json.dumps(_spec_dict(spec), indent=2))
            return 0
    registry = load_registry(args.root)
    entry = registry.get(args.skill_id)
    if entry is not None:
        print(json.dumps(entry.__dict__, indent=2))
        print(f"\n(status={entry.status}: not yet built on disk)")
        return 0
    print(f"unknown skill id: {args.skill_id}")
    return 1


def _cmd_validate(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    result = validate_library(args.root, harnesses=config.harnesses)
    for issue in result.issues:
        print(f"{issue.severity.upper():7}  {issue.skill_id:40}  {issue.message}")
    print(f"\n{len(result.errors)} error(s), {len(result.warnings)} warning(s)")
    return 0 if result.ok else 1


def _cmd_route(args: argparse.Namespace) -> int:
    matches = route_query(args.query, root=args.root, limit=args.limit)
    if not matches:
        print(f"no skill matches: {args.query!r}")
        return 1
    print(f"skills matching {args.query!r}:")
    for spec, score in matches:
        print(f"  [{score:3}] {spec.id:48}  {spec.name}")
    return 0


def _cmd_stats(args: argparse.Namespace) -> int:
    print(json.dumps(library_stats(args.root), indent=2))
    return 0


def _cmd_groups(args: argparse.Namespace) -> int:
    registry = load_registry(args.root)
    for group_id in sorted({e.group for e in registry.entries}):
        title = registry.groups.get(group_id, group_id)
        n = len(registry.by_group(group_id))
        print(f"{group_id:24}  {n:3}  {title}")
    return 0


def _cmd_catalogue(args: argparse.Namespace) -> int:
    markdown = render_catalogue_markdown(args.root)
    if args.output:
        args.output.write_text(markdown + "\n", encoding="utf-8")
        print(f"wrote {args.output}")
        return 0
    print(markdown)
    return 0


def _cmd_doctor(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    result = validate_library(args.root, harnesses=config.harnesses)
    findings = doctor(args.root, config)
    for issue in result.issues:
        print(f"{issue.severity.upper():7}  {issue.skill_id:40}  {issue.message}")
    for f in findings:
        print(f"{f['level'].upper():7}  {f['skill_id']:40}  {f['message']}")
    print(
        f"\nvalidation: {len(result.errors)} error(s); "
        f"quality: {len(findings)} finding(s)"
    )
    return 0 if result.ok and not findings else 1


def _cmd_manuscript_assets(args: argparse.Namespace) -> int:
    if args.write:
        result = write_assets(args.root)
        print(
            "wrote manuscript assets: "
            f"{len(result['markdown'])} markdown, "
            f"{len(result['data'])} data, "
            f"{len(result['figures'])} figures "
            f"for {result['skills']} skills"
        )
        return 0

    findings = check_assets(args.root)
    if findings:
        for finding in findings:
            print(f"DRIFT  {finding}")
        print(f"\n{len(findings)} manuscript asset issue(s)")
        return 1
    print("manuscript assets are current")
    return 0


def _cmd_definitions(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    if args.write:
        result = write_definitions(args.root, harnesses=config.harnesses)
        print(
            "wrote canonical definitions: "
            f"{len(result['definitions'])} definitions, "
            f"{len(result['rendered'])} rendered skills"
        )
        return 0

    findings = check_definitions(args.root, harnesses=config.harnesses)
    if findings:
        for finding in findings:
            print(f"DRIFT  {finding}")
        print(f"\n{len(findings)} definition issue(s)")
        return 1
    print("canonical definitions are current")
    return 0


def _cmd_scenarios(args: argparse.Namespace) -> int:
    findings = check_scenarios(args.root)
    if findings:
        for finding in findings:
            print(f"SCENARIO  {finding}")
        print(f"\n{len(findings)} scenario issue(s)")
        return 1
    summary = scenario_summary(args.root)
    print(
        "scenario readiness fixtures are current: "
        f"{summary['count']} scenarios across {len(summary['by_group'])} groups; "
        f"{summary['expected_answers']} expected answers checked"
    )
    return 0


def _cmd_dashboard(args: argparse.Namespace) -> int:
    if args.write:
        result = write_dashboard(args.root)
        print(
            "wrote quality dashboard: "
            f"{result['skills']} skills, {result['scenarios']} scenarios, "
            f"{result['examples']} worked examples, "
            f"{result['markdown']}, {result['html']}, {result['data']}"
        )
        return 0

    findings = check_dashboard(args.root)
    if findings:
        for finding in findings:
            print(f"DASHBOARD  {finding}")
        print(f"\n{len(findings)} dashboard issue(s)")
        return 1
    print("quality dashboard is current")
    return 0


def _cmd_examples(args: argparse.Namespace) -> int:
    if args.write:
        result = write_examples(args.root)
        print(
            "wrote worked examples: "
            f"{result['examples']} examples, {result['markdown']}, {result['data']}"
        )
        return 0

    findings = check_examples(args.root)
    if findings:
        for finding in findings:
            print(f"EXAMPLES  {finding}")
        print(f"\n{len(findings)} worked example issue(s)")
        return 1
    print("worked examples are current")
    return 0


def _cmd_evals(args: argparse.Namespace) -> int:
    if args.write:
        result = write_evals(args.root)
        print(
            "wrote offline eval fixtures: "
            f"{result['evaluations']} evaluations, {result['source']}, "
            f"{result['markdown']}, {result['data']}"
        )
        return 0

    findings = check_evals(args.root)
    if findings:
        for finding in findings:
            print(f"EVALS  {finding}")
        print(f"\n{len(findings)} offline eval issue(s)")
        return 1
    print("offline evaluation fixtures are current")
    return 0


def _cmd_release_metadata(args: argparse.Namespace) -> int:
    if args.write:
        result = write_release_metadata(args.root, mode=args.mode)
        print(
            "wrote release metadata: "
            f"mode={result['mode']}, {result['markdown']}, {result['data']}; "
            f"runtime git={result['git_revision'] or 'unavailable'}, "
            f"dirty={result['git_dirty']}"
        )
        return 0

    findings = check_release_metadata(args.root, mode=args.mode)
    if findings:
        for finding in findings:
            print(f"RELEASE  {finding}")
        print(f"\n{len(findings)} release metadata issue(s)")
        return 1
    print(f"release metadata is current ({args.mode} mode)")
    return 0


def _cmd_export(args: argparse.Namespace) -> int:
    skills = [_spec_dict(spec) for spec in discover_skills(args.root)]
    print(json.dumps({"skills": skills, "count": len(skills)}, indent=2))
    return 0


def _cmd_report(args: argparse.Namespace) -> int:
    print(json.dumps(conformance_report(args.root), indent=2))
    return 0


def _cmd_scaffold(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    created = scaffold_skill(
        args.skill_id,
        root=args.root,
        overwrite=args.overwrite,
        harnesses=config.harnesses,
    )
    print(f"scaffolded {len(created)} files for {args.skill_id}:")
    for path in created:
        print(f"  {path}")
    return 0


def _cmd_author(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    definition = load_definition_file(args.definition)
    written = render_definition(definition, root=args.root, harnesses=config.harnesses)
    print(f"authored {len(written)} files for {definition.get('id')}")
    return 0


def _cmd_author_batch(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    result = author_batch(
        root=args.root, delete_defs=not args.keep_defs, harnesses=config.harnesses
    )
    print(f"rendered {len(result['rendered'])} skills; {len(result['failed'])} failed")
    for skill_id, err in result["failed"].items():
        print(f"  FAIL {skill_id}: {err}")
    return 0 if not result["failed"] else 1


def _spec_dict(spec: SkillSpec) -> dict:
    return {
        "id": spec.id,
        "name": spec.name,
        "group": spec.group,
        "status": spec.status,
        "version": spec.version,
        "summary": spec.summary,
        "tags": list(spec.tags),
        "triggers": list(spec.triggers),
        "verbs": sorted(v.value for v in spec.verbs),
        "inputs": [io.name for io in spec.inputs],
        "outputs": [io.name for io in spec.outputs],
        "harness": dict(spec.harness),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cogsecskills", description=__doc__)
    parser.add_argument(
        "--version", action="version", version=f"cogsecskills {__version__}"
    )
    parser.add_argument("--root", type=Path, default=None, help="project root override")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list catalogued skill areas")
    p_list.add_argument("--group")
    p_list.add_argument("--status")
    p_list.set_defaults(func=_cmd_list)

    p_show = sub.add_parser("show", help="show one skill")
    p_show.add_argument("skill_id")
    p_show.set_defaults(func=_cmd_show)

    sub.add_parser("validate", help="validate the library").set_defaults(
        func=_cmd_validate
    )
    sub.add_parser("report", help="print a JSON conformance report").set_defaults(
        func=_cmd_report
    )

    p_scaffold = sub.add_parser("scaffold", help="scaffold a planned skill on disk")
    p_scaffold.add_argument("skill_id")
    p_scaffold.add_argument(
        "--overwrite",
        action="store_true",
        help="replace an existing scaffold for the same skill id",
    )
    p_scaffold.set_defaults(func=_cmd_scaffold)

    p_author = sub.add_parser(
        "author", help="render a full skill from a JSON or YAML definition"
    )
    p_author.add_argument("definition", help="path to the JSON or YAML definition file")
    p_author.set_defaults(func=_cmd_author)

    p_batch = sub.add_parser(
        "author-batch", help="render every _def.json under skills/ and promote them"
    )
    p_batch.add_argument(
        "--keep-defs",
        action="store_true",
        help="do not delete _def.json after rendering",
    )
    p_batch.set_defaults(func=_cmd_author_batch)

    p_route = sub.add_parser("route", help="rank skills matching a free-text need")
    p_route.add_argument("query")
    p_route.add_argument("--limit", type=int, default=5)
    p_route.set_defaults(func=_cmd_route)

    sub.add_parser("stats", help="library statistics (JSON)").set_defaults(
        func=_cmd_stats
    )
    sub.add_parser("groups", help="list groups with counts").set_defaults(
        func=_cmd_groups
    )
    p_catalogue = sub.add_parser("catalogue", help="print the full catalogue")
    p_catalogue.add_argument(
        "--markdown",
        action="store_true",
        help="emit Markdown (the only currently supported catalogue format)",
    )
    p_catalogue.add_argument(
        "--output",
        type=Path,
        help="write the generated catalogue to a file instead of stdout",
    )
    p_catalogue.set_defaults(func=_cmd_catalogue)
    sub.add_parser("doctor", help="validate + quality-lint the library").set_defaults(
        func=_cmd_doctor
    )
    p_defs = sub.add_parser(
        "definitions",
        help="generate or check canonical skill definitions and rendered skills",
    )
    defs_mode = p_defs.add_mutually_exclusive_group(required=True)
    defs_mode.add_argument(
        "--write",
        action="store_true",
        help="write canonical definitions and render definition-owned skills",
    )
    defs_mode.add_argument(
        "--check",
        action="store_true",
        help="fail if canonical definitions or rendered skills are missing or stale",
    )
    p_defs.set_defaults(func=_cmd_definitions)
    p_scenarios = sub.add_parser(
        "scenarios",
        help="check deterministic defensive scenario-readiness fixtures",
    )
    scenario_mode = p_scenarios.add_mutually_exclusive_group(required=True)
    scenario_mode.add_argument(
        "--check",
        action="store_true",
        help="fail if defensive scenario fixtures or referenced skills are stale",
    )
    p_scenarios.set_defaults(func=_cmd_scenarios)
    p_dashboard = sub.add_parser(
        "dashboard",
        help="generate or check the quality dashboard",
    )
    dashboard_mode = p_dashboard.add_mutually_exclusive_group(required=True)
    dashboard_mode.add_argument(
        "--write",
        action="store_true",
        help="write generated quality dashboard Markdown, HTML, and JSON",
    )
    dashboard_mode.add_argument(
        "--check",
        action="store_true",
        help="fail if generated quality dashboard files are missing or stale",
    )
    p_dashboard.set_defaults(func=_cmd_dashboard)
    p_examples = sub.add_parser(
        "examples",
        help="generate or check deterministic worked skill examples",
    )
    examples_mode = p_examples.add_mutually_exclusive_group(required=True)
    examples_mode.add_argument(
        "--write",
        action="store_true",
        help="write generated worked-example Markdown and JSON",
    )
    examples_mode.add_argument(
        "--check",
        action="store_true",
        help="fail if worked examples or generated example outputs are stale",
    )
    p_examples.set_defaults(func=_cmd_examples)
    p_evals = sub.add_parser(
        "evals",
        help="generate or check offline local output-evaluation fixtures",
    )
    evals_mode = p_evals.add_mutually_exclusive_group(required=True)
    evals_mode.add_argument(
        "--write",
        action="store_true",
        help="write offline eval source, Markdown, and JSON",
    )
    evals_mode.add_argument(
        "--check",
        action="store_true",
        help="fail if offline eval fixtures or generated outputs are stale",
    )
    p_evals.set_defaults(func=_cmd_evals)
    p_assets = sub.add_parser(
        "manuscript-assets",
        help="generate or check manuscript supplements and figures",
    )
    assets_mode = p_assets.add_mutually_exclusive_group(required=True)
    assets_mode.add_argument(
        "--write",
        action="store_true",
        help="write generated supplements, data exports, and figures",
    )
    assets_mode.add_argument(
        "--check",
        action="store_true",
        help="fail if generated manuscript assets are missing or stale",
    )
    p_assets.set_defaults(func=_cmd_manuscript_assets)
    p_release = sub.add_parser(
        "release-metadata",
        help="generate or check release metadata and claim matrix outputs",
    )
    release_mode = p_release.add_mutually_exclusive_group(required=True)
    release_mode.add_argument(
        "--write",
        action="store_true",
        help="write generated release metadata Markdown and JSON",
    )
    release_mode.add_argument(
        "--check",
        action="store_true",
        help="fail if release metadata outputs are stale or inconsistent",
    )
    p_release.add_argument(
        "--mode",
        choices=("local", "release-candidate", "public-archive"),
        default="local",
        help="strictness level for git/archive metadata checks",
    )
    p_release.set_defaults(func=_cmd_release_metadata)
    sub.add_parser("export", help="dump all on-disk skills as JSON").set_defaults(
        func=_cmd_export
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))
