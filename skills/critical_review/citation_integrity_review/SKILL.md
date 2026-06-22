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

## Defensive boundary

Use Citation Integrity Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Citation Integrity Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Citation Integrity Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Citation Integrity Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Citation Integrity Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Citation Integrity Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Citation Integrity Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Citation Integrity Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Citation Integrity Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Citation Integrity Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Citation Integrity Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Citation Integrity Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Citation Integrity Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Citation Integrity Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Citation Integrity Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Citation Integrity Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Citation Integrity Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Citation Integrity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Citation Integrity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Always check what the source actually states, not just whether it exists — a real source can be misquoted
- Distinguish four levels of citation failure: fabrication (source does not exist), distortion (source says the opposite or something different), selective quotation (source is accurate but stripped of qualifying context), and weak support (source is real and not distorted but does not specifically support this point)
- Context stripping is often more dangerous than fabrication because it survives surface-level verification — always read the surrounding passage
- Source laundering — citing a credible intermediary that itself misquotes the primary — requires tracing back to the primary source
