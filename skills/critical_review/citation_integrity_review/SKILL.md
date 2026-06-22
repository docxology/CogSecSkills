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

- For Citation Integrity Review, tie every match verdict and severity rating to concrete evidence from the retrieved source passage and the exact in-text claim it is meant to support, and treat a citation whose source text could not be located or compared as unverified evidence rather than as accurate.
- For Citation Integrity Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the citation audit table.
- Before recommending any Citation Integrity Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Citation Integrity Review: each citation's existence verdict and accurate/partial/distorted/fabricated match assessment is corroborated by the retrieved source text itself, the severity ratings are stable when any single citation is rechecked against the original passage, and no unresolved contradiction would change the document's overall trustworthiness recommendation.
- Medium for Citation Integrity Review: the citation audit table is plausible, but one important document source, comparison case, or alternative explanation remains incomplete.
- Low for Citation Integrity Review: the citation audit table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Citation Integrity Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Citation Integrity Review, use only authorized document, and citation list, public or source-approved records, and caller-provided context needed for the defensive task.
- For Citation Integrity Review, minimize person-level detail in the citation audit table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Citation Integrity Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Citation Integrity Review: treating the audit as complete when a citation's existence was confirmed but its actual source text was never retrieved and compared against the in-text claim, so context stripping or source laundering survives a surface check and a real source is wrongly counted as supporting the point.
- Citation Integrity Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Citation Integrity Review: reporting the citation audit table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Citation Integrity Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the citation audit table from Citation Integrity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Citation Integrity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with document, and citation list' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Always check what the source actually states, not just whether it exists — a real source can be misquoted
- Distinguish four levels of citation failure: fabrication (source does not exist), distortion (source says the opposite or something different), selective quotation (source is accurate but stripped of qualifying context), and weak support (source is real and not distorted but does not specifically support this point)
- Context stripping is often more dangerous than fabrication because it survives surface-level verification — always read the surrounding passage
- Source laundering — citing a credible intermediary that itself misquotes the primary — requires tracing back to the primary source
