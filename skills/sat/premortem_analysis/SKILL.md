---
name: sat.premortem_analysis
description: Assume the conclusion failed; work backward to find what would have caused it.
---

# Premortem Analysis

Premortem analysis (Klein) imagines the plan has already failed, then works backward to surface causes — converting hindsight into foresight and licensing dissent a prospective review suppresses. Participants adopt the cognitive stance that failure has occurred and are asked why, bypassing the social pressure to defend a committed plan. In cognitive-security contexts it is used both to stress-test analytic conclusions before they reach decision-makers and to surface assumptions that groupthink or authority bias has suppressed.

## When to use

- a plan or analytic conclusion is near commitment and overconfidence, groupthink, or authority bias is likely
- a prior review produced only mild critique that felt socially constrained
- a high-stakes assessment needs a documented dissent process before it reaches a decision-maker
- a team has been working on an issue long enough that loss-aversion and sunk-cost framing may suppress honest critique

## What it produces

- a ranked list of failure causes, each with a plausibility x impact estimate, a leading indicator, and a mitigation
- a set of assumption breaks that would be most dangerous if they occurred
- a documented dissent record that can be revisited if the prediction later fails

## Defensive boundary

Use Premortem Analysis only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Premortem Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Premortem Analysis, bind each failure cause, plausibility-by-impact score, and proposed mitigation to concrete evidence from the plan or assessment under review and to the assumption it would break, and pair every retained cause with an observable leading indicator, treating any cause that lacks a detectable signal as un-actionable rather than confirmed.
- For Premortem Analysis, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the failure modes.
- Before recommending any Premortem Analysis action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Premortem Analysis: each top-ranked failure cause carries a plausibility-by-impact score grounded in the plan's actual dependencies, every retained cause has a defined leading indicator and mitigation, the most dangerous assumption breaks are separately surfaced, and no unresolved contradiction in the failure logic would change which causes warrant a plan revision.
- Medium for Premortem Analysis: the failure modes is plausible, but one important plan or assessment source, comparison case, or alternative explanation remains incomplete.
- Low for Premortem Analysis: the failure modes rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Premortem Analysis cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Premortem Analysis, use only authorized plan or assessment, and time horizon, public or source-approved records, and caller-provided context needed for the defensive task.
- For Premortem Analysis, minimize person-level detail in the failure modes; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Premortem Analysis, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Premortem Analysis: declaring the plan stress-tested while softening the assumed-failure frame into a tentative "it might fail," ranking causes by the seniority of whoever raised them, or accepting failure modes with no leading indicator, so the exercise produces comfortable consensus instead of the actionable, monitorable dissent record it is designed to generate.
- Premortem Analysis: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Premortem Analysis: reporting the failure modes without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Premortem Analysis outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the failure modes from Premortem Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Premortem Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with plan or assessment, and time horizon' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- declare failure as a fact, not a possibility — the phrase 'it has failed badly' licenses candor that 'it might fail' suppresses
- rank causes by plausibility x impact, not by who raised them or how uncomfortable they are to hear
- every failure mode must have a leading indicator — a premortem without indicators is not actionable
