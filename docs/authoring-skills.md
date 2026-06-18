# Authoring skills

This guide explains how to add a new CogSecSkill or deepen an existing one.

CogSecSkills separates **substance** from **format**. An author supplies the
substance of a technique — its tool plan, inputs/outputs, the real step-by-step
procedure, and the anti-criteria that keep it honest. The library supplies the
format: the six conforming files every skill needs (`skill.yaml`, `SKILL.md`,
`workflow.md`, and one harness adapter per supported harness under `harness/`).
Because the renderer generates the adapters from the declared tool verbs, an
authored skill passes the validator **by construction** — there are no format
stragglers no matter how many skills are authored in parallel.

There are three ways to produce a skill. Prefer them in this order:

1. **`author`** — deterministic render from a JSON *definition* (preferred).
2. **`author-batch`** — render a `_def.json` from every skill folder at once.
3. **`scaffold`** — generate a hand-editable skeleton, then deepen it by hand.

Whichever path you take, always finish with `validate` and `doctor`.

See also: [`skill-contract.md`](skill-contract.md) for the field-by-field
meaning of a skill, [`cli.md`](cli.md) for the full command reference, and
[`configuration.md`](configuration.md) for the optional `cogsecskills.yaml`
(which controls, among other things, the harness set every command targets).

---

## The closed verb set

Every tool a skill declares uses a verb from a single **closed vocabulary**.
This is what lets the renderer bind each verb to a concrete tool on every
harness. The eight verbs are:

```
read      search    write    exec
reason    web       delegate ask
```

A definition that uses any other verb is rejected. `read` covers ingesting
supplied material; `search` and `web` cover local and external lookup; `write`
emits the product; `exec` runs commands or gates; `reason` applies the
technique; `delegate` fans out sub-analyses; `ask` surfaces a decision to the
caller. Every harness today realises the full set (see
[`configuration.md`](configuration.md) for how an unknown harness is handled).

---

## Path 1 — `author` (deterministic, preferred)

You write a JSON **definition** of the technique, then render it:

```bash
python -m cogsecskills author def.json
```

The renderer fills `name`, `group`, `summary`, and `ageint_topic` from the
**registry** (`registry/skills.yaml`) — the definition does not (and should
not) restate them. The `id` in the definition must already exist in the
registry. The renderer then writes all six files and binds **every declared
verb** in each harness adapter, so the result conforms automatically.

### Definition schema (full)

A definition is a JSON object with these keys:

| Key | Type | Required | Meaning |
| --- | --- | --- | --- |
| `id` | string | **yes** | `<group>.<slug>`; must exist in the registry. |
| `description` | string | no | 2–4 sentences. Falls back to the registry `summary`. |
| `tags` | `[string]` | no | Defaults to `["cognitive-security", <group>]`. |
| `triggers` | `[string]` | no | Phrases that should route to this skill. Defaults to `[<name lowercased>]`. |
| `tools` | `[{verb, purpose}]` | **yes (≥1)** | Each `verb` from the closed set; each `purpose` non-empty. |
| `inputs` | `[{name, type, required, description}]` | no | Defaults to a single `context` text input. |
| `outputs` | `[{name, type, description}]` | no | Defaults to a single `product` markdown output. |
| `references` | `[string]` | no | Citations. Defaults to `[]`. |
| `when_to_use` | `[string]` | no | Bullets for `SKILL.md` → "When to use". |
| `what_it_produces` | `[string]` | no | Bullets for `SKILL.md` → "What it produces". |
| `key_discipline` | `[string]` | no | Bullets for `SKILL.md` → "Key discipline". |
| `workflow_steps` | `[{verbs:[string], title, text}]` | **yes (≥1)** | The real procedure; each step names the verb(s) it uses. |
| `anti_criteria` | `[string]` | **yes (≥1)** | Things that must NOT happen — the integrity guard. |
| `harness_bindings` | `{harness: {verb: [tool, note]}}` | no | Override a default binding for a specific harness/verb. Defaults are used otherwise. |
| `version` | string | no | Defaults to `"0.1.0"`. |

Notes:

- Each `tools[].verb` is coerced and validated against the closed set; an
  unknown verb or an empty `purpose` is a hard error.
