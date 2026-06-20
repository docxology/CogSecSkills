---
name: critical_review.ethics_and_harms_review
description: Assess dual-use, harm, and misuse potential of a project or capability.
---

# Ethics & Harms Review

Ethics & Harms Review systematically assesses a project, capability, dataset, or publication for dual-use risks, potential harms to individuals or communities, misuse potential by adversarial actors, and gaps in informed consent or transparency. It draws on established frameworks (consequentialist, deontological, virtue-ethics, and rights-based) alongside discipline-specific codes (e.g., Menlo Report for security research, Belmont Report for human subjects) to produce a structured harm register and a set of mitigations or go/no-go recommendations. In the cognitive-security context it is especially important for evaluating influence-operation tooling, adversarial AI research, and dual-use OSINT capabilities where potential harms are diffuse and probabilistic.

## When to use

- before releasing a tool, dataset, or model that could be weaponized or repurposed for manipulation
- when a research capability has clear dual-use potential (e.g., deepfake detection that also teaches generation)
- when a proposed capability interacts with vulnerable populations or protected information
- when organizational policy, IRB, or funder requires documented harm assessment

## What it produces

- a harm register listing specific harm scenarios with affected parties, likelihood, severity, and mitigation controls
- an ethical-framework analysis cross-checking the artifact against consequentialist, deontological, and rights-based standards
- a transparency and consent gap analysis
- a go/no-go recommendation with explicit conditions for release or further review

## Defensive boundary

Use Ethics & Harms Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Ethics & Harms Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Ethics & Harms Review, tie each harm register, and ethics assessment claim to concrete evidence from the specific artifact, intended use, and deployment context item, source excerpt, observation, or command result that supports it.
- For Ethics & Harms Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the harm register.
- Before recommending any Ethics & Harms Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Ethics & Harms Review: the harm register is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; ingest and scope and multi-framework harm identification checks agree, and no unresolved contradiction would change the result.
- Medium for Ethics & Harms Review: the harm register is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Ethics & Harms Review: the harm register rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Ethics & Harms Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Ethics & Harms Review, use only authorized artifact, intended use, and deployment context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Ethics & Harms Review, minimize person-level detail in the harm register; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Ethics & Harms Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Ethics & Harms Review: treating artifact as complete when ingest and scope and multi-framework harm identification checks or contradictory evidence are missing.
- Ethics & Harms Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Ethics & Harms Review: reporting the harm register without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Ethics & Harms Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the harm register from Ethics & Harms Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Ethics & Harms Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, intended use, and deployment context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- enumerate harms by affected party, not just by harm type — diffuse harms to third parties are the ones most often missed
- distinguish between proximate misuse (the tool directly used for harm) and distal misuse (the tool enables a capability chain that causes harm)
- apply at least two incommensurable ethical frameworks; agreement across frameworks strengthens confidence, disagreement flags genuine ethical tension requiring human judgment
- do not conflate low-probability high-severity harms with low-probability low-severity ones — they require different responses
