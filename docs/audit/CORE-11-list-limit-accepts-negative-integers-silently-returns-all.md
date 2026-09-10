# CORE-11: `list --limit` accepts negative integers and silently returns all-but-last-N rows

|Field|Value|
|---|---|
|Audit ID|`CORE-11`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
`--limit` uses bare `argparse` `type=int` with no bounds check, and the row slice `rows[: args.limit]` inverts the documented "cap the number of results" contract for negatives: `--limit -3` returns everything except the last three rows, with the JSON payload's `count` reporting the truncated length as if intended. The same pattern exists in `route` via `route_query`.

## Evidence
`src/cogsecskills/cli.py:69-70` in `_cmd_list`:

```python
if args.limit is not None:
    rows = rows[: args.limit]
```

Help text at `cli.py:461-465`: `"--limit", type=int, default=None, help="cap the number of results (applies after filtering)"`. The verifier confirmed no bounds validation anywhere in `cli.py`, that tests cover only `--limit 0` and positive limits, and that docs (`CHANGELOG.md:165-166`, `README.md:138`) describe `--limit` only as a positive cap. The same unguarded slice exists in `route_query` (`quality/insights.py`: `scored[:limit]`), fed by `cli.py:518` (`--limit`, `type=int`, `default=5`).

## Impact
An interactive CLI-only defect: no wrong data ships downstream, but a typo'd negative limit silently produces surprising results — and in JSON mode the `count` field makes the truncation look intentional. The identical latent pattern in `route` doubles the surface.

## Remediation
Add a bounds check in both commands: in `_cmd_list` (cli.py:69) and in the route path (cli.py:518 / `route_query` in `quality/insights.py`), raise `SystemExit("argparse error: --limit must be >= 0")` for negative values, or use a custom argparse type that rejects negatives. Add a test asserting `--limit -3` exits with an error rather than returning all-but-last-3 rows.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified the cited lines verbatim in _cmd_list. The mechanism is real: argparse type=int admits negatives (no custom type, no bounds check in _cmd_list), and rows[: -N] slices from the end — the 'cap the number of results' contract is inverted, with JSON payload 'count' reporting the truncated length as if intended. Checked for existing mitigations: (a) no bounds validation anywhere in cli.py for --limit; (b) tests only cover --limit 0 (test_cogsecskills_coverage_gaps.py:61-66) and positive limits (test_cogsecskills_cli_scaffold.py:233-257) — no negative-limit test; (c) docs (CHANGELOG.md:165-166, README.md:138) describe --limit only as a positive cap. Same pattern exists in route_query (quality/insights.py: scored[:limit]) fed by cli.py:518 `--limit, type=int, default=5`, so route --limit -N would also return all-but-last-N matches — the fix should cover both commands. Severity: low is honest — interactive CLI-only, no wrong data shipped to downstream systems, user-visible oddity with misleading count in JSON mode.
<!-- PR and issue links are added to the Tracking field after filing. -->
