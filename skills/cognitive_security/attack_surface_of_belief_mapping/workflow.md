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

## Failure modes
- Belief Attack-Surface Mapping failure: mistaking persuasive resonance for verified harm or intent.
- Belief Attack-Surface Mapping failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Belief Attack-Surface Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Belief Attack-Surface Mapping to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Belief Attack-Surface Mapping into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Belief Attack-Surface Mapping to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not treat this map as a targeting document — it is a defensive tool and must not be used to design manipulation campaigns
- do not rank beliefs by political valence or policy preference — vulnerability is an epistemic property, not a content judgment
- do not reduce all vulnerability to a single score without documenting the component dimension scores — defenders need the breakdown to choose the right intervention type
- do not assume high emotional salience alone equals high vulnerability — emotional investment can also motivate verification behavior

## AGEINT upstream
`docs/ageint/cognitive-security.md`
