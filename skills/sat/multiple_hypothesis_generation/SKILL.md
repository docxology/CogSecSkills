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

## Defensive boundary

Use Multiple Hypothesis Generation only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Multiple Hypothesis Generation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Multiple Hypothesis Generation, ground each hypothesis and the completeness audit in concrete evidence from the evidence set, initial hypotheses, and domain context, recording every merge, split, and identified gap; a hypothesis admitted or excluded without evidence tied to its distinguishing claim weakens the MECE guarantee and must be documented as such.
- For Multiple Hypothesis Generation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the hypothesis set.
- Before recommending any Multiple Hypothesis Generation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Multiple Hypothesis Generation: the hypothesis set passes pairwise mutual-exclusivity testing, the collective-exhaustiveness check includes an explicit residual for the uncovered logical space, each hypothesis carries a unique distinguishing claim, and no unresolved overlap or remainder would change the completeness of the set before evaluation begins.
- Medium for Multiple Hypothesis Generation: the hypothesis set is plausible, but one important evidence set source, comparison case, or alternative explanation remains incomplete.
- Low for Multiple Hypothesis Generation: the hypothesis set rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Multiple Hypothesis Generation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Multiple Hypothesis Generation, use only authorized evidence set, initial hypotheses, and domain context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Multiple Hypothesis Generation, minimize person-level detail in the hypothesis set; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Multiple Hypothesis Generation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Multiple Hypothesis Generation: declaring the set complete when no test for a logical remainder was run or low-probability but possible explanations were excluded on perceived likelihood, leaving an artificially narrow set that confirmation bias can then exploit downstream in ACH.
- Multiple Hypothesis Generation: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Multiple Hypothesis Generation: reporting the hypothesis set without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Multiple Hypothesis Generation outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the hypothesis set from Multiple Hypothesis Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Multiple Hypothesis Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with evidence set, initial hypotheses, and domain context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- hypotheses must be mutually exclusive: if H2 can be true at the same time as H1, they are not separate hypotheses
- the set must be collectively exhaustive: always include a residual hypothesis ('none of the above / insufficient evidence') to avoid forcing a false choice
- generate before evaluating — do not permit the likelihood of a hypothesis to influence whether it appears in the set
- each hypothesis needs a unique distinguishing claim — without one it cannot be discriminated from its neighbors by any evidence
