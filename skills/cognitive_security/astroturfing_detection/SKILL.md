---
name: cognitive_security.astroturfing_detection
description: Distinguish manufactured grassroots activity from organic engagement.
---

# Astroturfing Detection

Astroturfing detection identifies manufactured grassroots activity — coordinated campaigns designed to simulate organic, spontaneous public support or opposition. The technique draws on network-structure analysis, account behavioral signals, and content-similarity patterns to distinguish authentic civic expression from synthetic amplification. Defensively, it helps analysts, journalists, and platform trust-and-safety teams surface coordinated inauthentic behavior (CIB) and protect genuine public discourse from being drowned out or misrepresented.

## When to use

- a narrative is spreading unusually fast and account patterns look homogeneous
- a social movement or petition appears but its account base lacks organic growth history
- a platform trust-and-safety team is investigating potential CIB
- an analyst needs to distinguish genuine public opinion from manufactured consensus before briefing decision-makers
- a journalist is fact-checking whether a hashtag campaign is organic

## What it produces

- a tiered confidence assessment (high/medium/low) that the activity is coordinated and inauthentic
- a list of behavioral and structural indicators used to reach the conclusion
- cluster-level view of which accounts appear to be operating in concert
- recommended follow-on steps (e.g., platform reporting, further OSINT, or temporal anchoring)

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- look for behavioral coordination, not just content similarity — same message from 1000 accounts with identical posting cadence is more diagnostic than similar phrasing alone
- anchor findings to observable signals (creation date spikes, follower-graph density, cross-platform account reuse) rather than inferred intent
- assign confidence tiers and document which specific indicators drove each tier to support adversarial review of the conclusion
