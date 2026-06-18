---
name: sat.morphological_analysis
description: Enumerate the parameter space of a problem to bound the set of possibilities.
---

# Morphological Analysis

Morphological analysis (Zwicky 1969; Ritchey 2011) decomposes a complex problem into its independent parameters, enumerates the discrete values each parameter can take, and maps the full cross-product to bound the space of possible configurations. In intelligence and cognitive-security contexts it prevents premature closure on a single scenario by forcing analysts to articulate every combination that remains logically consistent with current evidence, including surprising or low-salience possibilities.

## When to use

- an analysis is at risk of anchoring on the most familiar or most recent scenario while ignoring equally plausible alternatives
- a threat space has multiple independent axes (actor identity, method, target, timing) and all combinations need to be surfaced before prioritization
- collection requirements need to be written to discriminate among specific configurations in the parameter space
- a cognitive-security audit needs to catalogue the distinct narrative architectures an influence operation could adopt

## What it produces

- a complete enumeration of logically possible scenarios bounded by the chosen parameters
- explicit identification of which combinations are ruled out by known constraints and why
- a scenario inventory tagged by current evidential support, enabling targeted collection to close gaps

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- parameters must be genuinely independent — if two dimensions co-vary mechanically, collapse them into one
- enumerate value sets exhaustively before pruning — premature pruning re-introduces the closure the technique is designed to prevent
- record the reason for every pruned cell; a cell removed for the wrong reason is where the surprise will come from
- the most-dangerous scenario and the most-likely scenario are often different cells — report both
