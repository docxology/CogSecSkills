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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- enumerate harms by affected party, not just by harm type — diffuse harms to third parties are the ones most often missed
- distinguish between proximate misuse (the tool directly used for harm) and distal misuse (the tool enables a capability chain that causes harm)
- apply at least two incommensurable ethical frameworks; agreement across frameworks strengthens confidence, disagreement flags genuine ethical tension requiring human judgment
- do not conflate low-probability high-severity harms with low-probability low-severity ones — they require different responses
