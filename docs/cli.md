# CogSecSkills CLI Reference

The `cogsecskills` command-line interface is a thin orchestrator over the
library API. It catalogues, validates, routes, scaffolds, authors, reports on,
and generates manuscript assets from the skill library. All business logic lives
in the sibling modules
(`insights.py`, `validate.py`, `author.py`, `scaffold.py`, `registry.py`,
`config.py`, `definitions.py`, `scenarios.py`, `examples.py`, `dashboard.py`,
`manuscript_assets.py`); the CLI only parses arguments, calls them, and prints
results.

## Invocation

The CLI is exposed as a Python module and (after install) as a console script:

```bash
# As a module (no install required; run from the project root)
python -m cogsecskills <command> [options]

# After install (pip install -e . / uv sync)
cogsecskills <command> [options]
```

This reference uses `cogsecskills <command>` throughout; substitute
`python -m cogsecskills <command>` if you have not installed the console script.

### Global options

| Option | Applies to | Meaning |
| --- | --- | --- |
| `--root PATH` | every subcommand | Project-root override. Points the CLI at a different CogSecSkills tree (registry, `skills/`, and `cogsecskills.yaml`) than the installed package's own root. Defaults to the package's project root. |

`--root` is parsed on the top-level parser, so it must appear **before** the
subcommand:

```bash
cogsecskills --root /path/to/library list
```

A subcommand is required; running `cogsecskills` with no command is an error.

### Exit codes

| Code | Meaning |
| --- | --- |
| `0` | Success (or, for `validate`, zero errors). |
| `1` | Command-specific failure: `validate`/`doctor` found errors (and `doctor` also fails on quality findings), `route` found no matching skill, `show` got an unknown id, `definitions --check`, `scenarios --check`, `examples --check`, `dashboard --check`, or `manuscript-assets --check` found drift, or `author-batch` had at least one failed definition. |

### Config awareness

`validate`, `doctor`, `scaffold`, `author`, `author-batch`, and `definitions`
load `cogsecskills.yaml` (via `cogsecskills.config.load_config`) and honour its
`harnesses` list and `quality` thresholds. With no config file the defaults are
used: harnesses `claude, codex, hermes`, `min_workflow_steps: 3`,
`min_anti_criteria: 2`, `require_references: false`. See
[configuration.md](configuration.md).

---

## Commands

### `list` — catalogued skill areas and status counts

List the skill areas in the registry, optionally filtered by group or status,
with a trailing summary line of status counts.

```
cogsecskills list [--group G] [--status S] [--limit N] [--format text|json]
```

| Argument / flag | Meaning |
| --- | --- |
| `--group G` | Show only skills whose group is `G` (e.g. `sat`, `cognitive_security`). |
| `--status S` | Show only skills whose status is `S` (`implemented`, `stub`, or `planned`). |
| `--limit N` | Cap the number of results after filtering. |
| `--format text` | (default) Human-readable rows. |
| `--format json` | Machine-readable JSON payload with `count`, `total`, `status_counts`, and a `skills` array. |

Each row is `status  id  name`. The summary shows how many rows passed the
filter out of the registry total, plus the status counts across the **whole**
registry.

```bash
cogsecskills list --group sat
```

```
implemented  sat.getting_started_checklist                     Getting Started Checklist
implemented  sat.customer_aims_checklist                       Customer (AIMS) Checklist
implemented  sat.issue_redefinition                            Issue Redefinition
...
34 of 100 skill areas (implemented=100, stub=0, planned=0)
```

---

### `show` — show one skill

Print a single skill as JSON. If the skill is built on disk, the on-disk spec is
shown; otherwise the registry entry is shown with a note that it has not been
built yet.

```
cogsecskills show <skill-id>
```

| Argument | Meaning |
| --- | --- |
| `skill-id` | The fully-qualified skill id, `<group>.<slug>` (e.g. `sat.sorting`). |

The on-disk view includes `id`, `name`, `group`, `status`, `version`,
`summary`, `tags`, `triggers`, `verbs`, `inputs`, `outputs`, and the `harness`
adapter map. An unknown id prints `unknown skill id: <id>` and exits `1`.

