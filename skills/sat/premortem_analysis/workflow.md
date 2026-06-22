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
- For Premortem Analysis, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Premortem Analysis, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Premortem Analysis recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Premortem Analysis: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Premortem Analysis: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Premortem Analysis: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Premortem Analysis cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Premortem Analysis should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Premortem Analysis, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Premortem Analysis, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Premortem Analysis, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Premortem Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Premortem Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Premortem Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Premortem Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Premortem Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Premortem Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not soften 'it has failed badly' into 'it might fail' or 'if it were to fail' — the subjunctive frame suppresses the dissent the technique is designed to surface
- do not rank causes by the seniority or popularity of whoever raised them
- do not accept a failure cause without an associated leading indicator — an unmonitorable cause is not actionable

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
