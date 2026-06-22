# Configuration — `cogsecskills.yaml`

CogSecSkills — the defensive cognitive-security skill library of 100 skills
across seven groups (`sat`, `cognitive_security`, `critical_review`,
`osint_integrity`, `counterintelligence`, `information_environment`,
`research_methods`) — is configurable without editing code. An optional
`cogsecskills.yaml` at the project root overrides the built-in defaults.

**It is entirely optional.** Every setting has a sensible default, so the file
is never required — with no `cogsecskills.yaml` present, the library uses
`Config.defaults()` and behaves exactly as documented below. The file is YAML
(not TOML) deliberately: it adds **no new dependency** and keeps Python 3.10
supported.

Two things this guide will not do, because the library does not do them: it
never claims a generated adapter is verified outside this repository, and it
never promises behaviour you can only learn by running a skill in a live agent.
Configuration changes which adapters are *generated* and *structurally
validated* — nothing more, nothing less. Keeping that boundary sharp is what
makes the conformance model trustworthy.

## On this page

- [What the config controls](#what-the-config-controls) — the `Config` fields and their defaults
- [`harnesses`](#harnesses--the-agent-harnesses-the-library-targets) — the harness set, claim-status labels, and external profiles
- [`quality:`](#quality--thresholds-enforced-by-doctor) — depth thresholds enforced by `doctor`
- [Complete example](#complete-example) — a full annotated `cogsecskills.yaml`
- [Malformed config is rejected loudly](#malformed-config-is-rejected-loudly) — the loader's fail-fast contract

See also: [`cli.md`](cli.md) for the commands that consume this config, and
[`architecture.md`](architecture.md) for how the harness set fits the
multiharness conformance model.

---

## What the config controls

The config resolves to a small `Config` with these fields and defaults:

| Setting | Default | Used by |
| --- | --- | --- |
| `harnesses` | `[claude, codex, hermes]` | `definitions --write`, `scaffold`, `author`, `author-batch` (which adapters to generate) and `validate` (which adapters to require). |
| `quality.min_workflow_steps` | `3` | `doctor` |
| `quality.min_anti_criteria` | `2` | `doctor` |
| `quality.require_references` | `false` | `doctor` |

There are exactly two knobs: **which harnesses** the library targets, and **how
deep** a skill must be to be called healthy. The first is structural — it
decides which adapter files exist and are required. The second is qualitative —
it decides whether the prose in those files clears a depth bar. They are checked
by different commands (`validate` and `doctor`) and fail for different reasons,
so they are documented as two separate sections below.

---

## `harnesses` — the agent harnesses the library targets

`harnesses` is the list of agent harnesses the library targets and validates. A
CogSecSkill is "multiharness" when its single neutral spec is fully expressible
under **every** configured harness — meaning it declares an adapter file for
each and every harness can realise every tool verb the skill uses.

Changing this list is the **only** thing you do to add or remove a harness — no
code change is needed:

- **`definitions --write`, `scaffold`, `author`, and `author-batch`** generate one harness adapter
  (`harness/<name>.md`) per entry in `harnesses`.
- **`validate`** requires each on-disk skill to declare an adapter for each
  configured harness, and checks that each harness supports every verb the
  skill uses.

An **unknown** harness — one with no built-in verb-support entry — is assumed to
realise the **full closed verb vocabulary** (`read`, `search`, `write`, `exec`,
`reason`, `web`, `delegate`, `ask`). So adding one needs only the config entry;
the adapters and validation follow automatically. The built-in harnesses
(`claude`, `codex`, `hermes`) ship with hand-written default adapter bindings;
an unknown harness's adapter rows are generated with a generic fallback binding
per verb (e.g. `gemini` `read` tool) that you can refine afterward, or override
per skill via `harness_bindings` in a definition (see
[`authoring-skills.md`](authoring-skills.md)).

### Defaults, configured adapters, and optional profiles

Three claim-status labels describe *how much the library asserts* about a given
harness. They sit on a ladder of decreasing certainty, and keeping them distinct
is the whole point: it lets a reader tell at a glance whether a harness is a
shipped default, a validation target you opted into, or merely a documented
candidate. The config file is the only source of truth for validation. The
optional profile registry at `registry/harness_profiles.yaml` is reader
guidance, not config.

| Label | Source of truth | What it means |
| --- | --- | --- |
| default adapters | `Config.defaults()` | `claude`, `codex`, and `hermes`; these are the built-in defaults when no config is present, and they ship with hand-written verb bindings. |
| configured structural adapters | `cogsecskills.yaml` → `harnesses:` | The exact harness names in `cogsecskills.yaml`; every skill must declare and bind adapters for these names after regeneration, and `validate` fails the skill if one is missing. |
| documented external profiles | `registry/harness_profiles.yaml` | Optional integration candidates listed in `registry/harness_profiles.yaml`; they are not validation targets until copied into `harnesses:`. Being listed here is documentation only — it carries no guarantee about a live runtime. |

The progression is one-directional: a documented external profile becomes a
configured structural adapter the moment you add its id to `harnesses:` and
regenerate; `claude`, `codex`, and `hermes` are simply the three configured
structural adapters you get for free when there is no config at all. Promoting a
profile asserts only that adapters now exist and are structurally checked — it
does not assert anything about behaviour in that runtime.

Current documented external profiles are `gemini_cli`, `github_copilot`,
`devin_local`, `devin_cascade`, `cursor`, `cline`, `aider`, `continue`,
`jetbrains_ai`, `openai_agents_sdk`, `langgraph`,
`microsoft_agent_framework`, `autogen`, `crewai`, `pydantic_ai`, `mcp_host`,
and `perplexity_research`. Use the profile id as the `harnesses:` entry only
when you intend to generate and review adapters for that runtime.

The profile classes are intentionally mixed, and the class tells you what
integration work a promotion implies. Grouping them makes that work legible
before you commit a profile id to `harnesses:`:

- **Terminal and IDE profiles** — `gemini_cli`, `github_copilot`, `cursor`,
  `cline`, `aider`, `continue`, and `jetbrains_ai` — usually map skill files
  into product-specific instruction, rule, memory, or skill surfaces. The
  adapter's job is to render the neutral spec into whatever file format the tool
  reads.
- **Hosted/autonomous-agent profiles** — `devin_local` and `devin_cascade` —
  target a managed agent runtime; the adapter describes how the skill is
  surfaced to that agent rather than to an interactive editor.
- **Programmatic runtime profiles** — `openai_agents_sdk`, `langgraph`,
  `microsoft_agent_framework`, `autogen`, `crewai`, and `pydantic_ai` — require
  an application wrapper that owns orchestration and tools. The adapter alone is
  not runnable; it is guidance for the wrapper author.
- **Protocol and research profiles** — `mcp_host` is a protocol/tool-host
  profile, and `perplexity_research` is a research companion. Each is useful
  only once wrapped by an application that loads local files and adapters.

In every class the deliverable from a promotion is the same: generated,
structurally validated adapter files. None of these classes implies that a skill
has been exercised end to end in the corresponding product.

### Worked example — adding a 4th harness end to end

Suppose you want the library to also target `gemini_cli`.

1. **Add it to the config.** Create or edit `cogsecskills.yaml`:

   ```yaml
   harnesses: [claude, codex, hermes, gemini_cli]
   ```

2. **Regenerate adapters for existing skills.** Re-render each skill so it gains
   a `harness/gemini_cli.md` adapter. With definitions on disk:

   ```bash
   python -m cogsecskills definitions --write
   python -m cogsecskills definitions --check
   ```

   or re-author / re-scaffold individual skills. Every render now reads
   `harnesses` from the config and emits four adapters instead of three. Because
   `gemini_cli` has no built-in verb-support entry, it is assumed to support the
   full closed verb set, so every declared verb binds and the skill stays
   conformant.

3. **Validate.** `validate` now *requires* a `gemini_cli` adapter on every skill:

   ```bash
   python -m cogsecskills validate
   ```

   A skill missing `harness/gemini_cli.md` fails until re-rendered — that is the
   point: the config is the single source of truth for which harnesses the
   library guarantees adapters for.

No Python was edited at any step. The same three-step shape — *edit config →
regenerate → validate* — applies to any profile id from the list above; only the
name in step 1 changes. To **remove** a harness, delete its name from
`harnesses:` and regenerate; `validate` then stops requiring that adapter, and
the now-orphaned `harness/<name>.md` files can be cleaned up on the next render.

---

## `quality:` — thresholds enforced by `doctor`

The `quality` block tunes the quality lint that `doctor` runs **after**
`validate`. Structural conformance (validate) and depth (doctor) are separate:
a thin scaffold can pass `validate` while failing `doctor`. The mental model is
that `validate` asks *"does every required adapter exist and bind its verbs?"*
while `doctor` asks *"is the content in those skills deep enough to be worth
shipping?"* — and these thresholds set where "deep enough" is drawn.

| Key | Default | Meaning |
| --- | --- | --- |
| `min_workflow_steps` | `3` | Minimum number of `workflow.md` steps a skill must have. |
| `min_anti_criteria` | `2` | Minimum number of anti-criteria ("must NOT happen") entries. |
| `require_references` | `false` | When `true`, every skill must carry at least one reference. |

Each threshold maps to a concrete failure mode the library has reason to guard
against in defensive-security content:

- **`min_workflow_steps`** keeps a skill from collapsing into a one-line
  instruction. A real procedure — say, triaging a suspected influence operation
  or walking a source-reliability check — has discernible steps; a single step
  is usually a stub.
- **`min_anti_criteria`** forces every skill to state what *must not* happen.
  For a defensive library this is load-bearing: the anti-criteria are where a
  skill records that it stays observational and accountable and does not drift
  into operational-attack guidance.
- **`require_references`** turns citation into a hard gate. Left at `false` so a
  scaffold can exist before its sources are gathered; flipped to `true` once a
  group is mature enough that every claim should trace to a source.

Raise these to enforce a higher bar across the library; for example, set
`require_references: true` to make citations mandatory before a skill is
considered healthy. Because the values live in config rather than code, a
maintainer can ratchet the bar upward over time — start permissive while skills
are being authored, then tighten once the library stabilises — without touching
the `doctor` implementation.

---

## Complete example

```yaml
# cogsecskills.yaml — optional; everything here has a default.

# Agent harnesses the library targets and validates. scaffold/author generate
# one adapter per harness; validate requires one per harness. An unknown harness
# (here, gemini_cli) is assumed to support the full closed verb vocabulary.
harnesses: [claude, codex, hermes, gemini_cli]

# Quality thresholds the `doctor` command enforces (after `validate`).
quality:
  min_workflow_steps: 4
  min_anti_criteria: 2
  require_references: true
```

---

## Malformed config is rejected loudly

A config that is **present but wrong** is surfaced, not silently ignored.
Loading raises a `ValueError` with a precise message rather than quietly
falling back to defaults — a wrong config you didn't notice is worse than no
config. The loader rejects, among others:

- a top-level document that is not a mapping →
  `expected a top-level mapping`;
- `harnesses` that is not a non-empty list →
  `'harnesses' must be a non-empty list`;
- a `harnesses` list that becomes empty after trimming blanks →
  `'harnesses' resolved to empty after cleaning`;
- a `quality` block that is not a mapping →
  `'quality' must be a mapping`;
- a non-integer (or boolean) `min_workflow_steps` / `min_anti_criteria` →
  `quality.<key> must be an integer`.

Fix the message and re-run the command. When the file is absent, the defaults
apply with no error.
