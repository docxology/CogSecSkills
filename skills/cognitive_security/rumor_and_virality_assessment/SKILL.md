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

- For Rumor & Virality Assessment, bind the composite score, each virality-factor rating, the trajectory estimate, and every amplifier-pathway claim to concrete evidence — the claim text, the originating context, engagement metrics, or comparable precedent — and mark any factor scored without such evidence as a low-confidence estimate with explicit caveats.
- For Rumor & Virality Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the virality assessment.
- Before recommending any Rumor & Virality Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Rumor & Virality Assessment: the composite virality score and its per-factor ratings are each tied to the claim's wording, embedding context, and any propagation data, the score is corroborated by precedent spread rates for comparable claims, and no unresolved contradiction in the amplifier analysis would change the prioritised counter-messaging windows.
- Medium for Rumor & Virality Assessment: the virality assessment is plausible, but one important claim source, comparison case, or alternative explanation remains incomplete.
- Low for Rumor & Virality Assessment: the virality assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Rumor & Virality Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Rumor & Virality Assessment, use only authorized claim, originating context, and audience profile, public or source-approved records, and caller-provided context needed for the defensive task.
- For Rumor & Virality Assessment, minimize person-level detail in the virality assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Rumor & Virality Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Rumor & Virality Assessment: declaring spread assessed when the precedent-and-baseline search was skipped, low early engagement was read as low potential for a dormant claim, or coordinated amplification signals were left unexamined, so the score reflects an incomplete read rather than a calibrated forecast.
- Rumor & Virality Assessment: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Rumor & Virality Assessment: reporting the virality assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Rumor & Virality Assessment outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the virality assessment from Rumor & Virality Assessment into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Rumor & Virality Assessment to assess supplied material for manipulation indicators and recommend resilience measures with claim, originating context, and audience profile' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- false claims spread faster than true ones because they carry higher novelty and emotional charge — weight these factors heavily
- ambiguity is a virality accelerant: under-specified claims invite projection and partisan completion, broadening the audience
- moral-outrage content activates in-group/out-group dynamics that override normal credibility checking
- the first 2–6 hours after seeding are the highest-leverage counter-messaging window before sharing velocity compounds
- assess network fit separately from content quality: a claim may be weak but perfectly structured for the target network's sharing norms
- distinguish organic spread from coordinated amplification — the latter shows anomalously synchronized share timing and bot-signature accounts