```bash
cogsecskills show sat.sorting
```

```json
{
  "id": "sat.sorting",
  "name": "Sorting",
  "group": "sat",
  "status": "implemented",
  "version": "0.1.0",
  "summary": "Group large evidence sets by attributes to surface patterns and outliers.",
  "tags": ["cognitive-security", "sat", "pattern-recognition"],
  "triggers": ["sort this evidence", "organize these indicators", "..."],
  "verbs": ["read", "reason", "write"],
  "inputs": ["evidence_set", "sort_dimensions"],
  "outputs": ["..."],
  "harness": {"claude": "harness/claude.md", "codex": "harness/codex.md", "hermes": "harness/hermes.md"}
}
```

For a registry-only (not-yet-built) skill the output is the registry entry
followed by `(status=...: not yet built on disk)`.

---

### `validate` — validate the whole library

Run every validation gate over the on-disk skills and the registry. Zero errors
means the library is conforming. The command is config-aware: it uses the
harness set from `cogsecskills.yaml`, so a custom harness list adds adapter
requirements automatically.

```
cogsecskills validate
```

Validation covers: per-skill structural completeness (every spec-declared
companion file present, adapters binding every declared verb), multiharness
conformance, and library/registry coherence (every on-disk skill catalogued;
every `implemented` registry row present on disk). See
[skill-contract.md](skill-contract.md) for the full contract.

Each issue is printed as `SEVERITY  skill_id  message`, followed by an error /
warning tally. **Exit `1` if there are any errors**, `0` otherwise (warnings do
not fail the gate).

```bash
cogsecskills validate
```

```
0 error(s), 0 warning(s)
```

---

### `report` — JSON conformance report

Print a machine-readable conformance summary. Unlike `validate`, this command
always exits `0`; consume the JSON `ok` / `errors` fields programmatically.

```
cogsecskills report
```

The report fields are `registry_total`, `registry_status_counts`,
`on_disk_skills`, `errors`, `warnings`, and `ok`.

```bash
cogsecskills report
```

```json
{
  "registry_total": 100,
  "registry_status_counts": {
    "implemented": 100,
    "stub": 0,
    "planned": 0
  },
  "on_disk_skills": 100,
  "errors": 0,
  "warnings": 0,
  "ok": true
}
```

---

### `scaffold` — generate a conforming stub skill

Generate a conforming on-disk skill folder for a registry id. It reads the
registry entry and writes the multiharness file set (`skill.yaml`, `SKILL.md`,
`workflow.md`, and one `harness/<name>.md` adapter per configured harness),
pre-populated from the catalogue row with status `stub`. The structure conforms
immediately; the author then deepens the content.

```
cogsecskills scaffold <skill-id> [--overwrite]
```

| Argument / flag | Meaning |
| --- | --- |
| `skill-id` | A registry id, `<group>.<slug>`. Must already exist in the registry. |
| `--overwrite` | Replace an existing scaffold for the same id (removes the folder, then re-creates it — a clean replace, never a merge). Without this flag, an existing directory is an error. |

Prints the count and the list of files written.

```bash
cogsecskills scaffold sat.example_technique
```

```
scaffolded 6 files for sat.example_technique:
  .../skills/sat/example_technique/skill.yaml
  .../skills/sat/example_technique/SKILL.md
  .../skills/sat/example_technique/workflow.md
  .../skills/sat/example_technique/harness/claude.md
  .../skills/sat/example_technique/harness/codex.md
  .../skills/sat/example_technique/harness/hermes.md
```

---

### `author` — render a full skill from a JSON or YAML definition

Render a complete, deep skill from a structured JSON or YAML definition. Where
`scaffold` produces a stub from the catalogue row, `author` consumes a
definition that supplies the real substance (tool plan, inputs/outputs,
step-by-step procedure, anti-criteria, and quality fields) and renders all
conforming files with status `implemented`. Adapters bind exactly the declared
verbs, so an authored skill passes the validator by construction.

