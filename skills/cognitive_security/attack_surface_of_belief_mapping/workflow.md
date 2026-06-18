# Workflow — Belief Attack-Surface Mapping

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest audience and belief landscape (read)
Review the audience profile and belief inventory. Note the information environment they inhabit (which sources they trust, which social networks they use), their prior commitments, and any existing adversary narratives already in circulation.

## Step 2 — Score each belief on vulnerability dimensions (reason)
For each belief cluster, score it on four dimensions: (1) Evidence thinness — how well-supported is the belief by verifiable, widely-accessible evidence? (2) Emotional salience — how much is the belief bound up with fear, moral outrage, or in-group loyalty? (3) Identity anchoring — how closely tied is holding this belief to the audience's self-concept or group membership? (4) Social proof dependence — does the audience's confidence in the belief rest primarily on perceived consensus rather than direct evidence? Record scores and rationale for each.

## Step 3 — Map manipulation vectors to vulnerable beliefs (reason)
For beliefs with high exposure scores, identify the specific adversary manipulation vectors they are susceptible to: e.g., a belief that is both emotionally salient and evidence-thin is vulnerable to emotionally-charged disinformation; an identity-anchored belief is vulnerable to in-group messenger exploitation and tribal norm signaling. Cross-reference against the adversary playbook if available.

## Step 4 — Produce ranked map and defensive priorities (write)
Compile the belief attack-surface table ranked by composite vulnerability score. For each high-exposure belief, specify: the dominant manipulation vectors, the estimated impact if exploited, and the recommended defensive action (prebunking campaign, source-diversification initiative, norm-based reframing, or alliance with trusted in-group messengers). Flag any beliefs where intervention may itself carry backfire risk.

## Anti-criteria (must NOT happen)
- do not treat this map as a targeting document — it is a defensive tool and must not be used to design manipulation campaigns
- do not rank beliefs by political valence or policy preference — vulnerability is an epistemic property, not a content judgment
- do not reduce all vulnerability to a single score without documenting the component dimension scores — defenders need the breakdown to choose the right intervention type
- do not assume high emotional salience alone equals high vulnerability — emotional investment can also motivate verification behavior

## AGEINT upstream
`docs/ageint/cognitive-security.md`
