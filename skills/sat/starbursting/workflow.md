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
- For Starbursting, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Starbursting, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Starbursting recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Starbursting: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Starbursting: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Starbursting: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Starbursting cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Starbursting should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Starbursting, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Starbursting, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Starbursting, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Starbursting failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Starbursting failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Starbursting failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Starbursting to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Starbursting into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Starbursting to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not answer questions during the generation phase — answering during generation anchors and prunes the question space
- do not treat a sparse interrogative category (e.g., only one 'Why' question) as complete — push for multiple questions per category
- do not discard awkward or uncomfortable questions; the most uncomfortable are often the most analytically important

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
