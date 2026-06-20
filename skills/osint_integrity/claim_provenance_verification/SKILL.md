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

- For Claim Provenance Verification, tie each provenance chain, and verdict claim to concrete evidence from the specific claim, and starting sources item, source excerpt, observation, or command result that supports it.
- For Claim Provenance Verification, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the provenance chain.
- Before recommending any Claim Provenance Verification action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Claim Provenance Verification: the provenance chain is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; state the claim atomically and anchor the point of encounter checks agree, and no unresolved contradiction would change the result.
- Medium for Claim Provenance Verification: the provenance chain is plausible, but one important claim source, comparison case, or alternative explanation remains incomplete.
- Low for Claim Provenance Verification: the provenance chain rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Claim Provenance Verification cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Claim Provenance Verification, use only authorized claim, and starting sources, public or source-approved records, and caller-provided context needed for the defensive task.
- For Claim Provenance Verification, minimize person-level detail in the provenance chain; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Claim Provenance Verification, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Claim Provenance Verification: treating claim as complete when state the claim atomically and anchor the point of encounter checks or contradictory evidence are missing.
- Claim Provenance Verification: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Claim Provenance Verification: reporting the provenance chain without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Claim Provenance Verification outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the provenance chain from Claim Provenance Verification into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Claim Provenance Verification to verify supplied claims, media, sources, or datasets with documented public-source methods with claim, and starting sources' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- **Circular reporting is not corroboration.** Ten outlets that all cite the
- **Independence is the test.** Corroboration only counts when it comes from a
- **Scope drift must be flagged.** Claims mutate as they are retold: a finding
