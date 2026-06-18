---
name: osint_integrity.metadata_integrity_check
description: Use and sanity-check file/post metadata while accounting for stripping and spoofing.
---

# Metadata Integrity Check

Metadata integrity check extracts and critically evaluates embedded file and post metadata — EXIF, XMP, IPTC, platform timestamps, author fields, device identifiers — while explicitly accounting for the fact that metadata can be stripped, altered, or spoofed. The technique treats metadata as a corroborating signal rather than ground truth: consistent metadata raises confidence, but inconsistent or absent metadata must be explained before any evidential use. It is routinely applied in OSINT, legal discovery, and journalism verification workflows.

## When to use

- a file or image is submitted as evidence and its origin, date, or authorship needs verification
- a document is suspected of having been altered or back-dated
- forensic chain-of-custody requirements mandate metadata provenance documentation
- metadata has been stripped or is absent and the reason for absence must be assessed
- platform-assigned metadata (tweet timestamp, upload date) needs cross-referencing against embedded file metadata

## What it produces

- a field-by-field breakdown of all recoverable metadata with source (embedded vs. platform-assigned)
- an internal consistency check: do date, GPS, device model, software version, and author fields cohere?
- an external consistency check: does the metadata match the claimed provenance?
- a spoofing and stripping risk assessment for each key field
- an overall integrity verdict: consistent, inconsistent, or insufficient data

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- metadata absence is informative — platform stripping on upload is routine, but deliberate pre-upload stripping is a manipulation signal; explain why fields are missing
- cross-check multiple independent fields: a spoofed GPS coordinate rarely matches an authentic device model firmware timestamp
- platform-assigned timestamps are more tamper-resistant than embedded EXIF but are still imperfect — both must be examined
- internal consistency across metadata fields is evidence of authenticity; any single field in isolation is insufficient
