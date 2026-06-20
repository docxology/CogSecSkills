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

- For Project Critical Review, tie each report, findings, and recommendation claim to concrete evidence from the specific artifact, decision, and success criteria item, source excerpt, observation, or command result that supports it.
- For Project Critical Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the report.
- Before recommending any Project Critical Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Project Critical Review: the report is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; scope the review and map the project checks agree, and no unresolved contradiction would change the result.
- Medium for Project Critical Review: the report is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Project Critical Review: the report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Project Critical Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Project Critical Review, use only authorized artifact, decision, and success criteria, public or source-approved records, and caller-provided context needed for the defensive task.
- For Project Critical Review, minimize person-level detail in the report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Project Critical Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Project Critical Review: treating artifact as complete when scope the review and map the project checks or contradictory evidence are missing.
- Project Critical Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Project Critical Review: reporting the report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Project Critical Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the report from Project Critical Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Project Critical Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, decision, and success criteria' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Bind every finding to evidence.** A claimed defect with no file:line or no
- **Verify-the-verifier.** A green test suite that stays green when you inject a
- **Calibrate severity and confidence separately.** Severity is "how bad if
- **The constructive pass does not launder the critical pass.** Strengths are
- **Distrust self-report.** "All passing" is a claim about a process; reproduce
