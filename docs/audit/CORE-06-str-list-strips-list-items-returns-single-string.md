# CORE-06: _as_str_list strips list items but returns the single-string form unstripped

|Field|Value|
|---|---|
|Audit ID|`CORE-06`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/11)|

## Summary
In `SkillSpec` parsing, `_as_str_list` strips whitespace from list-form items but returns the bare-scalar form as-is, so `triggers: "  foo  "` is stored as `('  foo  ',)` while `triggers: ["  foo  "]` is stored as `('foo',)`. Identical logical data produces different specs depending on YAML spelling, and padded values flow inconsistently into consumers such as routing and canonical-definition text.

## Evidence
`src/cogsecskills/core/spec.py:129` (scalar branch):

```python
return (value,) if value.strip() else ()
```

`src/cogsecskills/core/spec.py:139` (list branch):

```python
items.append(item.strip())
```

The verifier confirmed both lines verbatim and that `_as_str_list` feeds at least nine fields — `triggers` (spec.py:209), `tags` (208), `references` (213), and six more — so an unstripped scalar flows into spec tuples. No gate covers it: `tests/unit/core/test_cogsecskills_spec.py:113` asserts `spec.triggers == ("single trigger",)` but never exercises padded scalar input, and all checked-in definitions use list-form triggers.

## Impact
Currently no shipped data is affected (all checked-in definitions use list form), but any future scalar-spelled spec silently carries padding into routing and canonical-definition text — and the same YAML value spelled two ways yields different behavior, a latent inconsistency that is hard to diagnose downstream.

## Remediation
Change the scalar branch of `_as_str_list` in `spec.py` (line 129) to `return (value.strip(),) if value.strip() else ()`, and add a test asserting `triggers: "  foo  "` and `triggers: ["  foo  "]` produce identical tuples.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Confirmed the scalar branch at spec.py:129 returns the raw string unstripped while the list branch strips each item (spec.py:139); _as_str_list is used for triggers (spec.py:209), tags (208), references (213), and six more fields, so an unstripped scalar flows into spec tuples. No mitigating gate: grep of tests found no test enforcing stripped scalars — tests/unit/core/test_cogsecskills_spec.py:113 asserts `spec.triggers == ("single trigger",)` but never exercises padded scalar input. All checked-in definitions/*.yaml use list-form triggers, so no real shipped data is currently affected; blast radius limited to future scalar-spelled specs — consistent with low severity. Re-derived reasoning independently: identical logical data yields ('foo',) vs ('  foo  ',) depending on YAML spelling. Proposed fix (return (value.strip(),)) is correct.
<!-- PR and issue links are added to the Tracking field after filing. -->
