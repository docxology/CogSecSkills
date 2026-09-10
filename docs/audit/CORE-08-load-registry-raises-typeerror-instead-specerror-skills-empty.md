# CORE-08: load_registry raises TypeError instead of SpecError when `skills:` is empty/null

|Field|Value|
|---|---|
|Audit ID|`CORE-08`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
A registry file containing `skills:` with no items parses to `{'skills': None}`, which passes the existing `'skills' in raw` guard and then crashes with `TypeError: 'NoneType' object is not iterable` during the tuple build. The unhandled exception carries no file context, defeating the module's precise-`SpecError` design — the very thing the guard one line above exists to provide.

## Evidence
`src/cogsecskills/core/registry.py:113-114`:

```python
raise SpecError(f"{skills_file}: expected top-level mapping with 'skills' key")
...
entries = tuple(RegistryEntry.from_obj(item) for item in raw["skills"])
```

The verifier re-derived the mechanism: `yaml.safe_load('skills:\n')` yields `{'skills': None}`; the isinstance-dict and `'skills' in raw` guard at line 112 passes; `for item in None` raises `TypeError` outside the module's `SpecError` contract. No mitigation exists — `tests/test_cogsecskills_loader_registry.py` covers a missing file, duplicate id, wrong top-level shape, and malformed groups, but never a null `skills:` value, and the tests that use empty registries (`tests/test_cogsecskills_edge_cases.py:533`, `tests/test_cogsecskills_final_coverage.py:352`) use a real `skills: []`, which works. The adjacent groups loader has the same gap for explicit `groups: null`.

## Impact
A one-character YAML mistake (a bare `skills:` key) produces an opaque traceback with no file path instead of the library's signature precise error, sending developers debugging the wrong layer. It fails fast and loud — no wrong results ship — hence low severity.

## Remediation
In `registry.py` `load_registry`, before the tuple build, replace direct iteration with a typed check: `raw_skills = raw.get("skills")` and `if not isinstance(raw_skills, list): raise SpecError(f"{skills_file}: 'skills' must be a list")`. Apply the same treatment to the groups loader's `groups: null` case, and add a test for a null `skills:` value asserting `SpecError` with the file path in the message.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Confirmed verbatim at lines 113-114 (citation accurate). Re-derived mechanism: yaml.safe_load('skills:\n') yields {'skills': None}; the isinstance-dict and 'skills'-in-raw guard at line 112 passes; `for item in None` raises TypeError: 'NoneType' object is not iterable, outside the module's SpecError contract and with no file context. Checked for existing mitigation: tests/test_cogsecskills_loader_registry.py covers missing file, duplicate id, wrong top-level shape (list), and malformed groups — never a null `skills:` value; tests/test_cogsecskills_edge_cases.py:533 and test_cogsecskills_final_coverage.py:352 use `skills: []` (a real empty list, which works), not null. No gate, test, or doc disclaimer handles the null case. Adjacent groups loader has the same gap (`graw.get('groups', [])` handles missing but not explicit `groups: null`), which supports rather than refutes the finding. Severity 'low' is honest: malformed registry YAML is developer-facing, fails fast loudly, does not ship wrong results.
<!-- PR and issue links are added to the Tracking field after filing. -->
