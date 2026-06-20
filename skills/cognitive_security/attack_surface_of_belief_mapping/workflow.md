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

## Evidence requirements
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

## Failure modes
- Belief Attack-Surface Mapping: treating audience profile as complete when ingest audience and belief landscape and score each belief on vulnerability dimensions checks or contradictory evidence are missing.
- Belief Attack-Surface Mapping: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Belief Attack-Surface Mapping: reporting the belief attack surface map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Belief Attack-Surface Mapping outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the belief attack surface map from Belief Attack-Surface Mapping into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Belief Attack-Surface Mapping to assess supplied material for manipulation indicators and recommend resilience measures with audience profile, belief inventory, and adversary playbook' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat this map as a targeting document — it is a defensive tool and must not be used to design manipulation campaigns
- do not rank beliefs by political valence or policy preference — vulnerability is an epistemic property, not a content judgment
- do not reduce all vulnerability to a single score without documenting the component dimension scores — defenders need the breakdown to choose the right intervention type
- do not assume high emotional salience alone equals high vulnerability — emotional investment can also motivate verification behavior

## AGEINT upstream
`docs/ageint/cognitive-security.md`
