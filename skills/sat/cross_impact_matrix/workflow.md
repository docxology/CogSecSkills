# Workflow — Cross-Impact Matrix

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Establish the driver set (read)
Read the input driver list and any background analysis. Confirm that the set is exhaustive for the focal question and not so large (>12) that the matrix becomes unworkable. Assign a short label to each driver.

## Step 2 — Fill the matrix cell by cell (reason)
For each ordered pair (driver i, driver j), assess: if driver i increases, what happens to driver j? Record the direction and magnitude using the agreed scale. Work row by row, treating each cell independently. Note conditional relationships explicitly (C) rather than forcing a sign.

## Step 3 — Identify feedback loops (reason)
Trace chains where the influence circles back to the originating driver. Flag reinforcing loops (all positive, or an even number of negatives) and balancing loops (odd number of negatives). Record each loop as an ordered list of drivers.

## Step 4 — Compute leverage rankings (reason, write)
Sum each driver's outgoing scores (active influence) and incoming scores (passive sensitivity). Rank drivers. Identify the top active drivers — interventions here cascade widely. Identify the top passive indicators — monitoring these reveals system state fastest.

## Step 5 — Synthesize findings (write)
Write the analytic narrative: which loops dominate under the focal scenario? Which leverage points should a decision-maker prioritize? What surprises does the matrix reveal relative to the initial intuition about the system?

## Evidence requirements
- For Cross-Impact Matrix, tie each cross impact matrix, loop inventory, and leverage ranking claim to concrete evidence from the specific driver list, influence scale, and focal question item, source excerpt, observation, or command result that supports it.
- For Cross-Impact Matrix, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the cross impact matrix.
- Before recommending any Cross-Impact Matrix action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Cross-Impact Matrix: the cross impact matrix is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; establish the driver set and fill the matrix cell by cell checks agree, and no unresolved contradiction would change the result.
- Medium for Cross-Impact Matrix: the cross impact matrix is plausible, but one important driver list source, comparison case, or alternative explanation remains incomplete.
- Low for Cross-Impact Matrix: the cross impact matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Cross-Impact Matrix cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Cross-Impact Matrix, use only authorized driver list, influence scale, and focal question, public or source-approved records, and caller-provided context needed for the defensive task.
- For Cross-Impact Matrix, minimize person-level detail in the cross impact matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Cross-Impact Matrix, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Cross-Impact Matrix: treating driver list as complete when establish the driver set and fill the matrix cell by cell checks or contradictory evidence are missing.
- Cross-Impact Matrix: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Cross-Impact Matrix: reporting the cross impact matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Cross-Impact Matrix outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the cross impact matrix from Cross-Impact Matrix into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cross-Impact Matrix to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with driver list, influence scale, and focal question' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate the influence of i on j with the influence of j on i — they are separate cells and need not be symmetric
- do not skip cells by assuming relationships are negligible without assessment — a zero score is a finding, not a default
- do not use the matrix to predict outcomes directly — it maps structure, not trajectories; scenario development is the next step

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
