---
name: sat.chronologies_and_timelines
description: Order events temporally to expose gaps, correlations, and causal sequencing.
---

# Chronologies & Timelines

Chronologies and Timelines is a structured-analytic technique that arranges known events in strict temporal order to reveal gaps in the record, surface correlations between concurrent streams, and clarify causal versus coincidental sequencing. By making the time dimension explicit and visual, analysts can spot anomalies — missing intervals, suspicious clustering, or reversed apparent causality — that narrative prose conceals. The technique is foundational in targeting, deception detection, and incident reconstruction, and it underpins more complex temporal analytics such as event-driven scenario building and link analysis.

## When to use

- reconstructing an incident or attack campaign where sequence of actions is disputed or unclear
- detecting deception by comparing declared timelines against independently sourced event dates
- preparing for an analysis of competing hypotheses where causality order matters
- surfacing intelligence gaps before a collection tasking decision

## What it produces

- a sorted, sourced table of events anchored to specific dates and actors
- explicit identification of gaps — periods with no sourced events — and their potential significance
- correlation findings: events in different streams that cluster or co-vary suspiciously
- a prioritized list of collection requirements to fill identified gaps

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate WHAT IS KNOWN (sourced, dated) from WHAT IS INFERRED — never merge them in the same row
- record confidence level per event, not just the event itself — a low-confidence date poisons downstream causal claims
- a gap in the record is itself a datum: note it explicitly rather than silently skipping it
