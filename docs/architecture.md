# Architecture

CogSecSkills is a library of 100 analytic skills — Structured Analytic
Techniques, cognitive-security defenses, OSINT integrity, counterintelligence,
and critical review — each authored once as a **harness-neutral skill** that
has default adapters for Claude Code, Codex, and Hermes and the same structural
contract for any additional configured harness. This document describes the
system design: the three coherent artifacts, the runner package, the
harness-neutral contract, and the deterministic definition-to-skill pipeline.

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

A CogSecSkill area exists as three artifacts that must stay coherent. Each
answers a different question, and the validation gate proves they agree.

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
  definition under `definitions/<group>/<slug>.yaml`. This is the durable
  source for all-skill editing and drift checking.
- **BUILD OUTPUT — the skills tree.** Each implemented area is rendered under
  `skills/<group>/<slug>/` with the harness-neutral spec plus its companion
  files (see [Anatomy](#anatomy-of-a-skill-build)). This is the harness-facing
  output that actually ships and runs.
- **TEACH — the AGEINT upstream.** `docs/ageint/` holds the educational
  concepts each skill references via its `ageint_topic`. The library is
  strictly defensive, educational, and accountable; the AGEINT material is the
  conceptual *why* behind each technique.
- **CHECK — scenario fixtures.** `scenarios/defensive_readiness.yaml` contains
  curated safe-use and unsafe-redirect probes for every group. The scenario gate
  checks routing, declared outputs, expected response shape, quality metadata,
  and refusal/redirect markers without executing an external model runtime.

### How `validate` keeps PLAN and BUILD coherent

`python -m cogsecskills validate` (implemented in
[`validate.py`](../src/cogsecskills/validate.py)) cross-checks PLAN against
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

All logic lives in `src/cogsecskills/`. Each module has one job:

| Module | Job |
|--------|-----|
| [`spec.py`](../src/cogsecskills/spec.py) | The harness-neutral `SkillSpec` dataclass and the **closed** `ToolVerb` enum. Total parsing: malformed `skill.yaml` raises `SpecError` rather than producing a half-built object. Also `SkillTool`, `SkillIO`, and the `SKILL_STATUSES` tuple (`implemented`, `stub`, `planned`). |
| [`registry.py`](../src/cogsecskills/registry.py) | The catalogue. `SkillRegistry` / `RegistryEntry` load and validate `registry/skills.yaml` and `registry/groups.yaml` (rejects duplicate ids, bad status, missing keys). Query helpers: `by_group`, `by_status`, `get`, `status_counts`. |
| [`loader.py`](../src/cogsecskills/loader.py) | Discovery. Turns the on-disk `skills/**/skill.yaml` tree into validated `SkillSpec` objects (`load_skill`, `discover_skills`, `skills_root`, `skill_dir`). Returns an empty list when the tree is absent, so callers never special-case bootstrap. |
| [`harness.py`](../src/cogsecskills/harness.py) | Multiharness conformance. Defines the default `HARNESSES` (`claude`, `codex`, `hermes`) and `HARNESS_VERB_SUPPORT`. `check_conformance` proves a spec declares an adapter for each configured harness and that each harness can realise every verb the skill uses. The check is structural, not behavioural. |
| [`validate.py`](../src/cogsecskills/validate.py) | The validation gates. `validate_skill` (per-skill structure + conformance), `validate_library` (every skill + registry coherence), `conformance_report` (machine-readable summary). Produces `ValidationResult` / `ValidationIssue`. |
| [`scaffold.py`](../src/cogsecskills/scaffold.py) | Skeletons. `scaffold_skill` reads a registry row and writes a conforming-but-shallow `stub` skill folder (spec + `SKILL.md` + `workflow.md` + one adapter per harness) for an author to deepen by hand. |
| [`author.py`](../src/cogsecskills/author.py) | The deterministic renderer. `render_definition` turns a structured JSON or YAML definition into the conforming files; adapters are generated to bind **exactly** the declared verbs. `author_batch` remains as a compatibility path for `_def.json`. |
| [`definitions.py`](../src/cogsecskills/definitions.py) | The canonical definition layer. `definitions --write` renders all 100 skills from `definitions/<group>/<slug>.yaml`; `definitions --check` proves the YAML definitions and rendered skill files have not drifted. |
| [`config.py`](../src/cogsecskills/config.py) | Configuration. Optional `cogsecskills.yaml` overrides the harness set and `doctor` quality thresholds; everything has a default, so the file is never required. A present-but-malformed config raises rather than silently falling back. |
| [`insights.py`](../src/cogsecskills/insights.py) | Affordances over the catalogue: `route_query` (rank skills for a free-text need), `library_stats` (counts by group/status/verb), `render_catalogue_markdown` (navigable index), `doctor` (quality lint vs configurable thresholds — depth, not conformance). |
| [`scenarios.py`](../src/cogsecskills/scenarios.py) | Deterministic defensive-readiness checks. Loads curated safe-use and unsafe-redirect fixtures, confirms route matches, output terms, quality metadata, and refusal/redirect markers without calling external model runtimes. |
| [`manuscript_assets.py`](../src/cogsecskills/manuscript_assets.py) | Generated manuscript layer. Joins registry entries to live skill specs and writes `S10_skill_catalogue.md`, `S11_skill_metadata_matrix.md`, data exports, and eight figures under `output/figures/`; `check_assets` detects drift. |
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

**"Multiharness" is a property the test suite proves, not a hope.** The
validator checks that every declared verb appears in *every* adapter
(`_adapter_bound_verbs`), and `harness.check_conformance` checks that each
harness can realise every declared verb. The live conformance test runs against
the real `skills/` tree, so a malformed or non-conforming skill fails the suite.

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
format stragglers no matter how many skills are authored in parallel. The live
tree is checked by `python -m cogsecskills definitions --check`, which compares
all canonical definitions with the rendered `skills/` files.

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
- **90% coverage gate** on `src/`; the current focused suite reports 90.93% coverage.
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
