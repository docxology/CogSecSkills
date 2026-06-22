---
name: critical_review.reproducibility_assessment
description: Assess whether a result can be regenerated from the stated data, code, and seeds.
---

# Reproducibility Assessment

Reproducibility Assessment systematically checks whether a claimed result — computational, empirical, or analytical — can be regenerated from the stated data, code, seeds, and environment by an independent party following only the documented procedure. It distinguishes direct reproduction (same data, same code), replication (same procedure, new data), and conceptual replication (same hypothesis, different operationalization), and assesses the degree to which the artifact meets the requirements of each tier. In the cognitive-security domain, reproducibility is a foundational epistemic standard: assessments, threat models, and evidence bases that cannot be independently verified are vulnerable to manipulation and should not be used as sole justification for consequential decisions.

## When to use

- when evaluating a research claim, intelligence assessment, or analytical product before using it as a basis for decisions
- when accepting an external artifact into an evidence base that will support consequential conclusions
- when auditing a published result in the cognitive-security, AI, or social-science domain for epistemic reliability
- when a result has influenced policy or public belief and its provenance needs independent verification

## What it produces

- a reproducibility scorecard rating each key criterion (data availability, code availability, environment specification, seed/randomness control, result match) against the direct/replication/conceptual tiers
- a specific gap report identifying which claimed results could not be reproduced, why, and what would be needed to close each gap
- an overall reproducibility tier assessment (fully reproducible / partially reproducible / not reproducible / not assessable) with confidence
- a prioritized set of recommendations for the artifact authors to improve reproducibility

## Defensive boundary

Use Reproducibility Assessment only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Reproducibility Assessment to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Reproducibility Assessment, tie each scorecard status to concrete evidence — the available data and code, the pinned environment spec, and captured output from the reproduction attempt compared against the claimed numbers — and classify any input that is missing or unversioned as a not-assessable gap rather than as supporting evidence.
- For Reproducibility Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the reproducibility scorecard.
- Before recommending any Reproducibility Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Reproducibility Assessment: each scorecard criterion's status is backed by an actual execution attempt against the stated data, code, seeds, and environment, the direct-versus-replication-versus-conceptual tier assignments hold when the documented procedure is re-run, and no unresolved contradiction between claimed and reproduced results would change the overall reproducibility tier.
- Medium for Reproducibility Assessment: the reproducibility scorecard is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Reproducibility Assessment: the reproducibility scorecard rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Reproducibility Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Reproducibility Assessment, use only authorized artifact, key claims, and environment spec, public or source-approved records, and caller-provided context needed for the defensive task.
- For Reproducibility Assessment, minimize person-level detail in the reproducibility scorecard; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Reproducibility Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Reproducibility Assessment: rating a result reproducible when no independent execution was attempted and an undocumented seed, preprocessing step, or missing dataset was treated as acceptable, so plausibility is mistaken for verification and a not-assessable claim is wrongly recorded as reproduced.
- Reproducibility Assessment: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Reproducibility Assessment: reporting the reproducibility scorecard without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Reproducibility Assessment outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the reproducibility scorecard from Reproducibility Assessment into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Reproducibility Assessment to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, key claims, and environment spec' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish the three reproducibility tiers — direct reproduction, replication, and conceptual replication — and assess each separately; conflating them obscures what is actually verifiable
- treat an undocumented seed, environment, or preprocessing step as a gap even if the result seems plausible — undocumented steps cannot be independently verified and create attack surfaces for manipulation
- a result is not reproducible merely because the authors say it is — independent execution is required for direct reproduction
- missing data or code should be classified as 'not assessable' not 'reproducible' — an absence of counter-evidence is not evidence of reproducibility