```
cogsecskills author <definition.json|definition.yaml>
```

| Argument | Meaning |
| --- | --- |
| `definition.json|definition.yaml` | Path to the JSON or YAML definition file. Its `id` must exist in the registry. |

The definition schema (required keys, optional sections, harness binding
overrides) is documented in [authoring-skills.md](authoring-skills.md). Prints a
one-line summary of how many files were written for which id.

```bash
cogsecskills author skills/sat/example_technique/_def.json
```

```
authored 6 files for sat.example_technique
```

---

### `author-batch` — render every definition and promote the registry

Find every `skills/**/_def.json` definition, render each into its conforming
skill folder, and promote those registry rows to `implemented`. The skill id for
each definition is inferred from its on-disk path (`<group>.<slug>`) when the
definition omits `id`. Rendered `_def.json` files are deleted by default.

```
cogsecskills author-batch [--keep-defs]
```

| Flag | Meaning |
| --- | --- |
| `--keep-defs` | Do not delete the `_def.json` files after rendering them. |

Prints a count of rendered and failed skills, with a `FAIL <id>: <error>` line
for each failure. **Exit `1` if any definition failed**, `0` otherwise.

```bash
cogsecskills author-batch
```

```
rendered 3 skills; 0 failed
```

---

### `definitions` — write or check the canonical all-skill definition layer

Render every canonical YAML definition under `definitions/<group>/<slug>.yaml`
into the harness-facing `skills/` tree, or fail if definitions or rendered
files have drifted. This is the preferred repo-wide source-of-truth command for
all 100 implemented skills.

```
cogsecskills definitions (--write | --check)
```

| Flag | Meaning |
| --- | --- |
| `--write` | Write canonical YAML definitions when missing and render every definition-owned skill file. |
| `--check` | Fail if any registry entry lacks a definition, a definition has schema drift, or a rendered skill file differs from the definition output. |

```bash
cogsecskills definitions --write
cogsecskills definitions --check
```

```
wrote canonical definitions: 100 definitions, 100 rendered skills
canonical definitions are current
```

---

### `scenarios` — check deterministic defensive-readiness fixtures

Check the curated repository-local scenario fixtures under
`scenarios/defensive_readiness.yaml`. The gate validates that each fixture routes
to the expected implemented skill, names a safe defensive or unsafe redirect
case, references declared output terms, declares an expected defensive response
shape, carries a reviewed local expected-answer fixture, and points at skills
with the required quality, evidence, uncertainty, and refusal/redirect metadata.

```
cogsecskills scenarios --check
```

| Flag | Meaning |
| --- | --- |
| `--check` | Fail if scenario fixtures are missing, stale, unsafe in wording, poorly covered by group/kind, missing expected-response or expected-answer terms, or no longer match the referenced skill contract. |

```bash
cogsecskills scenarios --check
```

```
scenario readiness fixtures are current: 28 scenarios across 7 groups; 28 expected answers checked
```

This is a deterministic repository gate. It does not call Claude, Codex,
Hermes, custom harness runtimes, browsers, OSINT connectors, or live APIs; it
only checks that the local source surfaces can support bounded defensive
scenario use and describe the expected answer shape.

---

### `examples` — generate or check deterministic worked examples

Generate Markdown and JSON worked-example views from the source-owned
`examples/skill-worked-examples.yaml` file. The source file contains one
reviewed local fixture per skill. The generated outputs are deterministic
examples, not live model transcripts or runtime certification.

```
cogsecskills examples (--write | --check)
```

| Flag | Meaning |
| --- | --- |
| `--write` | Write `docs/skill-worked-examples.md` and `output/data/skill_worked_examples.json`. |
| `--check` | Fail if source examples are missing, unsafe, incomplete, mismatched to the registry, or generated outputs are missing or stale. |

```bash
cogsecskills examples --write
cogsecskills examples --check
```

```
wrote worked examples: 100 examples, docs/skill-worked-examples.md, output/data/skill_worked_examples.json
worked examples are current
```

---

### `evals` — generate or check offline output-review fixtures

