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

## Defensive boundary

Use Logical Coherence Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Logical Coherence Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Logical Coherence Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Logical Coherence Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Logical Coherence Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Logical Coherence Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Logical Coherence Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Logical Coherence Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Logical Coherence Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Logical Coherence Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Logical Coherence Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Logical Coherence Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Logical Coherence Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Logical Coherence Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Logical Coherence Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Logical Coherence Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Logical Coherence Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Logical Coherence Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Logical Coherence Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate the argument's validity (does the conclusion follow from premises) from its soundness (are the premises true) — both matter but must be assessed independently
- surface hidden premises explicitly — the most dangerous logical gaps are the ones the author never stated
- classify fallacies by type before assessing severity — formal fallacies invalidate the argument; informal fallacies weaken it but may not defeat it alone
- equivocation on key terms is the most common source of apparent but spurious coherence — force explicit definition of contested terms before assessing inference
