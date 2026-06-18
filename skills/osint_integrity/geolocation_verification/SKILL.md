---
name: osint_integrity.geolocation_verification
description: Confirm where imagery was taken using corroborating geographic features (defensive OSINT).
---

# Geolocation Verification

Geolocation verification cross-references visual and contextual clues in imagery — terrain, vegetation, architecture, shadows, signage, infrastructure — against authoritative mapping data to confirm or refute a claimed location. It is a defensive OSINT discipline used to detect context-collapsed or fabricated imagery before it is treated as evidence. The technique draws on sun-angle computation, map comparison, satellite imagery, and street-level reference data. It provides an independently verifiable anchor for where and when a visual was plausibly captured.

## When to use

- an image or video is being considered as evidence of a specific event at a specific place
- there is a claim that footage shows a location that it may not depict
- context collapse is suspected — older or unrelated imagery being circulated with a new narrative
- a media organization or analyst needs to independently confirm a visual's provenance before publication

## What it produces

- a probable location fix with latitude/longitude estimate or named area, plus a confidence tier (confirmed / likely / inconclusive / contradicted)
- a list of corroborating features used (terrain shape, building style, road markings, vegetation, signage)
- a note on any features that contradict the claimed location
- a shadow-angle cross-check result where the sun position can be computed from the claimed date/time

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- build from fixed landmarks outward — unique terrain, infrastructure, or signage constrains the search space before general landscape features
- never anchor to the claimed location first; start landmark-agnostic and let features converge
- shadow angle and vegetation season are independent physical constraints — a mismatched shadow falsifies the claimed date as strongly as it falsifies the location
- document every reference source and feature match so the conclusion is reproducible
