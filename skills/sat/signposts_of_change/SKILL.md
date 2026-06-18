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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- each signpost must be discriminating — it must confirm at least one scenario and be neutral or disconfirming for at least one other; a signpost consistent with all scenarios has no diagnostic value
- observable means actually collectible from identified sources, not theoretically possible to observe
- absence of an expected signpost is evidence — the update protocol must handle non-observation as a probabilistic signal, not a null
- signpost thresholds must be set before collection begins; post-hoc threshold adjustment to protect the current assessment is a bias
