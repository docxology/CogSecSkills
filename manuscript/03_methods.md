# Source-Owned Authoring and Manuscript Generation {#sec:methods}

## Registry-to-Skill Construction

The manuscript is generated and maintained from the same project surfaces that the CLI validates. The registry is loaded first so the catalogue order, group membership, status, and AGEINT topic remain the plan of record. Canonical definitions under `definitions/` own the skill substance; `definitions --write` renders those definitions into on-disk `skill.yaml`, `SKILL.md`, `workflow.md`, and harness adapters. The manuscript asset generator then joins the registry and rendered typed skill specifications by skill id and emits supplemental Markdown, compact JSON and CSV exports, body figures, and a title-page cover image that explains installation into an agent harness. This source-first approach follows the reproducibility principle that outputs should retain enough workflow, version, and source context to be regenerated and inspected [@sandve2013reproducible; @wilkinson2016fair].

This source-first method prevents the manuscript from becoming a parallel catalogue. If skill substance changes, `cogsecskills definitions --check` proves the rendered skill tree still matches canonical YAML. If a skill name, trigger, tool verb, input, output, reference count, harness adapter, or source path changes, `cogsecskills manuscript-assets --check` detects drift in the generated manuscript inputs.

## Registry-to-Adapter Authoring Pipeline

Skill implementation follows a conservative pipeline:

1. A row in `registry/skills.yaml` declares the intended skill area and group.
2. A canonical definition under `definitions/<group>/<slug>.yaml` declares the tool plan, triggers, inputs, outputs, workflow steps, defensive boundary, evidence discipline, uncertainty rules, failure modes, and negative controls.
3. `definitions --write` renders a skill directory under `skills/<group>/<slug>/` with `skill.yaml`, `SKILL.md`, `workflow.md`, and one adapter per configured harness.
4. `skill.yaml` carries the generated neutral verbs, triggers, inputs, outputs, references, and AGEINT topic.
5. The validator checks that registry rows and implemented folders agree, that each adapter exists, and that tool verbs stay within the closed vocabulary.
6. The doctor command applies quality linting for thin, generic, incomplete, or unsafe skill content, including missing safe defensive negative controls and weak evidence or uncertainty labeling.
7. Tests exercise parsing, validation, definition drift, authoring, routing, reporting, configuration, and manuscript asset generation.

The optional harness profile registry sits beside the skill registry but has a different function. `registry/harness_profiles.yaml` records documented external profiles such as `gemini_cli`, `github_copilot`, `devin_local`, `devin_cascade`, `cursor`, `cline`, `aider`, `continue`, `jetbrains_ai`, `openai_agents_sdk`, `langgraph`, `microsoft_agent_framework`, `autogen`, `crewai`, `pydantic_ai`, `mcp_host`, and `perplexity_research`. These are documented external profiles, not validation targets. A profile becomes one of the configured structural adapters only when its id is added to `cogsecskills.yaml`, the skill tree is regenerated, and the adapter files pass validation. The default adapters remain `claude`, `codex`, and `hermes`. Profile classes are deliberately separated: instruction-file products, IDE rule systems, terminal pair-programming tools, SDK frameworks, MCP hosts, and research companions require different integration reviews even when they share the same neutral skill files.

## Generated Supplement and Figure Pipeline

`src/cogsecskills/manuscript_assets.py` is the producer for the generated manuscript layer. Its outputs are intentionally committed as manuscript source inputs because they support review and PDF rendering, but they remain generated. The command writes:

- `manuscript/S10_skill_catalogue.md`, a grouped catalogue of all skills with functionality, "Use when" text, verbs, inputs, outputs, AGEINT topic, reference count, and source path;
- `manuscript/S11_skill_metadata_matrix.md`, a compact matrix view of group counts, verb usage, AGEINT crosswalks, harness coverage, and figure inventory;
- `output/data/skill_catalogue.json` and `output/data/skill_catalogue.csv`, machine-readable exports of the same rows;
- deterministic PNG figures under `output/figures/`, including manuscript body figures and the configured title-page installation cover.

The generator treats static PNGs as the right output form because the manuscript is rendered to PDF and static web artifacts. Plot code uses explicit color maps for the seven real registry groups, direct labels where they reduce lookup, and subtitles that state the data scope. The chart data are not manually curated: counts, reference totals, harness coverage, AGEINT topics, verb matrices, and the install-cover skill counts are derived from the same `SkillRow` records used by the generated catalogue.

## Figure Question and Claim Contract

Each figure has a narrow analytical question. Taxonomy counts compare group size; the skill grid maps all 100 registry entries to one compact atlas; the verb heatmap counts closed-set tool verbs by group; the AGEINT crosswalk connects groups to teaching topics; the Plan/Build/Teach flow shows the source-to-render path; Reference Density compares declared source-reference backing; Harness Contract checks adapter coverage across the configured harness set, whose default is Claude, Codex, and Hermes; and the cover installation visual answers how a reader clones the public repository, validates it, and binds skills into an agent harness. These figures are descriptive views of the library metadata and installation contract. They do not measure field performance, adversary coverage, or user outcomes.

Reference Density is defined here as declared references per implemented skill within a taxonomy group. For group `g` in set `G`,

\begin{equation}
\label{eq:reference-density}
d_g := \frac{R_g}{N_g},
\end{equation}

where `R_g` is the total count of declared per-skill `refs` entries for implemented skills in `g`, and `N_g` is the number of implemented skills in `g`. The metric is metadata density, not evidence quality, empirical validity, or a proxy for operational effectiveness.

## Local Verification Gates

The local gate sequence is designed to catch different failure classes: `definitions --check` catches canonical-definition and rendered-skill drift, `validate` catches structural contract drift, `report` summarizes implementation status, `doctor` catches weak, generic, or incomplete skill content, `pytest` catches regression bugs, `manuscript-assets --check` catches generated-manuscript drift, and the sibling template renderer catches Markdown and PDF integration failures.

The stricter quality checks are deliberately local and textual. They require each canonical definition to include a defensive boundary, misuse redirect, evidence discipline, confidence rubric, uncertainty handling, privacy/legal constraints, failure modes, and negative controls. For sensitive skills, a generic safety sentence is insufficient: the negative controls must include an unsafe request redirected away from abuse, a safe defensive request pattern, wording specific to the skill, and no reused individual negative-control entry across the corpus. The same specificity pressure now applies to confidence rubrics, evidence requirements, and privacy/legal constraints: exact reused entries and group-only boilerplate fail the definition and doctor gates. Evidence requirements must distinguish evidence from inference, and uncertainty handling must preserve unknowns and credible alternatives. These checks raise the floor for the 100 rendered skills without claiming that the text has been field-validated.

The figure tests intentionally cover the inventory and palette contract as well as file existence. A missing generated PNG is easy to detect, but a stale palette can be more subtle: if the registry adds or renames a group, the visual system must be updated deliberately rather than silently falling back to an unrelated color.
