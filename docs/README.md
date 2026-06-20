# CogSecSkills Documentation

The complete documentation map. Start with whichever row matches what you need.

| I want to… | Read |
|------------|------|
| **Understand what this is** | [`../README.md`](../README.md) — overview, quick start, the 3 artifacts |
| **Start from clone to first harness use** | [`../QUICKSTART.md`](../QUICKSTART.md) — install, validate, route, inspect, and bind one skill |
| **Understand the design** | [`architecture.md`](architecture.md) — three artifacts, runner modules, harness model, authoring pipeline |
| **Install into an agent harness** | [`harness-installation.md`](harness-installation.md) — clone, validate, route, and bind `SKILL.md`/`workflow.md`/`harness/<name>.md` |
| **Use harness-specific snippets** | [`harness-cookbook.md`](harness-cookbook.md) — Codex, Claude, Hermes, and custom-harness handoff patterns |
| **See sample harness transcripts** | [`../examples/harness-smoke-transcripts.md`](../examples/harness-smoke-transcripts.md) — local non-secret transcript fixtures |
| **See one worked example per group** | [`../examples/group-worked-examples.md`](../examples/group-worked-examples.md) — defensive output shapes across all seven groups |
| **See one worked example per skill** | [`skill-worked-examples.md`](skill-worked-examples.md) — generated deterministic local examples for all 100 skills (regenerate: `cogsecskills examples --write`) |
| **Review offline output fixtures** | [`evaluation-readiness.md`](evaluation-readiness.md) — generated 28-scenario offline review matrix (regenerate: `cogsecskills evals --write`) |
| **Scan the evidence ladder** | [`quality-dashboard.md`](quality-dashboard.md) — generated 100-skill dashboard with quality, scenarios, offline evals, worked examples, harnesses, references, and claim-boundary status |
| **Check release claims** | [`release-claim-matrix.md`](release-claim-matrix.md) — generated local release metadata and claim-boundary matrix |
| **Know the exact rules a skill must satisfy** | [`skill-contract.md`](skill-contract.md) — the conformance contract `validate` enforces |
| **Add or deepen a skill** | [`authoring-skills.md`](authoring-skills.md) — canonical `definitions/`, `definitions --write|--check`, `author`, and `scaffold` |
| **Use the command line** | [`cli.md`](cli.md) — every `cogsecskills` subcommand with examples |
| **Configure the library** | [`configuration.md`](configuration.md) — `cogsecskills.yaml`, configurable harnesses, quality thresholds |
| **Check curated defensive scenarios** | [`cli.md#scenarios--check-deterministic-defensive-readiness-fixtures`](cli.md#scenarios--check-deterministic-defensive-readiness-fixtures) — route and quality checks for safe-use and unsafe-redirect fixtures |
| **Keep claims bounded** | [`claim-boundaries.md`](claim-boundaries.md) — what local gates prove and do not prove |
| **Prepare future output reviews** | [`analyst-output-review.md`](analyst-output-review.md) — lightweight rubric for scenario-output review |
| **Understand connector limits** | [`connector-boundaries.md`](connector-boundaries.md) — optional OSINT/web connector boundaries |
| **Plan future validation carefully** | [`future-validation-protocols.md`](future-validation-protocols.md) — baseline, usability, connector, and DOI protocols marked as future work |
| **Prepare a release candidate** | [`release-checklist.md`](release-checklist.md) — source, style, type, manuscript, and human review gates |
| **Browse all 100 skills** | [`catalogue.md`](catalogue.md) — generated index, grouped (regenerate: `cogsecskills catalogue`) |
| **Regenerate manuscript supplements and figures** | [`cli.md#manuscript-assets--generate-or-check-manuscript-supplements-and-figures`](cli.md#manuscript-assets--generate-or-check-manuscript-supplements-and-figures) — `manuscript-assets --write|--check` |
| **Learn the concepts** (the *why*) | [`ageint/`](ageint/README.md) — the AGEINT educational upstream + 7 topic primers |
| **Work in this repo as an agent** | [`../AGENTS.md`](../AGENTS.md) — contributor rules for AI agents |
| **See the ideal-state spec** | [`../ISA.md`](../ISA.md) — goals, criteria, decisions |

## The shape of the project (signpost)

```
CogSecSkills/
├── registry/            PLAN  — the catalogue of all skill areas
│   ├── skills.yaml          · 100 areas across 7 groups
│   └── groups.yaml          · the workflow-subfolder groups
├── definitions/<group>/<slug>.yaml
│                           BUILD source — canonical skill definitions
├── skills/<group>/<slug>/   BUILD — one multiharness skill per technique
│   ├── skill.yaml           · generated harness-neutral spec
│   ├── SKILL.md             · Claude Code native entry point
│   ├── workflow.md          · the agentic procedure (verb-tagged steps)
│   └── harness/{claude,codex,hermes}.md   · per-harness tool bindings
├── scenarios/           CHECK — curated safe-use and unsafe-redirect fixtures
├── examples/            EXAMPLES — source worked examples, harness transcripts, group examples
├── docs/                TEACH — this folder + ageint/ upstream
│   └── harness-installation.md · install and bind the library into an agent harness
├── manuscript/             manuscript source, including generated S10/S11 supplements
├── output/                 rebuild outputs: data exports, figures, PDF/HTML/slides
├── src/cogsecskills/        the runner (spec, registry, validate, author, insights, manuscript assets, cli)
└── cogsecskills.yaml        optional config (see configuration.md)
```

## Three commands to remember

```bash
python -m cogsecskills route "what should I use to rule out explanations?"  # find a skill
python -m cogsecskills definitions --check  # prove definitions and rendered skills agree
python -m cogsecskills validate    # prove the whole library conforms (0 errors)
python -m cogsecskills doctor       # validate + quality lint before publishing
python -m cogsecskills scenarios --check  # prove curated defensive scenarios still route and bind
python -m cogsecskills examples --check  # prove generated worked examples are current
python -m cogsecskills evals --check  # prove offline output-review fixtures are current
python -m cogsecskills dashboard --check  # prove the generated quality dashboard is current
python -m cogsecskills release-metadata --check  # prove local release metadata is current
python -m cogsecskills manuscript-assets --check  # prove generated manuscript assets are current
```

Everything is defensive, educational, and accountable — these skills recognize,
assess, and defend against cognitive attack; they never operate one.
