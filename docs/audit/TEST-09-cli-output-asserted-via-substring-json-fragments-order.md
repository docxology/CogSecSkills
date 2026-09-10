# TEST-09: CLI output asserted via substring JSON fragments — order/format-coupled

|Field|Value|
|---|---|
|Audit ID|`TEST-09`|
|Lens|`TEST`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/55) |

## Summary
Several CLI JSON tests assert substrings like `'"registry_total": 1' in out` against the serialized output, coupling the tests to exact JSON key-splice formatting (key order, spacing, indent) while verifying nothing that a JSON parse would not. The same files already parse JSON properly elsewhere (scaffold.py:225 `test_cli_list_json_format` uses `json.loads`), so the substring variant is a strictly weaker second convention in the same codebase. Red team verdict ADJUSTED: the four substring asserts are confirmed, but the finding's citation of scaffold.py:259-260 was a misread — those lines parse via `json.loads` and assert payload semantics (count vs total), not formatting — so the formatting-coupling charge applies only to the substring asserts. Severity stays low.

## Evidence
- tests/authoring/test_cogsecskills_cli_scaffold.py:156

```python
assert '"registry_total": 1' in out
```

  :167 — `assert '"id": "sat.two"' in out`.
- tests/quality/test_cogsecskills_insights.py:270 — `assert '"registry_total": 2' in capsys.readouterr().out`; :278 — `assert '"count": 2' in capsys.readouterr().out`.
- Weaker-than-existing convention: tests/authoring/test_cogsecskills_cli_scaffold.py:225 `test_cli_list_json_format` already parses with `json.loads(out)`.

## Impact
Substring checks against JSON output break on any serializer change (indent, key order, spacing) while verifying nothing the JSON parse wouldn't; where the same file parses JSON properly, the substring variant is a strictly weaker second convention that adds churn risk without coverage. One correction to the original analysis: scaffold.py:259-260 (`test_cli_list_limit_json`) parses via `json.loads(out)` at ~257 and `payload['count'] == 1` / `payload['total'] == 3` assert payload semantics, not formatting — those lines are fine and out of scope. Severity low confirmed: test hygiene only, breaks on serializer formatting changes, no shipped behavior affected.

## Remediation
Parse `json.loads(out)` in every CLI JSON test and assert on the payload, matching the existing `test_cli_list_json_format` convention (tests/authoring/test_cogsecskills_cli_scaffold.py:225):

1. tests/authoring/test_cogsecskills_cli_scaffold.py:156 — `payload = json.loads(out)` then `assert payload["registry_total"] == 1`; :167 — assert on the parsed element id instead of `'\"id\": \"sat.two\"'`.
2. tests/quality/test_cogsecskills_insights.py:270 and :278 — parse `capsys.readouterr().out` and assert `payload["registry_total"] == 2` / `payload["count"] == 2`.
3. Leave tests/authoring/test_cogsecskills_cli_scaffold.py `test_cli_list_limit_json` unchanged — it already parses correctly.

## Audit trail
- Discovered by the TEST lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Substring-JSON assertions confirmed at scaffold.py:156, scaffold.py:167, insights.py:270, insights.py:278, while the same files parse JSON elsewhere (scaffold.py:225 test_cli_list_json_format uses json.loads) — so the substring variant is a strictly weaker second convention, as claimed. Correction: the finding's citation of scaffold.py:259-260 is a misread — those lines are in test_cli_list_limit_json, which parses via json.loads(out) at ~257; `payload['count'] == 1` / `payload['total'] == 3` assert payload semantics (count vs total), not JSON formatting. Formatting-coupling charge applies only to the substring asserts. Severity low confirmed: test hygiene, breaks only on serializer formatting changes, no shipped behavior affected.
<!-- PR and issue links are added to the Tracking field after filing. -->