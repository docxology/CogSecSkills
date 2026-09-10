# DOCS-09: ISA.md constraint still describes the private-sidecar layout that no longer exists

|Field|Value|
|---|---|
|Audit ID|`DOCS-09`|
|Lens|`DOCS`|
|Severity|`low`|
|Red-team verdict|`VALID`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/25) |

## Summary
ISA.md contradicts itself: the Decisions section records the 2026-06-18 move to a clean standalone published repo (`github.com/docxology/CogSecSkills`, no monorepo dependency), while the Constraints section still states the suite lives at the private sidecar `projects/working/CogSecSkills` symlinked into the template repo. The Constraints bullet describes a layout that no longer exists and misleads anyone reading it as current truth.

## Evidence
ISA.md:66-67 (Constraints, verbatim):

```
Lives at the private sidecar `projects/working/CogSecSkills`, symlinked into the template repo's `projects/working/` — never committed to the public template repo.
```

ISA.md:135-138 (Decisions, 2026-06-18 entry, verbatim):

```
Stripped the inherited optimization payload for a clean standalone **published** repo (`github.com/docxology/CogSecSkills`, private, Apache-2.0) ... the suite is now self-contained (no monorepo dependency).
```

No disclaimer or later Constraints update mitigates the contradiction; the Constraints section was last touched per `updated: 2026-07-22`.

## Impact
Stale ideal-state prose with no code/runtime impact, but the contradiction is internal to the same artifact: a reader treating the Constraints section as current truth will look for (or recreate) a private-sidecar layout that was deliberately abandoned. Misleading for new contributors reasoning about repo placement and for anyone consuming ISA.md as the project's ideal-state reference.

## Remediation
Update the Constraints bullet (ISA.md:66-67) to reflect the standalone public repository location — e.g. state that the suite lives as the standalone public repo `github.com/docxology/CogSecSkills` and remove the private-sidecar/symlink rule.

## Audit trail
- Discovered by the DOCS lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `VALID`, confidence `high`.
- Verifier notes: Both quotes confirmed verbatim; Constraints section is at lines 61-68 (the sidecar bullet at 66-67, wrapping two lines). The Decisions section (2026-06-18 entry at lines 135-138) explicitly records the move to a clean standalone published repo with no monorepo dependency — directly contradicting the private-sidecar constraint. No disclaimer or later Constraints update mitigates it; Constraints section was last touched per `updated: 2026-07-22`. The contradiction is real and internal to the same artifact. Severity low is correct: stale ideal-state prose, no code/runtime impact, but misleading for anyone reading the Constraints section as current truth. Suggested fix (update the Constraints bullet) is appropriate.
<!-- PR and issue links are added to the Tracking field after filing. -->