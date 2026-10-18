# CORE-10: `catalogue --output` writes without creating parent directories

|Field|Value|
|---|---|
|Audit ID|`CORE-10`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/15)|

## Summary
The `catalogue` command's `--output` writer calls `write_text` directly without creating the parent directory, unlike every other file-writing path in the codebase. `--output docs/generated/catalogue.md` with a missing `docs/generated/` raises a raw `FileNotFoundError` — after all generation work has already been done.

## Evidence
`src/cogsecskills/cli.py:193-194` in `_cmd_catalogue`:

```python
if args.output:
    args.output.write_text(markdown + "\n", encoding="utf-8")
```

The verifier cross-checked every other writing path and found parent creation everywhere else: `write_definitions` (`authoring/definitions.py:253`), `scaffold` (`scaffold.py:138`), `author` (`author.py:563`), and the artifacts writers (`dashboard.py:784`, `evals.py:359/364`, `examples.py:270`, `release_metadata.py:303`, `assets_io.py:38`). The only catalogue-output test writes to a tmp_path root (`tests/quality/test_cogsecskills_insights.py:279-286`), so nothing covers missing parents.

## Impact
A convenience flag fails with a confusing traceback when the natural target directory doesn't exist yet — inconsistent with the CLI's other writers and wasting the generation work already performed. CLI hygiene only: it fails loudly and produces no wrong output.

## Remediation
In `_cmd_catalogue` (`cli.py:193`), add `args.output.parent.mkdir(parents=True, exist_ok=True)` before `write_text`, matching `write_definitions` at `authoring/definitions.py:253`. Add a test writing to a nested nonexistent tmp_path directory.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Read _cmd_catalogue in full: no parent mkdir before write_text, so missing parent dir raises FileNotFoundError after generation. Cross-checked: every other file-writing path creates parents — write_definitions (authoring/definitions.py:253), scaffold (scaffold.py:138), author (author.py:563), artifacts writers (dashboard.py:784, evals.py:359/364, examples.py:270, release_metadata.py:303, assets_io.py:38). Tests: test_cli_catalogue_output_file (tests/quality/test_cogsecskills_insights.py:279-286) writes only to tmp_path root; no test/doc mitigates missing parents. Severity low is right — CLI hygiene, fails loudly, no wrong output.
<!-- PR and issue links are added to the Tracking field after filing. -->
