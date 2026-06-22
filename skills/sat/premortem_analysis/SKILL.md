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

## Failure modes and negative controls

- Premortem Analysis failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Premortem Analysis failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Premortem Analysis failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Premortem Analysis to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Premortem Analysis into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Premortem Analysis to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- declare failure as a fact, not a possibility — the phrase 'it has failed badly' licenses candor that 'it might fail' suppresses
- rank causes by plausibility x impact, not by who raised them or how uncomfortable they are to hear
- every failure mode must have a leading indicator — a premortem without indicators is not actionable
