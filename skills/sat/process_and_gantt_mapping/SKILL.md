---
name: sat.process_and_gantt_mapping
description: Lay out a process or adversary plan as sequenced, dependency-aware steps.
---

# Process & Gantt Mapping

Process and Gantt Mapping is a structured analytic technique that decomposes a complex activity — an adversary plan, a supply chain, a disinformation campaign, or an operational sequence — into discrete, dependency-ordered steps laid out on a timeline. The visual sequence reveals critical path nodes, prerequisite chains, observable tripwires, and resource-intensive choke points that prose analysis obscures. In cognitive-security work it is used to model how an influence operation, deception campaign, or hostile cognitive attack is likely structured so that indicators can be assigned to specific nodes and disruption points identified.

## When to use

- analyzing an adversary operational plan where timing, sequencing, and dependencies are analytically significant
- modeling a disinformation or influence campaign lifecycle to identify observable stages and disruption opportunities
- assessing whether a detected indicator belongs to an early or late phase of a suspected activity sequence
- communicating complex multi-step adversary activity to decision-makers or non-specialist audiences

## What it produces

- a sequenced, dependency-ordered decomposition of the activity with observable indicators at each node
- identification of critical-path nodes where delay or disruption would maximally affect the whole sequence
- choke points — resource-intensive or irreversible steps that, if detected, confirm significant commitment by the adversary
- a timeline that can be overlaid with collected intelligence to assess phase and remaining lead time

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map what is required by the activity's logic, not only what has been observed — gaps in the map are collection requirements
- distinguish irreversible steps (choke points that confirm commitment) from reversible preparatory steps
- every step must have at least one observable indicator — steps with no indicator are collection gaps, not confirmed blanks
