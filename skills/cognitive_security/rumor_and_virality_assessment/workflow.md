# Workflow — Rumor & Virality Assessment

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and normalize the claim (read)
Read the full claim text, originating platform context, timestamp, and any early engagement metrics. Note the exact wording, format (headline, meme, video caption), and any embedded visual or audio cues that amplify emotional impact independent of the text.

## Step 2 — Establish baseline and precedent (search)
Search for prior occurrences of the same or similar claims — earlier seedings, dormant versions, analogous rumors in other contexts — and retrieve any known spread data. Cross-reference against rumor databases, fact-check archives, and platform transparency reports to calibrate against empirical spread rates for comparable claims.

## Step 3 — Score virality factors (reason)
Apply the seven-factor virality model: (1) Emotional valence and intensity — fear, anger, disgust, and awe drive sharing more than sadness or joy; (2) Ambiguity — rate the claim's specificity gap, which allows projection; (3) Moral-outrage load — identify norm violations and in-group threat framing; (4) Novelty — how surprising or schema-violating is the claim; (5) Narrative fit — how well it slots into pre-existing conspiracy frameworks or culturally activated threat models; (6) Network amplification potential — presence of hashtags, @ mentions, and formatting optimized for resharing; (7) Audience resonance — estimated alignment between the claim's framing and the target audience's prior beliefs and emotional priming. Rate each factor Low/Moderate/High with a one-sentence rationale.

## Step 4 — Assess spread trajectory and amplifier pathways (reason)
Combine the factor scores into a composite virality rating and estimate the spread trajectory: time-to-peak engagement, likely reach tier (local / regional / national / global), and decay rate. Identify the amplifier archetypes most likely to accelerate spread — coordinated inauthentic accounts, partisan influencer networks, mainstream media laundering, cross-platform migration pathways. Flag signals of coordinated amplification (synchronized posting, bot-signature accounts, artificial trending).

## Step 5 — Determine counter-messaging windows and produce report (reason, write)
Identify the intervention windows where counter-messaging or prebunking is most leveraged — typically before or immediately after initial seeding, before the claim achieves mainstream platform traction, and before it is cited as a source by secondary outlets. Write the structured virality assessment report including the composite score, factor table, trajectory estimate, amplifier map, and prioritized intervention recommendations. Include confidence intervals and explicit caveats for factors assessed with limited data.

## Evidence requirements
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

## Failure modes
- Rumor & Virality Assessment: declaring spread assessed when the precedent-and-baseline search was skipped, low early engagement was read as low potential for a dormant claim, or coordinated amplification signals were left unexamined, so the score reflects an incomplete read rather than a calibrated forecast.
- Rumor & Virality Assessment: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Rumor & Virality Assessment: reporting the virality assessment without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Rumor & Virality Assessment outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the virality assessment from Rumor & Virality Assessment into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Rumor & Virality Assessment to assess supplied material for manipulation indicators and recommend resilience measures with claim, originating context, and audience profile' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate virality potential with truth value — false claims often have higher virality scores than accurate ones
- do not treat a low initial engagement count as evidence of low virality potential — dormant or slow-seeding claims can achieve rapid spread once a triggering event occurs
- do not recommend suppression as a default counter-measure — heavy-handed removal frequently triggers Streisand-effect amplification
- do not omit the confidence level and data limitations from the assessment — overconfident virality predictions mislead response planning
- do not assess the claim's wording alone without accounting for the embedding context (platform norms, timing, audience priming)

## AGEINT upstream
`docs/ageint/cognitive-security.md`
