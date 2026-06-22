---
name: critical_review.assumption_surfacing_review
description: Make every implicit assumption explicit and assess its load-bearing role.
---

# Assumption Surfacing Review

Assumption Surfacing Review (rooted in Key Assumptions Check, Heuer & Pherson) makes every implicit premise that underlies an argument or assessment explicit, then evaluates how load-bearing each assumption is and how well it is supported. The technique is essential in cognitive-security contexts because manipulation and influence operations routinely exploit unexamined premises — by surfacing them, analysts create an audit trail that lets reviewers challenge the analytic foundations rather than only the conclusions.

## When to use

- Before committing to a policy, analytic judgment, or plan that rests on multiple premises
- When reviewing an intelligence product or briefing for cognitive-security weaknesses
- When an argument or narrative seems compelling but its foundations have not been scrutinized
- During adversarial red-teaming to identify which assumptions an opponent could falsify or exploit
- When onboarding a new analytic team to a long-running problem where inherited assumptions may be stale

## What it produces

- A complete register of explicit and implicit assumptions underlying the target text
- A load-bearing classification for each assumption (critical, supporting, peripheral)
- An evidentiary-support rating for each assumption
- A ranked list of the most dangerous unexamined premises and recommended validation or monitoring actions

## Defensive boundary

Use Assumption Surfacing Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Assumption Surfacing Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Assumption Surfacing Review, bind each surfaced assumption and its load-bearing and support ratings to concrete evidence drawn from the specific target-text passage or domain-context detail that reveals it, and label any premise resting only on confident assertion as an unsupported assumption rather than established evidence.
- For Assumption Surfacing Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the assumption register.
- Before recommending any Assumption Surfacing Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Assumption Surfacing Review: every load-bearing assumption in the register is grounded in a specific passage of the target text, the critical/supporting/peripheral classification and evidentiary-support rating hold up when any single excerpt is reconsidered, and no unresolved contradiction would change which premises are flagged as the most dangerous to the conclusion.
- Medium for Assumption Surfacing Review: the assumption register is plausible, but one important target text source, comparison case, or alternative explanation remains incomplete.
- Low for Assumption Surfacing Review: the assumption register rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Assumption Surfacing Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Assumption Surfacing Review, use only authorized target text, and domain context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Assumption Surfacing Review, minimize person-level detail in the assumption register; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Assumption Surfacing Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Assumption Surfacing Review: declaring the assumption register complete when implicit premises behind unstated reasoning gaps were never extracted or contradictory evidence about a critical premise was left unexamined, so an empty findings list reflects a shallow scan rather than a genuinely well-founded argument.
- Assumption Surfacing Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Assumption Surfacing Review: reporting the assumption register without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Assumption Surfacing Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the assumption register from Assumption Surfacing Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Assumption Surfacing Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with target text, and domain context' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Distinguish what the argument asserts from what it assumes — assumptions are premises treated as true without proof in this document
- Classify assumptions by load-bearing role: if this assumption is wrong, does the conclusion collapse (critical), weaken (supporting), or hold (peripheral)?
- Assess evidentiary support independently of how confidently the assumption is stated — confident assertion is not evidence
- Flag assumptions that adversaries could falsify cheaply or that rest on a single unverifiable source
