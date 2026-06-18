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

## Canonical skill folder layout

```
skills/<group>/<slug>/
  skill.yaml          # harness-neutral spec — the single source of truth
  SKILL.md            # Claude Code native entry point (required)
  workflow.md         # the procedure (filename must match the spec's `workflow:`)
  harness/
    claude.md         # one adapter per configured harness, each declared in skill.yaml
    codex.md
    hermes.md
```

- The folder is `skills/<group>/<slug>/`.
- The id is `<group>.<slug>`.
- The parent directory name must equal the spec's `group`; the leaf directory
  name must equal the `slug`.

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
overridden from `cogsecskills.yaml` when the CLI runs.

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

So a registry can list ~100 areas while only some are built — `planned` rows
are fine. Only `implemented`-without-build, and on-disk-without-catalogue, are
errors. `conformance_report` summarizes the totals
(`registry_total`, `on_disk_skills`, `registry_status_counts`, `errors`,
`warnings`, `ok`).

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
- [`cli.md`](cli.md) — the `validate`, `report`, and `doctor` commands.
- [`configuration.md`](configuration.md) — overriding the harness set the
  contract checks against.
- [project README](../README.md) — overview and exemplar roster.
