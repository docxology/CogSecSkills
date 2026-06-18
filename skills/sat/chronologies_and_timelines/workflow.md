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

## Anti-criteria (must NOT happen)
- do not merge inferred dates with sourced dates in the same table column — keep a confidence or date-type field
- do not treat absence of events in the record as evidence of absence of activity without explicitly noting the collection limitations
- do not allow the narrative framing of the focal question to dictate which events are included — include all sourced events and let the pattern speak

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
