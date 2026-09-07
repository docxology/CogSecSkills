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

Exit codes: `0` every scenario passed mechanical screening, `1` at least one
failed, `2` configuration error (unknown scenario, no command template, or the
harness executable is not on PATH). The runner fails closed before any
invocation in the exit-2 cases — a missing harness never produces a partial
report.

## Modes

- `pinned` (default): the prompt names the expected skill's on-disk directory;
  the run tests how well the skill executes the scenario.
- `routed`: the prompt asks the harness to route the query itself (e.g. via
  `cogsecskills route`) and then follow the chosen skill; the run additionally
  exercises routing.

## Configuring harness commands

Each harness is an argv template with exactly one `{prompt}` placeholder.
Built-in defaults exist for `claude`, `codex`, and `hermes`; override or add
harnesses in `cogsecskills.yaml`:

```yaml
runtime_eval:
  harness_commands:
    claude: [claude, -p, "{prompt}"]
    my-agent: [/usr/local/bin/my-agent, --skill, "{skill_dir}", --task, "{prompt}"]
```

`{skill_dir}` (optional) expands to the expected skill's directory in pinned
mode. The gate suite never invokes a model runtime: `eval-live` is opt-in,
local, and writes nothing inside CI.

## Outputs

Transcripts and the YAML report are written under `.live-evals/<timestamp>/`
(gitignored — transcripts are run artifacts, not deliverables):

- `<harness>/<scenario-id>.txt` — the raw model transcript;
- `report_<harness>.yaml` — the full machine-readable report (also printed as
  JSON with `--json`).

Each report carries the claim boundary and, per scenario: deterministic checks
(skill named, quality terms, output terms, required sections, must-include
terms, no forbidden terms, harness exit code), the mechanical rubric
screening, the harness exit code, and the transcript path. Transcripts may
contain model output — review them before quoting anywhere.
