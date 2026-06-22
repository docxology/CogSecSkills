---
name: sat.ranking_and_prioritization
description: Order items by weighted criteria (ranked voting, paired comparison, weighted scoring).
---

# Ranking & Prioritization

Ranking and Prioritization techniques (including paired comparison, weighted scoring, and ranked voting) impose structured criteria on a list of items — threats, hypotheses, options, or findings — to produce a defensible, criterion-transparent ordering. Rather than relying on unaided intuition or the implicit dominance of the most vocal participant, these methods make evaluative weights explicit and replicable. In cognitive-security contexts the technique surfaces hidden priority divergence among analysts and defends against availability and anchoring biases that distort informal ranking.

## When to use

- a group must allocate limited attention, resources, or response capacity across multiple competing items
- informal or intuitive ranking risks being dominated by availability bias, anchoring, or loudest-voice dynamics
- a decision maker needs a documented, auditable priority order rather than an undifferentiated list
- multiple analysts or stakeholders hold divergent implicit priorities that need to be surfaced and reconciled

## What it produces

- a criterion-weighted scoring matrix making evaluative assumptions explicit and auditable
- a ranked priority list with per-item scores and placement rationale
- a sensitivity analysis showing which items are most sensitive to weight choices, guiding further deliberation

## Defensive boundary

Use Ranking & Prioritization only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Ranking & Prioritization to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Ranking & Prioritization, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Ranking & Prioritization, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Ranking & Prioritization recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Ranking & Prioritization: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Ranking & Prioritization: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Ranking & Prioritization: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Ranking & Prioritization cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Ranking & Prioritization should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Ranking & Prioritization, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Ranking & Prioritization, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Ranking & Prioritization, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Ranking & Prioritization failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Ranking & Prioritization failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Ranking & Prioritization failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Ranking & Prioritization to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Ranking & Prioritization into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Ranking & Prioritization to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- define criteria before scoring items — post-hoc criteria inversion is a bias amplifier, not a correction
- weights must reflect the decision context, not the analyst's prior preference for the ranking outcome
- paired comparison is preferred when the number of items is small (≤10) and criteria feel incommensurable; weighted scoring scales better
- sensitivity analysis is not optional — a ranking that collapses under small weight changes deserves explicit acknowledgment
