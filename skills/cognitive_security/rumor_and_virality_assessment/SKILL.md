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

## Defensive boundary

Use Rumor & Virality Assessment only for cognitive-security defense: recognize, assess, document, or defend audiences, decision-makers, and public discourse. Do not use this skill to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.

## Misuse redirect

If a request asks Rumor & Virality Assessment to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation, refuse that path and redirect to the safe defensive form: assess supplied material for manipulation indicators and recommend resilience measures.

## Evidence discipline

- For Rumor & Virality Assessment, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Rumor & Virality Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Rumor & Virality Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Rumor & Virality Assessment: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Rumor & Virality Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Rumor & Virality Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Rumor & Virality Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Rumor & Virality Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Rumor & Virality Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Rumor & Virality Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Rumor & Virality Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Rumor & Virality Assessment failure: mistaking persuasive resonance for verified harm or intent.
- Rumor & Virality Assessment failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Rumor & Virality Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Rumor & Virality Assessment to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Rumor & Virality Assessment into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Rumor & Virality Assessment to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- false claims spread faster than true ones because they carry higher novelty and emotional charge — weight these factors heavily
- ambiguity is a virality accelerant: under-specified claims invite projection and partisan completion, broadening the audience
- moral-outrage content activates in-group/out-group dynamics that override normal credibility checking
- the first 2–6 hours after seeding are the highest-leverage counter-messaging window before sharing velocity compounds
- assess network fit separately from content quality: a claim may be weak but perfectly structured for the target network's sharing norms
- distinguish organic spread from coordinated amplification — the latter shows anomalously synchronized share timing and bot-signature accounts