Generate scenario-linked offline review fixtures and a Markdown/JSON report
from the deterministic scenario expected answers. These fixtures use the
analyst-output review rubric; they are not live model outputs or benchmark
results.

```
cogsecskills evals (--write | --check)
```

| Flag | Meaning |
| --- | --- |
| `--write` | Write `evals/local_output_review.yaml`, `docs/evaluation-readiness.md`, and `output/data/evaluation_readiness.json`. |
| `--check` | Fail if offline review fixtures are missing, stale, below the passing rubric score, unsafe, mismatched to scenarios, or generated outputs are missing or stale. |

```bash
cogsecskills evals --write
cogsecskills evals --check
```

```
wrote offline eval fixtures: 28 evaluations, evals/local_output_review.yaml, docs/evaluation-readiness.md, output/data/evaluation_readiness.json
offline evaluation fixtures are current
```

---

### `dashboard` — generate or check the quality dashboard

Generate a Markdown and JSON dashboard from the live registry, rendered skill
specs, canonical quality capsules, scenario fixtures, offline review fixtures,
worked examples, and current TODO verified state. The dashboard is a navigation
and drift surface, not evidence of field effectiveness.

```
cogsecskills dashboard (--write | --check)
```

| Flag | Meaning |
| --- | --- |
| `--write` | Write `docs/quality-dashboard.md`, `docs/quality-dashboard.html`, and `output/data/quality_dashboard.json`. |
| `--check` | Fail if the generated dashboard files are missing, stale, missing 100-skill coverage, missing scenario coverage, missing worked-example coverage, missing quality capsules, or missing verified-state rows. |

```bash
cogsecskills dashboard --write
cogsecskills dashboard --check
```

```
wrote quality dashboard: 100 skills, 28 scenarios, 100 worked examples, docs/quality-dashboard.md, docs/quality-dashboard.html, output/data/quality_dashboard.json
quality dashboard is current
```

The dashboard rows include skill id, group, neutral verbs, configured harnesses,
reference count, quality-capsule presence, scenario coverage, offline-eval
coverage, worked-example coverage, local claim-boundary status, and source paths.

---

### `release-metadata` — generate or check release claim metadata

Generate a local release claim matrix and JSON metadata snapshot. Default
`local` mode reports dirty git state truthfully without failing; stricter modes
can be used before public archive work.
Exact git revision, branch, and dirty-state values are runtime observations,
not drift-checked committed values.

```
cogsecskills release-metadata (--write | --check) [--mode local|release-candidate|public-archive]
```

| Flag | Meaning |
| --- | --- |
| `--write` | Write `docs/release-claim-matrix.md` and `output/data/release_metadata.json`. |
| `--check` | Fail if metadata is inconsistent or generated release metadata outputs are missing or stale. |
| `--mode` | Select local, release-candidate, or public-archive strictness. |

```bash
cogsecskills release-metadata --write
cogsecskills release-metadata --check
```

```
wrote release metadata: mode=local, docs/release-claim-matrix.md, output/data/release_metadata.json; runtime git=<revision>, dirty=<true|false>
release metadata is current (local mode)
```

---

### `route` — rank skills matching a free-text need

The intelligent router. Given a free-text description of an analytic need, rank
the on-disk skills that best fit it. Scoring is weighted token overlap across
each skill's name, triggers, tags, summary, and group (name and triggers count
most). Only skills with a positive score are returned.

```
cogsecskills route <query> [--limit N] [--format text|json]
```

| Argument / flag | Meaning |
| --- | --- |
| `query` | The free-text need (quote it if it contains spaces). |
| `--limit N` | Maximum number of matches to return. Default `5`. |
| `--format text` | (default) Human-readable `[score] id  name` rows. |
| `--format json` | Machine-readable JSON payload with `query`, `count`, and `matches` array. In JSON mode, no matches returns `{"matches": [], "count": 0}` and exit `0` (not `1`). |

Each match is printed as `[score] id  name`, highest score first. **If nothing
matches, prints `no skill matches: <query>` and exits `1`.**

