# DOCS-01: docs/harness-cookbook.md references a non-existent skill id counterintelligence.elicitation_resistance

|Field|Value|
|---|---|
|Audit ID|`DOCS-01`|
|Lens|`DOCS`|
|Severity|`medium`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/21) |

## Summary
The worked Hermes bind-and-run example in docs/harness-cookbook.md invokes `python -m cogsecskills show counterintelligence.elicitation_resistance`, but that skill id does not exist anywhere in the registry, definitions, or skills tree. The real id is `counterintelligence.elicitation_attempt_recognition`, so a reader copying the example gets an "unknown skill id" error (cli.py `_cmd_show` exits 1 for unknown ids) instead of the documented behavior. Red team adjusted severity from high to medium because it is a broken doc example command — one line in one doc with a trivially substitutable fix — not a broken contract or shipped wrong result.

## Evidence
docs/harness-cookbook.md:125 (verbatim):

```
PYTHONPATH="src:." python -m cogsecskills show counterintelligence.elicitation_resistance
```

Repo-wide grep for `elicitation_resistance` matches only this one line. The correct id is confirmed at:
- `definitions/counterintelligence/elicitation_attempt_recognition.yaml:1`
- `registry/skills.yaml:109`
- `skills/counterintelligence/elicitation_attempt_recognition/SKILL.md:2`

No gate or test enforces that cookbook `show` command ids resolve; the doc command is not exercised in CI, so nothing mitigates the error.

## Impact
Readers following the cookbook's Hermes bind-and-run flow hit an unknown-skill-id error and may conclude the suite is broken rather than the doc. Every registry entry, skill file, catalogue, dashboard, and worked example uses the correct id, so the cookbook line is the sole stale reference.

## Remediation
Replace the id in docs/harness-cookbook.md:125 with `counterintelligence.elicitation_attempt_recognition`. Optionally add a lightweight docs-lint step that validates every `cogsecskills show <id>` occurrence in docs against registry/skills.yaml to prevent recurrence.

## Audit trail
- Discovered by the DOCS lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Confirmed the quote and the uniqueness claim: docs/harness-cookbook.md:125 is the sole occurrence of `elicitation_resistance` anywhere in the repo; every registry entry, skill file, catalogue, dashboard, and worked example uses `elicitation_attempt_recognition`. No gate or test enforces that cookbook `show` command ids resolve (the doc command is not exercised in CI), so nothing mitigates it — a reader copying the Hermes bind-and-run example hits an unknown-skill-id error. Severity adjusted high→medium: it is a broken doc example command, not a broken contract or shipped wrong result — limited blast radius (one line in one doc), trivially fixable by substituting the correct id as proposed. Mechanism and fix are correct as stated.
<!-- PR and issue links are added to the Tracking field after filing. -->