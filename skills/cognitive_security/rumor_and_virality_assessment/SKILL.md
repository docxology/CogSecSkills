---
name: cognitive_security.rumor_and_virality_assessment
description: Estimate a claim's spread potential from emotional charge, ambiguity, and network fit.
---

# Rumor & Virality Assessment

Rumor and virality assessment applies social-epidemiological and computational models to estimate how quickly and widely a claim is likely to spread through social networks. It examines emotional valence, ambiguity, moral outrage, information gaps, and structural network properties to predict transmission probability and identify leverage points for early counter-messaging. Rooted in DiFonzo & Bordia's rumor research and computational work on information cascades, this technique helps analysts forecast misinformation spread before it becomes entrenched.

## When to use

- a novel claim or narrative fragment has just appeared and you need to decide how urgently to respond
- planning counter-messaging and need to know the optimal intervention window before the claim hardens into belief
- conducting a post-hoc analysis to understand why a past claim spread or stalled
- evaluating the information environment around a forthcoming event that adversaries might exploit
- assessing whether a slow-burning rumor is accelerating toward critical spread velocity

## What it produces

- a composite virality score (Low / Moderate / High / Critical) with confidence level
- a factor breakdown rating emotional charge, ambiguity, moral-outrage load, novelty, audience resonance, and network amplification potential
- a predicted spread trajectory curve (hours-to-peak, estimated reach tier, decay rate)
- a list of counter-messaging leverage windows ranked by time-sensitivity and estimated effectiveness
- identified amplifier archetypes — bots, partisan influencers, media laundering pathways — likely to accelerate spread

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- false claims spread faster than true ones because they carry higher novelty and emotional charge — weight these factors heavily
- ambiguity is a virality accelerant: under-specified claims invite projection and partisan completion, broadening the audience
- moral-outrage content activates in-group/out-group dynamics that override normal credibility checking
- the first 2–6 hours after seeding are the highest-leverage counter-messaging window before sharing velocity compounds
- assess network fit separately from content quality: a claim may be weak but perfectly structured for the target network's sharing norms
- distinguish organic spread from coordinated amplification — the latter shows anomalously synchronized share timing and bot-signature accounts
