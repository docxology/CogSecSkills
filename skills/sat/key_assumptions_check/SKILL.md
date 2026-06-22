---
name: sat.key_assumptions_check
description: Surface, classify, and stress-test the load-bearing assumptions an analysis rests on.
---

# Key Assumptions Check

The Key Assumptions Check (Heuer & Pherson) makes explicit the stated and UNSTATED beliefs an analytic line silently depends on, then interrogates each: why we believe it, what evidence supports it, and under what conditions it would NOT hold. Each assumption is classified as solid, caveated, unsupported, or a key uncertainty, and the few that are both load-bearing AND uncertain are flagged as "key assumptions". The decisive question for each is "if this assumption is wrong, does the conclusion collapse?" — the technique rewrites the judgment to expose that dependence and names the collection that would test it.

## When to use

- Before finalizing a high-stakes estimate, attribution, or recommendation.
- When a conclusion feels obvious or comfortable — comfort is where unstated
- When the situation has changed and old assumptions may no longer hold.
- As a precondition to other techniques (it pairs naturally with ACH and

## What it produces

- every stated and unstated assumption with rationale, contrary conditions, and confidence class
- the load-bearing and uncertain assumptions, with collapse analysis
- the conclusion rewritten to expose its dependence on key assumptions, plus collection that would test them

## Defensive boundary

Use Key Assumptions Check only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Key Assumptions Check to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Key Assumptions Check, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Key Assumptions Check, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Key Assumptions Check recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Key Assumptions Check: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Key Assumptions Check: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Key Assumptions Check: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Key Assumptions Check cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Key Assumptions Check should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Key Assumptions Check, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Key Assumptions Check, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Key Assumptions Check, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Key Assumptions Check failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Key Assumptions Check failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Key Assumptions Check failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Key Assumptions Check to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Key Assumptions Check into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Key Assumptions Check to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Hunt the unstated.** The assumptions that matter most are usually the ones
- **No free passes for comfort.** An assumption is not "solid" because it is
- **Load-bearing × uncertain = key.** A shaky assumption that nothing depends on
- **Expose the dependence.** A judgment that hides its assumptions overstates its
