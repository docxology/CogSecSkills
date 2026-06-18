---
name: sat.cross_impact_matrix
description: Assess how each driver influences every other to find leverage and feedback.
---

# Cross-Impact Matrix

The Cross-Impact Matrix is a structured technique for mapping how each driver, trend, or variable in a system affects every other one, enabling analysts to identify reinforcing feedback loops, inhibitory relationships, and high-leverage nodes whose change cascades through the system. Cells in the matrix record the direction and magnitude of influence (positive, negative, neutral, conditional) rather than independent assessments of each factor. The technique is widely used in scenario planning, strategic foresight, and systemic-threat analysis to surface non-obvious interdependencies that single-variable analysis misses.

## When to use

- preparing for scenario development where key drivers need to be understood as a system rather than independently
- assessing the systemic consequences of an adversary's action on multiple domains simultaneously
- prioritizing intervention points when resources are constrained — the high-leverage node deserves the most attention
- checking whether a single-driver analysis has missed critical feedback effects

## What it produces

- a filled N×N influence matrix making all pairwise driver relationships explicit and comparable
- an inventory of feedback loops — reinforcing loops that amplify change and balancing loops that dampen it
- a leverage ranking distinguishing active drivers (high outgoing influence) from passive indicators (high incoming influence)
- analytic narrative tying the structural findings to the focal analytic or planning question

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- assess each cell (i→j) independently before looking at the full matrix — premature holistic framing biases individual cells
- distinguish direction (positive/negative) from magnitude — a strong negative relationship is as important as a strong positive one
- row sums reveal active drivers; column sums reveal sensitive/dependent variables — both matter for intervention design
