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

## Defensive boundary

Use Cognitive Attack Kill Chain only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Cognitive Attack Kill Chain to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Cognitive Attack Kill Chain, tie each kill chain map, defender action plan, and residual uncertainty log claim to concrete evidence from the specific campaign evidence, target context, and prior threat intel item, source excerpt, observation, or command result that supports it.
- For Cognitive Attack Kill Chain, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the kill chain map.
- Before recommending any Cognitive Attack Kill Chain action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Cognitive Attack Kill Chain: the kill chain map is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; collect and organize campaign evidence and map evidence to kill-chain stages checks agree, and no unresolved contradiction would change the result.
- Medium for Cognitive Attack Kill Chain: the kill chain map is plausible, but one important campaign evidence source, comparison case, or alternative explanation remains incomplete.
- Low for Cognitive Attack Kill Chain: the kill chain map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Cognitive Attack Kill Chain cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Cognitive Attack Kill Chain, use only authorized campaign evidence, target context, and prior threat intel, public or source-approved records, and caller-provided context needed for the defensive task.
- For Cognitive Attack Kill Chain, minimize person-level detail in the kill chain map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Cognitive Attack Kill Chain, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cognitive Attack Kill Chain: treating campaign evidence as complete when collect and organize campaign evidence and map evidence to kill-chain stages checks or contradictory evidence are missing.
- Cognitive Attack Kill Chain: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Attack Kill Chain: reporting the kill chain map without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Cognitive Attack Kill Chain outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the kill chain map from Cognitive Attack Kill Chain into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cognitive Attack Kill Chain to assess supplied material for manipulation indicators and recommend resilience measures with campaign evidence, target context, and prior threat intel' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- earlier kill-chain stages are always cheaper to disrupt — a campaign interdicted at reconnaissance or weaponization stage causes far less harm than one disrupted only after content has been delivered and exploited at scale
- distinguish stage completion from impact: an adversary may have completed delivery without achieving exploitation if the content failed to resonate — do not conflate a completed stage with a successful one
- be explicit about uncertainty: kill-chain stage assignments based on incomplete evidence should be marked as hypotheses, not facts, and collection gaps should be surfaced rather than papered over
