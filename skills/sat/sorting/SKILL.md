---
name: sat.sorting
description: Group large evidence sets by attributes to surface patterns and outliers.
---

# Sorting

Sorting is a structured-analytic technique that organizes a large evidence or indicator set by one or more attributes (date, source reliability, geographic origin, significance) so that meaningful clusters, trends, and outliers become visible. It converts an unordered mass of raw data into a structured view that supports pattern recognition and gap detection. In cognitive-security contexts, sorting exposes anomalies—items that do not fit the dominant cluster—which may represent deception artifacts, seeded disinformation, or signals of an adversary's hand.

## When to use

- the evidence base is large enough that key patterns are invisible without organization
- an analyst suspects clustering or grouping effects that unaided review would miss
- outlier detection is needed to surface potential deception or seeded disinformation
- preparation for a more intensive technique (e.g., ACH, indicators validation) requires a tidy input

## What it produces

- a multi-dimensional sorted view of all evidence items in a structured table
- cluster labels that name the dominant groupings in the evidence
- a flagged outlier list with analytic notes on why each item is anomalous

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- choose sort dimensions before sorting to avoid unconsciously post-hoc selecting dimensions that confirm the current hypothesis
- treat every outlier as analytically significant until explicitly ruled out
- record which dimension was primary so reviewers can re-sort on alternative axes
