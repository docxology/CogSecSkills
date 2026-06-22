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

- For Assumption Surfacing Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Assumption Surfacing Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Assumption Surfacing Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Assumption Surfacing Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Assumption Surfacing Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Assumption Surfacing Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Assumption Surfacing Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Assumption Surfacing Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Assumption Surfacing Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Assumption Surfacing Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Assumption Surfacing Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Assumption Surfacing Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Assumption Surfacing Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Assumption Surfacing Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Assumption Surfacing Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Assumption Surfacing Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Assumption Surfacing Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Distinguish what the argument asserts from what it assumes — assumptions are premises treated as true without proof in this document
- Classify assumptions by load-bearing role: if this assumption is wrong, does the conclusion collapse (critical), weaken (supporting), or hold (peripheral)?
- Assess evidentiary support independently of how confidently the assumption is stated — confident assertion is not evidence
- Flag assumptions that adversaries could falsify cheaply or that rest on a single unverifiable source
