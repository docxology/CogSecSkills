---
name: critical_review.threat_model_review
description: Review a system's threat model for missing actors, surfaces, and assumptions.
---

# Threat Model Review

Threat Model Review systematically audits an existing threat model — such as a STRIDE, PASTA, attack tree, or narrative threat assessment — to identify missing actors, overlooked attack surfaces, unvalidated assumptions, and incomplete trust boundaries. The technique applies adversarial thinking to the threat model itself, asking whether it captures the realistic threat population, whether its mitigations are actually implemented, and whether its scope boundaries are justified or merely convenient. In cognitive-security contexts this extends to information-environment threat models: identifying omitted influence actors, uncovered cognitive attack surfaces, and assumptions about audience resilience that have not been empirically validated.

## When to use

- a threat model has not been reviewed since its initial creation and the system or threat environment has changed
- a security or cognitive-security assessment depends on an existing threat model that may have been authored under optimistic assumptions
- a red-team exercise has surfaced attack paths not present in the official threat model
- the threat model was authored by internal stakeholders with blind spots toward insider threats or sociotechnical surfaces
- an information-environment assessment needs to check whether all relevant influence actors and cognitive attack vectors are represented

## What it produces

- a gap table identifying missing actors, surfaces, trust-boundary errors, unvalidated assumptions, and mitigation gaps with severity ratings
- an assumption register distinguishing validated from unvalidated assumptions and flagging the highest-risk unvalidated ones
- a revised scope recommendation with rationale for expanding or recentering the model's boundaries
- a prioritized remediation list so owners can address critical gaps first

## Defensive boundary

Use Threat Model Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Threat Model Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Threat Model Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Threat Model Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Threat Model Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Threat Model Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Threat Model Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Threat Model Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Threat Model Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Threat Model Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Threat Model Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Threat Model Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Threat Model Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Threat Model Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Threat Model Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Threat Model Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Threat Model Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Threat Model Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Threat Model Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- derive what the threat model should contain independently from the system description before reading the existing model — compare derived set to present set to surface omissions
- treat every scope exclusion as an implicit assumption; make those assumptions explicit and then evaluate whether they are warranted
- for each stated mitigation, ask whether it is actually implemented and testable — a paper mitigation is not a real control
- in cognitive-security threat models, explicitly audit for social-engineering and influence-operation surfaces, which are systematically underrepresented in technically-oriented models
