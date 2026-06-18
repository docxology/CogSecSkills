---
name: counterintelligence.analytic_process_hardening
description: Harden an analytic workflow against being gamed, anchored, or fed planted evidence.
---

# Analytic Process Hardening

Analytic process hardening audits an intelligence or research workflow to identify the specific points at which an adversary — or a manipulation campaign — could plant evidence, anchor judgments, seed false leads, or exploit cognitive biases to corrupt conclusions. Rooted in counterintelligence tradecraft and structured analytic technique discipline, it maps each workflow node to its manipulation surface, then prescribes procedural controls that reduce exploitability without requiring analysts to become suspicious of all sources. The output is an action-ready hardening plan with prioritized controls.

## When to use

- a high-stakes analytic workflow will inform a major decision and manipulation by an adversary is a credible threat
- a prior assessment was later found to have relied on planted or manipulated evidence
- a workflow aggregates information from sources with adversarial access or that operate in contested information environments
- an organization is designing a new analytic process and wants manipulation-resistance built in from the start

## What it produces

- a node-by-node map of manipulation surfaces in the workflow with associated detection difficulty ratings
- a prioritized set of procedural controls targeting the highest-risk nodes first
- an explicit residual-risk statement so decision-makers know what cannot be fully mitigated

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- map attack surfaces structurally — ask 'what would a sophisticated deceiver do at this node?' not 'do we trust our sources?'
- controls must be proportionate — hardening every node equally creates analyst fatigue and degrades legitimate throughput; prioritize by adversary capability × consequence of manipulation
- independence of review is the strongest single control: a reviewer who processed different sources and was not present during drafting catches the most
