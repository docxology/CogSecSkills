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

- For Logical Coherence Review, tie each argument map, fallacy register, and coherence verdict claim to concrete evidence from the specific argument text, and key claims item, source excerpt, observation, or command result that supports it.
- For Logical Coherence Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the argument map.
- Before recommending any Logical Coherence Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Logical Coherence Review: the argument map is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; extract and segment and build argument map and surface hidden premises checks agree, and no unresolved contradiction would change the result.
- Medium for Logical Coherence Review: the argument map is plausible, but one important argument text source, comparison case, or alternative explanation remains incomplete.
- Low for Logical Coherence Review: the argument map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Logical Coherence Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Logical Coherence Review, use only authorized argument text, and key claims, public or source-approved records, and caller-provided context needed for the defensive task.
- For Logical Coherence Review, minimize person-level detail in the argument map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Logical Coherence Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Logical Coherence Review: treating argument text as complete when extract and segment and build argument map and surface hidden premises checks or contradictory evidence are missing.
- Logical Coherence Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Logical Coherence Review: reporting the argument map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Logical Coherence Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the argument map from Logical Coherence Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Logical Coherence Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with argument text, and key claims' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- separate the argument's validity (does the conclusion follow from premises) from its soundness (are the premises true) — both matter but must be assessed independently
- surface hidden premises explicitly — the most dangerous logical gaps are the ones the author never stated
- classify fallacies by type before assessing severity — formal fallacies invalidate the argument; informal fallacies weaken it but may not defeat it alone
- equivocation on key terms is the most common source of apparent but spurious coherence — force explicit definition of contested terms before assessing inference
