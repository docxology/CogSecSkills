---
name: sat.customer_aims_checklist
description: Clarify Audience, Issue, Message, and Storyline so the product fits the decision it serves.
---

# Customer (AIMS) Checklist

The Customer AIMS Checklist is a structured pre-production technique that forces analysts to explicitly specify four parameters before drafting any intelligence or analytic product: the Audience (who will read it and what their role is), the Issue (the precise question being answered), the Message (the single most important takeaway the customer needs to act on), and the Storyline (the logical flow from evidence to conclusion that will persuade the specific audience). By making these four parameters explicit, the checklist prevents the common failure mode of producing analytically correct but decision-irrelevant products. It is equally useful as a post-production review gate to assess whether a completed product actually serves its intended consumer.

## When to use

- before drafting any intelligence product to ensure it is scoped to the decision-maker's actual need
- when a product review reveals that the analysis is accurate but the customer did not find it useful
- when multiple analysts are contributing to one product and a shared framing is needed
- as a quality gate before publication or dissemination to catch decision-irrelevance before delivery

## What it produces

- a precise one-sentence statement of the audience, their role, and their decision context
- a precise one-sentence statement of the issue being answered (narrow enough to be answerable in this product)
- a precise one-sentence statement of the single most important message the customer must take away
- a brief outline of the storyline — the logical path from evidence to conclusion that will resonate with this audience

## Defensive boundary

Use Customer (AIMS) Checklist only for structured analytic technique support: recognize, assess, document, or defend analytic rigor, alternative hypotheses, and calibrated judgment. Do not use this skill to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.

## Misuse redirect

If a request asks Customer (AIMS) Checklist to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation, refuse that path and redirect to the safe defensive form: apply the structured technique to supplied evidence while preserving alternatives and uncertainty.

## Evidence discipline

- For Customer (AIMS) Checklist, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Customer (AIMS) Checklist, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Customer (AIMS) Checklist recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Customer (AIMS) Checklist: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Customer (AIMS) Checklist: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Customer (AIMS) Checklist: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Customer (AIMS) Checklist cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Customer (AIMS) Checklist should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Customer (AIMS) Checklist, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Customer (AIMS) Checklist, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Customer (AIMS) Checklist, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Customer (AIMS) Checklist failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Customer (AIMS) Checklist failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Customer (AIMS) Checklist failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Customer (AIMS) Checklist to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Customer (AIMS) Checklist into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Customer (AIMS) Checklist to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- the Message must be a single declarative sentence the customer can act on — 'we assess that X' not 'this paper examines X'
- the Audience field must name a role or position, not just an organization — the question is what decision they need to make
- the Storyline should be derived from the Message and Audience, not from the analyst's preferred logical order
