---
name: critical_review.red_team_review
description: Adversarially stress an artifact to find the failure mode its authors did not anticipate.
---

# Red-Team Review

Red-Team Review adversarially stresses an artifact — a plan, policy, argument, model, system, or narrative — to find failure modes, attack surfaces, and exploitable assumptions that the authors did not anticipate. Drawing on the structured analytic tradition of Devil's Advocacy and structured Team A/Team B analysis, the security tradition of adversarial red teaming, and the structured attack decomposition of threat modeling, the reviewer deliberately adopts an opposing or adversarial stance and builds the strongest possible critique, attack, or counter-narrative the artifact could face. Devil's Advocacy is a single analyst (or this skill) constructing the strongest contrary case against the prevailing view; structured Team A/Team B uses two independent teams that produce competing products to be adjudicated. This skill emulates the contrary case as one product and flags Team A/Team B as the heavier alternative when shared assumptions between reviewer and author are the real risk. The output is a ranked catalog of vulnerabilities, exploitation paths, compounding attack chains, mitigations, and an explicit go / no-go recommendation — not a balanced review. The goal is maximum stress, not fairness. In cognitive-security contexts this includes identifying how a disinformation actor or manipulative adversary could exploit a proposed policy, narrative, or analytical product.

## When to use

- before committing to a plan, policy, or analytical judgment where overconfidence or groupthink is plausible
- when a narrative or information campaign needs to be evaluated for exploitability by an adversary
- when a proposed cognitive-security countermeasure needs stress-testing before deployment
- when an analytical product has been produced by a team with shared assumptions and an independent adversarial check is warranted
- when an organization needs to identify how an adversary would undermine a proposed decision or communication
- when the existing analysis was produced inside a single shared frame and a single strong contrary case is wanted (Devil's Advocacy posture) — as opposed to when the stakes justify two independent teams building competing products to be adjudicated (structured Team A/Team B), which this skill emulates as one product but should flag as a heavier alternative

## What it produces

- a ranked vulnerability catalog with exploitation paths, exploitability and impact scores, priority bands, and mitigations for each identified failure mode
- an adversarial narrative — the strongest case an opposing actor could make against the artifact, routed through the highest-priority compounding attack chains
- explicit compounding chains showing how a low-impact flaw can unlock a high-impact one, re-banded to the worst outcome the chain reaches
- a set of mitigation recommendations addressing the highest-priority vulnerabilities, each re-tested against the modeled adversary to confirm it holds
- an explicit classification of each top vulnerability as inherent (informs go/no-go) or remediable (receives a mitigation)
- a go / no-go / go-with-conditions recommendation that states the residual risk a decision-maker would accept if the artifact proceeds unchanged

## Defensive boundary

Use Red-Team Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Red-Team Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Red-Team Review, tie every entry in the vulnerability catalog and every claim in the red-team narrative to concrete evidence — a quoted excerpt from the artifact, a referenced row of the artifact map, a stated capability in the adversary profile, a review-scope item, an observation, or a command result — and name the adversary capability that would turn that evidence into an exploit. A vulnerability with no cited evidence and no plausible exploitation path is a speculation, not a finding, and is labelled as such.
- For Red-Team Review, label observations, derived features, assumptions, and inferences (each marked as inference, not evidence) separately before writing the vulnerability catalog, so a reader can tell what was seen from what was reasoned.
- Before recommending any Red-Team Review go/no-go action, identify the weakest evidence link behind the highest-ranked finding, the alternative adversary model most likely to overturn it, and the next discriminating check that would settle it.

## Confidence and uncertainty

- High for Red-Team Review: the highest-ranked vulnerabilities are each tied to specific artifact excerpts and a coherent adversary capability, the exploitability-by-impact ranking is stable when any single excerpt is removed, the adversary model and the enumerated attack surface are mutually consistent, and no unresolved contradiction in the adversarial narrative would change the go/no-go conclusion.
- Medium for Red-Team Review: the vulnerability catalog is plausible, but one important artifact source, comparison case, or alternative adversary model remains incomplete.
- Low for Red-Team Review: the vulnerability catalog rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next discriminating check.
- State what Red-Team Review cannot determine from the supplied or authorized evidence, including which attack paths remain unknown.
- Preserve credible alternative adversary models and exploitation hypotheses rather than forcing a single worst-case narrative or attribution.
- Recommend the next discriminating piece of evidence to collect when confidence is low or medium, and name the alternative adversary model it would help rule out.
- Treat exploitability and impact scores as analyst estimates, not measurements; flag findings where two reviewers could reasonably score differently, and state that the priority bands and go/no-go are calibrated judgments to be peer-checked rather than objective values.

## Privacy, legal, and harm constraints

- For Red-Team Review, use only the authorized artifact, adversary profile, and review scope, together with public or source-approved records and the caller-provided context needed for the defensive task.
- For Red-Team Review, minimize person-level detail in the vulnerability catalog; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Red-Team Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Red-Team Review: declaring the artifact stress-tested when the adversary model was never grounded (no intent, capability, or access assumptions) or the attack-surface enumeration skipped a relevant dimension (logical, operational, technical, informational, reputational), so the absence of findings reflects an incomplete review rather than a hardened artifact.
- Red-Team Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Red-Team Review: reporting the vulnerability catalog without uncertainty labels, alternative adversary models, and the next discriminating check.
- Unsafe: 'Use Red-Team Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the Red-Team Review vulnerability catalog into a deployable attack recipe with no mitigations' -> refuse and offer governance, detection, or mitigation analysis of the same vulnerabilities instead.
- Safe defensive: 'Use Red-Team Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, adversary profile, and review scope' -> produce a bounded vulnerability catalog and adversarial narrative with evidence labels, uncertainty labels, and a go/no-go recommendation.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- commit fully to the adversarial perspective — half-hearted red teaming produces the illusion of scrutiny without the substance
- make exploitability and impact concrete before ranking — rate exploitability by the modeled adversary's required capability and access (trivial / feasible-with-effort / requires-rare-capability) and impact by consequence to the artifact's goal (cosmetic / degrading / mission-defeating), then rank on the product so a trivially exploitable mission-defeating flaw outranks a hard-to-reach cosmetic one
- rank vulnerabilities by exploitability times impact, never by how uncomfortable they are to surface or by the seniority of whoever introduced them
- the red team's job is to find failure modes, not to balance them against strengths — balance is for the final synthesis, not the red team phase
- distinguish vulnerabilities that are inherent to the approach from those that are remediable — remediable ones get mitigations, inherent ones plus any high-exploitability high-impact chain that mitigations cannot fully close feed the go/no-go call
