# Workflow — Chronologies & Timelines

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract and date events (read)
Read all source documents and extract every datable event: assign a date/time, an actor, a one-sentence description, and a source citation. Flag events where the date is approximate or inferred rather than explicit.

## Step 2 — Sort, align, and segment streams (reason)
Sort events chronologically. If the focal question involves multiple actors or domains, arrange them in parallel lanes. Identify the boundaries of the period of interest and mark any sub-periods with distinct analytic significance.

## Step 3 — Identify gaps, clusters, and reversals (reason)
Scan the sorted order for: (a) unexplained silence — intervals where sourced events are absent but activity is expected; (b) suspicious clustering — multiple consequential events bunched within a narrow window; (c) reversed apparent causality — where the purported cause post-dates the purported effect.

## Step 4 — Assess analytic significance (reason, write)
For each gap or anomaly, assess: Is this absence of evidence or evidence of absence? What alternative explanations account for the pattern? Rate each anomaly by analytic significance and document the reasoning.

## Step 5 — Produce chronology table and findings (write)
Emit the final chronology table with confidence ratings, the gap-and-anomaly report, key findings tied to the focal question, and a list of collection requirements to address residual gaps.

## Evidence requirements
- For Chronologies & Timelines, tie each chronology, gap and anomaly report, and key findings claim to concrete evidence from the specific event sources, analytic question, and parallel streams item, source excerpt, observation, or command result that supports it.
- For Chronologies & Timelines, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the chronology.
- Before recommending any Chronologies & Timelines action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Chronologies & Timelines: the chronology is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; extract and date events and sort, align, and segment streams checks agree, and no unresolved contradiction would change the result.
- Medium for Chronologies & Timelines: the chronology is plausible, but one important event sources source, comparison case, or alternative explanation remains incomplete.
- Low for Chronologies & Timelines: the chronology rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Chronologies & Timelines cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Chronologies & Timelines, use only authorized event sources, analytic question, and parallel streams, public or source-approved records, and caller-provided context needed for the defensive task.
- For Chronologies & Timelines, minimize person-level detail in the chronology; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Chronologies & Timelines, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Chronologies & Timelines: treating event sources as complete when extract and date events and sort, align, and segment streams checks or contradictory evidence are missing.
- Chronologies & Timelines: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Chronologies & Timelines: reporting the chronology without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Chronologies & Timelines outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the chronology from Chronologies & Timelines into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Chronologies & Timelines to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with event sources, analytic question, and parallel streams' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not merge inferred dates with sourced dates in the same table column — keep a confidence or date-type field
- do not treat absence of events in the record as evidence of absence of activity without explicitly noting the collection limitations
- do not allow the narrative framing of the focal question to dictate which events are included — include all sourced events and let the pattern speak

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
