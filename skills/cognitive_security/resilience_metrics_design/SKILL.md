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

- For Resilience Metrics Design, tie each indicator schema, measurement protocol, and implementation guidance claim to concrete evidence from the specific ecosystem definition, stakeholder goals, and existing data sources item, source excerpt, observation, or command result that supports it.
- For Resilience Metrics Design, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the indicator schema.
- Before recommending any Resilience Metrics Design action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Resilience Metrics Design: the indicator schema is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; define the ecosystem and decision context and map resilience dimensions and candidate indicators checks agree, and no unresolved contradiction would change the result.
- Medium for Resilience Metrics Design: the indicator schema is plausible, but one important ecosystem definition source, comparison case, or alternative explanation remains incomplete.
- Low for Resilience Metrics Design: the indicator schema rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Resilience Metrics Design cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Resilience Metrics Design, use only authorized ecosystem definition, stakeholder goals, and existing data sources, public or source-approved records, and caller-provided context needed for the defensive task.
- For Resilience Metrics Design, minimize person-level detail in the indicator schema; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Resilience Metrics Design, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Resilience Metrics Design: treating ecosystem definition as complete when define the ecosystem and decision context and map resilience dimensions and candidate indicators checks or contradictory evidence are missing.
- Resilience Metrics Design: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Resilience Metrics Design: reporting the indicator schema without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Resilience Metrics Design outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the indicator schema from Resilience Metrics Design into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Resilience Metrics Design to assess supplied material for manipulation indicators and recommend resilience measures with ecosystem definition, stakeholder goals, and existing data sources' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- operationalize each resilience dimension into at least one leading indicator (predicts degradation before it is manifest) and one lagging indicator (confirms degradation after the fact)
- distinguish structural resilience (diversity of sources, independence of fact-checking infrastructure) from behavioral resilience (audience correction uptake, lateral reading rates) — both are necessary
- design for measurement validity: a metric that is easy to game by bad actors is worse than no metric
- set benchmarks relative to baselines and comparable ecosystems, not absolute thresholds — resilience is comparative and dynamic
- build in a 'bright line' alert threshold for each metric where a breach triggers a mandatory review, not just a dashboard update
