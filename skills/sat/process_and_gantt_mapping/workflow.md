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
- For Process & Gantt Mapping, tie each process map, and gantt table claim to concrete evidence from the specific activity description, known steps, and time constraints item, source excerpt, observation, or command result that supports it.
- For Process & Gantt Mapping, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the process map.
- Before recommending any Process & Gantt Mapping action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Process & Gantt Mapping: the process map is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; characterize and scope the activity and decompose into ordered steps checks agree, and no unresolved contradiction would change the result.
- Medium for Process & Gantt Mapping: the process map is plausible, but one important activity description source, comparison case, or alternative explanation remains incomplete.
- Low for Process & Gantt Mapping: the process map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Process & Gantt Mapping cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Process & Gantt Mapping, use only authorized activity description, known steps, and time constraints, public or source-approved records, and caller-provided context needed for the defensive task.
- For Process & Gantt Mapping, minimize person-level detail in the process map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Process & Gantt Mapping, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Process & Gantt Mapping: treating activity description as complete when characterize and scope the activity and decompose into ordered steps checks or contradictory evidence are missing.
- Process & Gantt Mapping: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Process & Gantt Mapping: reporting the process map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Process & Gantt Mapping outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the process map from Process & Gantt Mapping into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Process & Gantt Mapping to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with activity description, known steps, and time constraints' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not map only confirmed steps — the map must represent what the activity requires by logic; confirmed steps fill in the map, gaps are collection requirements
- do not treat all steps as equally significant — the critical path and choke points must be explicitly identified
- do not produce a step without an associated observable indicator; an unobservable step is a collection gap that must be labeled as such, not silently omitted

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
