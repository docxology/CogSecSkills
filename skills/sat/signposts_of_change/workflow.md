# Workflow — Signposts of Change

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Map scenarios to divergence points (read, reason)
Read the alternative scenarios or hypotheses. Identify the key decision nodes, behavioral commitments, or structural changes at which the trajectories diverge. These divergence points are the natural parents of signposts. For each divergence point, ask: what observable event, behavior, or signal would occur before this point if Scenario A is unfolding versus Scenario B? Document the divergence map.

## Step 2 — Derive and filter signposts (reason)
From each divergence point, derive one to three candidate signposts. For each candidate, check: (a) Is it observable from an identified collection source? (b) Is it discriminating — does it change probabilities differently across at least two scenarios? (c) Is it a leading indicator, not a confirming indicator that arrives only after the trajectory is already clear? Remove non-discriminating and non-observable candidates. Assign each signpost to a collection source and a check frequency.

## Step 3 — Build the matrix, set thresholds, and emit (reason, write, search)
Construct the signpost matrix: signposts as rows, scenarios as columns, with Confirm / Neutral / Disconfirm in each cell. Set explicit observation thresholds (e.g., 'two independent reporting references within 30 days constitutes confirmation'). Write the update protocol: how scenario probabilities shift when a signpost fires or when an expected signpost is absent. If active monitoring mode is requested, search available sources for current signpost status and emit an initial scenario-probability update.

## Anti-criteria (must NOT happen)
- do not include signposts that are consistent with all scenarios — they consume collection resources without diagnostic value
- do not set observation thresholds after collection results are known — this retroactively protects the preferred scenario
- do not treat absence of a signpost as uninformative — if a signpost was expected and did not appear, the update protocol must apply
- do not let the signpost list grow so large that it is not operationally monitorable; prioritize the most discriminating and most observable indicators

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
