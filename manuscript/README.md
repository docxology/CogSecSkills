# Manuscript - CogSecSkills

This directory is a template-format manuscript scaffold for:

**CogSecSkills: Multiharness Cognitive Security Skill Library**

A defensive, educational, harness-neutral library of Cognitive Security and analytic tradecraft skills with registry, AGEINT upstream, and conformance tests.

## File Inventory

- `config.yaml`
- `preamble.md`
- `references.bib`
- `00_abstract.md`
- `01_introduction.md`
- `02_system_context.md`
- `03_methods.md`
- `04_artifacts_and_evidence.md`
- `05_reproducibility.md`
- `06_limitations_and_next_steps.md`
- `S01_source_surface.md`
- `98_symbols_glossary.md`
- `99_references.md`
- `AGENTS.md`
- `README.md`
- `SYNTAX.md`

## Source Surfaces

| Surface | Role |
|---|---|
| `registry/` | Source directory to inspect before turning prose into claims. |
| `skills/` | Source directory to inspect before turning prose into claims. |
| `docs/ageint/` | Source directory to inspect before turning prose into claims. |
| `src/cogsecskills/` | Source directory to inspect before turning prose into claims. |
| `tests/` | Source directory to inspect before turning prose into claims. |

## Verification

From the sibling template checkout, after `link-projects` has synced the sidecar:

```bash
uv run python -m infrastructure.orchestration link-projects
uv run python -m infrastructure.validation.cli markdown projects/working/CogSecSkills/manuscript/
```

Render only after replacing scaffold prose with project-bound evidence and checking any project-local gates documented in the repository root.
