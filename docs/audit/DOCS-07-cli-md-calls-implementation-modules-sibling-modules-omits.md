# DOCS-07: cli.md calls the implementation modules 'sibling modules' and omits four commands from the cli.py module summary

|Field|Value|
|---|---|
|Audit ID|`DOCS-07`|
|Lens|`DOCS`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/23) |

## Summary
Two doc inaccuracies compound: docs/cli.md describes the implementation modules as "sibling modules" when they actually live in the core/, quality/, authoring/, and artifacts/ subpackages, and docs/architecture.md's cli.py row lists only 16 of the 20 subcommands cli.py registers, omitting `dashboard`, `examples`, `evals`, and `release-metadata`. The inaccuracy originates in cli.py's own docstring, which mirrors the same "sibling modules" wording.

## Evidence
docs/cli.md:6-9 (verbatim):

```
All business logic lives in the sibling modules (`insights.py`, `validate.py`, `author.py`, `scaffold.py`, `registry.py`, `config.py`, `definitions.py`, `scenarios.py`, `examples.py`, `dashboard.py`, `manuscript_assets.py`); the CLI only parses arguments, calls them, and prints results.
```

The modules actually live in subpackages (e.g. `core/config.py`, `core/locate.py`, `quality/insights.py`, `artifacts/scenarios.py`, `artifacts/manuscript_assets/`). docs/architecture.md:~163 cli.py row (verbatim):

```
Thin orchestrator. Parses args, calls the library API, prints results — `list`, `show`, `validate`, `report`, `route`, `stats`, `groups`, `catalogue`, `doctor`, `definitions`, `scenarios`, `manuscript-assets`, `export`, `scaffold`, `author`, `author-batch`. No business logic.
```

cli.py `build_parser` additionally registers `dashboard` (:585), `examples` (:601), `evals` (:617), `release-metadata` (:649).

## Impact
Cosmetic doc drift with no functional impact — the commands are fully documented in their own sections of cli.md. But the "sibling" wording misdescribes the package layout, the module inventory in both docs is incomplete (cli.md's list omits evals.py as well), and the architecture table's command list undercounts the shipped CLI surface, so contributors reading the docs get an inaccurate mental model of the codebase layout. No test cross-checks either doc against cli.py's parser, so the drift persists silently.

## Remediation
1. In docs/cli.md:6-9, replace "sibling modules" with "subpackage modules (core/, authoring/, quality/, artifacts/)" and add `evals.py` to the module list.
2. In docs/architecture.md's cli.py row (~line 163), append `examples`, `evals`, `dashboard`, `release-metadata` to the command list.
3. Optionally fix the matching "sibling modules" wording in cli.py's docstring (line 3) so the doc and code agree.

## Audit trail
- Discovered by the DOCS lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Both claims confirmed against source. (1) cli.md:6-9 'sibling modules' wording is verbatim; modules are in core/, quality/, authoring/, artifacts/ subpackages per architecture.md's own table links (core/config.py, quality/insights.py, artifacts/scenarios.py). Note the architecture table itself lists only 11 modules and also omits examples.py/evals.py — so the module inventory in both docs is incomplete, not just misplaced. (2) cli.py registers 20 subcommands; architecture.md's cli.py row lists 16, omitting dashboard, examples, evals, release-metadata exactly as the finding says. (3) Checked for mitigating gates/tests: none — docs are hand-maintained; no test cross-checks architecture.md's command list or cli.md's module paths against cli.py's parser (cli.md sections for examples/evals/dashboard/release-metadata do exist later in the file, so only the module-summary sentence and architecture row are stale). (4) cli.py docstring line 3 mirrors the same 'sibling modules' wording, so the inaccuracy originates in the code docstring too. ADJUSTED rather than pure VALID for two small corrections: the actual cli.md text is at lines 6-9 (finding said 8-11), and the missing-commands issue applies not only to architecture.md's cli.py row but the same module list in cli.md also omits evals.py. Severity low is right: cosmetic doc drift with no functional impact; commands are fully documented in their own sections of cli.md.
<!-- PR and issue links are added to the Tracking field after filing. -->