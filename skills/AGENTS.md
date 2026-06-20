# AGENTS.md - Rendered Skill Tree

This directory is the harness-facing build output for the 100 implemented
skills.

## Editing Rules

- Treat `skill.yaml`, `SKILL.md`, `workflow.md`, and `harness/*.md` as rendered
  outputs for definition-owned skills.
- Change canonical substance in `definitions/<group>/<slug>.yaml`, then run
  `PYTHONPATH="src:." python -m cogsecskills definitions --write`.
- If a generated file looks wrong, fix the renderer or the canonical definition;
  do not patch the rendered file alone.
- Harness adapters must bind every declared neutral verb and must not request
  chain-of-thought. Use private model reasoning language where needed.

## Verification

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills doctor
```
