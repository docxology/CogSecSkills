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

- For Cognitive Attack Kill Chain, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Cognitive Attack Kill Chain, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Cognitive Attack Kill Chain recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Cognitive Attack Kill Chain: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Cognitive Attack Kill Chain: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Cognitive Attack Kill Chain: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Cognitive Attack Kill Chain cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Cognitive Attack Kill Chain should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Cognitive Attack Kill Chain, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Cognitive Attack Kill Chain, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Cognitive Attack Kill Chain, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cognitive Attack Kill Chain failure: mistaking persuasive resonance for verified harm or intent.
- Cognitive Attack Kill Chain failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Cognitive Attack Kill Chain failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Cognitive Attack Kill Chain to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cognitive Attack Kill Chain into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cognitive Attack Kill Chain to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- earlier kill-chain stages are always cheaper to disrupt — a campaign interdicted at reconnaissance or weaponization stage causes far less harm than one disrupted only after content has been delivered and exploited at scale
- distinguish stage completion from impact: an adversary may have completed delivery without achieving exploitation if the content failed to resonate — do not conflate a completed stage with a successful one
- be explicit about uncertainty: kill-chain stage assignments based on incomplete evidence should be marked as hypotheses, not facts, and collection gaps should be surfaced rather than papered over
