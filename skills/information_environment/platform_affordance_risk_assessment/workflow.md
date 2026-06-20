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

## Evidence requirements
- For Platform Affordance Risk Assessment, tie each affordance risk matrix, and risk narrative claim to concrete evidence from the specific platform name, threat actor profile, and prior incident reports item, source excerpt, observation, or command result that supports it.
- For Platform Affordance Risk Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the affordance risk matrix.
- Before recommending any Platform Affordance Risk Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Platform Affordance Risk Assessment: the affordance risk matrix is supported by multiple independent platform observations, narrative movement, automation signals, and provenance data; inventory platform features and map features to manipulation vectors checks agree, and no unresolved contradiction would change the result.
- Medium for Platform Affordance Risk Assessment: the affordance risk matrix is plausible, but one important platform name source, comparison case, or alternative explanation remains incomplete.
- Low for Platform Affordance Risk Assessment: the affordance risk matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Platform Affordance Risk Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating information_environment evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Platform Affordance Risk Assessment, use only authorized platform name, threat actor profile, and prior incident reports, public or source-approved records, and caller-provided context needed for the defensive task.
- For Platform Affordance Risk Assessment, minimize person-level detail in the affordance risk matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Platform Affordance Risk Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Platform Affordance Risk Assessment: treating platform name as complete when inventory platform features and map features to manipulation vectors checks or contradictory evidence are missing.
- Platform Affordance Risk Assessment: producing advice that would help a requester amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement.
- Platform Affordance Risk Assessment: reporting the affordance risk matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Platform Affordance Risk Assessment outputs to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the affordance risk matrix from Platform Affordance Risk Assessment into an operational playbook to amplify coordinated behavior, tune platform manipulation, or design inauthentic engagement' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Platform Affordance Risk Assessment to map supplied narratives, automation signals, or platform affordance risks for defensive review with platform name, threat actor profile, and prior incident reports' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate a platform being used for manipulation with the platform being uniquely or irredeemably risky — assess the specific architectural features, not general reputation
- do not omit mitigating affordances — features that constrain manipulation (identity verification, rate limits, reporting systems) belong in the assessment to give a balanced picture
- do not assign High severity without at least one real-world documented precedent or a clearly articulated exploitation pathway — severity inflation undermines prioritization
- do not treat policy text at face value — assess whether enforcement mechanisms actually constrain the manipulation vector in practice

## AGEINT upstream
`docs/ageint/information-environment.md`