- Each `workflow_steps[].verbs` entry is also validated against the closed set.
  A step with no `verbs` defaults to `reason`.
- `harness_bindings` lets you override the wording of an adapter row for a
  particular harness and verb — for example to point `exec` at a project's own
  gate. Anything you do not override uses the built-in default binding for that
  harness, so partial overrides are fine.

### Worked example — `sat.what_if_analysis`

Assume the registry already carries this entry (it would supply the `name`,
`group`, `summary`, and `ageint_topic`):

```yaml
- {id: sat.what_if_analysis, name: What If? Analysis, group: sat,
   status: planned, ageint_topic: structured-analytic-techniques,
   summary: "Assume a surprising event has occurred, then reason backward to the path that produced it."}
```

Write `what_if.json`:

```json
{
  "id": "sat.what_if_analysis",
  "description": "What If? Analysis assumes a surprising or high-impact event has already occurred, then reasons backward to reconstruct the plausible path that produced it. By treating the surprise as established fact it bypasses the 'that can't happen here' reflex that suppresses low-probability, high-consequence scenarios. In cognitive-security work it is used to pressure-test assessments against adversary moves and shocks that a forward-only forecast would dismiss.",
  "tags": ["cognitive-security", "sat", "foresight"],
  "triggers": [
    "what if",
    "assume this happened",
    "imagine the surprise",
    "reason backward from a shock"
  ],
  "tools": [
    {"verb": "read", "purpose": "ingest the current assessment and the surprising event to be assumed"},
    {"verb": "reason", "purpose": "reconstruct plausible pathways from the assumed event backward to the present"},
    {"verb": "write", "purpose": "emit the pathway analysis, indicators, and hedges"}
  ],
  "inputs": [
    {"name": "assessment", "type": "text", "required": true,
     "description": "The current analytic line of march or forecast being stress-tested"},
    {"name": "surprising_event", "type": "text", "required": true,
     "description": "The high-impact event to assume has occurred"}
  ],
  "outputs": [
    {"name": "pathway_analysis", "type": "markdown",
     "description": "Reconstructed pathways to the event, each with leading indicators and a hedge"}
  ],
  "references": [
    "Pherson, R. H., & Heuer, R. J. (2021). Structured Analytic Techniques for Intelligence Analysis (3rd ed.). CQ Press. Chapter: What If? Analysis."
  ],
  "when_to_use": [
    "a low-probability, high-consequence event would invalidate the current assessment",
    "the team is anchored on the most likely outcome and dismissing tail risks"
  ],
  "what_it_produces": [
    "ranked pathways to the assumed surprise, each grounded in observable indicators"
  ],
  "key_discipline": [
    "treat the surprising event as fact, not as a possibility, for the whole exercise"
  ],
  "workflow_steps": [
    {"verbs": ["read"], "title": "Assume the surprise as fact",
     "text": "Read the current assessment and state the surprising event in the past tense: 'The event has occurred.' Treat this as established for the rest of the exercise; do not hedge it back into the conditional."},
    {"verbs": ["reason"], "title": "Reconstruct the pathways",
     "text": "Working backward from the event to today, lay out the chains of plausible developments that could have produced it. Include adversary adaptation, assumption breaks, and external shocks. Generate several distinct pathways, not one."},
    {"verbs": ["reason", "write"], "title": "Indicators and hedges",
     "text": "For each pathway, name a leading indicator that would appear early if it were unfolding, and a hedge or contingency. Rank pathways by plausibility and consequence."},
    {"verbs": ["write"], "title": "Document",
     "text": "Produce the pathway-analysis document. Flag which assumptions, if broken, most increase the event's plausibility, and which indicators warrant active monitoring."}
  ],
  "anti_criteria": [
    "do not relax 'the event has occurred' into 'the event might occur' — the conditional frame restores the dismissal the technique is built to overcome",
    "do not accept a pathway without at least one observable leading indicator — an unmonitorable pathway is not actionable"
  ]
}
```

Render it:

```bash
python -m cogsecskills author what_if.json
```

This writes (relative to the project root):

```
skills/sat/what_if_analysis/
├── skill.yaml
├── SKILL.md
├── workflow.md
└── harness/
    ├── claude.md
    ├── codex.md
    └── hermes.md
```

