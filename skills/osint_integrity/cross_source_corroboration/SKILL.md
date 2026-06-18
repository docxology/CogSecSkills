---
name: osint_integrity.cross_source_corroboration
description: Require independent corroboration before promoting a claim to a finding.
---

# Cross-Source Corroboration

Cross-source corroboration is the practice of requiring independent confirmation from at least one additional source before elevating a claim from raw collection to an analytic finding. The technique recognizes that a single source — however credible — is insufficient because it may be fabricated, mistaken, or part of a coordinated deception campaign seeding the same narrative across multiple outlets. True corroboration demands source independence: two sources must not share a common origin, be controlled by the same actor, or derive their claim from the same original report. The technique is a primary defense against amplified misinformation and manufactured consensus.

## When to use

- Before any OSINT claim is promoted from raw collection to an analytic product or shared finding
- When a claim is spreading rapidly across social media, news, or analyst channels and speed is creating pressure to accept it
- When the original source of a claim cannot be independently verified or appears to have been recently created
- When the topic is one where coordinated information operations are known or suspected

## What it produces

- A corroboration tier for the claim: independently confirmed, single-source only, or contradicted
- An origin trace that identifies whether multiple reporting sources derive from a single original claim
- A documented promotion decision that can be reviewed and overturned if new corroborating sources emerge

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Independence is defined by origin, not by number — ten outlets repeating one wire report is one source, not ten
- Trace each source's claim back to its original assertion; corroboration requires independent origination, not independent repetition
- Coordinated amplification (bot networks, state media ecosystems, astroturfing) is designed to defeat corroboration — look for identical phrasing, synchronized timing, and shared network infrastructure
- A hold decision is not a rejection — it is a documented waiting state pending additional independent evidence
