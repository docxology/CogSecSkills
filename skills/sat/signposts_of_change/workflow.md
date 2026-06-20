# Workflow — Signposts of Change

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Map scenarios to divergence points (read, reason)
Read the alternative scenarios or hypotheses. Identify the key decision nodes, behavioral commitments, or structural changes at which the trajectories diverge. These divergence points are the natural parents of signposts. For each divergence point, ask: what observable event, behavior, or signal would occur before this point if Scenario A is unfolding versus Scenario B? Document the divergence map.

## Step 2 — Derive and filter signposts (reason)
From each divergence point, derive one to three candidate signposts. For each candidate, check: (a) Is it observable from an identified collection source? (b) Is it discriminating — does it change probabilities differently across at least two scenarios? (c) Is it a leading indicator, not a confirming indicator that arrives only after the trajectory is already clear? Remove non-discriminating and non-observable candidates. Assign each signpost to a collection source and a check frequency.

## Step 3 — Build the matrix, set thresholds, and emit (reason, write, search)
Construct the signpost matrix: signposts as rows, scenarios as columns, with Confirm / Neutral / Disconfirm in each cell. Set explicit observation thresholds (e.g., 'two independent reporting references within 30 days constitutes confirmation'). Write the update protocol: how scenario probabilities shift when a signpost fires or when an expected signpost is absent. If active monitoring mode is requested, search available sources for current signpost status and emit an initial scenario-probability update.

## Evidence requirements
- For Signposts of Change, tie each signpost matrix, collection guidance, and update protocol claim to concrete evidence from the specific scenarios or hypotheses, current assessment, and collection resources item, source excerpt, observation, or command result that supports it.
- For Signposts of Change, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the signpost matrix.
- Before recommending any Signposts of Change action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Signposts of Change: the signpost matrix is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; map scenarios to divergence points and derive and filter signposts checks agree, and no unresolved contradiction would change the result.
- Medium for Signposts of Change: the signpost matrix is plausible, but one important scenarios or hypotheses source, comparison case, or alternative explanation remains incomplete.
- Low for Signposts of Change: the signpost matrix rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Signposts of Change cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Signposts of Change, use only authorized scenarios or hypotheses, current assessment, and collection resources, public or source-approved records, and caller-provided context needed for the defensive task.
- For Signposts of Change, minimize person-level detail in the signpost matrix; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Signposts of Change, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Signposts of Change: treating scenarios or hypotheses as complete when map scenarios to divergence points and derive and filter signposts checks or contradictory evidence are missing.
- Signposts of Change: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Signposts of Change: reporting the signpost matrix without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Signposts of Change outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the signpost matrix from Signposts of Change into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Signposts of Change to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with scenarios or hypotheses, current assessment, and collection resources' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not include signposts that are consistent with all scenarios — they consume collection resources without diagnostic value
- do not set observation thresholds after collection results are known — this retroactively protects the preferred scenario
- do not treat absence of a signpost as uninformative — if a signpost was expected and did not appear, the update protocol must apply
- do not let the signpost list grow so large that it is not operationally monitorable; prioritize the most discriminating and most observable indicators

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
