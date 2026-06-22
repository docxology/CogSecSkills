---
name: sat.signposts_of_change
description: Track leading indicators over time to detect trajectory shifts early.
---

# Signposts of Change

Signposts of Change (Heuer & Pherson) is a prospective monitoring technique that derives observable leading indicators from a set of alternative scenarios or hypotheses, then tracks those indicators over time to detect which trajectory is unfolding before it becomes undeniable. Unlike static indicators lists, the technique pairs each signpost explicitly with the scenario it confirms or rules out, allowing analysts to update scenario probabilities continuously as new evidence arrives. In cognitive-security contexts it also serves as an early-warning system for narrative shifts, influence campaign pivots, and disinformation trajectory changes.

## When to use

- multiple plausible trajectories exist and the current analytic line could be invalidated by emerging developments
- a situation is evolving and continuous monitoring is needed to detect trajectory shifts before they become obvious
- an influence campaign, narrative, or adversary operation is suspected and early pivot detection is required
- decision makers need a structured watch-list rather than periodic re-assessments from scratch

## What it produces

- a scenario-keyed signpost matrix where each indicator is explicitly tied to the scenario(s) it confirms or disconfirms
- observable, collection-source-anchored indicators with defined observation thresholds
- an update protocol that prevents analysts from ignoring the absence of expected signposts (absence as evidence)

## Defensive boundary

Use Signposts of Change only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Signposts of Change to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

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

## Failure modes and negative controls

- Signposts of Change failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Signposts of Change failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Signposts of Change failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Signposts of Change to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Signposts of Change into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Signposts of Change to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- each signpost must be discriminating — it must confirm at least one scenario and be neutral or disconfirming for at least one other; a signpost consistent with all scenarios has no diagnostic value
- observable means actually collectible from identified sources, not theoretically possible to observe
- absence of an expected signpost is evidence — the update protocol must handle non-observation as a probabilistic signal, not a null
- signpost thresholds must be set before collection begins; post-hoc threshold adjustment to protect the current assessment is a bias
