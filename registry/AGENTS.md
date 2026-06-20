# AGENTS.md - Registry Metadata

This directory defines catalogue and profile metadata.

## Files

- `skills.yaml` is the plan of record for all skill ids, names, groups, status,
  AGEINT topics, and summaries.
- `groups.yaml` is the group vocabulary.
- `harness_profiles.yaml` is documentation metadata for optional external
  profiles. It does not change validation until a profile id is copied into
  `cogsecskills.yaml`, regenerated, reviewed, and validated.

## Editing Rules

- Keep every skill id as `<group>.<slug>` and every group present in
  `groups.yaml`.
- If the skill count or group distribution changes, update README/docs/manuscript
  claims and the tests that intentionally lock the 100-skill corpus.
- Keep optional harness wording bounded: default adapters are `claude`, `codex`,
  and `hermes`; optional profiles are not live runtime certification.

## Verification

```bash
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills manuscript-assets --check
```
