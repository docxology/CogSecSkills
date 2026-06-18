# Adversarial Assurance

Adversarial assurance is the practice of deliberately attacking your own analysis, code, and claims — first adversarially, then constructively — to find where they break *before* an adversary or reality does.

## Why it matters for cognitive security

Defensive work fails silently when its checks are weak: a green test suite, a passing review, or a confident brief can all be wrong in ways no one looked for. Adversarial assurance is the antidote to false confidence. By treating your own outputs as the target, you surface the gaps that ordinary verification — designed to confirm, not to falsify — systematically misses.

## Core concepts

- **Adversarial-then-constructive critique** — first attack an artifact for its weakest points (the red pass), then propose the strongest fix (the blue pass), so criticism produces improvement rather than just doubt.
- **Red-teaming** — independent challenge of plans, claims, models, and systems by someone tasked to break them, distinct from the author's self-review.
- **Verify-the-verifier** — the load-bearing discipline: *a test suite that stays green when you inject a real defect proves nothing*. Mutate the system, confirm the check fails, then trust it. Non-vacuity (the gate actually fires on the failure it claims to catch) is mandatory.
- **Claim–evidence binding** — every claim in a report or caption must resolve to its actual source of truth, not to forgeable stored or restated values; bind verification to the registry, not the rows.
- **Severity vs. confidence** — rating findings on two independent axes (how bad if true × how sure it is true) to prioritize honestly and avoid conflating loud with likely.
- **Premortem & structured self-critique** — assume the project failed; enumerate why; apply the same falsification discipline to code and process that SATs apply to analysis.

## How CogSecSkills operationalizes this

Skills in this group make assurance repeatable: running adversarial-then-constructive review passes, injecting defects to confirm a gate actually fires (verify-the-verifier), checking claim-to-source binding, and driving premortems over a project or codebase. Each emits a severity-and-confidence-scored findings artifact for human triage.

## Defensive & ethical framing

The target is always your *own* work — analysis, code, and claims — to make defenses sounder and honesty enforceable. This is self-directed assurance under human oversight, never offensive exploitation of others' systems.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- Bryce G. Hoffman, *Red Teaming: How Your Business Can Conquer the Competition by Challenging Yourself* (2017).
- Gary Klein, "Performing a Project Premortem," *Harvard Business Review* (2007); software mutation-testing literature (e.g., PIT / mutation analysis).
