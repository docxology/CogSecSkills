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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- commit fully to the adversarial perspective — half-hearted red teaming produces the illusion of scrutiny without the substance
- rank vulnerabilities by exploitability x impact, not by how uncomfortable they are to surface
- the red team's job is to find failure modes, not to balance them against strengths — balance is for the final synthesis, not the red team phase
- distinguish vulnerabilities that are inherent to the approach from those that are remediable — remediable ones get mitigations, inherent ones inform go/no-go
