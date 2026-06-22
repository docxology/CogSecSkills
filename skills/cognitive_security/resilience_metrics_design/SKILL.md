---
name: cognitive_security.resilience_metrics_design
description: Define measurable indicators of an information ecosystem's resistance to manipulation.
---

# Resilience Metrics Design

Resilience Metrics Design defines a measurable indicator set for assessing an information ecosystem's capacity to resist, absorb, and recover from deliberate manipulation. Drawing on the RAND information environment resilience framework, the EU Digital Media Observatory methodology, and the NATO Strategic Communications Centre of Excellence measurement guidance, it operationalizes abstract resilience concepts (source diversity, correction uptake, narrative elasticity, trust calibration) into concrete, trackable metrics. The output is an indicator schema that can be implemented in monitoring dashboards, periodic assessments, or research studies.

## When to use

- designing a monitoring program for an information environment before or during an anticipated influence operation
- evaluating the effectiveness of a media-literacy, prebunking, or content-moderation intervention over time
- building a resilience baseline assessment before a high-stakes information period (election, health crisis, military operation)
- advising policymakers or platform operators on which leading indicators of ecosystem degradation to track

## What it produces

- a structured indicator schema table covering multiple resilience dimensions with measurement specifications and validity limitations
- a measurement protocol for data collection, normalization, and longitudinal tracking
- implementation guidance for embedding the metric set in a monitoring or dashboard system

## Defensive boundary

Use Resilience Metrics Design only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Resilience Metrics Design to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Resilience Metrics Design, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Resilience Metrics Design, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Resilience Metrics Design recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Resilience Metrics Design: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Resilience Metrics Design: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Resilience Metrics Design: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Resilience Metrics Design cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Resilience Metrics Design should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Resilience Metrics Design, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Resilience Metrics Design, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Resilience Metrics Design, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Resilience Metrics Design failure: mistaking persuasive resonance for verified harm or intent.
- Resilience Metrics Design failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Resilience Metrics Design failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Resilience Metrics Design to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Resilience Metrics Design into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Resilience Metrics Design to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- operationalize each resilience dimension into at least one leading indicator (predicts degradation before it is manifest) and one lagging indicator (confirms degradation after the fact)
- distinguish structural resilience (diversity of sources, independence of fact-checking infrastructure) from behavioral resilience (audience correction uptake, lateral reading rates) — both are necessary
- design for measurement validity: a metric that is easy to game by bad actors is worse than no metric
- set benchmarks relative to baselines and comparable ecosystems, not absolute thresholds — resilience is comparative and dynamic
- build in a 'bright line' alert threshold for each metric where a breach triggers a mandatory review, not just a dashboard update
