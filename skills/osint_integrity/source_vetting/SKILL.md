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

- For Source Vetting, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Source Vetting, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Source Vetting recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Source Vetting: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Source Vetting: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Source Vetting: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Source Vetting cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Source Vetting should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Source Vetting, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Source Vetting, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Source Vetting, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Source Vetting failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Source Vetting failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Source Vetting failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Source Vetting to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Source Vetting into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Source Vetting to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess reliability on four independent axes — identity, access, motive, and track record — and do not let a strong score on one compensate for a weak score on another
- separate source reliability (a property of the source) from information credibility (a property of the specific claim) — a reliable source can still be wrong about this claim
- motive analysis must consider not just obvious conflicts of interest but also cognitive biases, in-group loyalty, and reputational incentives that can distort reporting without conscious intent
- treat corroboration from sources that share a common origin as a single evidence point, not as independent confirmation — source genealogy must be traced
- document the vetting result in a retrievable record so the assessment compounds across sessions rather than being re-derived each time
