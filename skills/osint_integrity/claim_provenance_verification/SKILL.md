---
name: osint_integrity.claim_provenance_verification
description: >-
  Verify a public claim by tracing it back through the chain of republication to
  its primary source, detecting circular reporting, assessing the primary source
  directly, and seeking independent corroboration — separating what is actually
  established from what is merely repeated. Produces a documented provenance
  chain and a graded verdict with confidence and the single weakest link.
---

# Claim Provenance Verification

A public claim is rarely born where you find it. It has been retold, requoted,
and reframed across a chain of outlets, and each retelling can drop a caveat,
widen a scope, or simply cite the outlet upstream of it. This skill walks that
chain backward to its origin, distinguishes a genuine primary source from a
secondary one that merely points at another secondary, and tests whether
anything independent actually corroborates the claim.

## When to use

- Someone asks "is this true?" about a circulating statistic, quote, or report.
- A claim is widely repeated but you cannot tell where it actually came from.
- You suspect circular reporting — many outlets that all trace back to one
  unverified origin.
- A claim seems to have drifted in scope from what a study or document said.

## What it produces

- A **provenance chain**: an ordered list of sources from the point of
  encounter back to the earliest/origin instance, each with a link and a
  timestamp, plus a chain-of-custody note describing how each link cites the
  next.
- A **circular-reporting assessment**: whether the chain converges on a single
  unverified origin or genuinely branches into independent sources.
- A **primary-source assessment**: whether the origin actually states the claim,
  at the same scope, without dropped caveats.
- A **verdict**: verified / partially verified / unverified / false /
  unverifiable, with a confidence level and the single weakest link.

## Procedure

The full step-by-step procedure — atomic claim statement, upstream tracing,
circular-reporting detection, primary-source assessment, independent
corroboration, provenance recording, and verdict — is in
[workflow.md](workflow.md). Follow it in order; do not skip the
independent-corroboration step even when the claim "feels" obviously true.

## Key discipline

- **Circular reporting is not corroboration.** Ten outlets that all cite the
  same single origin are one source, not ten. Volume of repetition carries no
  evidentiary weight; trace each citation upstream and collapse the chain to its
  distinct origins before counting.
- **Independence is the test.** Corroboration only counts when it comes from a
  source that does not derive from the same origin — a separate primary
  document, a separate eyewitness, a separate measurement. Two outlets sharing a
  wire story are one source.
- **Scope drift must be flagged.** Claims mutate as they are retold: a finding
  about one cohort becomes a claim about everyone; "associated with" becomes
  "causes." When the primary source's scope is narrower than the claim as
  stated, the claim is at best partially verified — never collapse the
  difference silently.
