---
name: sat.analytic_matrices
description: Cross-tabulate variables to organize evidence and reveal relationships.
---

# Analytic Matrices

Analytic Matrices organize analytic variables (hypotheses, actors, drivers, criteria) as rows and columns of a structured grid, then systematically populate each cell with evidence, ratings, or judgments. The technique makes the analyst's logic explicit and auditable, surfaces blank cells (missing evidence) and conflicting cells (contradictory evidence), and reduces the cognitive load of tracking multiple dimensions simultaneously. It is used in intelligence analysis as a pre-step to ACH, in option analysis, and in influence-operation assessment to map actors against capabilities and behaviors.

## When to use

- Multiple competing hypotheses, options, or actors must be systematically compared against the same evidence base or criteria
- The analyst needs to make implicit evidence-weighting explicit and auditable for peer review or management
- There is risk of selective attention — remembering only the evidence that fits the leading hypothesis
- A complex problem involves several interacting dimensions that are hard to hold in working memory simultaneously

## What it produces

- A structured grid making the analyst's reasoning transparent and independently reviewable
- An explicit map of evidential coverage showing where gaps and conflicts exist
- A pattern-level view of the problem that is harder to achieve through narrative alone
- A reusable artifact that can be updated as new evidence arrives without rewriting prose

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Choose axes so that the row-column intersection captures a meaningful, decidable relationship — not just a label intersection
- Blank cells are as analytically important as populated ones: they represent collection gaps or logical impossibilities that should be explained
- Conflicting cells (same position, contradictory evidence) must be flagged and adjudicated, not averaged away
- Rating schemes must be defined before filling the matrix; post-hoc scale adjustments introduce motivated reasoning
