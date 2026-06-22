# Workflow — Elicitation Attempt Recognition

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Catalog the interaction (read)
Read the conversation transcript or behavioral description in full. Note every question asked, statement volunteered, compliment offered, or redirect attempted, creating a chronological behavioral log.

## Step 2 — Apply elicitation taxonomy (reason)
Map each logged behavior to the canonical elicitation technique taxonomy: flattery/ego appeal, quid pro quo, volunteering false info to elicit correction, feigned ignorance, provocative statement, appeal to vanity/ideology, apparent disinterest, and topic bracketing. Score each technique hit; note whether the interaction re-probed after deflection (a strong positive indicator).

## Step 3 — Assess pattern and intent (reason)
Evaluate the cluster: single isolated techniques may be benign; multiple techniques targeting the same sensitive topic domain are high-confidence elicitation. Consider the elicitor's access, the sensitivity of the information sought, and any anomalies in the relationship or setting.

## Step 4 — Produce recognition report and response guidance (write)
Write a structured report naming which techniques appeared, the composite risk rating with rationale, the information domains targeted, and specific recommended defensive actions (limit future contact, report to security officer, provide only authorized information, document the interaction).

## Evidence requirements
- For Elicitation Attempt Recognition, bind each finding to a labeled source — interaction records, process artifacts, deception indicators, and alternative explanations, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Elicitation Attempt Recognition, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Elicitation Attempt Recognition recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Elicitation Attempt Recognition: independent lines of interaction records, process artifacts, deception indicators, and alternative explanations converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Elicitation Attempt Recognition: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Elicitation Attempt Recognition: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Elicitation Attempt Recognition cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Elicitation Attempt Recognition should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Elicitation Attempt Recognition, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Elicitation Attempt Recognition, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Elicitation Attempt Recognition, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Elicitation Attempt Recognition failure: turning defensive tradecraft recognition into operational evasion advice.
- Elicitation Attempt Recognition failure: producing guidance that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Elicitation Attempt Recognition failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Elicitation Attempt Recognition to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Elicitation Attempt Recognition into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Elicitation Attempt Recognition to review supplied interactions or processes for deception, elicitation, or insider-risk indicators' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not attribute malicious intent solely on a single technique hit — a pattern of multiple techniques re-probing the same topic is required for high confidence
- Do not include guidance for running elicitation operations offensively — this skill is strictly for recognition and defense
- Do not recommend confronting the suspected elicitor directly without security officer guidance
- Do not treat this analysis as legally conclusive — it is a risk assessment to inform reporting, not a determination of guilt

## AGEINT upstream
`docs/ageint/counterintelligence.md`
