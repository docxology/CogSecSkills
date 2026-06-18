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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- declare failure as a fact, not a possibility — the phrase 'it has failed badly' licenses candor that 'it might fail' suppresses
- rank causes by plausibility x impact, not by who raised them or how uncomfortable they are to hear
- every failure mode must have a leading indicator — a premortem without indicators is not actionable
