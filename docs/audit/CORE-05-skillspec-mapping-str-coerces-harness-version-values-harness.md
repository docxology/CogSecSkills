# CORE-05: SkillSpec.from_mapping str()-coerces harness and version values: `harness: {claude: null}` becomes the adapter path 'None' and passes the conformance has_adapter check

|Field|Value|
|---|---|
|Audit ID|`CORE-05`|
|Lens|`CORE`|
|Severity|`medium`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/10)|

## Summary
`SkillSpec.from_mapping` stringifies harness mapping values (`str(v)`), so a null or numeric adapter path becomes the truthy strings `'None'`/`'123'` and passes `has_adapter` in the conformance check — reporting a declared adapter for a file that cannot exist. This directly contradicts the same file's `_require_text` doctrine, which forbids exactly this coercion class for `id`, and the same str()-coercion applies to `version`, `description`, and `ageint_topic`.

## Evidence
`src/cogsecskills/core/spec.py:236`:

```python
harness={str(k): str(v) for k, v in harness.items()}
```

`src/cogsecskills/core/spec.py:205-207`:

```python
version=str(data.get("version", "0.1.0")).strip() or "0.1.0"
description=str(data.get("description", "")).strip()
ageint_topic=str(data.get("ageint_topic", "")).strip()
```

Consumed at `src/cogsecskills/core/harness.py:77`:

```python
has_adapter=bool(spec.harness.get(harness, "").strip())
```

The file's own doctrine at `spec.py:112-115` (`_require_text` docstring): "Coercion (``str(...)``) would silently accept ``id: 0`` / ``id: []`` / ``id: null`` as the strings \"0\" / \"[]\" / \"None\". Require the real type." The verifier confirmed line-exactly that only a Mapping-type check (~line 199) guards structure, not value types, and that no test or CLI gate covers null/numeric harness values (`tests/core/test_cogsecskills_spec.py:158-162` only tests a non-mapping list).

## Impact
`harness: {claude: null}` yields `has_adapter=True` for `claude` with the fabricated path `'None'`, so multiharness conformance can pass while no real adapter file exists — silently weakening the check that `harness.py`'s docstring says requires "the spec declares an adapter path for it". The failure mode is a fabricated conformance signal rather than corrupted shipped data, hence medium rather than high.

## Remediation
In `spec.py` `from_mapping`, replace the harness dict comprehension with validation: require `isinstance(v, str) and v.strip()` for each value (raising `SpecError` otherwise, matching `_require_text` style), and apply the same `_require_text`-style checks to `version`, `description`, and `ageint_topic` instead of `str(...)` coercion. Add tests covering `harness: {claude: null}` and numeric values, asserting `SpecError`.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified all three citations line-exactly: spec.py:236 dict comprehension str-coerces keys and values of the harness mapping (only the Mapping-type check at ~199 guards structure, not value types); spec.py:205-207 str-coerce version/description/ageint_topic. Re-derived mechanism: harness value null → str(None)=='None' (truthy, non-blank after strip) → check_conformance sets has_adapter=True for that harness → is_multiharness can pass while no real adapter file exists; numeric 123 → '123' likewise. Checked mitigations: (a) harness.py:55 docstring explicitly says conformance requires 'the spec declares an adapter path for it' — the coercion undermines that contract; (b) the only adapter-path existence check is tests/conformance/test_skill_library_conformance.py:211-213, which validates the shipped library's own skills, not arbitrary specs parsed via from_mapping; (c) tests/core/test_cogsecskills_spec.py:158-162 only tests harness as a non-mapping list, never null/numeric values — no gate covers this; (d) no CLI/validator elsewhere enforces string harness values (grep found only manuscript docs and the same code lines). Contradiction with the file's own _require_text doctrine is real (SkillIO.required got the strict-boolean treatment for exactly this class of bug; harness/version/description/ageint_topic did not). Severity medium is fair: it weakens the multiharness conformance signal and reports a fabricated path, but only for malformed YAML and does not corrupt shipped results. Fix as proposed (isinstance(v, str) and v.strip(), plus _require_text-style checks for the scalar fields) is consistent with existing patterns (_as_str_list, SkillIO.required).
<!-- PR and issue links are added to the Tracking field after filing. -->
