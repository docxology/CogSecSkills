# CogSecSkills Documentation

The complete documentation map. Start with whichever row matches what you need.

| I want to… | Read |
|------------|------|
| **Understand what this is** | [`../README.md`](../README.md) — overview, quick start, the 3 artifacts |
| **Understand the design** | [`architecture.md`](architecture.md) — three artifacts, runner modules, harness model, authoring pipeline |
| **Know the exact rules a skill must satisfy** | [`skill-contract.md`](skill-contract.md) — the conformance contract `validate` enforces |
| **Add or deepen a skill** | [`authoring-skills.md`](authoring-skills.md) — `author` / `author-batch` / `scaffold`, the definition schema |
| **Use the command line** | [`cli.md`](cli.md) — every `cogsecskills` subcommand with examples |
| **Configure the library** | [`configuration.md`](configuration.md) — `cogsecskills.yaml`, configurable harnesses, quality thresholds |
| **Browse all 100 skills** | [`catalogue.md`](catalogue.md) — generated index, grouped (regenerate: `cogsecskills catalogue`) |
| **Learn the concepts** (the *why*) | [`ageint/`](ageint/README.md) — the AGEINT educational upstream + 7 topic primers |
| **Work in this repo as an agent** | [`../AGENTS.md`](../AGENTS.md) — contributor rules for AI agents |
| **See the ideal-state spec** | [`../ISA.md`](../ISA.md) — goals, criteria, decisions |

## The shape of the project (signpost)

```
CogSecSkills/
├── registry/            PLAN  — the catalogue of all skill areas
│   ├── skills.yaml          · 100 areas across 7 groups
│   └── groups.yaml          · the workflow-subfolder groups
├── skills/<group>/<slug>/   BUILD — one multiharness skill per technique
│   ├── skill.yaml           · harness-neutral spec (source of truth)
│   ├── SKILL.md             · Claude Code native entry point
│   ├── workflow.md          · the agentic procedure (verb-tagged steps)
│   └── harness/{claude,codex,hermes}.md   · per-harness tool bindings
├── docs/                TEACH — this folder + ageint/ upstream
├── src/cogsecskills/        the runner (spec, registry, validate, author, insights, cli)
└── cogsecskills.yaml        optional config (see configuration.md)
```

## Three commands to remember

```bash
python -m cogsecskills route "what should I use to rule out explanations?"  # find a skill
python -m cogsecskills validate    # prove the whole library conforms (0 errors)
python -m cogsecskills doctor       # validate + quality lint before publishing
```

Everything is defensive, educational, and accountable — these skills recognize,
assess, and defend against cognitive attack; they never operate one.
