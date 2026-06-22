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

- For Claim-Evidence Audit, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Claim-Evidence Audit, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Claim-Evidence Audit recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Claim-Evidence Audit: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Claim-Evidence Audit: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Claim-Evidence Audit: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Claim-Evidence Audit cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Claim-Evidence Audit should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Claim-Evidence Audit, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Claim-Evidence Audit, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Claim-Evidence Audit, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Claim-Evidence Audit failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Claim-Evidence Audit failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Claim-Evidence Audit failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Claim-Evidence Audit to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Claim-Evidence Audit into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Claim-Evidence Audit to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Distinguish the claim (what is asserted) from the evidence (what is offered in support) before assessing the relationship between them
- Overclaiming is not the same as being wrong — a claim can be true yet still overclaim the available evidence
- Evidence types differ in evidentiary force: primary data > peer-reviewed synthesis > expert opinion > authority citation > rhetorical assertion; apply corresponding discount rates
- Cherry-picking is a structural overclaim: the evidence offered may be real and accurate, but the omission of contradicting evidence means the overall inference from 'this evidence' to 'this conclusion' is inflated
- Confidence language (certainly, clearly, obviously) is a claim amplifier — treat it as a claim about evidence strength that must itself be evaluated
