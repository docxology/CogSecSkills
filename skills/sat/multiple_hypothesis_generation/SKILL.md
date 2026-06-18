---
name: sat.multiple_hypothesis_generation
description: Force a complete, mutually exclusive hypothesis set before evaluating any one.
---

# Multiple Hypothesis Generation

Multiple Hypothesis Generation (MHG) is a structured analytic technique that requires analysts to produce a complete, mutually exclusive and collectively exhaustive (MECE) set of hypotheses before evaluating any of them individually. Developed by Heuer and Pherson as a precursor to Analysis of Competing Hypotheses (ACH), MHG counters confirmation bias and anchoring by ensuring that the hypothesis set is not inadvertently incomplete — the most common failure mode in analytical forecasting and cognitive-security threat assessment.

## When to use

- analysis is beginning and the goal is to ensure the initial hypothesis set is not artificially narrow before any evaluation takes place
- an existing analysis feels anchored on a single explanation and team review is needed to surface alternatives
- prepping for ACH — MHG must precede ACH to guarantee the ACH matrix is not trivially incomplete
- a cognitive-security assessment needs to catalog all plausible explanations for an anomalous information event before attributing it

## What it produces

- a MECE-tested, labeled set of hypotheses covering the full logical space implied by the evidence
- a completeness audit showing which pairs overlap, which were merged, and whether any logical remainder (unaddressed possibility) was identified
- a clear distinguishing claim for each hypothesis that enables targeted evidence collection

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- hypotheses must be mutually exclusive: if H2 can be true at the same time as H1, they are not separate hypotheses
- the set must be collectively exhaustive: always include a residual hypothesis ('none of the above / insufficient evidence') to avoid forcing a false choice
- generate before evaluating — do not permit the likelihood of a hypothesis to influence whether it appears in the set
- each hypothesis needs a unique distinguishing claim — without one it cannot be discriminated from its neighbors by any evidence
