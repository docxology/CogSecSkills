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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- operationalize each resilience dimension into at least one leading indicator (predicts degradation before it is manifest) and one lagging indicator (confirms degradation after the fact)
- distinguish structural resilience (diversity of sources, independence of fact-checking infrastructure) from behavioral resilience (audience correction uptake, lateral reading rates) — both are necessary
- design for measurement validity: a metric that is easy to game by bad actors is worse than no metric
- set benchmarks relative to baselines and comparable ecosystems, not absolute thresholds — resilience is comparative and dynamic
- build in a 'bright line' alert threshold for each metric where a breach triggers a mandatory review, not just a dashboard update
