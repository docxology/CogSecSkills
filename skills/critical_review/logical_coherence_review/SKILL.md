---
name: critical_review.logical_coherence_review
description: Test an argument's internal consistency and the validity of its inferential steps.
---

# Logical Coherence Review

Logical Coherence Review tests an argument's internal consistency and the validity of its inferential steps by mapping claims to their supporting premises and checking whether the conclusions follow by valid deductive or inductive inference. It identifies formal fallacies (affirming the consequent, undistributed middle, equivocation), informal fallacies (ad hominem, strawman, slippery slope), hidden premises, and equivocal use of key terms. In the cognitive-security domain, logical coherence review is a first-line defense against narratives that appear compelling through rhetorical momentum rather than sound inference — including disinformation frames, policy recommendations resting on non-sequiturs, and intelligence assessments where the analytic confidence overstates the logical support.

## When to use

- when a narrative or policy argument needs to be accepted or rejected on its logical merits, not its rhetorical appeal
- when evaluating an intelligence assessment to determine whether its confidence level is supported by the inferential chain
- when a disinformation narrative is spreading and analysts need to identify the specific logical breaks that make it vulnerable to rebuttal
- when reviewing a proposed response to an influence operation to ensure the counter-argument is itself logically sound

## What it produces

- an explicit argument map showing conclusion, premises, and linking inferences, with hidden premises surfaced
- a classified list of formal and informal fallacies with location references and severity ratings
- a verdict on whether the conclusion validly follows from premises, and under what conditions it could
- specific recommendations: which premises to strengthen, which inferences to restate, or a recommendation to reject the argument

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate the argument's validity (does the conclusion follow from premises) from its soundness (are the premises true) — both matter but must be assessed independently
- surface hidden premises explicitly — the most dangerous logical gaps are the ones the author never stated
- classify fallacies by type before assessing severity — formal fallacies invalidate the argument; informal fallacies weaken it but may not defeat it alone
- equivocation on key terms is the most common source of apparent but spurious coherence — force explicit definition of contested terms before assessing inference
