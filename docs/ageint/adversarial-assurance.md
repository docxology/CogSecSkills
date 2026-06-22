# Adversarial Assurance

Adversarial assurance is the practice of deliberately attacking your own analysis, code, and claims — first adversarially, then constructively — to find where they break *before* an adversary or reality does. It is the upstream primer for the `critical_review` skill group, and especially for its flagship, `red_team_review`.

## Contents

- [Why it matters for cognitive security](#why-it-matters-for-cognitive-security)
- [Two adversarial postures: Devil's Advocacy vs. Team A/Team B](#two-adversarial-postures-devils-advocacy-vs-team-a-team-b)
- [Adversary modeling](#adversary-modeling)
- [Attack-surface enumeration](#attack-surface-enumeration)
- [Exploitability × impact prioritization](#exploitability--impact-prioritization)
- [Inherent vs. remediable, and the go/no-go](#inherent-vs-remediable-and-the-go-no-go)
- [Other core concepts](#other-core-concepts)
- [How CogSecSkills operationalizes this](#how-cogsecskills-operationalizes-this)
- [The critical_review skill group](#the-critical_review-skill-group)
- [Defensive & ethical framing](#defensive--ethical-framing)
- [Further study](#further-study)

## Why it matters for cognitive security

Defensive work fails silently when its checks are weak: a green test suite, a passing review, or a confident brief can all be wrong in ways no one looked for. Ordinary verification is built to *confirm* — to show that the thing works on the cases the author already imagined. An adversary, a critic, or reality itself probes exactly the cases the author did *not* imagine. Adversarial assurance closes that gap by deliberately adopting the opposing stance against your own output, so the failure mode is found by you, on your schedule, instead of by an attacker on theirs.

This matters acutely in cognitive security, where the "system under test" is often a narrative, a policy, or an analytical judgment rather than a binary. A disinformation actor does not file a bug report; they exploit the framing your analysis took for granted. Treating your own product as the target is how you surface those framings before they ship.

## Two adversarial postures: Devil's Advocacy vs. Team A/Team B

Structured analytic technique gives two distinct ways to manufacture an opposing view, and choosing between them is the first decision in any assurance effort.

**Devil's Advocacy** is a single analyst — or a single skill invocation — constructing the strongest possible contrary case against the prevailing view. One actor builds one adversarial product. It is fast, cheap, and well suited to most reviews. Its weakness is that the advocate still shares a mind, and often a frame, with the original analysis: the contrary case can inherit the very assumption that needed challenging.

**Structured Team A/Team B** uses two *independent* teams that each produce a competing product, which is then adjudicated by a third party. It is heavier and slower, and it is the right tool precisely when the risk is a shared assumption between the reviewer and the author — the situation Devil's Advocacy is least able to catch. When two teams reason from independent priors and still diverge, the divergence itself is diagnostic.

`red_team_review` emulates the **contrary case as one product** (the Devil's Advocacy posture) and explicitly flags Team A/Team B as the heavier alternative to reach for when shared assumptions between reviewer and author are the real danger. Knowing which posture you are in keeps you from mistaking a cheap single-frame critique for the independent adjudication a high-stakes decision actually warrants.

## Adversary modeling

A red-team finding is only as credible as the adversary behind it. Before enumerating any vulnerability, ground a concrete adversary model along three axes:

- **Intent** — what outcome does the adversary want (degrade trust, exfiltrate, mislead a decision, launder a false narrative)?
- **Capability** — what can they actually do (technical access, compute, social reach, insider knowledge)?
- **Access** — what surface can they touch, and under what authorization?

An ungrounded adversary is the most common way a red team produces theater instead of assurance: with no stated intent, capability, or access, "the absence of findings reflects an incomplete review rather than a hardened artifact." Every vulnerability should name the specific adversary capability that turns an observation into an exploit. A flaw with no plausible exploitation path under the modeled adversary is a speculation, and is labelled as such — not promoted to a finding.

Because any single adversary model can be wrong, preserve credible *alternative* adversary models rather than forcing one worst-case narrative. The next discriminating check is often the one that would rule a competing adversary in or out.

## Attack-surface enumeration

Coverage is the second failure point. A review that attacks only the dimension the author finds most natural — usually the technical one — declares the artifact hardened while leaving whole categories untouched. Enumerate the surface across at least these dimensions:

- **Logical** — flawed inferences, hidden premises, non-sequiturs in the argument itself.
- **Operational** — process, workflow, and human-in-the-loop steps that can be bypassed or overloaded.
- **Technical** — code, configuration, data handling, and dependency weaknesses.
- **Informational** — how the artifact sources, frames, and presents evidence, and how that can be poisoned or spun.
- **Reputational** — how the artifact, if exploited, damages trust, standing, or the credibility of the defense.

Skipping a relevant dimension is its own negative control: an empty findings list is only meaningful once every applicable surface has actually been examined.

## Exploitability × impact prioritization

Not every weakness deserves equal attention, and "loud" is not the same as "likely." Score each finding on two independent axes:

- **Exploitability** — how feasible the attack is for the *modeled* adversary, given their stated capability and access.
- **Impact** — how bad the outcome is if the exploit succeeds.

The product orders the vulnerability catalog into priority bands. Two refinements keep the ranking honest. First, **compounding chains**: a low-impact flaw that unlocks a high-impact one is re-banded to the worst outcome the chain reaches, because an adversary will chain flaws even when each link looks minor in isolation. Second, **estimate discipline**: exploitability and impact are analyst *estimates*, not measurements. Flag any finding where two reasonable reviewers could score differently, and treat the bands — and the go/no-go they feed — as calibrated judgments to be peer-checked, never as objective values. A ranking that flips when a single supporting excerpt is removed is not yet stable enough to act on.

## Inherent vs. remediable, and the go/no-go

The final discipline is to classify each top vulnerability:

- **Remediable** — the artifact can be fixed and re-tested against the modeled adversary to confirm the mitigation holds. These receive concrete mitigation recommendations.
- **Inherent** — the weakness is a property of the approach itself and cannot be patched away. These do not get a mitigation; they inform the decision directly.

This classification feeds an explicit **go / no-go / go-with-conditions** recommendation. The output of adversarial assurance is not a balanced review and is not fairness — it is maximum stress plus a clear statement of the **residual risk** a decision-maker would accept if the artifact proceeds unchanged. "Go-with-conditions" names the mitigations that must land first; "no-go" is reserved for inherent risk a decision-maker should not accept. Before any go/no-go is recommended, identify the weakest evidence link behind the highest-ranked finding and the next discriminating check that would settle it, so the recommendation carries its own uncertainty with it.

## Other core concepts

- **Adversarial-then-constructive critique** — first attack an artifact for its weakest points (the red pass), then propose the strongest fix (the blue pass), so criticism produces improvement rather than just doubt.
- **Verify-the-verifier** — the load-bearing discipline: *a test suite that stays green when you inject a real defect proves nothing*. Mutate the system, confirm the check fails, then trust it. Non-vacuity (the gate actually fires on the failure it claims to catch) is mandatory.
- **Claim–evidence binding** — every claim in a report or caption must resolve to its actual source of truth, not to forgeable stored or restated values; bind verification to the registry, not the rows.
- **Severity vs. confidence** — rating findings on two independent axes (how bad if true × how sure it is true) to prioritize honestly and avoid conflating loud with likely.
- **Premortem & structured self-critique** — assume the project failed; enumerate why; apply the same falsification discipline to code and process that SATs apply to analysis.

## How CogSecSkills operationalizes this

Skills in the `critical_review` group make assurance repeatable: running adversarial-then-constructive review passes, grounding an adversary model before enumerating an attack surface, injecting defects to confirm a gate actually fires (verify-the-verifier), checking claim-to-source binding, and driving premortems over a project or codebase. Each emits a findings artifact — scored on exploitability/impact or severity/confidence — for human triage, and every entry ties back to concrete evidence: a quoted excerpt, a row of the artifact map, a stated adversary capability, an observation, or a command result.

## The critical_review skill group

Adversarial assurance is realized as a family of concrete, composable skills under `skills/critical_review/`. The flagship sits at the center; the others narrow the lens to a single assurance dimension:

- **`red_team_review`** — the flagship. Adversarially stresses an artifact to find the failure mode its authors did not anticipate, producing a grounded adversary model, an enumerated attack surface, an exploitability×impact-ranked vulnerability catalog with compounding chains, an inherent-vs-remediable classification, and an explicit go/no-go.
- **`project_critical_review`** — adversarial-then-constructive review of a whole project: claims, evidence, risks, gaps, and a go/no-go.
- **`threat_model_review`** — reviews a system's threat model for missing actors, surfaces, and assumptions; the natural partner to attack-surface enumeration.
- **`assumption_surfacing_review`** — makes every implicit assumption explicit and assesses its load-bearing role — directly addressing the shared-assumption risk that distinguishes Team A/Team B from Devil's Advocacy.
- **`claim_evidence_audit`** — binds every claim to its supporting evidence and flags overclaims; the operational form of claim–evidence binding.
- **`logical_coherence_review`**, **`statistical_validity_review`**, **`research_design_critique`**, **`reproducibility_assessment`** — attack the logical, statistical, design, and reproducibility surfaces respectively.
- **`code_security_review`**, **`citation_integrity_review`**, **`ethics_and_harms_review`** — harden the technical, sourcing, and harm surfaces.

Together they let an assurance effort start broad (red-team the whole artifact) and then drill into whichever surface the red pass flagged as weakest.

## Defensive & ethical framing

The target is always your *own* work — analysis, code, and claims — to make defenses sounder and honesty enforceable. This is self-directed assurance under human oversight, never offensive exploitation of others' systems. `red_team_review` is scoped accordingly: it refuses to launder weak claims, fabricate findings, or produce exploit guidance without mitigation, and redirects any such request to the safe defensive form of reviewing supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures. Scores are analyst estimates to be peer-checked, not guarantees; the artifact states what it cannot determine and which attack paths remain unknown.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- Bryce G. Hoffman, *Red Teaming: How Your Business Can Conquer the Competition by Challenging Yourself* (2017).
- Gary Klein, "Performing a Project Premortem," *Harvard Business Review* (2007); software mutation-testing literature (e.g., PIT / mutation analysis).
- Richards J. Heuer Jr. & Randolph H. Pherson, *Structured Analytic Techniques for Intelligence Analysis* — canonical treatment of Devil's Advocacy and Team A/Team B.
