---
name: critical_review.red_team_review
description: Adversarially stress an artifact to find the failure mode its authors did not anticipate.
---

# Red-Team Review

Red-Team Review adversarially stresses an artifact — a plan, policy, argument, model, system, or narrative — to find failure modes, attack surfaces, and exploitable assumptions that the authors did not anticipate. Drawing on the structured analytic tradition of Devil's Advocacy and Team A/Team B analysis, and the security tradition of adversarial red teaming, the reviewer deliberately adopts an opposing or adversarial stance, generating the strongest possible critique, attack, or counter-narrative the artifact could face. The output is a ranked catalog of vulnerabilities, exploitation paths, and proposed mitigations, not a balanced review — the goal is maximum stress, not fairness. In cognitive-security contexts this includes identifying how a disinformation actor or manipulative adversary could exploit a proposed policy, narrative, or analytical product.

## When to use

- before committing to a plan, policy, or analytical judgment where overconfidence or groupthink is plausible
- when a narrative or information campaign needs to be evaluated for exploitability by an adversary
- when a proposed cognitive-security countermeasure needs stress-testing before deployment
- when an analytical product has been produced by a team with shared assumptions and an independent adversarial check is warranted
- when an organization needs to identify how an adversary would undermine a proposed decision or communication

## What it produces

- a ranked vulnerability catalog with exploitation paths and mitigations for each identified failure mode
- an adversarial narrative — the strongest case an opposing actor could make against the artifact
- a set of mitigation recommendations addressing the highest-priority vulnerabilities
- identification of the assumptions whose failure would be most catastrophic

## Defensive boundary

Use Red-Team Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Red-Team Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Red-Team Review, tie each vulnerability catalog, and red team narrative claim to concrete evidence from the specific artifact, adversary profile, and review scope item, source excerpt, observation, or command result that supports it.
- For Red-Team Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the vulnerability catalog.
- Before recommending any Red-Team Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Red-Team Review: the vulnerability catalog is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; ingest and model the adversary and generate attack surface checks agree, and no unresolved contradiction would change the result.
- Medium for Red-Team Review: the vulnerability catalog is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Red-Team Review: the vulnerability catalog rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Red-Team Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Red-Team Review, use only authorized artifact, adversary profile, and review scope, public or source-approved records, and caller-provided context needed for the defensive task.
- For Red-Team Review, minimize person-level detail in the vulnerability catalog; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Red-Team Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Red-Team Review: treating artifact as complete when ingest and model the adversary and generate attack surface checks or contradictory evidence are missing.
- Red-Team Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Red-Team Review: reporting the vulnerability catalog without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Red-Team Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the vulnerability catalog from Red-Team Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Red-Team Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, adversary profile, and review scope' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- commit fully to the adversarial perspective — half-hearted red teaming produces the illusion of scrutiny without the substance
- rank vulnerabilities by exploitability x impact, not by how uncomfortable they are to surface
- the red team's job is to find failure modes, not to balance them against strengths — balance is for the final synthesis, not the red team phase
- distinguish vulnerabilities that are inherent to the approach from those that are remediable — remediable ones get mitigations, inherent ones inform go/no-go
