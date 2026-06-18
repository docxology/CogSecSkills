---
name: cognitive_security.attack_surface_of_belief_mapping
description: Map which beliefs of a target audience are most exposed to manipulation and why.
---

# Belief Attack-Surface Mapping

Belief Attack-Surface Mapping identifies which held beliefs of a target audience are structurally most exposed to adversarial manipulation — analyzing the epistemic properties (evidence base, social anchoring, emotional loading, and prior-belief dependencies) that make specific beliefs more or less resistant to influence operations. The output is a ranked map that defenders can use to design targeted inoculation, prebunking, or counter-messaging interventions before an adversary exploits a vulnerability. This is a defensive analytical technique analogous to network attack-surface analysis applied to epistemic infrastructure.

## When to use

- designing a pre-emptive defense against anticipated influence operations targeting a specific community
- advising a communications team on which narratives to inoculate audiences against before an adversary can seed them
- conducting a red-team assessment of an audience's epistemic resilience
- prioritizing limited prebunking or media-literacy resources across a complex belief landscape
- informing policy decisions about where epistemic infrastructure investment is most urgently needed

## What it produces

- a ranked map of belief vulnerabilities ordered by exploitation likelihood and potential impact
- per-belief scoring on four vulnerability dimensions: evidence thinness, emotional salience, identity anchoring, and social proof dependence
- the manipulation vectors (narrative frames, emotional appeals, messenger types) most likely to exploit each high-exposure belief
- a prioritized intervention menu for defenders (prebunking, counter-messaging, source diversification, social norm reframing)

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess beliefs across multiple independent vulnerability dimensions — a belief that scores high on only one dimension is far less exposed than one that scores high on all four
- distinguish beliefs that are epistemically thin (poorly evidenced) from those that are identity-anchored (correcting them triggers backfire) — the defensive intervention is different for each type
- focus on exposure, not just prevalence — a widely-held but well-evidenced belief is less dangerous to hold than a narrowly-held but epistemically fragile one that gatekeeps key decisions
