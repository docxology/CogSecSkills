---
name: critical_review.project_critical_review
description: Adversarial-then-constructive review of a project: claims, evidence, risks, gaps, and go/no-go.
---

# Project Critical Review

The flagship critical-review skill. It reviews a project — codebase, research project, or initiative — by first MAPPING what the project claims and how it is built, then running an ADVERSARIAL pass that attacks every load-bearing claim for missing evidence, silent-failure and dual-use risk, and unstated assumptions, followed by a CONSTRUCTIVE pass that names genuine strengths and the cheapest fix for each top risk. Findings are classified by severity and confidence, every finding is bound to evidence (file:line or command output), and the project's own tests and gates are run to confirm they actually have teeth before any "all passing" claim is trusted. The product is a BLUF report with a calibrated go/no-go recommendation and the top three things to fix first.

## When to use

- A decision is imminent — ship, merge, fund, publish, deprecate — and a wrong
- A project reports "all tests passing / everything works" and you need to know
- You inherited a codebase, manuscript, or initiative and must form an honest

## What it produces

- BLUF report with map, findings, strengths, and recommendation
- each finding with severity, confidence, and evidence (file:line)
- calibrated go/no-go plus the top three things to fix first

## Defensive boundary

Use Project Critical Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Project Critical Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Project Critical Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Project Critical Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Project Critical Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Project Critical Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Project Critical Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Project Critical Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Project Critical Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Project Critical Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Project Critical Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Project Critical Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Project Critical Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Project Critical Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Project Critical Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Project Critical Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Project Critical Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Project Critical Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Project Critical Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Bind every finding to evidence.** A claimed defect with no file:line or no
- **Verify-the-verifier.** A green test suite that stays green when you inject a
- **Calibrate severity and confidence separately.** Severity is "how bad if
- **The constructive pass does not launder the critical pass.** Strengths are
- **Distrust self-report.** "All passing" is a claim about a process; reproduce
