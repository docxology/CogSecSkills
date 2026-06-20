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

## Evidence requirements
- For Premortem Analysis, tie each failure modes claim to concrete evidence from the specific plan or assessment, and time horizon item, source excerpt, observation, or command result that supports it.
- For Premortem Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the failure modes.
- Before recommending any Premortem Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Premortem Analysis: the failure modes is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; frame the failure as fact and generate failure causes checks agree, and no unresolved contradiction would change the result.
- Medium for Premortem Analysis: the failure modes is plausible, but one important plan or assessment source, comparison case, or alternative explanation remains incomplete.
- Low for Premortem Analysis: the failure modes rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Premortem Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Premortem Analysis, use only authorized plan or assessment, and time horizon, public or source-approved records, and caller-provided context needed for the defensive task.
- For Premortem Analysis, minimize person-level detail in the failure modes; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Premortem Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Premortem Analysis: treating plan or assessment as complete when frame the failure as fact and generate failure causes checks or contradictory evidence are missing.
- Premortem Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Premortem Analysis: reporting the failure modes without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Premortem Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the failure modes from Premortem Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Premortem Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with plan or assessment, and time horizon' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not soften 'it has failed badly' into 'it might fail' or 'if it were to fail' — the subjunctive frame suppresses the dissent the technique is designed to surface
- do not rank causes by the seniority or popularity of whoever raised them
- do not accept a failure cause without an associated leading indicator — an unmonitorable cause is not actionable

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
