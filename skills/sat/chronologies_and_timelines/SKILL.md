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

- For Chronologies & Timelines, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Chronologies & Timelines, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Chronologies & Timelines recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Chronologies & Timelines: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Chronologies & Timelines: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Chronologies & Timelines: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Chronologies & Timelines cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Chronologies & Timelines should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Chronologies & Timelines, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Chronologies & Timelines, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Chronologies & Timelines, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Chronologies & Timelines failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Chronologies & Timelines failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Chronologies & Timelines failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Chronologies & Timelines to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Chronologies & Timelines into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Chronologies & Timelines to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate WHAT IS KNOWN (sourced, dated) from WHAT IS INFERRED — never merge them in the same row
- record confidence level per event, not just the event itself — a low-confidence date poisons downstream causal claims
- a gap in the record is itself a datum: note it explicitly rather than silently skipping it
