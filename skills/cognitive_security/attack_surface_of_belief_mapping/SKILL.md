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

- For Belief Attack-Surface Mapping, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Belief Attack-Surface Mapping, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Belief Attack-Surface Mapping recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Belief Attack-Surface Mapping: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Belief Attack-Surface Mapping: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Belief Attack-Surface Mapping: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Belief Attack-Surface Mapping cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Belief Attack-Surface Mapping should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Belief Attack-Surface Mapping, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Belief Attack-Surface Mapping, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Belief Attack-Surface Mapping, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Belief Attack-Surface Mapping failure: mistaking persuasive resonance for verified harm or intent.
- Belief Attack-Surface Mapping failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Belief Attack-Surface Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Belief Attack-Surface Mapping to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Belief Attack-Surface Mapping into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Belief Attack-Surface Mapping to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess beliefs across multiple independent vulnerability dimensions — a belief that scores high on only one dimension is far less exposed than one that scores high on all four
- distinguish beliefs that are epistemically thin (poorly evidenced) from those that are identity-anchored (correcting them triggers backfire) — the defensive intervention is different for each type
- focus on exposure, not just prevalence — a widely-held but well-evidenced belief is less dangerous to hold than a narrowly-held but epistemically fragile one that gatekeeps key decisions
