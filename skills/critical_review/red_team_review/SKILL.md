---
name: critical_review.red_team_review
description: Adversarially stress an artifact to find the failure mode its authors did not anticipate.
---

# Red-Team Review

Red-Team Review adversarially stresses an artifact — a plan, policy, argument, model, system, or narrative — to find failure modes, attack surfaces, and exploitable assumptions that the authors did not anticipate. Drawing on the structured analytic tradition of Devil's Advocacy and Team A/Team B analysis, and the security tradition of adversarial red teaming, the reviewer deliberately adopts an opposing or adversarial stance, generating the strongest possible critique, attack, or counter-narrative the artifact could face. The output is a ranked catalog of vulnerabilities, exploitation paths, and proposed mitigations, not a balanced review — the goal is maximum stress, not fairness. In cognitive-security contexts this includes identifying how a disinformation actor or manipulative adversary could exploit a proposed policy, narrative, or analytical product.

## When to use

- before committing to a plan, policy, or analytical judgment where overconfidence or groupthink is plausible
- when a narrative or information campaign needs to be evaluated for exploitability by an adversary
- when a proposed cognitive-security countermeasure needs stress-testing before deployment
- when an analytical product has been produced by a team with shared assumptions and an independent adversarial check is warranted
- when an organization needs to identify how an adversary would undermine a proposed decision or communication

## What it produces

- a ranked vulnerability catalog with exploitation paths and mitigations for each identified failure mode
- an adversarial narrative — the strongest case an opposing actor could make against the artifact
- a set of mitigation recommendations addressing the highest-priority vulnerabilities
- identification of the assumptions whose failure would be most catastrophic

## Defensive boundary

Use Red-Team Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Red-Team Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Red-Team Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Red-Team Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Red-Team Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Red-Team Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Red-Team Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Red-Team Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Red-Team Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Red-Team Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Red-Team Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Red-Team Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Red-Team Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Red-Team Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Red-Team Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Red-Team Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Red-Team Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Red-Team Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Red-Team Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- commit fully to the adversarial perspective — half-hearted red teaming produces the illusion of scrutiny without the substance
- rank vulnerabilities by exploitability x impact, not by how uncomfortable they are to surface
- the red team's job is to find failure modes, not to balance them against strengths — balance is for the final synthesis, not the red team phase
- distinguish vulnerabilities that are inherent to the approach from those that are remediable — remediable ones get mitigations, inherent ones inform go/no-go
