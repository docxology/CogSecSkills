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

- For Ethics & Harms Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Ethics & Harms Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Ethics & Harms Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Ethics & Harms Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Ethics & Harms Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Ethics & Harms Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Ethics & Harms Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Ethics & Harms Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Ethics & Harms Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Ethics & Harms Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Ethics & Harms Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Ethics & Harms Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Ethics & Harms Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Ethics & Harms Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Ethics & Harms Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Ethics & Harms Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Ethics & Harms Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- enumerate harms by affected party, not just by harm type — diffuse harms to third parties are the ones most often missed
- distinguish between proximate misuse (the tool directly used for harm) and distal misuse (the tool enables a capability chain that causes harm)
- apply at least two incommensurable ethical frameworks; agreement across frameworks strengthens confidence, disagreement flags genuine ethical tension requiring human judgment
- do not conflate low-probability high-severity harms with low-probability low-severity ones — they require different responses
