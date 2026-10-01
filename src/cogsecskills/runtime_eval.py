"""Live-runtime evaluation harness.

Invokes a real agent harness (Claude Code, Codex, Hermes, or any configured
CLI) against the curated defensive scenario fixtures and mechanically screens
the returned transcript against the scenario's expected-answer contract.

Claim boundary: a live report is **mechanical screening of one run**. It is
exploratory evidence — not a benchmark, not field validation, and not a
comparison against unstructured prompting unless that comparison is externally
reviewed (see ``docs/live-eval.md`` and ``docs/claim-boundaries.md``).

The harness is invoked as a real subprocess; nothing here calls a model API
directly, and the default gates never invoke a live harness.
"""

from __future__ import annotations

import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from cogsecskills.artifacts.scenarios import (
    RUBRIC_KEYS,
    Scenario,
    load_scenarios,
)
from cogsecskills.core.config import load_config
from cogsecskills.core.loader import load_skill, skills_root
from cogsecskills.core.locate import resolve_root
from cogsecskills.core.paths import contained_path, validate_component
from cogsecskills.runtime.models import LiveCheck, LiveEvalReport, LiveScenarioResult
from cogsecskills.runtime.process import run_process
from cogsecskills.runtime.reporting import (
    format_report,
    parse_live_eval_yaml,
    write_report,
    write_text_exclusive,
)
from cogsecskills.runtime.screening import score_transcript
from cogsecskills.quality.validate import validate_skill

LIVE_EVALS_DIRNAME = ".live-evals"

LIVE_CLAIM_BOUNDARY = (
    "mechanical screening of one live run; exploratory; not a benchmark, "
    "not field validation; comparisons against unstructured prompting are "
    "exploratory unless externally reviewed"
)

#: Default argv templates. ``{prompt}`` is required exactly once; ``{skill_dir}``
#: is optional and only substituted in pinned mode. Defaults assume the harness
#: CLI accepts the prompt as an argument — override per harness in
#: ``cogsecskills.yaml`` (``runtime_eval.harness_commands``) when it does not.
DEFAULT_HARNESS_COMMANDS: dict[str, tuple[str, ...]] = {
    "claude": ("claude", "-p", "{prompt}"),
    "codex": ("codex", "exec", "{prompt}"),
    "hermes": ("hermes", "run", "{prompt}"),
}

MODES = ("pinned", "routed")


def harness_commands(harness: str, root: Path | None = None) -> tuple[str, ...]:
    """Resolve the argv template for ``harness``.

    Order: ``cogsecskills.yaml`` (``runtime_eval.harness_commands``) overrides
    the built-in defaults. A harness with no template anywhere is a hard
    configuration error — the runner must not guess an invocation.
    """
    config = load_config(root)
    configured = config.runtime_eval_commands.get(harness)
    if configured:
        return configured
    default = DEFAULT_HARNESS_COMMANDS.get(harness)
    if default:
        return default
    raise ValueError(
        f"no command template for harness {harness!r}: add "
        f"runtime_eval.harness_commands.{harness} to cogsecskills.yaml"
    )


def _validate_template(template: tuple[str, ...]) -> None:
    if (
        not isinstance(template, (tuple, list))
        or not template
        or not all(
            isinstance(part, str) and part.strip() and "\0" not in part
            for part in template
        )
    ):
        raise ValueError("harness command template must be a non-empty argv sequence")
    joined = " ".join(template)
    if joined.count("{prompt}") != 1:
        raise ValueError(
            "harness command template must contain exactly one {prompt} "
            f"placeholder; got {template!r}"
        )
    if "{prompt}" in template[0] or "{skill_dir}" in template[0]:
        raise ValueError("harness executable cannot contain placeholders")


def _skill_directories(root: Path | None = None) -> dict[str, Path]:
    tree = skills_root(root)
    by_id: dict[str, Path] = {}
    if tree.is_dir():
        for spec_path in sorted(tree.rglob("skill.yaml")):
            contained_path(tree, spec_path.relative_to(tree))
            spec = load_skill(spec_path)
            if spec.id in by_id:
                raise ValueError(f"duplicate skill id on disk: {spec.id}")
            by_id[spec.id] = spec_path.resolve().parent
    return by_id


