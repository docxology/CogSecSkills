# Authoring skills

This guide explains how to add a new CogSecSkill or deepen an existing one. The
library is mature — 100 skills across 7 groups (`sat`, `cognitive_security`,
`critical_review`, `osint_integrity`, `counterintelligence`,
`information_environment`, `research_methods`) — so most authoring now means
**deepening** an existing skill's definition rather than introducing a new one.
Hold every change to the bar the corpus already meets.

## The canonical workflow in one line

> Edit `definitions/<group>/<slug>.yaml` → `definitions --write` → `validate` and `doctor`.

That is the whole loop. You change the **substance** in one canonical YAML file,
the renderer regenerates the conforming **files** from it, and the two gates
prove the change is real and skill-specific. Everything below expands this loop;
the other paths (`author`, `author-batch`, `scaffold`) exist for one-offs and
bootstrapping, but the canonical `definitions/` file is the single source of
truth for any skill that ships.

## Substance vs. format

CogSecSkills separates **substance** from **format**. An author supplies the
substance of a technique in canonical YAML under `definitions/<group>/<slug>.yaml`:
its tool plan, inputs/outputs, step-by-step procedure, anti-criteria, defensive
boundary, evidence discipline, uncertainty rules, privacy/legal constraints,
failure modes, and negative controls. The library supplies the format: the
conforming files every skill needs (`skill.yaml`, `SKILL.md`, `workflow.md`,
and one harness adapter per configured harness under `harness/`).
Because the renderer generates the adapters from the declared tool verbs, an
authored skill passes the validator **by construction** — there are no format
stragglers no matter how many skills are authored in parallel.

This separation is why deepening is cheap: you never touch a generated file.
Edit the definition, re-render, and the six conforming files follow. If you find
yourself hand-editing a `SKILL.md` or a `harness/<name>.md`, stop — that change
belongs in the definition, and `definitions --check` will flag the drift.

There are four ways to produce a skill. Prefer them in this order:

1. **`definitions --write|--check`** — repo-wide render/check from canonical YAML definitions (preferred).
2. **`author`** — deterministic one-skill render from a JSON or YAML definition.
3. **`author-batch`** — compatibility path that renders `_def.json` files from skill folders.
4. **`scaffold`** — generate a hand-editable skeleton, then deepen it by hand.

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

## Path 1 — canonical `definitions/` (repo-wide, preferred)

Write or update `definitions/<group>/<slug>.yaml`, then render and check the
library:

```bash
python -m cogsecskills definitions --write
python -m cogsecskills definitions --check
```

`--write` bootstraps missing definitions from existing rendered skills, writes
stable YAML, and renders every definition-owned skill folder. `--check` fails
when any registry entry lacks a definition, a definition contains unknown or
stale schema fields, or any rendered `skills/**` file differs from what its
definition would produce.

### Quality fields must be grammatical and skill-specific (the de-stitch rule)

The single most important authoring discipline is how you write the quality
fields: `evidence_requirements`, `confidence_rubric`, `uncertainty_handling`,
`privacy_legal_constraints`, `failure_modes`, `negative_controls`, and the
`SKILL.md` prose (`when_to_use`, `what_it_produces`, `key_discipline`).

Early in the library's life these fields were **machine-stitched** — assembled
by concatenating the skill name with a generic template fragment. The result
read as boilerplate: grammatically awkward, interchangeable between skills, and
hollow. The whole corpus was de-stitched into **grammatical, domain-specific
prose**, and `doctor` now enforces that bar (see the gate below). When you
deepen or add a skill, write these fields the way you would write them for a
reviewer who knows the technique:

- **Grammatical.** Each entry is a real sentence or clause, not a name with a
  suffix bolted on. "Label every claim with its source and the date it was
  observed" — not "what_if_analysis evidence requirement."
- **Skill-specific.** The entry must only make sense for *this* technique. If you
  could paste it verbatim into another skill and it would still fit, it is too
  generic and `doctor` will reject the repeated boilerplate.
