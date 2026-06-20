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

- For Ranking & Prioritization, tie each scoring matrix, ranked list, and sensitivity analysis claim to concrete evidence from the specific item list, criteria, and decision context item, source excerpt, observation, or command result that supports it.
- For Ranking & Prioritization, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the scoring matrix.
- Before recommending any Ranking & Prioritization action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Ranking & Prioritization: the scoring matrix is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; establish criteria and weights and score each item checks agree, and no unresolved contradiction would change the result.
- Medium for Ranking & Prioritization: the scoring matrix is plausible, but one important item list source, comparison case, or alternative explanation remains incomplete.
- Low for Ranking & Prioritization: the scoring matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Ranking & Prioritization cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Ranking & Prioritization, use only authorized item list, criteria, and decision context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Ranking & Prioritization, minimize person-level detail in the scoring matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Ranking & Prioritization, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Ranking & Prioritization: treating item list as complete when establish criteria and weights and score each item checks or contradictory evidence are missing.
- Ranking & Prioritization: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Ranking & Prioritization: reporting the scoring matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Ranking & Prioritization outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the scoring matrix from Ranking & Prioritization into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Ranking & Prioritization to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with item list, criteria, and decision context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- define criteria before scoring items — post-hoc criteria inversion is a bias amplifier, not a correction
- weights must reflect the decision context, not the analyst's prior preference for the ranking outcome
- paired comparison is preferred when the number of items is small (≤10) and criteria feel incommensurable; weighted scoring scales better
- sensitivity analysis is not optional — a ranking that collapses under small weight changes deserves explicit acknowledgment
