# Live Evaluation

`eval-live` runs the curated defensive scenario fixtures through a real agent
harness and mechanically screens each returned transcript against the
scenario's expected-answer contract. It is the live-runtime counterpart of the
deterministic `evals` fixtures: the same scenarios, the same rubric
dimensions, but a real model invocation instead of a reviewed local fixture.

## Claim boundary

A live report is **mechanical screening of one run**. It is exploratory
evidence — not a benchmark, not field validation, and not a comparison against
unstructured prompting unless that comparison is externally reviewed (the
rubric itself lives in [`analyst-output-review.md`](analyst-output-review.md);
study design in [`future-validation-protocols.md`](future-validation-protocols.md)).
Auto-assigned rubric scores are heuristic screening, not certified grades.

## Usage

```bash
# One scenario through the default Claude Code template
uv run cogsecskills eval-live --harness claude --scenario sat-ach-safe

# All 28 scenarios, JSON report, routed mode (tests routing too)
uv run cogsecskills eval-live --harness claude --mode routed --json
```

Exit codes: `0` every scenario passed mechanical screening; `1` a scenario
failed or preflight rejected the runtime configuration; `2` argparse rejected
command-line syntax. Preflight validates a positive integer timeout, safe
harness and scenario identifiers, unique selection, available executable, and
command-template placeholders before invoking a harness. Pinned mode validates
each selected skill's entry point, workflow, configured adapters, and structural
contract before creating run outputs. It prepares every pinned prompt before starting the first selected scenario,
so a missing later skill cannot cause a partly billed run.

## Modes

- `pinned` (default): the prompt names the expected skill's on-disk directory;
  the run tests how well the skill executes the scenario.
- `routed`: the prompt asks the harness to route the query itself (e.g. via
  `cogsecskills route`) and then follow the chosen skill; the run additionally
  exercises routing.

## Configuring harness commands

Each harness is an argv template with exactly one `{prompt}` placeholder. The
runner executes the argument vector directly, with the resolved library root
as its working directory. It does not invoke a shell for the template; shell
syntax is literal unless you explicitly configure a shell executable.
Built-in defaults exist for `claude`, `codex`, and `hermes`; override or add
harnesses in `cogsecskills.yaml`:

```yaml
runtime_eval:
  harness_commands:
    claude: [claude, -p, "{prompt}"]
    my-agent: [/usr/local/bin/my-agent, --skill, "{skill_dir}", --task, "{prompt}"]
```

`{skill_dir}` (optional) expands to the expected skill's directory in pinned
mode; it is rejected in routed mode because it would reveal the expected
selection. The executable itself cannot contain either placeholder. The gate
suite never invokes a model runtime: `eval-live` is opt-in,
local, and writes nothing inside CI.

## Outputs

Transcripts and the YAML report are written under `.live-evals/<timestamp>-<unique-suffix>/`
(gitignored — transcripts are run artifacts, not deliverables):

- `<harness>/<scenario-id>.txt` — raw stdout, when nonempty;
- `<harness>/<scenario-id>.stderr.txt` — separate stderr diagnostics, when nonempty;
- `report_<harness>.yaml` — the full machine-readable report (also printed as
  JSON with `--json`).

An explicit `--output-dir` must have unused report and transcript filenames;
existing artifacts cause preflight to fail. Transcript, stderr, and report
receipts use exclusive creation, reject symlink escapes, and recheck their
output boundary after the harness returns. These checks protect local evidence
persistence; they do not sandbox the configured harness. Only stdout is
screened as the answer. Stderr remains diagnostic evidence, and an exact echoed prompt is
removed from the scoring view while remaining in the raw stdout file. This
prevents prompt or diagnostic text from satisfying answer checks.

`--timeout` bounds each harness invocation (default 300 seconds). POSIX
runs start a separate process group and terminate any remaining ordinary
descendants after direct-child completion or timeout. The direct child is
reaped; Windows currently cleans up the direct child on timeout only. Retained stdout and stderr are capped at
4 MiB each, and oversized output fails screening. The file-backed spool during
execution is not a disk-quota guarantee.

Each report carries the claim boundary and, per scenario: deterministic checks
(skill named, quality terms, output terms, required sections, must-include
terms, no forbidden terms, harness exit code), the mechanical rubric
screening, the harness exit code, transcript path, and stderr path.
Transcripts may contain model output — review them before quoting anywhere.
