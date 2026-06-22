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
- For Elicitation Attempt Recognition, tie each identified technique and the composite risk rating to concrete evidence quoted from the conversation transcript or behavioral description, noting whether the partner re-probed after deflection, and treat an unsupported intent claim as speculation rather than evidence of elicitation.
- For Elicitation Attempt Recognition, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the elicitation recognition report.
- Before recommending any Elicitation Attempt Recognition action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Elicitation Attempt Recognition: multiple named techniques from the taxonomy cluster around the same sensitive topic, the interaction demonstrably re-probed after deflection, the composite risk rating follows from that pattern, and no unresolved contradiction would change the recommended defensive response.
- Medium for Elicitation Attempt Recognition: the elicitation recognition report is plausible, but one important conversation or description source, comparison case, or alternative explanation remains incomplete.
- Low for Elicitation Attempt Recognition: the elicitation recognition report rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Elicitation Attempt Recognition cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating counterintelligence evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Elicitation Attempt Recognition, use only authorized conversation or description, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Elicitation Attempt Recognition, minimize person-level detail in the elicitation recognition report; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Elicitation Attempt Recognition, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Elicitation Attempt Recognition: declaring an interaction hostile elicitation on a single isolated technique hit without the re-probing pattern that distinguishes it from genuine curiosity, or conversely dismissing a clustered pattern, so the risk rating reflects an incomplete behavioral log rather than the actual conversation.
- Elicitation Attempt Recognition: producing advice that would help a requester evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft.
- Elicitation Attempt Recognition: reporting the elicitation recognition report without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Elicitation Attempt Recognition outputs to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the elicitation recognition report from Elicitation Attempt Recognition into an operational playbook to evade detection, improve elicitation, profile targets for exploitation, or conceal tradecraft' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Elicitation Attempt Recognition to review supplied interactions or processes for deception, elicitation, or insider-risk indicators with conversation or description, and context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not attribute malicious intent solely on a single technique hit — a pattern of multiple techniques re-probing the same topic is required for high confidence
- Do not include guidance for running elicitation operations offensively — this skill is strictly for recognition and defense
- Do not recommend confronting the suspected elicitor directly without security officer guidance
- Do not treat this analysis as legally conclusive — it is a risk assessment to inform reporting, not a determination of guilt

## AGEINT upstream
`docs/ageint/counterintelligence.md`
