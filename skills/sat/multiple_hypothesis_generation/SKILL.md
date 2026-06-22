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

- For Multiple Hypothesis Generation, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Multiple Hypothesis Generation, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Multiple Hypothesis Generation recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Multiple Hypothesis Generation: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Multiple Hypothesis Generation: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Multiple Hypothesis Generation: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Multiple Hypothesis Generation cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Multiple Hypothesis Generation should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Multiple Hypothesis Generation, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Multiple Hypothesis Generation, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Multiple Hypothesis Generation, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Multiple Hypothesis Generation failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Multiple Hypothesis Generation failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Multiple Hypothesis Generation failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Multiple Hypothesis Generation to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Multiple Hypothesis Generation into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Multiple Hypothesis Generation to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- hypotheses must be mutually exclusive: if H2 can be true at the same time as H1, they are not separate hypotheses
- the set must be collectively exhaustive: always include a residual hypothesis ('none of the above / insufficient evidence') to avoid forcing a false choice
- generate before evaluating — do not permit the likelihood of a hypothesis to influence whether it appears in the set
- each hypothesis needs a unique distinguishing claim — without one it cannot be discriminated from its neighbors by any evidence
