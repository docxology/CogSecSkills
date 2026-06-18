# Workflow — Premortem Analysis

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Frame the failure as fact (read)
Read the plan or assessment. State it clearly. Then declare: 'It is now N months later and this has failed badly.' Treat this as established fact for the remainder of the exercise. Do not hedge.

## Step 2 — Generate failure causes (reason)
From the assumed-failure standpoint, brainstorm every plausible reason the failure occurred. Include assumption breaks, external shocks, execution failures, adversary adaptation, and cognitive biases that distorted the original assessment. Quantity matters at this stage — do not filter.

## Step 3 — Score, rank, and mitigate (reason, write)
Score each cause on plausibility and impact (1–5 each; multiply for a priority score). Rank the list. For the top causes, write a leading indicator — an observable signal that would appear early if this cause were active — and a mitigation or contingency. Discard causes that score below threshold.

## Step 4 — Document and integrate (write)
Produce the final failure-modes document. Flag any causes that require a plan revision versus a monitoring posture. Note which assumptions, if broken, would most change the assessment. Archive as a dissent record.

## Anti-criteria (must NOT happen)
- do not soften 'it has failed badly' into 'it might fail' or 'if it were to fail' — the subjunctive frame suppresses the dissent the technique is designed to surface
- do not rank causes by the seniority or popularity of whoever raised them
- do not accept a failure cause without an associated leading indicator — an unmonitorable cause is not actionable

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
