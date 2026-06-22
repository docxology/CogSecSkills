---
name: critical_review.claim_evidence_audit
description: Bind every claim to its supporting evidence; flag overclaims and unsupported assertions.
---

# Claim-Evidence Audit

Claim-Evidence Audit is a structured review technique that walks through every substantive claim in a document, identifies the evidence offered in support, and renders a verdict on the strength and sufficiency of that support. It distinguishes overclaims (conclusions that exceed what the evidence can bear), underclaims (conclusions hedged beyond what strong evidence warrants), unsupported assertions (claims with no evidence offered), and well-supported claims. In cognitive-security work, this technique is a primary defense against epistemic manipulation: fabricated confidence, cherry-picked data, and rhetorical amplification all fail a rigorous claim-evidence audit.

## When to use

- When reviewing a document intended to influence a decision and the strength of the evidentiary support has not been independently assessed
- When detecting potential disinformation or manipulated narrative — both rely heavily on overclaiming from thin evidence
- When performing quality assurance on an analytic product before it is disseminated
- When calibrating confidence levels in a report — separating well-established findings from speculative conclusions
- When adversarial content has been introduced into a document pipeline and the evidence basis of individual claims must be traced

## What it produces

- A complete inventory of substantive claims in the document
- A per-claim evidence binding: what evidence was offered and whether it is sufficient
- Severity-rated overclaims, underclaims, and unsupported assertions
- A pattern analysis of how the document systematically misrepresents the evidence-claim relationship
- Specific corrections: how each flagged claim should be reframed to match the actual evidence

## Defensive boundary

Use Claim-Evidence Audit only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Claim-Evidence Audit to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Claim-Evidence Audit, bind each claim's verdict to concrete evidence by recording exactly what the document offers in support and classifying its type, and treat confidence language such as 'clearly' or 'obviously' as a claim about evidence strength to be evaluated, never as the evidence itself.
- For Claim-Evidence Audit, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the claim evidence table.
- Before recommending any Claim-Evidence Audit action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Claim-Evidence Audit: each substantive claim's sufficiency verdict is anchored to the specific evidence the document actually offers for it, the evidence-type classification and overclaim or unsupported ratings remain stable when any single claim-evidence pair is re-examined, and no unresolved contradiction would change the overall judgment of whether the conclusions can be trusted as stated.
- Medium for Claim-Evidence Audit: the claim evidence table is plausible, but one important document source, comparison case, or alternative explanation remains incomplete.
- Low for Claim-Evidence Audit: the claim evidence table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Claim-Evidence Audit cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Claim-Evidence Audit, use only authorized document, and claim taxonomy, public or source-approved records, and caller-provided context needed for the defensive task.
- For Claim-Evidence Audit, minimize person-level detail in the claim evidence table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Claim-Evidence Audit, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Claim-Evidence Audit: declaring the document sound when substantive claims were never separated from the evidence offered for them, so cherry-picked data, rhetorical confidence words, and implicit overclaims in how conclusions are framed pass unexamined and an unsupported assertion is mistaken for a well-supported finding.
- Claim-Evidence Audit: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Claim-Evidence Audit: reporting the claim evidence table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Claim-Evidence Audit outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the claim evidence table from Claim-Evidence Audit into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Claim-Evidence Audit to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with document, and claim taxonomy' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Distinguish the claim (what is asserted) from the evidence (what is offered in support) before assessing the relationship between them
- Overclaiming is not the same as being wrong — a claim can be true yet still overclaim the available evidence
- Evidence types differ in evidentiary force: primary data > peer-reviewed synthesis > expert opinion > authority citation > rhetorical assertion; apply corresponding discount rates
- Cherry-picking is a structural overclaim: the evidence offered may be real and accurate, but the omission of contradicting evidence means the overall inference from 'this evidence' to 'this conclusion' is inflated
- Confidence language (certainly, clearly, obviously) is a claim amplifier — treat it as a claim about evidence strength that must itself be evaluated
