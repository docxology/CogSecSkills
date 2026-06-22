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

- For Threat Model Review, bind every gap, flagged assumption, and scope recommendation to concrete evidence from the supplied threat model, system description, or review focus — a quoted scope exclusion, a named actor or trust relationship, or a mitigation statement — and identify what an attacker would do where that element is missing; an unsupported gap is a conjecture, not a finding, and must be labelled as such.
- For Threat Model Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the gap report.
- Before recommending any Threat Model Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Threat Model Review: every gap-report row ties a missing actor, surface, trust-boundary error, or unvalidated assumption to a specific element absent from the reviewed model and present in the independently derived expected set; the assumption register and revised scope recommendation are each corroborated by the system description rather than a single anchoring read of the model; the prioritized remediation ordering holds when any one finding is set aside; and no unresolved contradiction about realistic threats would change the scope conclusion.
- Medium for Threat Model Review: the gap report is plausible, but one important threat model source, comparison case, or alternative explanation remains incomplete.
- Low for Threat Model Review: the gap report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Threat Model Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Threat Model Review, use only authorized threat model, system description, and review focus, public or source-approved records, and caller-provided context needed for the defensive task.
- For Threat Model Review, minimize person-level detail in the gap report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Threat Model Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Threat Model Review: declaring a model reviewed when the expected actors and attack surfaces were never independently derived from the system description, so the analysis merely echoes the original authors' blind spots — for example crediting a stated mitigation as an implemented control without verifying it, or omitting social-engineering and influence surfaces entirely — and the absence of gaps reflects an anchored review rather than a complete one.
- Threat Model Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Threat Model Review: reporting the gap report without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Threat Model Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the gap report from Threat Model Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Threat Model Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with threat model, system description, and review focus' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- derive what the threat model should contain independently from the system description before reading the existing model — compare derived set to present set to surface omissions
- treat every scope exclusion as an implicit assumption; make those assumptions explicit and then evaluate whether they are warranted
- for each stated mitigation, ask whether it is actually implemented and testable — a paper mitigation is not a real control
- in cognitive-security threat models, explicitly audit for social-engineering and influence-operation surfaces, which are systematically underrepresented in technically-oriented models
