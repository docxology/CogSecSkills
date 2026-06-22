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

- For Reproducibility Assessment, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Reproducibility Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Reproducibility Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Reproducibility Assessment: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Reproducibility Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Reproducibility Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Reproducibility Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Reproducibility Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Reproducibility Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Reproducibility Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Reproducibility Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Reproducibility Assessment failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Reproducibility Assessment failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Reproducibility Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Reproducibility Assessment to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Reproducibility Assessment into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Reproducibility Assessment to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish the three reproducibility tiers — direct reproduction, replication, and conceptual replication — and assess each separately; conflating them obscures what is actually verifiable
- treat an undocumented seed, environment, or preprocessing step as a gap even if the result seems plausible — undocumented steps cannot be independently verified and create attack surfaces for manipulation
- a result is not reproducible merely because the authors say it is — independent execution is required for direct reproduction
- missing data or code should be classified as 'not assessable' not 'reproducible' — an absence of counter-evidence is not evidence of reproducibility
