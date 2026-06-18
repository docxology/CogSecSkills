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

## Anti-criteria (must NOT happen)
- do not conflate virality potential with truth value — false claims often have higher virality scores than accurate ones
- do not treat a low initial engagement count as evidence of low virality potential — dormant or slow-seeding claims can achieve rapid spread once a triggering event occurs
- do not recommend suppression as a default counter-measure — heavy-handed removal frequently triggers Streisand-effect amplification
- do not omit the confidence level and data limitations from the assessment — overconfident virality predictions mislead response planning
- do not assess the claim's wording alone without accounting for the embedding context (platform norms, timing, audience priming)

## AGEINT upstream
`docs/ageint/cognitive-security.md`
