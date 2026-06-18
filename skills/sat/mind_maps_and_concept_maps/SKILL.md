---
name: sat.mind_maps_and_concept_maps
description: Externalize a problem's concepts and relationships as a navigable graph.
---

# Mind Maps & Concept Maps

Mind maps and concept maps externalize the structure of a complex problem as a navigable node-link graph, making implicit conceptual relationships visible and shareable. Mind maps radiate from a central topic in a hierarchical tree; concept maps allow labeled, directional links between any pair of nodes (following Novak's knowledge-representation theory). Both techniques combat working-memory overload, surface hidden assumptions, and expose gaps or tangled chains of reasoning that prose analysis obscures.

## When to use

- the problem involves many interacting concepts and verbal analysis keeps losing track of their relationships
- a team needs a shared, inspectable representation of how they understand a situation
- preparing for ACH or other hypothesis-generation techniques and wanting to inventory all relevant factors first
- detecting where an adversary's narrative is internally inconsistent or exploits a real knowledge gap in the audience

## What it produces

- a structured node-link graph with labeled directed relationships between all key concepts
- identification of orphan nodes (concepts not connected to the core topic) and missing links
- a checklist of conflicts or contradictions visible in the link structure

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- name links, not just draw them — unlabeled edges carry no analytic information
- use directed arrows to record WHO acts on WHOM or WHAT causes WHAT, not mere association
- distinguish 'is a', 'causes', 'depends on', and 'contradicts' as distinct link types
- after drafting, check every leaf node: if it has no outbound links, ask whether it is truly terminal or whether reasoning stopped prematurely
