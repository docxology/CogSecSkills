---
name: osint_integrity.source_vetting
description: Vet a source's identity, track record, motive, and access before relying on it.
---

# Source Vetting

Source vetting is a structured credibility-assessment process that evaluates a source's identity, access, track record, and motivation before incorporating its claims into analysis. Drawn from intelligence tradecraft (the classic MICE framework and FBI source-reliability scales) and adapted for open-source information environments, it surfaces deceptive, mistaken, or biased sources before their output can anchor downstream judgments. The technique is applied at intake — before a source's claims are treated as evidence — and revisited whenever a source's circumstances or behavior change.

## When to use

- a source is being cited for the first time in an analytic product
- a source makes a claim that would significantly change an analytic judgment if true
- a source's behavior, ownership, or funding has recently changed
- multiple sources all trace back to a single original source that has not been vetted
- a source is anonymous or pseudonymous and no independent corroboration exists
- the stakes of relying on a mistaken or deceptive source are high

## What it produces

- a structured reliability rating (e.g., A–F identity confidence × 1–6 information credibility, NATO standard) with evidence basis
- a motive map identifying who benefits if the source's claims are believed
- an access assessment confirming whether the source could plausibly know what they claim to know
- a track-record summary of prior accurate and inaccurate claims with dated examples
- a table of red flags — deception indicators, anomalies, or bias markers — each linked to evidence
- recommended use conditions: how the source may be used, what corroboration is needed, and what claims fall outside its demonstrated expertise

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess reliability on four independent axes — identity, access, motive, and track record — and do not let a strong score on one compensate for a weak score on another
- separate source reliability (a property of the source) from information credibility (a property of the specific claim) — a reliable source can still be wrong about this claim
- motive analysis must consider not just obvious conflicts of interest but also cognitive biases, in-group loyalty, and reputational incentives that can distort reporting without conscious intent
- treat corroboration from sources that share a common origin as a single evidence point, not as independent confirmation — source genealogy must be traced
- document the vetting result in a retrievable record so the assessment compounds across sessions rather than being re-derived each time
