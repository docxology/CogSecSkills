# CORE-09: definition_path / definition_from_skill unpack `split('.', 1)` into two variables and crash with an opaque ValueError on a dot-less id

|Field|Value|
|---|---|
|Audit ID|`CORE-09`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|PENDING-ISSUE-LINK|

## Summary
Registry validation only requires a non-empty id, so a dot-less id like `satx` passes loading — and then explodes `definition_path`/`definition_from_skill` with `ValueError: not enough values to unpack (expected 2, got 1)` instead of a precise `SpecError` naming the bad id. Elsewhere in the codebase the same input is handled gracefully via `[-1]`, making the behavior inconsistent.

## Evidence
`src/cogsecskills/authoring/definitions.py:77`:

```python
group, slug = skill_id.split(".", 1)
```

`src/cogsecskills/authoring/definitions.py:156`:

```python
group, slug = spec.id.split(".", 1)
```

Registry validation at `registry.py:55-57` checks only that `id`, `name`, `group`, `summary` are non-empty strings — no `<group>.<slug>` shape check. The verifier confirmed these are the only two-variable unpacks: `validate.py:198` explicitly tolerates dot-less ids (`spec.id.split(".", 1)[1] if "." in spec.id else spec.id`), while `author.py:145`, `scaffold.py:75`, and `rows.py:65` use `[-1]`. Mitigation paths are incomplete: `check_definitions` catches `ValueError` only around the render block (`:480`), while `definition_path` calls at `:455` and `:463` sit outside the try, and `write_definitions` (`:252`) has no catch at all.

## Impact
A malformed dot-less id in curated registry/definition data crashes the check/write tooling with an opaque `ValueError` that names no skill, rather than the library's precise-`SpecError` convention. Blast radius is limited to checked-in data plus a confusing message — hence low.

## Remediation
Validate the `<group>.<slug>` shape where ids enter the system — e.g. in `RegistryEntry.from_obj` (registry.py) and/or in `definition_path`/`definition_from_skill` (definitions.py:77, 156) — raising `SpecError` like `f"id must be <group>.<slug>: {skill_id!r}"`, or use a split with an explicit length check before unpacking. Add a test with a dot-less id asserting the precise error.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Quotes confirmed verbatim at current lines. RegistryEntry.from_obj only enforces non-empty id/name/group/summary strings; nothing validates the id contains a dot, and validate.py:198 even tolerates dot-less ids explicitly (`spec.id.split(".", 1)[1] if "." in spec.id else spec.id`), while author.py:145, scaffold.py:75, rows.py:65 use `[-1]` — so definition_path/definition_from_skill are the only two-variable unpacks and the inconsistency claim holds. Mitigations checked: check_definitions catches ValueError at :480 but only around the render block — definition_path calls at :455 and :463 sit outside the try, so a dot-less id in a definition raises an uncaught `ValueError: not enough values to unpack` from check_definitions; write_definitions (:252) has no catch at all. author.py:659 catches ValueError for its own flow but does not cover these two functions. Crash path real; blast radius limited to curated checked-in registry/definition data with a malformed id, message opaque — 'low' is honest. Fix suggestion sound.
<!-- PR and issue links are added to the Tracking field after filing. -->
