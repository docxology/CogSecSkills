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

- For Key Assumptions Check, tie each assumption, its confidence class, and its collapse analysis to concrete evidence from the judgment and analytic line, stating the actual basis for belief and the conditions that would falsify it; an assumption rated solid without supporting evidence is unsupported and must be reclassified rather than waved through.
- For Key Assumptions Check, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the assumptions table.
- Before recommending any Key Assumptions Check action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Key Assumptions Check: the unstated as well as stated assumptions have been recovered, each is classified by genuine evidentiary support rather than familiarity, the load-bearing-and-uncertain ones carry an explicit collapse analysis, and no unresolved contradiction would change which assumptions are key or how the revised judgment depends on them.
- Medium for Key Assumptions Check: the assumptions table is plausible, but one important judgment source, comparison case, or alternative explanation remains incomplete.
- Low for Key Assumptions Check: the assumptions table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Key Assumptions Check cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Key Assumptions Check, use only authorized judgment, analytic line, and stated assumptions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Key Assumptions Check, minimize person-level detail in the assumptions table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Key Assumptions Check, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Key Assumptions Check: treating the analysis as done when the silent unstated assumptions the argument requires were never surfaced, or when a comfortable assumption was marked solid without evidence, so the rewritten judgment still hides the dependence that could make the conclusion collapse.
- Key Assumptions Check: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Key Assumptions Check: reporting the assumptions table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Key Assumptions Check outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the assumptions table from Key Assumptions Check into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Key Assumptions Check to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with judgment, analytic line, and stated assumptions' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Hunt the unstated.** The assumptions that matter most are usually the ones
- **No free passes for comfort.** An assumption is not "solid" because it is
- **Load-bearing × uncertain = key.** A shaky assumption that nothing depends on
- **Expose the dependence.** A judgment that hides its assumptions overstates its
