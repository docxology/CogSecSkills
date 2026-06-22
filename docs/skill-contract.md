# The Skill Conformance Contract

This is the exact contract a CogSecSkill must satisfy, as enforced by
[`src/cogsecskills/validate.py`](../src/cogsecskills/validate.py). A skill is
*conforming* when `validate_skill` reports zero errors against it, and the
library is coherent when `validate_library` reports zero errors across every
skill plus the registry. Run the gate with:

```bash
python -m cogsecskills validate   # must report 0 errors
```

Each check below cites the validator function (or `spec.py` parser) that
enforces it. See [`architecture.md`](architecture.md) for the design rationale.

## Two gates, two questions

An author has two distinct gates to clear, and they answer different questions.
Both must pass before a skill is committed.

| Gate | Command | Question it answers | Code |
| --- | --- | --- | --- |
| **Conformance** | `python -m cogsecskills validate` | *Is this skill structurally well-formed and multiharness?* | `validate.py` |
| **Quality lint** | `python -m cogsecskills doctor` | *Is this skill deep, specific, and defensively complete?* | `insights.py` → `doctor` |

`validate` is binary and hard: any failure is an error and the skill does not
ship. `doctor` runs `validate` first, then layers on quality findings (`warn`
level) about *depth* rather than *form* — short workflows, thin quality fields,
generic negative controls, and quality language copied between skills. The 100
implemented areas in this mature library are expected to pass both cleanly.