```bash
cogsecskills route "detect manipulation in a message"
```

```
skills matching 'detect manipulation in a message':
  [ 20] cognitive_security.manipulation_technique_identification  Manipulation Technique Identification
  [ 11] cognitive_security.emotional_manipulation_analysis  Emotional Manipulation Analysis
  [ 11] cognitive_security.framing_and_priming_analysis   Framing & Priming Analysis
  [ 11] sat.team_a_team_b                                 Team A / Team B
  [ 10] cognitive_security.logical_fallacy_detection      Logical Fallacy Detection
```

---

### `stats` — library statistics (JSON)

Print library statistics as JSON: totals, counts by status, by group, by tool
verb, and AGEINT topic coverage.

```
cogsecskills stats
```

Fields: `registry_total`, `on_disk`, `by_status`, `by_group`, `verb_usage`
(sorted by frequency), `ageint_topics`, and `groups_defined`.

```bash
cogsecskills stats
```

```json
{
  "registry_total": 100,
  "on_disk": 100,
  "by_status": {"implemented": 100, "stub": 0, "planned": 0},
  "by_group": {"cognitive_security": 24, "...": 0, "sat": 34},
  "verb_usage": {"read": 100, "reason": 100, "write": 100, "search": 26, "web": 12, "ask": 7, "exec": 5},
  "ageint_topics": {"cognitive-security": 24, "...": 0, "structured-analytic-techniques": 34},
  "groups_defined": 7
}
```

---

### `groups` — list groups with counts and titles

List every group with its skill count and human-readable title. Each row is
`group_id  count  title`.

```
cogsecskills groups [--format text|json]
```

| Argument / flag | Meaning |
| --- | --- |
| `--format text` | (default) Human-readable rows. |
| `--format json` | Machine-readable JSON array of `{id, title, count}` objects. |

```bash
cogsecskills groups
```

```
cognitive_security         24  Cognitive Security
counterintelligence         8  Counterintelligence & Deception Detection
critical_review            12  Critical Review & Assurance
information_environment     7  Information Environment & Influence Analysis
osint_integrity            10  OSINT & Source Integrity
research_methods            5  Research & Synthesis Methods
sat                        34  Structured Analytic Techniques
```

---

### `catalogue` — print the full catalogue as Markdown

Render the entire catalogue as a grouped, navigable Markdown index, generated
from the registry. This is how [catalogue.md](catalogue.md) is produced. By
default the Markdown is printed to stdout; `--output` writes it to a file
instead (with a trailing newline) and prints `wrote <path>`.

```
cogsecskills catalogue [--markdown] [--output PATH]
```

| Flag | Meaning |
| --- | --- |
| `--markdown` | Emit Markdown (the only currently supported catalogue format). |
| `--output PATH` | Write the generated catalogue to `PATH` instead of stdout. |

```bash
# Regenerate the catalogue doc
cogsecskills catalogue --markdown --output docs/catalogue.md
```

```
wrote docs/catalogue.md
```

The generated document is grouped by area, with a status-count header and one
table per group linking each skill to its `SKILL.md`. It carries a "do not edit
by hand — regenerate after changing the registry" banner.

---

### `manuscript-assets` — generate or check manuscript supplements and figures

Generate source-owned manuscript supplements and visualizations from the live
registry plus on-disk skill specs. This command owns the generated supplemental
sections and figure files used by the manuscript.

```
cogsecskills manuscript-assets (--write | --check)
```

| Flag | Meaning |
| --- | --- |
| `--write` | Write generated supplements, data exports, and PNG figures. |
| `--check` | Fail if generated Markdown/data files are missing or stale, or if expected PNG figures are missing/invalid. |

`--write` updates:

