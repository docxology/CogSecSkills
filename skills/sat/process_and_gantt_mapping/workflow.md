# Workflow — Process & Gantt Mapping

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize and scope the activity (read)
Read the source material. Define the start state and the end state of the process. Confirm what is known versus inferred. Establish the level of granularity appropriate for the analytic question — operational-level steps for tactical warning, campaign-level phases for strategic assessment.

## Step 2 — Decompose into ordered steps (reason, write)
List all steps the activity requires, in logical sequence. For each step, identify: (a) predecessor steps it depends on, (b) resources it requires, (c) approximate duration, (d) whether it is reversible or irreversible, and (e) confidence that this step is actually required. Note gaps where logic demands a step but no intelligence supports or denies it.

## Step 3 — Build the dependency graph and critical path (reason, write)
Arrange steps into a dependency graph. Identify the critical path — the longest chain of dependent steps determining the minimum time to completion. Flag choke points: irreversible, resource-intensive, or low-redundancy nodes. Flag steps with multiple parallel paths (resilient nodes where disruption is less effective).

## Step 4 — Assign indicators and confidence levels (reason, write)
For each step, assign at least one observable indicator — a signal that would be detectable if that step were underway or completed. Rate each indicator's diagnostic value (distinguishing this step from alternative activities) and the current collection posture against it. Identify collection gaps.

## Step 5 — Produce the Gantt table and summary (write)
Render the process map as a Gantt table (steps as rows, time buckets as columns, with critical-path and choke-point annotations). Summarize: estimated remaining lead time if activity is in progress, highest-confidence indicators to prioritize, and recommended collection actions for gaps.

## Anti-criteria (must NOT happen)
- do not map only confirmed steps — the map must represent what the activity requires by logic; confirmed steps fill in the map, gaps are collection requirements
- do not treat all steps as equally significant — the critical path and choke points must be explicitly identified
- do not produce a step without an associated observable indicator; an unobservable step is a collection gap that must be labeled as such, not silently omitted

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
