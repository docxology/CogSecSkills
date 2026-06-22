---
name: sat.sorting
description: Group large evidence sets by attributes to surface patterns and outliers.
---

# Sorting

Sorting is a structured-analytic technique that organizes a large evidence or indicator set by one or more attributes (date, source reliability, geographic origin, significance) so that meaningful clusters, trends, and outliers become visible. It converts an unordered mass of raw data into a structured view that supports pattern recognition and gap detection. In cognitive-security contexts, sorting exposes anomalies—items that do not fit the dominant cluster—which may represent deception artifacts, seeded disinformation, or signals of an adversary's hand.

## When to use

- the evidence base is large enough that key patterns are invisible without organization
- an analyst suspects clustering or grouping effects that unaided review would miss
- outlier detection is needed to surface potential deception or seeded disinformation
- preparation for a more intensive technique (e.g., ACH, indicators validation) requires a tidy input

## What it produces

- a multi-dimensional sorted view of all evidence items in a structured table
- cluster labels that name the dominant groupings in the evidence
- a flagged outlier list with analytic notes on why each item is anomalous

## Defensive boundary

Use Sorting only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Sorting to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Sorting, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Sorting, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Sorting recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Sorting: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Sorting: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Sorting: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Sorting cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Sorting should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Sorting, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Sorting, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Sorting, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Sorting failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Sorting failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Sorting failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Sorting to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Sorting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Sorting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- choose sort dimensions before sorting to avoid unconsciously post-hoc selecting dimensions that confirm the current hypothesis
- treat every outlier as analytically significant until explicitly ruled out
- record which dimension was primary so reviewers can re-sort on alternative axes
