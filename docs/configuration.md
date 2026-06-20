# Configuration — `cogsecskills.yaml`

CogSecSkills is configurable without editing code. An optional
`cogsecskills.yaml` at the project root overrides the built-in defaults.

**It is entirely optional.** Every setting has a sensible default, so the file
is never required — with no `cogsecskills.yaml` present, the library uses
`Config.defaults()` and behaves exactly as documented below. The file is YAML
(not TOML) deliberately: it adds **no new dependency** and keeps Python 3.10
supported.

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

The config file is the only source of truth for validation. The optional profile
registry at `registry/harness_profiles.yaml` is reader guidance, not config.

| Label | What it means |
| --- | --- |
| default adapters | `claude`, `codex`, and `hermes`; these are the built-in defaults when no config is present. |
| configured structural adapters | The exact harness names in `cogsecskills.yaml`; every skill must declare and bind adapters for these names after regeneration. |
| documented external profiles | Optional integration candidates listed in `registry/harness_profiles.yaml`; they are not validation targets until copied into `harnesses:`. |

Current documented external profiles are `gemini_cli`, `github_copilot`,
`devin_local`, `devin_cascade`, `cursor`, `cline`, `aider`, `continue`,
`jetbrains_ai`, `openai_agents_sdk`, `langgraph`,
`microsoft_agent_framework`, `autogen`, `crewai`, `pydantic_ai`, `mcp_host`,
and `perplexity_research`. Use the profile id as the `harnesses:` entry only
when you intend to generate and review adapters for that runtime.

The profile classes are intentionally mixed. Terminal and IDE profiles usually
map skill files into product-specific instruction, rule, memory, or skill
surfaces. Programmatic runtime profiles such as `openai_agents_sdk`,
`langgraph`, `autogen`, `crewai`, and `pydantic_ai` require an application
wrapper that owns orchestration and tools. `mcp_host` is a protocol/tool-host
profile, and `perplexity_research` is a research companion unless wrapped by an
application that loads local files and adapters.

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
   library guarantees.

No Python was edited at any step.

---

## `quality:` — thresholds enforced by `doctor`

The `quality` block tunes the quality lint that `doctor` runs **after**
`validate`. Structural conformance (validate) and depth (doctor) are separate:
a thin scaffold can pass `validate` while failing `doctor`.

| Key | Default | Meaning |
| --- | --- | --- |
| `min_workflow_steps` | `3` | Minimum number of `workflow.md` steps a skill must have. |
| `min_anti_criteria` | `2` | Minimum number of anti-criteria ("must NOT happen") entries. |
| `require_references` | `false` | When `true`, every skill must carry at least one reference. |

Raise these to enforce a higher bar across the library; for example, set
`require_references: true` to make citations mandatory before a skill is
considered healthy.

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
