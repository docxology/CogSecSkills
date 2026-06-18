---
name: critical_review.citation_integrity_review
description: Verify citations exist, say what they're claimed to say, and support the cited point.
---

# Citation Integrity Review

Citation Integrity Review is a systematic audit that verifies each citation in a document actually exists, that the cited source says what the author claims it says, and that the source genuinely supports the specific point being made at that location. In cognitive-security contexts, citation misrepresentation — whether through fabrication, selective quotation, context stripping, or source laundering — is a primary mechanism for lending false authority to disinformation or manipulated narratives; this review defends against that attack surface.

## When to use

- When a document's conclusions rest heavily on cited authorities and those citations have not been independently verified
- When reviewing material from an unfamiliar or potentially adversarial source that uses extensive references to establish credibility
- When a cited claim seems inconsistent with broader domain knowledge, suggesting possible misquotation or context stripping
- When conducting due diligence on a research product, policy brief, or intelligence report before acting on its conclusions
- When investigating a suspected disinformation product that relies on 'source laundering' — citing real sources inaccurately to borrow their credibility

## What it produces

- A per-citation verdict: exists / does not exist, says what is claimed / does not, supports the specific point / does not
- A severity classification for each citation problem: fabricated (most severe), distorted, partial, accurate
- An overall integrity rating for the document and a pattern analysis of how citations are misused
- A recommendation on whether the document can be used as a reliable source

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Always check what the source actually states, not just whether it exists — a real source can be misquoted
- Distinguish four levels of citation failure: fabrication (source does not exist), distortion (source says the opposite or something different), selective quotation (source is accurate but stripped of qualifying context), and weak support (source is real and not distorted but does not specifically support this point)
- Context stripping is often more dangerous than fabrication because it survives surface-level verification — always read the surrounding passage
- Source laundering — citing a credible intermediary that itself misquotes the primary — requires tracing back to the primary source
