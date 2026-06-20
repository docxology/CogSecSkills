---
name: sat.structured_brainstorming
description: Divergent then convergent idea generation with explicit anti-anchoring steps.
---

# Structured Brainstorming

Structured Brainstorming is a two-phase diverge-then-converge technique that separates unconstrained idea generation from critical evaluation to prevent anchoring, groupthink, and premature convergence on the most socially acceptable or seniority-endorsed hypothesis. The divergence phase enforces deferral of judgment while the convergence phase uses explicit criteria to cluster, rank, and discard ideas. In cognitive-security analysis it surfaces hypotheses and threat vectors that a linear, hierarchical review would suppress, and the explicit anti-anchoring steps protect against an adversary's ability to pre-seed the analytic frame.

## When to use

- the problem space has not been rigorously scoped and unknown hypotheses may have been missed
- a dominant hypothesis has hardened in the analytic team and alternative possibilities are being systematically overlooked
- an adversary may have deliberately seeded a single compelling narrative to anchor analytic attention
- planning stage of a complex investigation where the hypothesis list is the first deliverable

## What it produces

- a raw, unconstrained idea inventory that captures every plausible hypothesis or option before filtering
- a convergence output with ideas clustered by theme, ranked by stated criteria, and a record of discarded ideas and the reasons for discarding them

## Defensive boundary

Use Structured Brainstorming only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Structured Brainstorming to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Structured Brainstorming, tie each raw idea inventory, and ranked shortlist claim to concrete evidence from the specific problem statement, prior framing, and convergence criteria item, source excerpt, observation, or command result that supports it.
- For Structured Brainstorming, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the raw idea inventory.
- Before recommending any Structured Brainstorming action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Structured Brainstorming: the raw idea inventory is supported by multiple independent hypotheses, assumptions, indicators, evidence tables, and confidence notes; frame the problem and set aside prior framing and diverge: unconstrained idea generation checks agree, and no unresolved contradiction would change the result.
- Medium for Structured Brainstorming: the raw idea inventory is plausible, but one important problem statement source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Brainstorming: the raw idea inventory rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Brainstorming cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Structured Brainstorming, use only authorized problem statement, prior framing, and convergence criteria, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Brainstorming, minimize person-level detail in the raw idea inventory; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Brainstorming, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Brainstorming: treating problem statement as complete when frame the problem and set aside prior framing and diverge: unconstrained idea generation checks or contradictory evidence are missing.
- Structured Brainstorming: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Brainstorming: reporting the raw idea inventory without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Structured Brainstorming outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the raw idea inventory from Structured Brainstorming into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Brainstorming to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with problem statement, prior framing, and convergence criteria' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- no criticism, evaluation, or ranking is permitted during the divergence phase — deferral of judgment is the technique's core mechanism
- quantity of ideas in divergence is a feature: more ideas reduce the probability that the best one was anchored out
- every discarded idea from convergence must be recorded with an explicit reason — silent omission is how groupthink re-enters
