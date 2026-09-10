# CORE-12: load_config str()-coerces harness list entries: null/number elements become harness names 'None'/'3'

|Field|Value|
|---|---|
|Audit ID|`CORE-12`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
`load_config` stringifies every element of the `harnesses` list, so `harnesses: [claude, null, 3]` silently yields `('claude', 'None', '3')`. Scaffold/author then generate `harness/None.md`, and validation demands adapters for the bogus harness `'3'` — which conformance accepts through the full-vocabulary fallback for unknown harness names. Non-string entries should be rejected, not stringified.

## Evidence
`src/cogsecskills/core/config.py:72`:

```python
harnesses = tuple(str(h).strip() for h in harnesses if str(h).strip())
```

The list-type guard at line 70 checks only the list itself, not elements. Downstream fallback at `src/cogsecskills/harness.py:69`:

```python
supported = support_map.get(harness, full)
```

where `full = frozenset(ToolVerb)`, so any stringified junk harness name passes conformance with the full verb vocabulary. The verifier found no gate, test, or code path validating harness name types or membership — the documented unknown-harness design (`config.py:18-20`, `harness-installation.md:117-120`) is about named extension harnesses like `gemini`, not type validation — and noted that `load_config`'s own docstring policy of raising `ValueError` with a precise message for malformed configs makes the silent coercion inconsistent with the module's stated behavior.

## Impact
A type-o'd config entry produces confusing artifacts (`harness/None.md`) and conformance demands for harnesses that don't exist. The failure mode is loud (validate requires the adapter), so no silent corruption — user-error hygiene rather than wrong shipped results.

## Remediation
In `config.py` `load_config` (line 72), replace the str()-coercion with a per-element check: require `isinstance(h, str)` and non-empty after strip, raising `ValueError` naming the offending element — consistent with the module's documented fail-loud policy and the sibling `_int` helper. Add a test that `harnesses: [claude, null, 3]` raises instead of yielding `'None'`/`'3'`.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified the verbatim quote and current line numbers (line 72 exactly matches). Re-derived the chain: yaml like `harnesses: [claude, null, 3]` passes the isinstance(list) guard, elements are str()-coerced to 'None'/'3', scaffold/author then generate harness/None.md and validate demands adapters for bogus names, and check_conformance accepts them via the documented unknown-harness fallback. Checked for existing mitigations: no gate, test, or code path validates harness name types or membership — grep for isinstance(h/isinstance(harness/'not in HARNESSES'/'unknown harness' found only the deliberate unknown-harness-vocabulary design (config.py:18-20 docstring, harness-installation.md:117-120, configuration.md), which is about *named* extension harnesses like gemini, not type validation. A docstring note that malformed configs should raise ValueError with a precise message (config.py load_config) makes the silent str-coercion mildly inconsistent with the module's own stated policy, reinforcing the finding. Severity 'low' is honest: it's user-error hygiene producing confusing artifacts ('harness/None.md') rather than wrong/misleading shipped results — an unknown harness by design just needs an adapter, and the failure mode is loud (validate requires the adapter), not silent corruption. Suggested fix (reject non-string elements with ValueError naming the offender) is correct and consistent with load_config's documented fail-loud policy.
<!-- PR and issue links are added to the Tracking field after filing. -->
