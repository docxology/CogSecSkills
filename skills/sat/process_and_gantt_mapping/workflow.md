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

## Evidence requirements
- For Process & Gantt Mapping, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Process & Gantt Mapping, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Process & Gantt Mapping recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Process & Gantt Mapping: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Process & Gantt Mapping: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Process & Gantt Mapping: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Process & Gantt Mapping cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Process & Gantt Mapping should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Process & Gantt Mapping, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Process & Gantt Mapping, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Process & Gantt Mapping, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Process & Gantt Mapping failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Process & Gantt Mapping failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Process & Gantt Mapping failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Process & Gantt Mapping to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Process & Gantt Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Process & Gantt Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not map only confirmed steps — the map must represent what the activity requires by logic; confirmed steps fill in the map, gaps are collection requirements
- do not treat all steps as equally significant — the critical path and choke points must be explicitly identified
- do not produce a step without an associated observable indicator; an unobservable step is a collection gap that must be labeled as such, not silently omitted

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
