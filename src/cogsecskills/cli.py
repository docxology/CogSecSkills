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
    python -m cogsecskills scaffold <skill-id> [--root PATH]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .author import author_batch, render_definition
from .config import load_config
from .insights import (
    doctor,
    library_stats,
    render_catalogue_markdown,
    route_query,
)
from . import __version__
from .loader import discover_skills
from .registry import load_registry
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
    definition = json.loads(Path(args.json).read_text(encoding="utf-8"))
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
        "author", help="render a full skill from a JSON definition"
    )
    p_author.add_argument("json", help="path to the JSON definition file")
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
    sub.add_parser("export", help="dump all on-disk skills as JSON").set_defaults(
        func=_cmd_export
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))
