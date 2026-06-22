# Workflow — Signposts of Change

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Map scenarios to divergence points (read, reason)
Read the alternative scenarios or hypotheses. Identify the key decision nodes, behavioral commitments, or structural changes at which the trajectories diverge. These divergence points are the natural parents of signposts. For each divergence point, ask: what observable event, behavior, or signal would occur before this point if Scenario A is unfolding versus Scenario B? Document the divergence map.

## Step 2 — Derive and filter signposts (reason)
From each divergence point, derive one to three candidate signposts. For each candidate, check: (a) Is it observable from an identified collection source? (b) Is it discriminating — does it change probabilities differently across at least two scenarios? (c) Is it a leading indicator, not a confirming indicator that arrives only after the trajectory is already clear? Remove non-discriminating and non-observable candidates. Assign each signpost to a collection source and a check frequency.

## Step 3 — Build the matrix, set thresholds, and emit (reason, write, search)
Construct the signpost matrix: signposts as rows, scenarios as columns, with Confirm / Neutral / Disconfirm in each cell. Set explicit observation thresholds (e.g., 'two independent reporting references within 30 days constitutes confirmation'). Write the update protocol: how scenario probabilities shift when a signpost fires or when an expected signpost is absent. If active monitoring mode is requested, search available sources for current signpost status and emit an initial scenario-probability update.

## Evidence requirements
- For Signposts of Change, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Signposts of Change, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Signposts of Change recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Signposts of Change: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Signposts of Change: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Signposts of Change: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Signposts of Change cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Signposts of Change should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Signposts of Change, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Signposts of Change, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Signposts of Change, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Signposts of Change failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Signposts of Change failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Signposts of Change failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Signposts of Change to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Signposts of Change into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Signposts of Change to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not include signposts that are consistent with all scenarios — they consume collection resources without diagnostic value
- do not set observation thresholds after collection results are known — this retroactively protects the preferred scenario
- do not treat absence of a signpost as uninformative — if a signpost was expected and did not appear, the update protocol must apply
- do not let the signpost list grow so large that it is not operationally monitorable; prioritize the most discriminating and most observable indicators

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