- **Concrete.** Name the actual artifact, the actual adversary move, the actual
  unsafe request this skill must refuse. A negative control that says "refuse
  unsafe requests" is worthless; "refuse a request to fabricate a corroborating
  source for an uncorroborated claim" is a real control.

#### Mini-example — stitched vs. de-stitched

For `sat.what_if_analysis`, the difference looks like this.

**Machine-stitched (rejected by `doctor`):**

```yaml
negative_controls:
  - "Unsafe: what_if_analysis used for a manipulation goal — refuse."
  - "Safe: what_if_analysis used defensively — proceed."
failure_modes:
  - "what_if_analysis can fail if inputs are bad."
```

**De-stitched (grammatical, skill-specific, concrete):**

```yaml
negative_controls:
  - "Unsafe: a request to reason backward from an assumed shock in order to script a deception or disinformation pathway — refuse and redirect to defensive scenario stress-testing."
  - "Safe: assume a named high-impact event has occurred against the team's own assessment, reconstruct plausible pathways, and surface leading indicators to monitor."
failure_modes:
  - "Relaxing 'the event has occurred' back into the conditional, which restores the dismissal reflex the technique exists to overcome."
  - "Producing pathways with no observable leading indicator, leaving the analysis unmonitorable and therefore unactionable."
```

The second pair names the actual technique behavior, the actual unsafe ask, and
the actual way the analysis goes wrong. That is the bar for every quality field.

---

## Path 2 — `author` (single-skill render)

You write a JSON or YAML **definition** of the technique, then render it:

```bash
python -m cogsecskills author definition.yaml
```

The renderer fills `name`, `group`, `summary`, and `ageint_topic` from the
**registry** (`registry/skills.yaml`) — the definition does not (and should
not) restate them. The `id` in the definition must already exist in the
registry. The renderer then writes all six files and binds **every declared
verb** in each harness adapter, so the result conforms automatically.

### Canonical definition schema

A canonical definition is a YAML mapping with these keys. One-off `author`
input may be JSON or YAML, but persistent repo definitions are YAML.

| Key | Type | Required | Meaning |
| --- | --- | --- | --- |
| `id` | string | **yes** | `<group>.<slug>`; must exist in the registry. |
| `description` | string | **yes** | 2–4 sentences. Falls back only for one-off authoring, not canonical checks. |
| `tags` | `[string]` | **yes** | Skill tags used for routing and catalogue navigation. |
| `triggers` | `[string]` | **yes** | Phrases that should route to this skill. |
| `tools` | `[{verb, purpose}]` | **yes (≥1)** | Each `verb` from the closed set; each `purpose` non-empty. |
| `inputs` | `[{name, type, required, description}]` | **yes** | Declared inputs for the harness-neutral spec. |
| `outputs` | `[{name, type, description}]` | **yes** | Declared outputs for the harness-neutral spec. |
| `references` | `[string]` | **key required; may be empty** | Per-skill metadata references; not manuscript citation keys. Do not invent entries. |
| `when_to_use` | `[string]` | **yes** | Bullets for `SKILL.md` → "When to use". |
| `what_it_produces` | `[string]` | **yes** | Bullets for `SKILL.md` → "What it produces". |
| `key_discipline` | `[string]` | **yes** | Bullets for `SKILL.md` → "Key discipline". |
| `workflow_steps` | `[{verbs:[string], title, text}]` | **yes (≥1)** | The real procedure; each step names the verb(s) it uses. |
| `anti_criteria` | `[string]` | **yes (≥1)** | Things that must NOT happen — the integrity guard. |
| `defensive_boundary` | string | **yes** | What the skill is allowed to do defensively and what it must not become. |
| `misuse_redirect` | string | **yes** | Refusal/redirect rule for manipulation, deception, targeting, evasion, or offensive guidance. |
| `evidence_requirements` | `[string]` | **yes** | Evidence labeling and traceability requirements. |
| `confidence_rubric` | `[string]` | **yes** | Calibrated confidence labels and what each means. |
| `uncertainty_handling` | `[string]` | **yes** | How to preserve unknowns, alternatives, and next evidence. |
| `privacy_legal_constraints` | `[string]` | **yes** | Authorization, privacy, protected-trait, and legal-risk boundaries. |
| `failure_modes` | `[string]` | **yes** | Common ways the skill can produce bad or unsafe work. |
| `negative_controls` | `[string]` | **yes** | At least one unsafe refusal/redirect example and one safe defensive example. |
| `harness_bindings` | `{harness: {verb: [tool, note]}}` | no | Override a default binding for a specific harness/verb. Defaults are used otherwise. |