Parts 1–4 below specify the conformance contract. [Part 5](#part-5--quality-lint-doctor)
specifies what `doctor` enforces so you can self-check the depth bar before you
commit. The fastest route to a clean self-check is to run `doctor` and treat
every finding as a to-do:

```bash
python -m cogsecskills doctor    # validate + the quality findings in Part 5
```

## Canonical skill folder layout

```
skills/<group>/<slug>/
  skill.yaml          # generated harness-neutral spec
  SKILL.md            # Claude Code native entry point (required)
  workflow.md         # the procedure (filename must match the spec's `workflow:`)
  harness/
    claude.md         # default adapter; one adapter per configured harness
    codex.md
    hermes.md
    <name>.md         # optional configured harness adapter
```

- The folder is `skills/<group>/<slug>/`.
- The id is `<group>.<slug>`.
- The parent directory name must equal the spec's `group`; the leaf directory
  name must equal the `slug`.
- The source-owned definition for repo-wide editing lives at
  `definitions/<group>/<slug>.yaml`; the folder above is the rendered
  harness-facing build output.

## Part 1 — `skill.yaml` parsing (`spec.py`)

A `skill.yaml` is parsed by `SkillSpec.from_mapping`. Parsing is total: any
violation raises `SpecError` (which the loader wraps with the file path) rather
than producing a half-built spec. Checklist:

- [ ] **Top level is a mapping.** A non-mapping document is rejected.
- [ ] **`id`, `name`, `group`, `summary` are non-empty strings.** Enforced by
  `_require_text` — these must be *real* strings, not coerced. `id: 0`,
  `id: []`, or `id: null` are rejected (no silent `"0"` / `"[]"` / `"None"`).
- [ ] **`status` ∈ {`implemented`, `stub`, `planned`}.** Must be a string; any
  other value is rejected (`SKILL_STATUSES`). Defaults to `planned`.
- [ ] **`tools` entries are `{verb, purpose}` mappings.** Each tool entry
  (`SkillTool.from_obj`) needs a `verb` from the closed set and a non-empty
  `purpose`. A missing `verb`, a non-mapping entry, or an empty `purpose` is
  rejected.
- [ ] **Tool verbs come from the closed set.** `ToolVerb.coerce` accepts only
  `read, search, write, exec, reason, web, delegate, ask` (case-insensitive,
  trimmed). An unknown verb is rejected with the allowed list.
- [ ] **`harness` is a mapping of `harness -> path`.** A non-mapping `harness`
  field is rejected; absent, it defaults to `{}` (which then fails the
  per-harness adapter checks below for any configured harness).
- [ ] **`inputs` / `outputs` entries are valid `SkillIO` mappings.** Each needs
  a non-empty `name`; `required`, when present, must be a real boolean (the
  string `"false"` is rejected, since coercing it would invert the channel's
  semantics).
- [ ] **`workflow`** defaults to `workflow.md` when absent.

> An `implemented` skill that declares no tools is rejected by the validator
> (see Part 3), but parsing alone does not require tools.

## Part 2 — Per-skill structure (`validate_skill`)

`validate_skill(spec, directory, harnesses)` checks one skill's on-disk folder.
`harnesses` defaults to `HARNESSES` (`claude`, `codex`, `hermes`) but is
overridden from `cogsecskills.yaml` when the CLI runs; every configured harness
is part of the same structural contract.

- [ ] **`SKILL.md` is present.** Missing `SKILL.md` (the Claude Code native
  entry point) is an error.
- [ ] **The workflow document is present.** The file named by the spec's
  `workflow:` field must exist. Its declared path may not escape the skill
  directory — `_safe_declared_path` rejects an absolute path or any path
  containing `..`.
- [ ] **One adapter per configured harness, declared AND present.** For each
  harness in `harnesses`:
  - The spec's `harness:` map must declare a non-empty path for that harness
    (else: *"spec does not declare a `<h>` harness adapter"*).
  - The declared path must stay inside the skill dir (no `..`, not absolute) —
    `_safe_declared_path`.
  - The file at that path must exist (else: *"declared `<h>` adapter not
    found"*) and be readable.
- [ ] **Each adapter binds every declared verb.** `_adapter_bound_verbs` reads
  the adapter's Markdown table rows and collects the verb in each row's **first
  column**. Every verb in `spec.verbs` (the distinct verbs across the spec's
  tools) must appear among those bound verbs, or the adapter is reported as not
  binding the missing verbs. This is the mechanism that makes "multiharness" a
  proven property, not a hope.
- [ ] **Multiharness verb support.** `check_conformance` (Part below) is also
  run inside `validate_skill`: if any configured harness cannot realise a verb
  the skill uses, that is an error. (Today every harness supports the full
  closed vocabulary; this guards against a future narrower harness.)
- [ ] **An `implemented` skill declares ≥1 tool.** An implemented spec with an
  empty `tools` list is an error.
- [ ] **id is `<group>.<slug>`.** `spec.id` must start with `"<group>."` and
  must not equal `"<group>."` alone (a bare prefix with no slug).
- [ ] **On-disk group matches.** `directory.parent.name` must equal
  `spec.group`.
- [ ] **On-disk slug matches.** `directory.name` must equal the slug portion of
  the id (the part after the first `.`), so a skill can never be reached at a
  folder that disagrees with its id.

### How adapter verbs are extracted (`_adapter_bound_verbs`)

For each line of the adapter that starts with `|`, the validator splits the
Markdown row on `|`, strips backticks / `*` / `_` / spaces and lowercases the
**first cell**, skips separator rows (cells made only of `-`), and tries to
coerce that first cell to a `ToolVerb`. So the binding table's first column is
the contract surface — it must list every neutral verb the skill declares:

```markdown
| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| `read`   | `Read` / `Grep`        | Read supplied material. |
| `reason` | private model reasoning | Apply the technique.    |
| `write`  | `Write` / final response | Emit the product.      |
```

## Part 3 — Multiharness conformance (`harness.check_conformance`)

A skill is *multiharness* when its single spec maps onto every configured
harness. `check_conformance` returns, per harness, a `HarnessConformance` that
is `ok` only when:

- [ ] **An adapter is declared** for that harness (non-empty path in the spec's
  `harness:` map), and
- [ ] **The harness supports every verb the skill uses.** A harness with no
  entry in `HARNESS_VERB_SUPPORT` is assumed to support the full closed
  vocabulary, so adding a harness needs only an adapter file — not a code
  change. `validate_skill` surfaces any `unsupported_verbs` as an error.

### Harness status labels

The contract uses three labels consistently:

| Label | Contract role |
| --- | --- |
| default adapters | `claude`, `codex`, and `hermes` are the default `HARNESSES` and are rendered for every committed skill. |
| configured structural adapters | Any name in `cogsecskills.yaml` becomes part of the configured harness set checked by `validate`. |
| documented external profiles | Entries such as `gemini_cli`, `github_copilot`, `devin_local`, `devin_cascade`, `cursor`, `cline`, `aider`, `continue`, `jetbrains_ai`, `openai_agents_sdk`, `langgraph`, `microsoft_agent_framework`, `autogen`, `crewai`, `pydantic_ai`, `mcp_host`, and `perplexity_research` are integration examples only until configured. |

`registry/harness_profiles.yaml` does not affect parsing, rendering, or
validation by itself. To make one of those documented external profiles part of
the contract, copy its id into `cogsecskills.yaml`, run `definitions --write`,
review the generated adapter language, and then run `validate`.

The profile class matters. Instruction-file products, IDE rule systems,
terminal pair-programming tools, SDK frameworks, and MCP tool hosts do not share
one universal adapter semantics. CogSecSkills validates the rendered adapter
files against the closed verb contract; it does not certify a vendor runtime,
connector policy, or application wrapper.

## Part 4 — Registry coherence (`validate_library`)

`validate_library(root, harnesses)` discovers every on-disk skill, runs
`validate_skill` on each, then cross-checks the registry. The checks:

- [ ] **Registry ids are well-formed.** Each entry's `id` must be
  `<group>.<slug>` using its own `group` (start with `"<group>."`, not equal to
  the bare prefix).
- [ ] **`implemented` registry entries exist on disk (HARD).** For every
  registry row whose status is `implemented`, a matching on-disk skill id must
  exist — otherwise it is a hard error
  (*"registry marks skill 'implemented' but no on-disk skill found"*).
- [ ] **Catalogued groups are defined in `groups.yaml`.** When `groups.yaml`
  defines any groups, every registry entry's `group` must be one of them.
- [ ] **Every on-disk skill is catalogued with a matching group.** Each
  discovered skill id must appear in the registry; if it does, the registry
  entry's `group` must equal the spec's `group`.

### The deliberate missing-vs-extra asymmetry

The contract treats the two directions of drift differently, on purpose (the
validation-asymmetry lesson):

| Situation | Verdict | Why |
|-----------|---------|-----|
| Registry says `implemented`, no folder on disk | **HARD ERROR** | A broken promise — the catalogue claims something that does not ship. |
| Registry says `planned`, no folder on disk | **Normal** | The expected state of an un-built area. The backlog is allowed to be ahead of the build. |
| On-disk skill not in the registry | **ERROR** | A skill ships that the catalogue never accounted for. |
| On-disk skill whose group disagrees with the registry | **ERROR** | The plan and build name the same skill differently. |

The current library has 100 implemented areas, but the contract still supports
future planned rows. A registry may list a future area as `planned` before its
folder exists. Only `implemented`-without-build, and on-disk-without-catalogue,
are errors. `conformance_report` summarizes the totals
(`registry_total`, `on_disk_skills`, `registry_status_counts`, `errors`,
`warnings`, `ok`).

## Part 5 — Quality lint (`doctor`)

Structural conformance proves a skill is *well-formed*. The quality lint proves
it is *worth shipping*. `doctor` (in `insights.py`) walks every implemented
skill and emits `warn`-level findings; a clean library produces none. Use this
section as the author's self-check: each row names the finding, what triggers
it, and the fix.

The depth thresholds come from `cogsecskills.yaml` (`Config` defaults shown);
see [`configuration.md`](configuration.md) to tune them.

### Workflow depth and references

| Finding | Trigger | Default | Fix |
| --- | --- | --- | --- |
| `N workflow steps (< M)` | The workflow document has fewer numbered steps than `min_workflow_steps`. | `min_workflow_steps: 3` | Decompose the procedure into at least the minimum discrete, checkable steps. |
| `N anti-criteria (< M)` | Fewer "do NOT / stop if" guardrails than `min_anti_criteria`. | `min_anti_criteria: 2` | Add explicit out-of-scope / refusal criteria so the skill knows when *not* to act. |
| `no references` | An implemented skill has an empty `references` list while `require_references` is on. | `require_references: false` | Cite the methodological sources the technique rests on. |

### Quality fields must be present and substantive

Every implemented skill carries eight quality fields; an empty one is a
finding (`missing quality field: <field>`). These are the de-stitched,
domain-specific prose fields the recent improvement pass populated:

- `defensive_boundary` — what the skill is *for*, framed defensively.
- `misuse_redirect` — how the skill redirects an unsafe request.
- `evidence_requirements` — what counts as evidence vs. inference.
- `confidence_rubric` — how to assign HIGH / MEDIUM / LOW (or equivalent) calibration.
- `uncertainty_handling` — how unknowns and alternatives are preserved.
- `privacy_legal_constraints` — the privacy and authorization limits.
- `failure_modes` — the characteristic ways the analysis goes wrong.
- `negative_controls` — paired safe/unsafe examples that exercise the boundary.

### Defensive-content lints

These checks read the `defensive_boundary`, `misuse_redirect`,
`negative_controls`, and the workflow text together:

| Finding | What it enforces |
| --- | --- |
| `forbidden chain-of-thought wording` | The phrase `chain-of-thought` may not appear — expose concise rationale, not exhaustive private reasoning. |
| `negative controls must include unsafe redirect coverage` | The combined text must mention both an `unsafe` case and a `redirect`, so the boundary is exercised, not just asserted. |
| `negative controls must include a safe defensive example` | The `negative_controls` must contain both `safe` and `defensive`, so a legitimate use is shown alongside the refused one. |
| `sensitive skill missing defensive/privacy misuse guardrails` | For skills in sensitive groups (`cognitive_security`, `counterintelligence`, `information_environment`, `osint_integrity`) or naming sensitive subjects, the text must address `refuse`, `defensive`, `privacy`, and `authorized`. |

### Evidence, inference, unknowns, and alternatives

Two fields have mandatory vocabulary because they encode the library's
epistemic discipline:

- `evidence_requirements` must label both `evidence` and `inference`
  (*evidence requirements must label evidence and inference*) — observations and
  the conclusions drawn from them are never conflated.
- `uncertainty_handling` must preserve both `unknown` and `alternative`
  (*uncertainty handling must preserve unknowns and alternatives*) — the skill
  states what it does not know and keeps credible competing explanations alive
  rather than forcing one narrative or attribution.

### Specificity: nothing generic, nothing reused

A mature library earns trust by being specific. Three families of finding guard
against thin, boilerplate, or copy-pasted quality language:

| Finding | What triggers it (`insights.py`) |
| --- | --- |
| `negative controls are too generic for the skill or group` | `_negative_controls_are_specific` finds no skill name, slug words, or group name in the controls — they could belong to any skill. |
| `negative controls repeat generic boilerplate examples` | The controls reuse a known boilerplate phrase (e.g. *"assess this material for manipulation indicators"*). |
| `<field> must include skill-specific language` | A specificity-checked field (`confidence_rubric`, `evidence_requirements`, `privacy_legal_constraints`, `failure_modes`) contains no token from the skill's name or slug. |
| `<field> entry reused across skills` | A `confidence_rubric`, `evidence_requirements`, or `privacy_legal_constraints` entry is byte-identical (normalized) across two or more implemented skills — the de-stitching pass exists precisely to eliminate this. |

The reuse check (`_reused_quality_field_findings`) is library-wide: it compares
every implemented skill against every other, so a phrase copied between two
skills is caught even though each skill passes on its own. This is what keeps
100 skills from collapsing into one templated voice.

### Author self-check, in order

Before committing a new or edited skill:

1. `python -m cogsecskills definitions --write` — re-render the harness adapters.
2. `python -m cogsecskills validate` — clear all of Parts 1–4 (must report 0 errors).
3. `python -m cogsecskills doctor` — clear every finding above.
4. Re-read your `negative_controls`: one safe/defensive example, one unsafe case
   that is *redirected*, both naming this skill's subject.
5. Confirm `evidence_requirements` separates evidence from inference and
   `uncertainty_handling` keeps unknowns and alternatives open.

The flagship `cognitive_security.red_team_review` skill is the reference for
this bar — its adversary model, attack-surface taxonomy, exploitability×impact
rubric, and go/no-go output show the depth `doctor` is steering every skill
toward.

## The closed tool-verb vocabulary

A skill declares capabilities as harness-neutral verbs, never harness-specific
tool names. The set is closed (`ToolVerb` in `spec.py`); inventing a verb fails
parsing.

| Verb | Meaning |
|------|---------|
| `read` | Read supplied material and locate local evidence |
| `search` | Search local and external sources |
| `write` | Emit the structured analytic product |
| `exec` | Run commands or the project's own gates |
| `reason` | Apply the technique; expose concise rationale |
| `web` | Fetch and inspect web sources |
| `delegate` | Fan out independent sub-analyses |
| `ask` | Ask the user only for a decision that cannot be resolved |

## Cross-references

- [`architecture.md`](architecture.md) — system design and the three coherent
  artifacts.
- [`authoring-skills.md`](authoring-skills.md) — how the deterministic renderer
  makes skills conform by construction.
- [`cli.md`](cli.md) — the `validate`, `report`, `doctor`, and
  `scenarios --check` commands.
- [`configuration.md`](configuration.md) — overriding the harness set the
  contract checks against, the claim-status labels, and the quality thresholds
  used by [Part 5](#part-5--quality-lint-doctor).
- [project README](../README.md) — overview and exemplar roster.
