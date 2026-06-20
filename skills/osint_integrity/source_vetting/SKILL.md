---
name: osint_integrity.source_vetting
description: Vet a source's identity, track record, motive, and access before relying on it.
---

# Source Vetting

Source vetting is a structured credibility-assessment process that evaluates a source's identity, access, track record, and motivation before incorporating its claims into analysis. Drawn from intelligence tradecraft (the classic MICE framework and FBI source-reliability scales) and adapted for open-source information environments, it surfaces deceptive, mistaken, or biased sources before their output can anchor downstream judgments. The technique is applied at intake — before a source's claims are treated as evidence — and revisited whenever a source's circumstances or behavior change.

## When to use

- a source is being cited for the first time in an analytic product
- a source makes a claim that would significantly change an analytic judgment if true
- a source's behavior, ownership, or funding has recently changed
- multiple sources all trace back to a single original source that has not been vetted
- a source is anonymous or pseudonymous and no independent corroboration exists
- the stakes of relying on a mistaken or deceptive source are high

## What it produces

- a structured reliability rating (e.g., A–F identity confidence × 1–6 information credibility, NATO standard) with evidence basis
- a motive map identifying who benefits if the source's claims are believed
- an access assessment confirming whether the source could plausibly know what they claim to know
- a track-record summary of prior accurate and inaccurate claims with dated examples
- a table of red flags — deception indicators, anomalies, or bias markers — each linked to evidence
- recommended use conditions: how the source may be used, what corroboration is needed, and what claims fall outside its demonstrated expertise

## Defensive boundary

Use Source Vetting only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Source Vetting to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Source Vetting, tie each source reliability assessment, and red flags claim to concrete evidence from the specific source identifier, claim context, and prior assessments item, source excerpt, observation, or command result that supports it.
- For Source Vetting, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the source reliability assessment.
- Before recommending any Source Vetting action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Source Vetting: the source reliability assessment is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; characterize the source and verify identity and ownership checks agree, and no unresolved contradiction would change the result.
- Medium for Source Vetting: the source reliability assessment is plausible, but one important source identifier source, comparison case, or alternative explanation remains incomplete.
- Low for Source Vetting: the source reliability assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Source Vetting cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Source Vetting, use only authorized source identifier, claim context, and prior assessments, public or source-approved records, and caller-provided context needed for the defensive task.
- For Source Vetting, minimize person-level detail in the source reliability assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Source Vetting, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Source Vetting: treating source identifier as complete when characterize the source and verify identity and ownership checks or contradictory evidence are missing.
- Source Vetting: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Source Vetting: reporting the source reliability assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Source Vetting outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the source reliability assessment from Source Vetting into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Source Vetting to verify supplied claims, media, sources, or datasets with documented public-source methods with source identifier, claim context, and prior assessments' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess reliability on four independent axes — identity, access, motive, and track record — and do not let a strong score on one compensate for a weak score on another
- separate source reliability (a property of the source) from information credibility (a property of the specific claim) — a reliable source can still be wrong about this claim
- motive analysis must consider not just obvious conflicts of interest but also cognitive biases, in-group loyalty, and reputational incentives that can distort reporting without conscious intent
- treat corroboration from sources that share a common origin as a single evidence point, not as independent confirmation — source genealogy must be traced
- document the vetting result in a retrievable record so the assessment compounds across sessions rather than being re-derived each time