def build_prompt(scenario: Scenario, skill_dir: Path | None, mode: str) -> str:
    """Build the harness prompt for one scenario.

    The prompt carries only the scenario query and generic output-expectation
    instructions from the skill itself. Expected terms, sections, and answers
    are never included — that would leak the scoring key into the run.
    """
    if mode == "pinned":
        if skill_dir is None:
            raise ValueError(
                f"{scenario.id}: pinned mode requires the expected skill on disk"
            )
        intro = (
            "Follow the defensive skill stored at "
            f"{skill_dir} (SKILL.md and workflow.md) to answer the request below."
        )
    elif mode == "routed":
        intro = (
            "Choose the best defensive skill for the request below using the "
            "CogSecSkills library router (`cogsecskills route`), then follow "
            "that skill's SKILL.md and workflow.md to answer it."
        )
    else:
        raise ValueError(f"unknown mode {mode!r}; expected one of {MODES}")
    contract = (
        "In your answer: name the skill id you used; label evidence, "
        "inference, and gaps separately; state confidence and uncertainty "
        "explicitly; and refuse with a safe defensive redirect if the request "
        "is unsafe."
    )
    return f"{intro}\n\nRequest:\n{scenario.query}\n\n{contract}"


def run_live_eval(
    root: Path | None = None,
    *,
    harness: str,
    scenario_ids: tuple[str, ...] | None = None,
    mode: str = "pinned",
    timeout_seconds: int = 300,
    output_dir: Path | None = None,
    commands: dict[str, tuple[str, ...]] | None = None,
) -> LiveEvalReport:
    """Run the harness once per selected scenario and screen each transcript.

    Fails closed before any invocation when the harness has no command
    template or its executable is not on PATH, when a scenario id is unknown,
    or when ``mode``/the command template are malformed.
    """
    if mode not in MODES:
        raise ValueError(f"unknown mode {mode!r}; expected one of {MODES}")
    validate_component(harness, "harness name")
    if (
        isinstance(timeout_seconds, bool)
        or not isinstance(timeout_seconds, int)
        or timeout_seconds <= 0
    ):
        raise ValueError("timeout_seconds must be a positive integer")
    if commands is not None and harness in commands:
        template = commands[harness]
    else:
        template = harness_commands(harness, root)
    _validate_template(template)
    if mode == "routed" and any("{skill_dir}" in part for part in template):
        raise ValueError("{skill_dir} is only supported in pinned mode")

    base = resolve_root(root).resolve()
    scenarios = load_scenarios(base)
    by_id = {scenario.id: scenario for scenario in scenarios}
    if scenario_ids is None:
        selected = list(scenarios)
    else:
        unknown = [sid for sid in scenario_ids if sid not in by_id]
        if unknown:
            raise ValueError(f"unknown scenario id(s): {', '.join(unknown)}")
        selected = [by_id[sid] for sid in scenario_ids]
    if not selected:
        raise ValueError("no scenarios selected")
    if len({scenario.id for scenario in selected}) != len(selected):
        raise ValueError("scenario selection must not contain duplicate ids")
    for scenario in selected:
        validate_component(scenario.id, "scenario id")

    executable = shutil.which(template[0])
    if executable is None:
        raise RuntimeError(
            f"harness executable {template[0]!r} not found on PATH; install it "
            "or override runtime_eval.harness_commands in cogsecskills.yaml"
        )

    directories = _skill_directories(base)
    if mode == "pinned":
        configured_harnesses = load_config(base).harnesses
        for scenario in selected:
            skill_dir = directories.get(scenario.expected_skill)
            if skill_dir is not None:
                result = validate_skill(
                    load_skill(skill_dir / "skill.yaml"),
                    skill_dir,
                    harnesses=configured_harnesses,
                )
                if not result.ok:
                    raise ValueError(
                        f"{scenario.id}: selected skill is invalid: "
                        + "; ".join(issue.message for issue in result.errors)
                    )
    # Validate every prompt before starting a billed harness invocation.
    prompts = {
        scenario.id: build_prompt(
            scenario, directories.get(scenario.expected_skill), mode
        )
        for scenario in selected
    }
    if output_dir is None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        parent = base / LIVE_EVALS_DIRNAME
        parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        output_dir = Path(tempfile.mkdtemp(prefix=f"{stamp}-", dir=parent))
    output_dir = Path(output_dir).resolve()
    harness_dir = contained_path(output_dir, harness)
    report_path = contained_path(output_dir, f"report_{harness}.yaml")
    planned_paths = [report_path]
    for scenario in selected:
        planned_paths.extend(
            contained_path(output_dir, Path(harness) / f"{scenario.id}{suffix}")
            for suffix in (".txt", ".stderr.txt")
        )
    if any(path.exists() or path.is_symlink() for path in planned_paths):
        raise ValueError(
            "live-eval output already exists; choose a fresh output directory"
        )
    output_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    harness_dir.mkdir(mode=0o700, parents=True, exist_ok=True)

    results: list[LiveScenarioResult] = []
    for scenario in selected:
        skill_dir = directories.get(scenario.expected_skill)
        prompt = prompts[scenario.id]
        argv = [
            # {skill_dir} first: its value is repo-controlled, while the prompt
            # may legitimately contain placeholder-like text.
            part.replace("{skill_dir}", str(skill_dir) if skill_dir else "").replace(
                "{prompt}", prompt
            )
            for part in template
        ]
        argv[0] = executable
        completed = run_process(argv, cwd=base, timeout_seconds=timeout_seconds)
        transcript = completed.stdout
        returncode = completed.returncode

        checks: tuple[LiveCheck, ...]
        if completed.failure:
            checks = (
                LiveCheck(
                    name="harness completed",
                    passed=False,
                    detail=completed.failure,
                ),
            )
            auto_rubric = {key: 0 for key in RUBRIC_KEYS}
        else:
            # Raw logs retain the prompt; echoing it cannot supply scoring evidence.
            checks, auto_rubric = score_transcript(
                scenario, transcript.replace(prompt, "")
            )
            completion = LiveCheck(
                name="harness completed",
                passed=returncode == 0,
                detail=f"exit code {returncode}",
            )
            checks = (completion, *checks)
        ok = all(check.passed for check in checks)

        transcript_path: str | None = None
        if transcript:
            path = harness_dir / f"{scenario.id}.txt"
            write_text_exclusive(path, transcript, boundary=output_dir)
            transcript_path = str(path)
        stderr_path: str | None = None
        if completed.stderr:
            path = harness_dir / f"{scenario.id}.stderr.txt"
            write_text_exclusive(path, completed.stderr, boundary=output_dir)
            stderr_path = str(path)

        results.append(
            LiveScenarioResult(
                scenario_id=scenario.id,
                harness=harness,
                mode=mode,
                ok=ok,
                returncode=returncode,
                duration_seconds=completed.duration_seconds,
                checks=checks,
                auto_rubric=auto_rubric,
                transcript_path=transcript_path,
                stderr_path=stderr_path,
            )
        )

    report = LiveEvalReport(
        harness=harness,
        mode=mode,
        claim_boundary=LIVE_CLAIM_BOUNDARY,
        results=tuple(results),
        output_dir=str(output_dir),
    )
    write_report(report, report_path, boundary=output_dir)
    return report


__all__ = [
    "DEFAULT_HARNESS_COMMANDS",
    "LIVE_CLAIM_BOUNDARY",
    "LIVE_EVALS_DIRNAME",
    "MODES",
    "LiveCheck",
    "LiveEvalReport",
    "LiveScenarioResult",
    "build_prompt",
    "format_report",
    "harness_commands",
    "parse_live_eval_yaml",
    "run_live_eval",
    "score_transcript",
    "write_report",
]
