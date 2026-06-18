---
name: osint_integrity.chain_of_custody_documentation
description: Document collection, handling, and hashing so evidence integrity is auditable.
---

# Chain-of-Custody Documentation

Chain-of-custody documentation records every step in the collection, transfer, and analysis of OSINT evidence — capturing who handled each item, when, by what method, and what cryptographic hashes confirm it remained unaltered. The technique adapts law-enforcement chain-of-custody principles to open-source intelligence so that findings can withstand legal, journalistic, or organizational scrutiny. Without it, adversaries and skeptics can challenge whether evidence was fabricated, tampered, or misidentified. A complete chain anchors findings in verifiable, time-stamped, hash-confirmed records.

## When to use

- Before sharing OSINT findings with legal, journalistic, or institutional decision-makers who may face adversarial challenge
- When evidence could be subpoenaed or used in formal proceedings
- After collecting from volatile sources (social media, live websites) where content may disappear or be altered
- When multiple analysts or teams handle the same artifacts across time

## What it produces

- A row-per-artifact custody table with hash, timestamps, collector identity, and tool used
- A completeness assessment flagging any gaps where handling is undocumented
- A hash manifest that allows third-party verification that files have not been altered since collection

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Hash at the moment of collection — post-hoc hashing only proves integrity from that later moment, not from capture
- Each transfer event (person A to person B, local to cloud storage) must be logged as its own row
- Volatile web content must be archived to a persistent store (Wayback Machine, local WARC) before any hash is considered meaningful
- A gap in custody is not automatically disqualifying but must be explicitly acknowledged and explained
