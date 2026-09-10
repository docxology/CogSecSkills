# DOCS-10: README.md renders two example links without a separator

|Field|Value|
|---|---|
|Audit ID|`DOCS-10`|
|Lens|`DOCS`|
|Severity|`low`|
|Red-team verdict|`ADJUSTED`|
|Status|Open (validated 2026-09-10)|
| Tracking | [GitHub issue](https://github.com/docxology/CogSecSkills/issues/26) |

## Summary
In README.md's bounded-examples pointer, two consecutive Markdown links are adjacent with no separator between them, while the third link gets an explicit ", and" — an inconsistent list formatting. Red team narrowed the original claim: under CommonMark the single newlines inside the paragraph render as spaces, so the link texts do not run together as `…mdexamples/…`; the real defect is the cosmetic punctuation inconsistency, not a run-together render.

## Evidence
README.md:190-193 (raw, verbatim):

```
For bounded examples, see
[`examples/harness-smoke-transcripts.md`](examples/harness-smoke-transcripts.md)
[`examples/group-worked-examples.md`](examples/group-worked-examples.md), and
[`docs/skill-worked-examples.md`](docs/skill-worked-examples.md).
```

The two links are adjacent with no `·` or comma between them, while the third link gets an explicit ", and". No lint/markdown gate in the repo enforces link separation (no markdownlint config found in the repo layout).

## Impact
Cosmetic punctuation inconsistency in the README's rendered output: the example list reads as an unseparated run rather than a deliberate enumeration, unlike the correctly separated third link. No functional impact; purely a polish issue on the project's front-page document.

## Remediation
Insert a separator (e.g. `·` or a comma) between the `examples/harness-smoke-transcripts.md` and `examples/group-worked-examples.md` links at README.md:191-192, matching the enumerated style used for the third link.

## Audit trail
- Discovered by the DOCS lens agent (2026-09-10 red-team audit).
- Independently re-verified: verdict `ADJUSTED`, confidence `high`.
- Verifier notes: Confirmed the quote at the cited location (verbatim text matches; exact lines are 190-193, finding said 191-192 — immaterial). No lint/markdown gate in the repo enforces link separation (no markdownlint config found in the repo layout). One correction to the 'why': in standard Markdown (CommonMark) a single newline inside a paragraph is a soft break rendered as a space, so the two link texts do NOT visually run together as '…mdexamples/…' — rendered output shows them space-separated. The real defect is narrower: inconsistent list formatting (no separator before the second link while the third gets ', and'), a cosmetic punctuation inconsistency, not a run-together render. Severity low is correct.
<!-- PR and issue links are added to the Tracking field after filing. -->