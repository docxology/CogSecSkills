---
name: sat.structured_brainstorming
description: Divergent then convergent idea generation with explicit anti-anchoring steps.
---

# Structured Brainstorming

Structured Brainstorming is a two-phase diverge-then-converge technique that separates unconstrained idea generation from critical evaluation to prevent anchoring, groupthink, and premature convergence on the most socially acceptable or seniority-endorsed hypothesis. The divergence phase enforces deferral of judgment while the convergence phase uses explicit criteria to cluster, rank, and discard ideas. In cognitive-security analysis it surfaces hypotheses and threat vectors that a linear, hierarchical review would suppress, and the explicit anti-anchoring steps protect against an adversary's ability to pre-seed the analytic frame.

## When to use

- the problem space has not been rigorously scoped and unknown hypotheses may have been missed
- a dominant hypothesis has hardened in the analytic team and alternative possibilities are being systematically overlooked
- an adversary may have deliberately seeded a single compelling narrative to anchor analytic attention
- planning stage of a complex investigation where the hypothesis list is the first deliverable

## What it produces

- a raw, unconstrained idea inventory that captures every plausible hypothesis or option before filtering
- a convergence output with ideas clustered by theme, ranked by stated criteria, and a record of discarded ideas and the reasons for discarding them

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- no criticism, evaluation, or ranking is permitted during the divergence phase — deferral of judgment is the technique's core mechanism
- quantity of ideas in divergence is a feature: more ideas reduce the probability that the best one was anchored out
- every discarded idea from convergence must be recorded with an explicit reason — silent omission is how groupthink re-enters
