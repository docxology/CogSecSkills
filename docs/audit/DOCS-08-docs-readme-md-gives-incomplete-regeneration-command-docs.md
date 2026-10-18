# DOCS-08: docs/README.md gives an incomplete regeneration command for docs/catalogue.md

|Field|Value|
|---|---|
|Audit ID|`DOCS-08`|
|Lens|`DOCS`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/24) |

## Summary
The catalogue row in docs/README.md tells readers to regenerate the generated index with bare `cogsecskills catalogue`, but that form only prints the markdown to stdout (cli.py `_cmd_catalogue` writes a file only when `--output` is passed) — so following the hint leaves docs/catalogue.md unregenerated while exiting 0, and the stdout output can be mistaken for success. The correct full command (`catalogue --markdown --output docs/catalogue.md`) is documented in four other authoritative places.

## Evidence
docs/README.md:30 (verbatim; the finding cited line 22, the row is at line 30 in the current file):

```
| **Browse all 100 skills** | [`catalogue.md`](catalogue.md) — generated index, grouped (regenerate: `cogsecskills catalogue`) |
```

cli.py:191-195 (`_cmd_catalogue`) only writes a file when `--output` is passed; otherwise it prints the markdown to stdout with exit 0. The correct full command is documented elsewhere: CLAUDE.md:34 (`catalogue --markdown --output docs/catalogue.md`), README.md:154, docs/cli.md:610/780, docs/authoring-skills.md:383. No gate enforces docs/catalogue.md staleness (drift checks exist only for manuscript-assets, evals, examples, dashboard — not docs/catalogue.md), so this doc hint is the only regeneration guidance for that file.

## Impact
Hygiene-level doc inaccuracy with no runtime impact: a contributor following the docs/README hint runs the bare command, sees success (exit 0, markdown printed), and the committed docs/catalogue.md stays stale — or worse, redirects stdout thinking that is the documented flow. Since no staleness gate covers docs/catalogue.md, this hint is the only regeneration guidance for the file, making the wrong instruction load-bearing.

## Remediation
Change the regenerate hint in docs/README.md:30 to `cogsecskills catalogue --markdown --output docs/catalogue.md`, matching CLAUDE.md:34, README.md:154, docs/cli.md:610/780, and docs/authoring-skills.md:383.

## Audit trail
- Discovered by the DOCS lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Confirmed the quote and mechanism. docs/README.md:30 (not 22) gives the regenerate hint as bare `cogsecskills catalogue`. cli.py:191-195 (`_cmd_catalogue`) only writes a file when `--output` is passed; otherwise it prints the markdown to stdout with exit 0 — so following the hint leaves docs/catalogue.md unregenerated. Correct full command is documented elsewhere: CLAUDE.md:34 (`catalogue --markdown --output docs/catalogue.md`), README.md:154, docs/cli.md:610/780, docs/authoring-skills.md:383. Minor correction to the finding's supporting claim: CONTRIBUTING.md:53 does NOT document the --output form correctly either — it suggests `catalogue > docs/catalogue.md` (stdout redirect), which does regenerate the file equivalently (modulo the trailing-newline nuance: --output appends an explicit `\n`, print adds one via print, so both produce identical bytes; the finding's aside that README.md and CLAUDE.md 'correctly document' holds for README.md and CLAUDE.md but CONTRIBUTING.md uses a redirect variant). No gate enforces docs/catalogue.md staleness (drift checks exist only for manuscript-assets, evals, examples, dashboard — not docs/catalogue.md), so the doc hint is the only regeneration guidance for that file. Severity low confirmed: hygiene-level doc inaccuracy, no runtime impact, corrected regeneration command available in four other authoritative docs.
<!-- PR and issue links are added to the Tracking field after filing. -->