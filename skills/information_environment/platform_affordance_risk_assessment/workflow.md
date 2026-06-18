# Workflow — Platform Affordance Risk Assessment

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory platform features (read, search)
Enumerate the platform's significant technical and policy features: identity requirements (anonymity/pseudonymity/real-name), content amplification mechanics (shares, retweets, algorithmic recommendation), group and channel structures, advertising and targeting systems, content moderation tools, API access, and cross-platform bridging capabilities. Retrieve platform documentation, prior academic research, and investigative incident reports.

## Step 2 — Map features to manipulation vectors (reason)
For each feature, identify the manipulation vector it enables or amplifies. Common vectors: artificial amplification (virality + bot accounts), astroturfing (pseudonymity + coordinated posting), micro-targeted persuasion (ad targeting APIs), closed-group radicalization (private channels + recommendation), cross-platform laundering (open API + third-party sharing). Note bidirectionality — the same feature may also constrain certain manipulation types.

## Step 3 — Assess severity and interaction effects (reason)
Rate each feature-vector pair by severity (High/Medium/Low) based on: exploitation ease, detection difficulty, scale potential, and real-world precedent. Explicitly identify cross-feature interaction effects where two or more features combine to produce elevated risk not visible from either alone (e.g., algorithmic recommendation + group structures + pseudonymity = radicalization pipeline).

## Step 4 — Prioritize and recommend mitigations (reason, write)
Rank affordance risks by combined severity and exploitation likelihood given the defined threat actor profile. For each high-severity item, identify whether the mitigation lever is design (change the feature), policy (enforce existing rules), detection (build monitoring), or education (inform users). Produce the risk matrix and narrative findings.

## Anti-criteria (must NOT happen)
- do not conflate a platform being used for manipulation with the platform being uniquely or irredeemably risky — assess the specific architectural features, not general reputation
- do not omit mitigating affordances — features that constrain manipulation (identity verification, rate limits, reporting systems) belong in the assessment to give a balanced picture
- do not assign High severity without at least one real-world documented precedent or a clearly articulated exploitation pathway — severity inflation undermines prioritization
- do not treat policy text at face value — assess whether enforcement mechanisms actually constrain the manipulation vector in practice

## AGEINT upstream
`docs/ageint/information-environment.md`
