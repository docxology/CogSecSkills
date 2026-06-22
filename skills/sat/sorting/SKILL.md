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

- For Sorting, bind every cluster label and every outlier flag to concrete evidence from a specific item in the evidence set, citing the attribute value or source excerpt that places it in or outside a cluster, and record which dimension was primary so reviewers can re-sort and test whether the anomaly survives.
- For Sorting, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the sorted table.
- Before recommending any Sorting action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Sorting: the cluster labels and outlier flags are each grounded in evidence items whose attributes were inventoried before any sorting dimension was chosen, the same clusters and anomalies recur under independently selected primary and secondary axes, and no unresolved contradiction in the underlying data would change which items the technique flags as anomalous.
- Medium for Sorting: the sorted table is plausible, but one important evidence set source, comparison case, or alternative explanation remains incomplete.
- Low for Sorting: the sorted table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Sorting cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Sorting, use only authorized evidence set, and sort dimensions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Sorting, minimize person-level detail in the sorted table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Sorting, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Sorting: declaring the sorted table complete when the sort dimensions were picked after viewing the data to favour a hypothesis, or when flagged outliers were dropped without written justification, so the structure reflects the analyst's expectation rather than the genuine distribution of the evidence.
- Sorting: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Sorting: reporting the sorted table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Sorting outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the sorted table from Sorting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Sorting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with evidence set, and sort dimensions' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- choose sort dimensions before sorting to avoid unconsciously post-hoc selecting dimensions that confirm the current hypothesis
- treat every outlier as analytically significant until explicitly ruled out
- record which dimension was primary so reviewers can re-sort on alternative axes
