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
- For Chronologies & Timelines, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Chronologies & Timelines, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Chronologies & Timelines recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Chronologies & Timelines: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Chronologies & Timelines: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Chronologies & Timelines: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Chronologies & Timelines cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Chronologies & Timelines should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Chronologies & Timelines, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Chronologies & Timelines, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Chronologies & Timelines, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Chronologies & Timelines failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Chronologies & Timelines failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Chronologies & Timelines failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Chronologies & Timelines to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Chronologies & Timelines into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Chronologies & Timelines to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not merge inferred dates with sourced dates in the same table column — keep a confidence or date-type field
- do not treat absence of events in the record as evidence of absence of activity without explicitly noting the collection limitations
- do not allow the narrative framing of the focal question to dictate which events are included — include all sourced events and let the pattern speak

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
