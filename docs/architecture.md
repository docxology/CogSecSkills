# Architecture

CogSecSkills is a mature, published library of 100 analytic skills —
Structured Analytic Techniques (`sat`), cognitive-security defenses
(`cognitive_security`), critical review (`critical_review`), OSINT integrity
(`osint_integrity`), counterintelligence (`counterintelligence`), the
information environment (`information_environment`), and research methods
(`research_methods`) — each authored once as a **harness-neutral skill** that
has default adapters for Claude Code, Codex, and Hermes and the same structural
contract for any additional configured harness. This document describes the
system design: the three coherent artifacts, the runner package, the
harness-neutral contract, and the deterministic definition-to-skill pipeline.

The single most important idea to hold while reading the rest of this document:
**substance flows in exactly one direction.** A human edits the canonical YAML
definition; the renderer turns that definition into the harness-facing skill
folder; a drift gate proves the folder still matches the definition. You never
hand-edit the rendered output and expect it to survive — the definition owns the
skill's substance, and everything downstream is regenerated from it. The
sections below trace that flow artifact by artifact and module by module.

> The deliverable is the skills system. The package under
> `src/cogsecskills/` is the small, fully-tested engine that discovers,
> parses, validates, authors, reports on, and generates manuscript assets from
> those skills. All logic lives in the package; the CLI and scripts only
> orchestrate (the thin-orchestrator contract).

See also: [`skill-contract.md`](skill-contract.md) (the exact conformance
contract), [`cli.md`](cli.md) (commands), [`authoring-skills.md`](authoring-skills.md)
(how to add a skill), [`configuration.md`](configuration.md)
(`cogsecskills.yaml`), and the [project README](../README.md).

## The three coherent artifacts

A CogSecSkill area is expressed across a small set of artifacts that must stay
coherent. Each answers a different question, and the validation and drift gates
prove they agree. Three of them carry the build itself — the **registry**
(PLAN), the **canonical definitions** (BUILD SOURCE), and the **rendered skill
folders** (BUILD OUTPUT) — and form the data-flow spine:

```
   registry/skills.yaml          definitions/<group>/<slug>.yaml          skills/<group>/<slug>/
   (PLAN: what exists)    ──▶    (BUILD SOURCE: skill substance)   ──▶    (BUILD OUTPUT: what ships)
        id, group,                tools, workflow_steps,                   skill.yaml + SKILL.md +
        status, summary           anti_criteria, inputs/outputs            workflow.md + harness/*.md
            │                              │                                        │
            │  validate: PLAN ⇄ BUILD      │  author.render_definition()            │
            └──────────────────────────────┴────────────────────────────────────────┘
                                           │
                              definitions --check  (no drift between SOURCE and OUTPUT)
```

The arrows are the contract: the registry names an area, the definition
supplies its substance, and the renderer produces the folder. Substance never
travels backward — a change made directly in `skills/` is detected as drift, not
absorbed. Two further artifacts wrap this spine: the **AGEINT upstream**
(TEACH, the conceptual *why*) and the **scenario fixtures** (CHECK, proof that
curated defensive scenarios still route and bind).

| Artifact | Question | Role | Where |
|----------|----------|------|-------|
| **PLAN** | *what* skill areas exist | catalogue of all 100 areas | [`registry/skills.yaml`](../registry/skills.yaml) (+ [`registry/groups.yaml`](../registry/groups.yaml)) |
| **BUILD SOURCE** | *how* each skill should be rendered | canonical definitions | [`definitions/<group>/<slug>.yaml`](../definitions/) |
| **BUILD OUTPUT** | *how* each skill works in a harness | multiharness skill folders | [`skills/<group>/<slug>/`](../skills/) |
| **TEACH** | *why* the concept matters | educational upstream | [`docs/ageint/`](ageint/README.md) |
| **CHECK** | *can curated defensive scenarios still route and bind?* | safe-use and unsafe-redirect fixtures | [`scenarios/defensive_readiness.yaml`](../scenarios/defensive_readiness.yaml) |

