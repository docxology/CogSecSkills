# CORE-03: author_batch's per-item exception tuple is too narrow; a malformed _def.json aborts the whole batch with a raw traceback instead of the promised failed-report

|Field|Value|
|---|---|
|Audit ID|`CORE-03`|
|Lens|`CORE`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/8)|

## Summary
`author_batch` catches only `(AuthorError, SpecError, ValueError, KeyError)` per item, but a `_def.json` containing a JSON array or scalar crashes earlier — at `definition.setdefault("id", skill_id)`, which runs before `render_definition`'s own dict guard — raising an uncaught `AttributeError` (or `TypeError`, or `OSError` from an unreadable file). One malformed file then aborts the whole batch with a raw traceback, and the remaining `_def.json` files are never rendered, breaking the documented `{"rendered": [...], "failed": {id: error}}` contract.

## Evidence
`src/cogsecskills/authoring/author.py:653-659`:

```python
definition = json.loads(def_path.read_text(encoding="utf-8"))
...
definition.setdefault("id", skill_id)
...
except (AuthorError, SpecError, ValueError, KeyError) as exc:
```

The verifier re-derived the mechanism independently: `render_definition` does validate non-mapping inputs (`author.py:551-552` raises `AuthorError` for a non-dict), but `definition.setdefault("id", skill_id)` executes **before** that guard, so a `_def.json` holding a JSON array (`[].setdefault` → `AttributeError`) or scalar crashes before the existing protection runs. Neither `AttributeError` nor `TypeError` is in the catch tuple; `json.JSONDecodeError` is a `ValueError` subclass, which is why the existing `test_author_batch_reports_malformed` test covering `'{not valid json'` passes and masks the gap. `OSError` from an unreadable file is likewise uncaught. The contract is documented in the docstring at `author.py:638-639`.

## Impact
A single malformed or unreadable `_def.json` turns the promised per-item failed-report into a whole-batch crash: remaining definitions are silently never rendered, and the operator gets a raw traceback with no per-file diagnostics. No other gate, test, or doc mitigates this — tests cover only invalid-JSON and good-definition paths.

## Remediation
In `author.py` `author_batch` (the loop around lines 653-659), validate the parsed payload immediately after `json.loads` — e.g. `if not isinstance(definition, dict): raise AuthorError(...)` — and record it as a failure; alternatively broaden the catch tuple to `(AuthorError, SpecError, ValueError, KeyError, AttributeError, TypeError, OSError)`. Either way, add a regression test with a `_def.json` containing a JSON array asserting the batch still renders the remaining files and reports the failure by id.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Re-derived independently. The tempting refutation — render_definition already validates non-mapping inputs (author.py:551-552 `if not isinstance(definition, dict): raise AuthorError(...)`) and AuthorError is in the catch tuple — does not hold, because `definition.setdefault("id", skill_id)` executes BEFORE render_definition is called; a `_def.json` containing a JSON array (`[].setdefault` -> AttributeError) or scalar (`int.setdefault` -> AttributeError) crashes before that guard runs. Neither AttributeError nor TypeError is in the catch tuple (json.JSONDecodeError is a ValueError subclass, so the existing test_author_batch_reports_malformed covering '{not valid json' passes and masks the gap). OSError from an unreadable file is likewise uncaught, aborting the whole batch loop and violating the documented contract '{"rendered": [...], "failed": {id: error}}' (docstring author.py:638-639). No other gate/test/doc mitigates; tests only cover invalid-JSON and good-def paths. Suggested fix (isinstance-dict validation right after json.loads, or broadened catch) is sound. Medium severity fair: crash of a compatibility-path CLI command, no silent wrong output, no data loss beyond remaining defs unrendered.
<!-- PR and issue links are added to the Tracking field after filing. -->