The generated `skill.yaml` merges your definition with the registry-supplied
`name`/`group`/`summary`/`ageint_topic` and sets `status: implemented`. The
`workflow.md` carries each step you wrote, with its verb(s) noted in the
heading, followed by the anti-criteria and the AGEINT upstream link. Each
`harness/<name>.md` adapter binds your three verbs (`read`, `reason`, `write`)
to that harness's concrete tools.

After authoring, flip the registry status if it is still `planned`/`stub`
(the batch command below does this for you), then validate and doctor:

```bash
python -m cogsecskills validate
python -m cogsecskills doctor
```

---

## Path 2 — `author-batch`

When you have many definitions to render at once, drop a `_def.json` file in
each skill folder under `skills/<group>/<slug>/` and run:

```bash
python -m cogsecskills author-batch
```

For each `_def.json` it finds, the command infers the `id` from the folder
path (`<group>.<slug>`), renders the six files, deletes the `_def.json`, and —
once all renders succeed — **promotes** each rendered skill's registry status
from `stub`/`planned` to `implemented`. It reports `{"rendered": [...], "failed":
{...}}`; a definition that fails to render leaves its `_def.json` in place and is
listed under `failed`, while the rest still render.

This is exactly how the **92 non-exemplar skills** in this library were built:
parallel agents each wrote a `_def.json` into its skill folder, then a single
`author-batch` rendered them all and promoted the registry in one pass. Because
the renderer binds verbs by construction, a hundred skills authored this way are
all format-conformant without any manual reconciliation.

---

## Path 3 — `scaffold`

When you want a hand-edited skeleton rather than a fully specified definition,
scaffold the registry entry directly:

```bash
python -m cogsecskills scaffold sat.what_if_analysis
```

This reads the registry entry and writes the same six-file set, pre-populated
from the catalogue row with a placeholder three-verb tool plan (`read`,
`reason`, `write`) and `status: stub`. The structure already conforms; you then
**deepen the six files by hand** — flesh out the real `workflow.md` steps,
sharpen the tool plan and `tools` block in `skill.yaml`, write genuine
anti-criteria, add references, and update each harness adapter if you changed
the verb set. Flip `status` to `implemented` in both `skill.yaml` and the
registry when the content is real, then validate and doctor.

Scaffolding an id whose directory already exists fails unless you pass an
overwrite flag; overwrite **replaces** the directory rather than merging, so
stale files from a prior partial scaffold cannot survive and validate clean.

---

## Adding a brand-new skill AREA

The three paths above turn an existing registry entry into files. To introduce
a skill area that is not yet catalogued:

1. **Add a row to `registry/skills.yaml`** with `status: planned`. The `id` is
   `<group>.<slug>`, and the **`group` must already exist** in
   `registry/groups.yaml`. Include `name`, `summary`, and `ageint_topic`:

   ```yaml
   - {id: sat.what_if_analysis, name: What If? Analysis, group: sat,
      status: planned, ageint_topic: structured-analytic-techniques,
      summary: "Assume a surprising event has occurred, then reason backward to the path that produced it."}
   ```

   If you need a brand-new *group*, add it to `registry/groups.yaml` first
   (with its own `id`, `title`, `description`, and `ageint_topic`); validation
   requires every catalogued group to be defined there.

2. **Build the skill** via `author`, `author-batch`, or `scaffold` as above.
   These commands flip (or you flip) the status to `implemented`.

3. **Regenerate the catalogue** so the docs match the registry:

   ```bash
   python -m cogsecskills catalogue --markdown --output docs/catalogue.md
   ```

---

## Always finish: validate and doctor

Two gates close every authoring change.

`validate` cross-checks the **plan vs. the build**: every on-disk skill is
catalogued, every `implemented` entry exists on disk, every skill declares an
adapter for each configured harness, and every harness can realise every verb a
skill uses. Run it until it reports **0 errors**:

```bash
python -m cogsecskills validate
```

`doctor` runs `validate` and then **quality-lints** each skill against the
thresholds in [`configuration.md`](configuration.md): `min_workflow_steps`
(default 3), `min_anti_criteria` (default 2), and `require_references` (default
false). A thin scaffold that conforms structurally can still fail `doctor`
until you deepen it:

```bash
python -m cogsecskills doctor
```

When both come back clean, the skill is done.
