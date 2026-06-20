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

## Failure modes and negative controls

- Signposts of Change: treating scenarios or hypotheses as complete when map scenarios to divergence points and derive and filter signposts checks or contradictory evidence are missing.
- Signposts of Change: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Signposts of Change: reporting the signpost matrix without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Signposts of Change outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the signpost matrix from Signposts of Change into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Signposts of Change to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with scenarios or hypotheses, current assessment, and collection resources' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- each signpost must be discriminating — it must confirm at least one scenario and be neutral or disconfirming for at least one other; a signpost consistent with all scenarios has no diagnostic value
- observable means actually collectible from identified sources, not theoretically possible to observe
- absence of an expected signpost is evidence — the update protocol must handle non-observation as a probabilistic signal, not a null
- signpost thresholds must be set before collection begins; post-hoc threshold adjustment to protect the current assessment is a bias
