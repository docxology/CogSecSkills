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

## Defensive boundary

Use Chronologies & Timelines only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Chronologies & Timelines to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Chronologies & Timelines, anchor every entry and every gap-and-anomaly finding to the dated source evidence that supports it, record a confidence level per event, and explicitly note collection limitations so absence of evidence is never silently read as evidence of absence.
- For Chronologies & Timelines, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the chronology.
- Before recommending any Chronologies & Timelines action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Chronologies & Timelines: each event carries an explicit date, actor, source, and confidence level, sourced facts are kept strictly separate from inferences, identified gaps and clustering are corroborated across independent streams, and no unresolved contradiction would change the timeline's bearing on the focal question.
- Medium for Chronologies & Timelines: the chronology is plausible, but one important event sources source, comparison case, or alternative explanation remains incomplete.
- Low for Chronologies & Timelines: the chronology rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Chronologies & Timelines cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Chronologies & Timelines, use only authorized event sources, analytic question, and parallel streams, public or source-approved records, and caller-provided context needed for the defensive task.
- For Chronologies & Timelines, minimize person-level detail in the chronology; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Chronologies & Timelines, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Chronologies & Timelines: merging inferred dates with sourced ones or treating a silent interval as proof of inactivity rather than a recorded collection gap, so a low-confidence or absent date poisons the downstream causal and foreknowledge claims the timeline is meant to test.
- Chronologies & Timelines: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Chronologies & Timelines: reporting the chronology without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Chronologies & Timelines outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the chronology from Chronologies & Timelines into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Chronologies & Timelines to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with event sources, analytic question, and parallel streams' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate WHAT IS KNOWN (sourced, dated) from WHAT IS INFERRED — never merge them in the same row
- record confidence level per event, not just the event itself — a low-confidence date poisons downstream causal claims
- a gap in the record is itself a datum: note it explicitly rather than silently skipping it
