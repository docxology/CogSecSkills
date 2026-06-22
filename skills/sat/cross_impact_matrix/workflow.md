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
- For Cross-Impact Matrix, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Cross-Impact Matrix, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Cross-Impact Matrix recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Cross-Impact Matrix: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Cross-Impact Matrix: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Cross-Impact Matrix: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Cross-Impact Matrix cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Cross-Impact Matrix should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Cross-Impact Matrix, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Cross-Impact Matrix, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Cross-Impact Matrix, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Cross-Impact Matrix failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Cross-Impact Matrix failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Cross-Impact Matrix failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Cross-Impact Matrix to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cross-Impact Matrix into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cross-Impact Matrix to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate the influence of i on j with the influence of j on i — they are separate cells and need not be symmetric
- do not skip cells by assuming relationships are negligible without assessment — a zero score is a finding, not a default
- do not use the matrix to predict outcomes directly — it maps structure, not trajectories; scenario development is the next step

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
