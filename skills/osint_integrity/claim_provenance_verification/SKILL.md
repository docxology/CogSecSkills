---
name: osint_integrity.claim_provenance_verification
description: Verify a public claim by tracing it to a primary source and corroborating independently.
---

# Claim Provenance Verification

Takes a public claim and traces it upstream through the chain of republication to its earliest origin or primary source, detecting circular reporting where outlets merely cite one another back to a single unverified point. Assesses the primary source directly for scope, caveats, and whether it actually supports the claim, then seeks independent corroboration that does not derive from the same origin. Produces a documented provenance chain and a graded verdict with confidence and the single weakest link in the chain.

## When to use

- Someone asks "is this true?" about a circulating statistic, quote, or report.
- A claim is widely repeated but you cannot tell where it actually came from.
- You suspect circular reporting — many outlets that all trace back to one
- A claim seems to have drifted in scope from what a study or document said.

## What it produces

- A **provenance chain**: an ordered list of sources from the point of
- A **circular-reporting assessment**: whether the chain converges on a single
- A **primary-source assessment**: whether the origin actually states the claim,
- A **verdict**: verified / partially verified / unverified / false /

## Defensive boundary

Use Claim Provenance Verification only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Claim Provenance Verification to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Claim Provenance Verification, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Claim Provenance Verification, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Claim Provenance Verification recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Claim Provenance Verification: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Claim Provenance Verification: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Claim Provenance Verification: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Claim Provenance Verification cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Claim Provenance Verification should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Claim Provenance Verification, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Claim Provenance Verification, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Claim Provenance Verification, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Claim Provenance Verification failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Claim Provenance Verification failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Claim Provenance Verification failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Claim Provenance Verification to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Claim Provenance Verification into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Claim Provenance Verification to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Circular reporting is not corroboration.** Ten outlets that all cite the
- **Independence is the test.** Corroboration only counts when it comes from a
- **Scope drift must be flagged.** Claims mutate as they are retold: a finding
