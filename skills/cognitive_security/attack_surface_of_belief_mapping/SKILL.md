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

## Defensive boundary

Use Belief Attack-Surface Mapping only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Belief Attack-Surface Mapping to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Belief Attack-Surface Mapping, tie each belief attack surface map, and priority interventions claim to concrete evidence from the specific audience profile, belief inventory, and adversary playbook item, source excerpt, observation, or command result that supports it.
- For Belief Attack-Surface Mapping, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the belief attack surface map.
- Before recommending any Belief Attack-Surface Mapping action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Belief Attack-Surface Mapping: the belief attack surface map is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; ingest audience and belief landscape and score each belief on vulnerability dimensions checks agree, and no unresolved contradiction would change the result.
- Medium for Belief Attack-Surface Mapping: the belief attack surface map is plausible, but one important audience profile source, comparison case, or alternative explanation remains incomplete.
- Low for Belief Attack-Surface Mapping: the belief attack surface map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Belief Attack-Surface Mapping cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Belief Attack-Surface Mapping, use only authorized audience profile, belief inventory, and adversary playbook, public or source-approved records, and caller-provided context needed for the defensive task.
- For Belief Attack-Surface Mapping, minimize person-level detail in the belief attack surface map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Belief Attack-Surface Mapping, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Belief Attack-Surface Mapping: treating audience profile as complete when ingest audience and belief landscape and score each belief on vulnerability dimensions checks or contradictory evidence are missing.
- Belief Attack-Surface Mapping: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Belief Attack-Surface Mapping: reporting the belief attack surface map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Belief Attack-Surface Mapping outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the belief attack surface map from Belief Attack-Surface Mapping into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Belief Attack-Surface Mapping to assess supplied material for manipulation indicators and recommend resilience measures with audience profile, belief inventory, and adversary playbook' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess beliefs across multiple independent vulnerability dimensions — a belief that scores high on only one dimension is far less exposed than one that scores high on all four
- distinguish beliefs that are epistemically thin (poorly evidenced) from those that are identity-anchored (correcting them triggers backfire) — the defensive intervention is different for each type
- focus on exposure, not just prevalence — a widely-held but well-evidenced belief is less dangerous to hold than a narrowly-held but epistemically fragile one that gatekeeps key decisions
