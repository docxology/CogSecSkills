---
name: counterintelligence.adversary_tradecraft_profiling
description: Profile an adversary's methods, patterns, and signatures to anticipate their moves.
---

# Adversary Tradecraft Profiling

Adversary tradecraft profiling systematically characterizes the methods, patterns, tools, and operational signatures an adversary habitually employs across known operations. Drawn from counterintelligence practice, it converts scattered incident data into a durable behavioral model that enables anticipation of future moves, attribution of ambiguous incidents, and identification of gaps the adversary exploits. The technique applies structured elicitation across the TTPS (Tactics, Techniques, Procedures, and Signatures) framework to distinguish stable behavioral fingerprints from adaptive camouflage.

## When to use

- a threat actor has left multiple attributed incidents and a durable behavioral model would aid defense or attribution
- an analyst needs to distinguish a known adversary's pattern from coincidental or unrelated activity
- decision-makers require anticipatory warning indicators rather than post-hoc attribution
- a new incident is ambiguous and comparison against a tradecraft profile could resolve attribution

## What it produces

- a TTPS table mapping observed tactics to their techniques, confidence levels, and frequency across known cases
- a set of behavioral signatures and leading indicators to watch for in future operations
- explicit caveats on collection bias, mirror-imaging risk, and adversary adaptive capacity

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- distinguish stable signatures (consistent across operations under pressure) from adaptive camouflage (one-off deceptions); the former is probative, the latter is noise
- profile the behavior, not the identity — capabilities and habits leave evidence even when attribution is uncertain
- flag collection gaps explicitly; a profile derived from only visible operations systematically misses the techniques used when the adversary evades detection
