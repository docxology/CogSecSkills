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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- define criteria before scoring items — post-hoc criteria inversion is a bias amplifier, not a correction
- weights must reflect the decision context, not the analyst's prior preference for the ranking outcome
- paired comparison is preferred when the number of items is small (≤10) and criteria feel incommensurable; weighted scoring scales better
- sensitivity analysis is not optional — a ranking that collapses under small weight changes deserves explicit acknowledgment
