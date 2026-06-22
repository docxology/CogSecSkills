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

- For Structured Brainstorming, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Brainstorming, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Brainstorming recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Structured Brainstorming: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Brainstorming: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Brainstorming: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Brainstorming cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Brainstorming should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Structured Brainstorming, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Brainstorming, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Brainstorming, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Structured Brainstorming failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Structured Brainstorming failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Brainstorming failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Structured Brainstorming to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Brainstorming into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Brainstorming to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- no criticism, evaluation, or ranking is permitted during the divergence phase — deferral of judgment is the technique's core mechanism
- quantity of ideas in divergence is a feature: more ideas reduce the probability that the best one was anchored out
- every discarded idea from convergence must be recorded with an explicit reason — silent omission is how groupthink re-enters
