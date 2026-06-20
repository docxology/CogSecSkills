# AGENTS.md - Canonical Skill Definitions

This directory is the canonical source of skill substance. Every file is one
definition for one registry id at `definitions/<group>/<slug>.yaml`.

## Source Rules

- Edit definitions here when changing what a skill does, when to use it, what it
  produces, its workflow, defensive boundary, evidence discipline, confidence
  rubric, uncertainty handling, privacy/legal constraints, failure modes, or
  negative controls.
- Do not make corresponding hand edits under `skills/**`; regenerate rendered
  skills with `definitions --write`.
- Preserve the defensive-only boundary. Unsafe examples belong only as negative
  controls with refusal or safe defensive redirects.
- Do not invent references, DOI metadata, external validation, or field
  effectiveness claims.

## Required Gate

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills doctor
```
