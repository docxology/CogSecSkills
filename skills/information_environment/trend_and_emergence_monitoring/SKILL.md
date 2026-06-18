---
name: information_environment.trend_and_emergence_monitoring
description: Monitor an information space for emerging narratives and inflection points.
---

# Trend & Emergence Monitoring

Trend and Emergence Monitoring provides a structured, continuous-or-periodic process for detecting nascent narratives, coordinated-behavior signals, and inflection-point events before they reach mainstream salience in an information space. Drawing on open-source intelligence tradecraft and social-network analysis, the technique combines quantitative signal monitoring (volume spikes, velocity changes, network topology shifts) with qualitative analysis to distinguish organic trend formation from artificially amplified or coordinated emergence. It is designed as an early-warning system that cues deeper analytic responses before an influence operation or harmful narrative achieves significant reach.

## When to use

- when running an ongoing information-environment monitoring program and you need a structured cycle to distinguish signal from noise
- when a high-risk event (election, crisis, policy decision) is approaching and early-warning is operationally valuable
- when you have previously identified a threat actor and want to monitor for new activity from that actor or their narrative templates
- when standing up a new monitoring program and need to establish baselines before emergence detection becomes meaningful

## What it produces

- a prioritized signal log of emerging narratives, accounts, or topics with emergence-stage classification
- an authenticity assessment for each signal distinguishing organic trend formation from coordinated or artificial amplification
- escalation recommendations indicating which signals warrant deeper investigation (attribution, network mapping, content analysis)
- a new baseline for the next monitoring cycle, enabling trend-over-time comparisons

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- measure velocity (rate of change) not just volume — a small signal growing rapidly is more operationally relevant than a large stable signal
- compare against baseline — emergence is meaningful only relative to the established normal distribution in the space
- apply the three-signal rule before escalating: corroborate an apparent signal across at least three independent content instances or sources to avoid single-post false alarms
- classify emergence stage (seeding, early-growth, acceleration, plateau) — the appropriate countermeasure differs by stage
