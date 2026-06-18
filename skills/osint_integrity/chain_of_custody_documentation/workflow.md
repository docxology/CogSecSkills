# Workflow — Chain-of-Custody Documentation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory evidence items (read)
List every artifact to be documented — files, screenshots, archived pages, raw URLs. Record the original collection timestamp, source URL, and the identity of the collector for each item.

## Step 2 — Compute and record hashes (exec)
Generate a SHA-256 (or SHA-3) hash of each file or archived page at the point of collection or at the earliest available moment. Log the hash alongside the timestamp in the custody table. For web captures, archive to a persistent store first.

## Step 3 — Identify gaps and anomalies (reason)
Review the chain for missing handling events, undocumented transfers, or time gaps where tampering could have occurred. Flag any item where the hash cannot be verified against the original collection moment.

## Step 4 — Produce custody log and integrity summary (write)
Write the structured custody table and a narrative summary that acknowledges gaps, explains their cause, and recommends remediation steps (re-collection, additional archiving, or explicit uncertainty disclosure).

## Anti-criteria (must NOT happen)
- Do not backfill hashes after files have been processed, converted, or shared — only original-capture hashes have integrity value
- Do not omit transfer events on the assumption they are routine — every hand-off is a potential integrity break
- Do not declare custody complete when there are undocumented time gaps; acknowledge gaps explicitly in the integrity summary

## AGEINT upstream
`docs/ageint/osint-integrity.md`