- `manuscript/S10_skill_catalogue.md`
- `manuscript/S11_skill_metadata_matrix.md`
- `output/data/skill_catalogue.json`
- `output/data/skill_catalogue.csv`
- `output/figures/cogsecskills_taxonomy_counts.png`
- `output/figures/cogsecskills_skill_grid.png`
- `output/figures/cogsecskills_verb_heatmap.png`
- `output/figures/cogsecskills_ageint_network.png`
- `output/figures/cogsecskills_plan_build_teach_flow.png`
- `output/figures/cogsecskills_reference_density.png`
- `output/figures/cogsecskills_harness_contract.png`
- `output/figures/cogsecskills_cover_installation.png`
- `figures/cogsecskills_cover_installation.png` (title-page cover mirror)

```bash
cogsecskills manuscript-assets --write
cogsecskills manuscript-assets --check
```

```
wrote manuscript assets: 2 markdown, 2 data, 8 figures for 100 skills
manuscript assets are current
```

The `output/` files are rebuild artifacts; the generated supplemental Markdown
under `manuscript/` is committed source input for the renderer and carries a
"do not edit by hand" header.

---

### `doctor` — validate plus quality lint

Run full validation **and** a quality lint, in one pass. Validation covers
structural conformance (same gates as `validate`); the quality lint flags
*thin* or *under-referenced* implemented skills against the thresholds in
`cogsecskills.yaml` (`min_workflow_steps`, `min_anti_criteria`,
`require_references`). Use it as the health check before publishing.

```
cogsecskills doctor
```

Validation issues are printed as `SEVERITY  skill_id  message`; quality findings
as `LEVEL  skill_id  message`. The trailing line tallies validation errors and
quality findings. **Exit `1` if there are validation errors OR any quality
findings**, `0` only when both are clean.

```bash
cogsecskills doctor
```

```
validation: 0 error(s); quality: 0 finding(s)
```

---

### `export` — dump all on-disk skills as JSON

Dump every on-disk skill as a single JSON object — the same per-skill shape as
`show`, wrapped in `{"skills": [...], "count": N}`. Useful for feeding the whole
library into other tooling.

```
cogsecskills export
```

```bash
cogsecskills export > skills.json
```

```json
{
  "skills": [
    {"id": "cognitive_security....", "name": "...", "verbs": ["read", "reason", "write"], "...": "..."}
  ],
  "count": 100
}
```

---

## Common workflows

**Add a new skill (from registry to deep, conforming files).**

```bash
# Option A — scaffold a stub, then deepen it by hand
cogsecskills scaffold <group>.<slug>
# ...edit the generated files...
cogsecskills validate

# Option B — author from a JSON/YAML definition (see authoring-skills.md)
cogsecskills author definitions/<group>/<slug>.yaml
cogsecskills validate

# Option C — update canonical definitions and render the whole library
cogsecskills definitions --write
cogsecskills definitions --check
```

**Find the right skill for a need.**

```bash
cogsecskills route "verify a viral claim before sharing it" --limit 10
cogsecskills show <id>   # inspect the top match
```

**Check health before publishing.**

```bash
cogsecskills doctor        # validation + quality lint; exit 1 on any problem
cogsecskills scenarios --check
cogsecskills examples --check
cogsecskills dashboard --check
cogsecskills report        # machine-readable conformance snapshot
cogsecskills manuscript-assets --check
```

**Regenerate the catalogue doc after editing the registry.**

```bash
cogsecskills catalogue --markdown --output docs/catalogue.md
```

**Regenerate manuscript supplements and figures after editing registry/skills.**

```bash
cogsecskills manuscript-assets --write
cogsecskills manuscript-assets --check
```

**Survey the library.**

```bash
cogsecskills groups        # groups, counts, titles
cogsecskills stats         # counts by status / group / verb, AGEINT topics
cogsecskills list --status implemented
```

---

## See also

- [architecture.md](architecture.md) — how the registry, specs, harness
  adapters, and CLI fit together.
- [authoring-skills.md](authoring-skills.md) — the canonical YAML definition
  format consumed by `definitions --write` and `author`.
- [configuration.md](configuration.md) — `cogsecskills.yaml` harness set and
  `doctor` quality thresholds.
- [skill-contract.md](skill-contract.md) — the validation contract enforced by
  `validate` and `doctor`.
- [catalogue.md](catalogue.md) — the generated catalogue (`catalogue --markdown`).
