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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Distinguish the claim (what is asserted) from the evidence (what is offered in support) before assessing the relationship between them
- Overclaiming is not the same as being wrong — a claim can be true yet still overclaim the available evidence
- Evidence types differ in evidentiary force: primary data > peer-reviewed synthesis > expert opinion > authority citation > rhetorical assertion; apply corresponding discount rates
- Cherry-picking is a structural overclaim: the evidence offered may be real and accurate, but the omission of contradicting evidence means the overall inference from 'this evidence' to 'this conclusion' is inflated
- Confidence language (certainly, clearly, obviously) is a claim amplifier — treat it as a claim about evidence strength that must itself be evaluated
