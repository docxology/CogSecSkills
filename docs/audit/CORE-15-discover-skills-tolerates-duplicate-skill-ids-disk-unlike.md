# CORE-15: discover_skills tolerates duplicate skill ids on disk (unlike the registry, which raises), and dict-based consumers silently drop one

|Field|Value|
|---|---|
|Audit ID|`CORE-15`|
|Lens|`CORE`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
|Tracking|[GitHub issue](https://github.com/docxology/CogSecSkills/issues/20)|

## Summary
`discover_skills` returns one `SkillSpec` per `skill.yaml` on disk with no seen-id tracking, unlike `load_registry`, which raises on duplicate ids. If the same id exists in two directories (e.g. a stray copy in the wrong group), every dict-comprehension consumer keeps the path-sorted-last one silently — so validation and definition-drift checks run against an arbitrary copy while the other is ignored, the exact silent drift the registry layer exists to prevent.

## Evidence
`src/cogsecskills/core/loader.py:67-68` (finding cited 62-68, same block):

```python
for spec_path in sorted(tree.rglob(SPEC_FILENAME)):
    specs.append(load_skill(spec_path))
```

Contrast the registry's guard at `core/registry.py:118-119`:

```python
if entry.id in seen:
    raise SpecError(f"duplicate registry id {entry.id!r}")
```

Dict-based consumers with last-wins semantics: `authoring/definitions.py:234` (`specs = {spec.id: spec for spec in discover_skills(root)}`), plus `artifacts/scenarios.py:314`, `artifacts/examples.py:208` (a fifth site the finding missed), and `artifacts/manuscript_assets/rows.py:131`. The verifier confirmed `quality/validate.py` `validate_library` has no duplicate-on-disk detection — the registry duplicate check only guards `registry/skills.yaml` — and no test or doc gate covers the case.

## Impact
A stray duplicate `skill.yaml` (a copy in the wrong group, a bad merge) is silently resolved by path sort order: validation and drift checks run against one arbitrary copy while the other is ignored with no warning. Blast radius is one silently ignored copy — requires the stray file to exist — hence low severity.

## Remediation
In `discover_skills` (`loader.py:67-68`), track seen ids while iterating and raise `SpecError` on a second occurrence, mirroring `load_registry`'s check at `registry.py:118-119` (or at minimum emit a warning naming both paths). Add a test with two directories declaring the same id asserting the error.

## Audit trail
- Discovered by the CORE lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Verified all quotes against current files; rglob loop is at lines 67-68 (finding said 62-68, same block). Mechanism confirmed: discover_skills returns one SkillSpec per skill.yaml with no seen-id tracking, so two files declaring the same id both survive; every dict-comprehension consumer keeps the path-sorted-last spec silently (4 sites — examples.py:208 is a fifth the finding missed). Checked for mitigations: quality/validate.py validate_library iterates specs individually and checks registry coherence (missing/extra/group mismatch) but has no duplicate-on-disk detection — two same-id specs both pass if each is registry-enumerated; the registry duplicate check only guards registry/skills.yaml. No test or doc gate covers this. Severity low is honest: requires a stray duplicate skill.yaml, blast radius is one silently ignored copy chosen by sort order. Suggested fix (mirror load_registry's seen-set or warn) is appropriate.
<!-- PR and issue links are added to the Tracking field after filing. -->
