---
name: information_environment.coordinated_inauthentic_behavior_detection
description: Detect coordination signatures across accounts, timing, and content reuse.
---

# Coordinated Inauthentic Behavior Detection

Coordinated Inauthentic Behavior (CIB) detection identifies groups of accounts that act in concert to manipulate public discourse while concealing the organized nature of their activity. Unlike single-account bot detection, CIB detection looks for temporal co-occurrence, content reuse, synchronized amplification, and network clustering patterns that reveal cross-account coordination even when individual accounts appear authentic in isolation. The technique operationalizes the Facebook-originated CIB framework and related academic methods to distinguish organic consensus from manufactured consensus.

## When to use

- Investigating whether a trending narrative or hashtag is being artificially inflated by a coordinated group
- Assessing whether apparent public support for a position reflects genuine opinion or organized amplification
- Auditing influence operations targeting elections, public health messaging, or conflict narratives
- Supporting platform trust-and-safety teams in network-level enforcement decisions
- Providing evidence for journalistic or policy investigations into information operations

## What it produces

- Clusters of accounts linked by co-activity, content reuse, or network topology signatures
- Estimated reach and amplification multiplier of the coordinated behavior
- Behavioral typology of the coordination (synchronized posting, relay amplification, narrative seeding, etc.)
- Confidence-rated assessment distinguishing genuine coordination from coincidental co-activity

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Coordination must be demonstrated across multiple independent dimensions — timing alone, or content reuse alone, is insufficient
- Inauthentic means the behavior misrepresents its organized nature, not that the viewpoint expressed is wrong
- Use temporal co-activity windows carefully: too narrow misses slow-rolling coordination, too wide captures organic convergence
- Always distinguish the coordination finding from any attribution claim about who orchestrates it — these require separate evidence chains