- **PLAN — the registry.** `registry/skills.yaml` enumerates every skill area
  in the taxonomy (id, name, group, status, summary, optional `ageint_topic`),
  independent of whether each area has been built on disk yet.
  `registry/groups.yaml` defines the workflow subfolders (groups) a skill can
  belong to. The registry is the *plan*: it can list a `planned` area that has
  no on-disk folder.
- **BUILD SOURCE — canonical definitions.** Each implemented area has a YAML
  definition under `definitions/<group>/<slug>.yaml`. This file **owns the
  skill's substance** — its tool plan, workflow steps, anti-criteria, inputs,
  outputs, and references. It is the one place a human edits a skill, and the
  durable source for all-skill editing and drift checking. When the recent
  de-stitching pass rewrote every skill's quality fields into grammatical,
  domain-specific prose, that work landed here, in the definitions — not in the
  generated output.
- **BUILD OUTPUT — the skills tree.** Each implemented area is **rendered**
  under `skills/<group>/<slug>/` with the harness-neutral spec plus its
  companion files (see [Anatomy](#anatomy-of-a-skill-build)). This is the
  harness-facing output that actually ships and runs. It is *generated* from the
  definition — treat it as a build artifact, not a place to author. The drift
  gate exists precisely so a stale or hand-edited folder cannot ship silently.
- **TEACH — the AGEINT upstream.** `docs/ageint/` holds the educational
  concepts each skill references via its `ageint_topic`. The library is
  strictly defensive, educational, and accountable; the AGEINT material is the
  conceptual *why* behind each technique.
- **CHECK — scenario fixtures.** `scenarios/defensive_readiness.yaml` contains
  curated safe-use and unsafe-redirect probes for every group. The scenario gate,
  run with `python -m cogsecskills scenarios --check`, confirms routing, declared
  outputs, expected response shape, quality metadata, and refusal/redirect
  markers without executing an external model runtime. A safe-use probe must
  route to the expected skill and surface the expected product; an
  unsafe-redirect probe must be turned away. This keeps the library's defensive
  posture verifiable rather than aspirational — for example, the flagship
  `critical_review.red_team_review` skill now carries an adversary model, an
  attack-surface taxonomy, an exploitability×impact scoring rubric, and a
  go/no-go output, and its scenario fixtures assert that this deepened structure
  still routes and binds.

### How `validate` keeps PLAN and BUILD coherent

`python -m cogsecskills validate` (implemented in
[`validate.py`](../src/cogsecskills/quality/validate.py)) cross-checks PLAN against
BUILD so the catalogue can never silently drift from what ships:

- Every **on-disk skill must be catalogued** in the registry with a matching
  group.
- Every registry entry marked **`implemented` must exist on disk** (a hard
  error if it does not).
- A registry entry marked **`planned` with no folder is normal** — the expected
  state of an un-built area, not an error.

This *missing-vs-extra asymmetry* is deliberate: an implemented-but-missing
build is a broken promise (hard error), while planned-but-not-yet-built is the
ordinary backlog (silent and fine). The full enumeration of checks lives in
[`skill-contract.md`](skill-contract.md).

## The runner package

All logic lives in `src/cogsecskills/`, organized into cohesive subpackages that
mirror the data flow above and form a clean dependency DAG (`core` ← `authoring`,
`quality`; `quality` ← `artifacts`; everything ← `cli`):

- **`core/`** — the data model and what reads it: `spec.py` (a rendered skill),
  `registry.py` (the catalogue), `loader.py` (discover skills on disk),
  `config.py` (optional overrides), `harness.py` (the harness/verb model).
- **`authoring/`** — produce skills from canonical definitions: `author.py` and
  `definitions.py` (generate and render), `scaffold.py` (skeletons).
- **`quality/`** — prove conformance: `validate.py` (the contract gate) and
  `insights.py` (route/stats/catalogue/doctor quality lint).
- **`artifacts/`** — generated views over the library: `scenarios.py`
  (defensive-readiness), `examples.py`, `evals.py`, `dashboard.py`,
  `release_metadata.py`, and the `manuscript_assets/` package (split into
  `paths`, `rows`, `tables`, `figures`, `assets_io` behind a façade `__init__`).
- **`cli.py`** — the thin command-line orchestrator over all of the above.

Each subpackage has a single responsibility, so a reader can open one folder and
see a complete layer without wading through the rest of the engine.

Each module in detail:

| Module | Job |
|--------|-----|
| [`spec.py`](../src/cogsecskills/core/spec.py) | The harness-neutral `SkillSpec` dataclass and the **closed** `ToolVerb` enum. Total parsing: malformed `skill.yaml` raises `SpecError` rather than producing a half-built object. Also `SkillTool`, `SkillIO`, and the `SKILL_STATUSES` tuple (`implemented`, `stub`, `planned`). |
| [`registry.py`](../src/cogsecskills/core/registry.py) | The catalogue. `SkillRegistry` / `RegistryEntry` load and validate `registry/skills.yaml` and `registry/groups.yaml` (rejects duplicate ids, bad status, missing keys). Query helpers: `by_group`, `by_status`, `get`, `status_counts`. |
| [`loader.py`](../src/cogsecskills/core/loader.py) | Discovery. Turns the on-disk `skills/**/skill.yaml` tree into validated `SkillSpec` objects (`load_skill`, `discover_skills`, `skills_root`, `skill_dir`). Returns an empty list when the tree is absent, so callers never special-case bootstrap. |
| [`harness.py`](../src/cogsecskills/core/harness.py) | Multiharness conformance. Defines the default `HARNESSES` (`claude`, `codex`, `hermes`) and `HARNESS_VERB_SUPPORT`. `check_conformance` proves a spec declares an adapter for each configured harness and that each harness can realise every verb the skill uses. The check is structural, not behavioural. |
| [`validate.py`](../src/cogsecskills/quality/validate.py) | The validation gates. `validate_skill` (per-skill structure + conformance), `validate_library` (every skill + registry coherence), `conformance_report` (machine-readable summary). Produces `ValidationResult` / `ValidationIssue`. |
| [`scaffold.py`](../src/cogsecskills/authoring/scaffold.py) | Skeletons. `scaffold_skill` reads a registry row and writes a conforming-but-shallow `stub` skill folder (spec + `SKILL.md` + `workflow.md` + one adapter per harness) for an author to deepen by hand. |
| [`author.py`](../src/cogsecskills/authoring/author.py) | The deterministic renderer. `render_definition` turns a structured JSON or YAML definition into the conforming files; adapters are generated to bind **exactly** the declared verbs. `author_batch` remains as a compatibility path for `_def.json`. |
| [`definitions.py`](../src/cogsecskills/authoring/definitions.py) | The canonical definition layer. `definitions --write` renders all 100 skills from `definitions/<group>/<slug>.yaml`; `definitions --check` proves the YAML definitions and rendered skill files have not drifted. |
| [`config.py`](../src/cogsecskills/core/config.py) | Configuration. Optional `cogsecskills.yaml` overrides the harness set and `doctor` quality thresholds; everything has a default, so the file is never required. A present-but-malformed config raises rather than silently falling back. |
| [`locate.py`](../src/cogsecskills/core/locate.py) | Project-root discovery. Walks up from the module file to find `registry/skills.yaml` or `pyproject.toml`, replacing fragile `parents[N]` magic-depths. Fails loud if no sentinel is found. |
| [`quality_constants.py`](../src/cogsecskills/core/quality_constants.py) | Shared quality-policy constants (field names, generic-phrase lists, sensitive groups/terms, normalization helper) used by both `insights.py` and `definitions.py`. Prevents drift between the two quality-check modules. |
| [`text_utils.py`](../src/cogsecskills/core/text_utils.py) | Shared text utilities (`clean_cell`, `as_text`) used by `evals.py`, `examples.py`, and `rows.py`. Prevents drift between the three artifact generators. |
| [`insights.py`](../src/cogsecskills/quality/insights.py) | Affordances over the catalogue: `route_query` (rank skills for a free-text need), `library_stats` (counts by group/status/verb), `render_catalogue_markdown` (navigable index), `doctor` (quality lint vs configurable thresholds — depth, not conformance). |
| [`scenarios.py`](../src/cogsecskills/artifacts/scenarios.py) | Deterministic defensive-readiness checks. Loads curated safe-use and unsafe-redirect fixtures, confirms route matches, output terms, quality metadata, and refusal/redirect markers without calling external model runtimes. |
| [`manuscript_assets.py`](../src/cogsecskills/artifacts/manuscript_assets/__init__.py) | Generated manuscript layer. Joins registry entries to live skill specs and writes `S10_skill_catalogue.md`, `S11_skill_metadata_matrix.md`, data exports, and eight figures under `output/figures/`; `check_assets` detects drift. |
| [`cli.py`](../src/cogsecskills/cli.py) | Thin orchestrator. Parses args, calls the library API, prints results — `list`, `show`, `validate`, `report`, `route`, `stats`, `groups`, `catalogue`, `doctor`, `definitions`, `scenarios`, `manuscript-assets`, `export`, `scaffold`, `author`, `author-batch`. No business logic. |

## Anatomy of a skill (BUILD)

Each implemented area is a folder of six files:

```
skills/<group>/<slug>/
  skill.yaml          # generated harness-neutral spec
  SKILL.md            # Claude Code native entry point (frontmatter + doc)
  workflow.md         # the agentic procedure, each step tagged with a tool verb
  harness/
    claude.md         # default adapter: verb -> Claude Code tools
    codex.md          # default adapter: verb -> Codex tools
    hermes.md         # default adapter: verb -> Hermes function calls
    <name>.md         # optional configured harness adapter
```

The id is `<group>.<slug>`; the parent directory name equals the `group` and
the leaf directory equals the `slug`, so a skill can never be reached at a
folder that disagrees with its id.

For repo-wide editing, the durable source of skill substance is the canonical
YAML file under `definitions/<group>/<slug>.yaml`. The files in `skills/` are
the generated build output that agent harnesses consume and validators inspect.

## The harness-neutral design

A skill declares the **capabilities** it needs, not the concrete tools of any
one harness. The vocabulary is a **closed set** of eight tool verbs:

| Verb | Meaning |
|------|---------|
| `read` | Read supplied material / locate local evidence |
| `search` | Search local and external sources |
| `write` | Emit the structured product |
| `exec` | Run commands or the project's own gates |
| `reason` | Apply the technique; expose concise rationale |
| `web` | Fetch and inspect web sources |
| `delegate` | Fan out independent sub-analyses |
| `ask` | Ask the user for an unresolvable decision |

Keeping the vocabulary closed (`ToolVerb` in `spec.py`) makes conformance
machine-checkable and keeps skills portable. Inventing a verb fails parsing.

**Per-harness adapter files bind verbs to concrete tools.** Each skill ships
one adapter per configured harness under `harness/` — a Markdown binding table
whose first column lists the neutral verb and whose remaining columns name the
concrete tool. For example, in the default harness set, `read` binds to Claude
Code `Read`/`Grep`, to Codex `shell` (`cat`, `rg`), and to Hermes `fs.read`.

Concretely, a skill whose definition declares `read`, `reason`, and `write`
produces an adapter table in each harness file binding exactly those three verbs
— no more (an unbound verb is a stray tool) and no fewer (an unrealised verb is
a broken skill). Add a fourth verb to the definition, regenerate, and the new
row appears in every adapter.

**"Multiharness" is a property the test suite proves, not a hope.** The
validator checks that every declared verb appears in *every* adapter
(`_adapter_bound_verbs`), and `harness.check_conformance` checks that each
harness can realise every declared verb. The live conformance test runs against
the real `skills/` tree, so a malformed or non-conforming skill fails the suite.
Because the adapters are generated from the definition's verb set, this property
holds across all 100 skills without per-skill bookkeeping.

## The authoring pipeline: substance vs format

Authoring separates **substance** (what a technique does) from **format** (the
conforming harness-facing files). The repository now preserves substance as
canonical YAML under `definitions/`; `author.py` supplies format
deterministically.

```
                 SUBSTANCE                          FORMAT
   ┌─────────────────────────────┐     ┌──────────────────────────────────┐
   │  canonical YAML definition  │     │   author.render_definition()      │
   │  - id (must be in registry) │ ──▶ │   (deterministic renderer)        │
   │  - tools: [{verb, purpose}] │     │   adapters bind EXACTLY the       │
   │  - workflow_steps           │     │   declared verbs                  │
   │  - anti_criteria            │     └────────────────┬──────────────────┘
   │  - inputs / outputs / refs  │                      │
   └─────────────────────────────┘                      ▼
                                        skills/<group>/<slug>/
                                          skill.yaml      (the neutral spec)
                                          SKILL.md        (Claude Code entry)
                                          workflow.md     (the procedure)
                                          harness/claude.md
                                          harness/codex.md   <- one per harness
                                          harness/hermes.md
                                                  │
                                                  ▼
                                   validate_library()  ->  0 errors
                                   (conforms by construction)
```

The renderer reads name / group / summary / `ageint_topic` from the registry
entry (not the definition), so substance and catalogue cannot disagree. Because
adapters are generated to bind precisely the verbs the definition declares,
**every authored skill passes the validator by construction** — there are no
format stragglers no matter how many skills are authored in parallel.

### The generate → check drift discipline

The pipeline is governed by a two-command loop that keeps the rendered output
honest about its source:

1. **Generate.** `python -m cogsecskills definitions --write` renders all 100
   skills from `definitions/<group>/<slug>.yaml` into the `skills/` tree. This
   is the only sanctioned way to change the rendered output.
2. **Check.** `python -m cogsecskills definitions --check` re-renders in memory
   and compares against the committed `skills/` files, failing on any
   difference. Run in CI, it catches both a definition edited without a
   re-render and a skill folder hand-edited out from under its definition.

The discipline is simple to state and load-bearing in practice: **edit the
definition, regenerate, and let `--check` prove the tree matches.** Pair it with
`scenarios --check` and the two together assert that the shipped skills both
*match their source* and *still behave defensively*. Anyone tempted to patch a
file under `skills/` directly should instead patch the definition and rerun the
generator — otherwise the next `--check` (or the next full regeneration) reverts
the change.

`scaffold_skill` is the lighter-weight sibling: it writes a `stub` skeleton
(default `read`/`reason`/`write` tool plan) from the registry row for an author
to deepen and then promote.

## Engineering principles

- **Thin-orchestrator pattern.** Business logic lives only in the package
  modules; `cli.py`, the scaffold/author entry points, and any scripts merely
  parse input, call the tested API, and print. (See `cli.py` — it imports the
  library and formats output, nothing more.)
- **No-mocks testing.** Tests use real `tmp_path` directories and real YAML —
  no `MagicMock`, `unittest.mock`, or patching. The live conformance test
  exercises the actual `skills/` tree.
- **90% coverage gate** on `src/`; the current focused suite reports 90.94% coverage.
- **Defensive only.** Skills recognize, assess, and defend against cognitive
  attack — they never author manipulation. This is inherited from AGEINT and
  enforced by review.

## Cross-references

- [`skill-contract.md`](skill-contract.md) — the exact per-skill and
  registry conformance contract `validate.py` enforces.
- [`cli.md`](cli.md) — the `python -m cogsecskills` command surface.
- [`authoring-skills.md`](authoring-skills.md) — how to add a skill (scaffold
  vs deterministic author).
- [`configuration.md`](configuration.md) — `cogsecskills.yaml` (harness set,
  quality thresholds).
- [project README](../README.md) — overview and exemplar roster.
