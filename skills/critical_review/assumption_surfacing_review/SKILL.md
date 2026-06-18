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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Distinguish what the argument asserts from what it assumes — assumptions are premises treated as true without proof in this document
- Classify assumptions by load-bearing role: if this assumption is wrong, does the conclusion collapse (critical), weaken (supporting), or hold (peripheral)?
- Assess evidentiary support independently of how confidently the assumption is stated — confident assertion is not evidence
- Flag assumptions that adversaries could falsify cheaply or that rest on a single unverifiable source
