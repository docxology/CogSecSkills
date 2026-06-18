---
name: sat.analysis_of_competing_hypotheses
description: >-
  Score evidence by diagnosticity across a full hypothesis set to find the
  least-disconfirmed explanation, countering confirmation bias. Use when there
  are multiple plausible explanations and you must adjudicate rigorously.
---

# Analysis of Competing Hypotheses (ACH)

Use ACH when a question has **several plausible explanations** and the cost of
anchoring on the wrong one is high. ACH inverts ordinary reasoning: instead of
assembling evidence *for* a favored hypothesis, you assemble *all* hypotheses
and look for evidence that **disconfirms** each. The strongest hypothesis is the
one left standing with the least evidence against it.

## When to use

- Multiple competing explanations for an event, attribution, or trend.
- You suspect you (or the source) have anchored on a first impression.
- A high-stakes judgment where confirmation bias would be costly.

**Not for** single-hypothesis confirmation (that is the bias ACH exists to break)
or trivial questions with one obvious answer.

## What it produces

1. A complete, mutually-exclusive hypothesis set.
2. An evidence × hypothesis **matrix** scored Consistent / Inconsistent / N/A,
   with diagnosticity weights.
3. A **ranking** by inconsistency score (least-disconfirmed first).
4. **Indicators** — future observations that would change the conclusion.
5. A confidence statement and the most damaging single piece of evidence.

## Procedure

Run the eight-step loop in [`workflow.md`](workflow.md). The harness-specific
tool bindings are in [`harness/`](harness/).

## Key discipline

- **Diagnosticity over weight of evidence.** Evidence consistent with *every*
  hypothesis has zero diagnostic value, however voluminous.
- **Disconfirm, don't confirm.** Rank by inconsistency, not consistency.
- **Absence of evidence is evidence.** A missing observation a hypothesis
  predicts is itself diagnostic.
- **Sensitivity check.** Identify which one or two items, if wrong, flip the
  conclusion — those are the items to re-verify.