Notes:

- Each `tools[].verb` is coerced and validated against the closed set; an
  unknown verb or an empty `purpose` is a hard error.
- Each `workflow_steps[].verbs` entry is also validated against the closed set.
  A step with no `verbs` defaults to `reason`.
- Canonical definitions reject unknown top-level fields; this catches typos
  before they become silent documentation drift.
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

Write `definitions/sat/what_if_analysis.yaml` or a one-off `what_if.yaml`:

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
python -m cogsecskills author what_if.yaml
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

## Path 3 — `author-batch`

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

## Path 4 — `scaffold`

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

The paths above turn an existing registry entry into files. To introduce a
skill area that is not yet catalogued:

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

2. **Build the skill** by adding `definitions/<group>/<slug>.yaml` and running
   `definitions --write`, or via `author`, `author-batch`, or `scaffold` as above.
   These commands flip (or you flip) the status to `implemented`.

3. **Regenerate the catalogue** so the docs match the registry:

   ```bash
   python -m cogsecskills catalogue --markdown --output docs/catalogue.md
   ```

---

## Always finish: definitions check, validate, and doctor

Three gates close every authoring change.

`definitions --check` proves that every registry entry has one canonical
definition and that the rendered `skills/**` files match those definitions:

```bash
python -m cogsecskills definitions --check
```

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
false). It also rejects generic quality text: negative controls, confidence
rubrics, evidence requirements, and privacy/legal constraints must be
skill-specific, and repeated individual boilerplate entries across the corpus
fail the gate. A thin scaffold that conforms structurally can still fail
`doctor` until you deepen it:

```bash
python -m cogsecskills doctor
```

When both come back clean, the skill is done.

---

## Authoring checklist

Run through this before you call a definition finished. It mirrors what the
gates enforce, plus the judgment calls they cannot make for you.

**Substance**

- [ ] The technique is described accurately in `description` (2–4 sentences) and
      a reviewer who knows the field would recognize it.
- [ ] `workflow_steps` capture the *real* procedure (at least
      `min_workflow_steps`, default 3), each naming the verb(s) it uses.
- [ ] `anti_criteria` (at least `min_anti_criteria`, default 2) state things
      that must NOT happen — the integrity guard, not restatements of the steps.
- [ ] `tools` use only the closed verb set, each with a non-empty, specific
      `purpose`.

**Quality fields (the de-stitch rule)**

- [ ] Every quality field is **grammatical** — real sentences, never a skill
      name with a suffix stitched on.
- [ ] Every quality field is **skill-specific** — it would not fit verbatim in
      any other skill.
- [ ] `negative_controls` include at least one concrete unsafe refusal/redirect
      and one concrete safe defensive use.
- [ ] `defensive_boundary` and `misuse_redirect` keep the skill strictly
      defensive and accountable, with no operational-attack guidance.
- [ ] No quality entry is duplicated boilerplate shared across the corpus.

**Format and gates**

- [ ] Built from the canonical `definitions/<group>/<slug>.yaml` and rendered
      with `definitions --write` (not by hand-editing generated files).
- [ ] Registry `status` is `implemented` once the content is real.
- [ ] `definitions --check`, `validate`, and `doctor` all come back clean.

The flagship `red_team_review` skill is the reference for this bar: its
definition carries an explicit adversary model, an attack-surface taxonomy, an
exploitability×impact scoring rubric, and a go/no-go output — every field
grammatical, concrete, and specific to red-team review. Read its definition when
you want a model of how deep a mature CogSecSkill should go.
