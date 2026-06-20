# Workflow — Starbursting

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Frame the topic (read)
Read the topic statement or artifact. Define the boundaries: what is the subject being questioned, and what time frame, actor set, or information environment is in scope?

## Step 2 — Generate questions per interrogative (reason)
Working through each interrogative in turn—Who, What, When, Where, Why, How—generate at least three to five questions per category. Include questions about absences, counterfactuals, and adversary intent. Do not attempt to answer any question at this stage.

## Step 3 — Rate and prioritize (reason)
For each question, estimate its analytic priority: how much would the answer change the assessment? Classify as High / Medium / Low. Flag questions that are currently unanswerable (collection gap) versus those answerable from existing sources.

## Step 4 — Produce the question map and key unknowns summary (write)
Emit the full question table organized by interrogative with priority ratings. Write the key-unknowns summary highlighting the highest-priority unanswered questions and what analytic collection actions they imply.

## Evidence requirements
- For Starbursting, tie each question map, and key unknowns summary claim to concrete evidence from the specific topic or artifact, and context item, source excerpt, observation, or command result that supports it.
- For Starbursting, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the question map.
- Before recommending any Starbursting action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Starbursting: the question map is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; frame the topic and generate questions per interrogative checks agree, and no unresolved contradiction would change the result.
- Medium for Starbursting: the question map is plausible, but one important topic or artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Starbursting: the question map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Starbursting cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Starbursting, use only authorized topic or artifact, and context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Starbursting, minimize person-level detail in the question map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Starbursting, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Starbursting: treating topic or artifact as complete when frame the topic and generate questions per interrogative checks or contradictory evidence are missing.
- Starbursting: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Starbursting: reporting the question map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Starbursting outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the question map from Starbursting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Starbursting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with topic or artifact, and context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not answer questions during the generation phase — answering during generation anchors and prunes the question space
- do not treat a sparse interrogative category (e.g., only one 'Why' question) as complete — push for multiple questions per category
- do not discard awkward or uncomfortable questions; the most uncomfortable are often the most analytically important

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
