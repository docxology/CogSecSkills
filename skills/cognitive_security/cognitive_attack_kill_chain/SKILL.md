---
name: cognitive_security.cognitive_attack_kill_chain
description: Stage a cognitive attack (recon→delivery→exploitation→persistence) to plan defenses per stage.
---

# Cognitive Attack Kill Chain

The Cognitive Attack Kill Chain adapts the cyber-security kill-chain model to influence operations, decomposing a cognitive attack into stages — reconnaissance, weaponization, delivery, exploitation, installation, command-and-control, and persistence — so that defenders can identify intervention points at each stage before the attack achieves its goal. By mapping observed or anticipated adversary activities to kill-chain stages, defenders can assess which stages have already been traversed, which are in progress, and which can still be disrupted. This is a defensive red-teaming and threat-modeling technique, not an operational planning framework.

## When to use

- an analyst needs to understand what stage an ongoing influence campaign has reached and what remains to be disrupted
- a defender is planning countermeasures and needs to allocate effort across stages of a prospective attack
- a red team is stress-testing a community's resilience by modeling a full attack sequence before it occurs
- a post-campaign analysis is needed to learn which defensive interventions were available at each stage and which were missed
- a threat-intelligence team is producing a brief on an adversary's influence-operation TTPs for decision-makers

## What it produces

- a stage-by-stage mapping of the adversary's campaign activities to kill-chain phases
- an assessment of which stages have been completed, which are in progress, and which can still be prevented
- a prioritized defender action table with one or more disruption options per accessible stage
- an explicit uncertainty log so analysts can distinguish high-confidence stage assessments from speculative ones

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- earlier kill-chain stages are always cheaper to disrupt — a campaign interdicted at reconnaissance or weaponization stage causes far less harm than one disrupted only after content has been delivered and exploited at scale
- distinguish stage completion from impact: an adversary may have completed delivery without achieving exploitation if the content failed to resonate — do not conflate a completed stage with a successful one
- be explicit about uncertainty: kill-chain stage assignments based on incomplete evidence should be marked as hypotheses, not facts, and collection gaps should be surfaced rather than papered over
