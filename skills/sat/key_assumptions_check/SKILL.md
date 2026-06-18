---
name: sat.key_assumptions_check
description: >-
  Surface every assumption an analysis rests on — stated and unstated — classify
  each as solid, caveated, unsupported, or a key uncertainty, and stress-test the
  load-bearing ones by asking whether the conclusion collapses if they are wrong.
  Use before committing to a judgment that quietly depends on beliefs taken for granted.
---

# Key Assumptions Check

Every analytic judgment rests on assumptions — premises accepted as true without
being re-examined. Most are never written down, which is exactly why they are
dangerous: an unstated assumption that is both **load-bearing** and **wrong** can
make a confident conclusion fail silently. The Key Assumptions Check (Heuer &
Pherson) forces those premises into the open, tests each against evidence and
contrary conditions, and isolates the few "key" assumptions on which the whole
judgment actually pivots.

## When to use

- Before finalizing a high-stakes estimate, attribution, or recommendation.
- When a conclusion feels obvious or comfortable — comfort is where unstated
  assumptions hide.
- When the situation has changed and old assumptions may no longer hold.
- As a precondition to other techniques (it pairs naturally with ACH and
  scenario work, which depend on knowing what is being assumed).

**Not for** questions with no real analytic line, or trivial judgments that rest
on directly observed fact rather than inference.

## What it produces

1. A complete list of assumptions, including the **unstated** ones the analysis
   silently relies on.
2. For each assumption: why we believe it, the evidence that supports it, and
   the conditions under which it would **not** hold.
3. A confidence **classification** per assumption — solid / caveated /
   unsupported / key uncertainty.
4. **Key assumptions** flagged: those that are both load-bearing and uncertain,
   each with a "does the conclusion collapse if this is wrong?" analysis.
5. The **collection or research** that would test the key assumptions.
6. A **rewritten judgment** that states the conclusion together with the
   assumptions it depends on.

## Procedure

Run the six-step loop in [`workflow.md`](workflow.md). The harness-specific tool
bindings are in [`harness/`](harness/).

## Key discipline

- **Hunt the unstated.** The assumptions that matter most are usually the ones
  no one bothered to write down. Do not let one pass unexamined.
- **No free passes for comfort.** An assumption is not "solid" because it is
  familiar or convenient — it is solid only when evidence makes it so. Never mark
  a comfortable assumption solid without evidence.
- **Load-bearing × uncertain = key.** A shaky assumption that nothing depends on
  is harmless; a rock-solid one is fine. Only the intersection deserves the
  "key" flag and the collapse test.
- **Expose the dependence.** A judgment that hides its assumptions overstates its
  confidence. Rewrite it so the reader sees exactly what it rests on.
