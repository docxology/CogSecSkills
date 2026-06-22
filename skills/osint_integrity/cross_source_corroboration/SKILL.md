---
name: osint_integrity.cross_source_corroboration
description: Require independent corroboration before promoting a claim to a finding.
---

# Cross-Source Corroboration

Cross-source corroboration is the practice of requiring independent confirmation from at least one additional source before elevating a claim from raw collection to an analytic finding. The technique recognizes that a single source — however credible — is insufficient because it may be fabricated, mistaken, or part of a coordinated deception campaign seeding the same narrative across multiple outlets. True corroboration demands source independence: two sources must not share a common origin, be controlled by the same actor, or derive their claim from the same original report. The technique is a primary defense against amplified misinformation and manufactured consensus.

## When to use

- Before any OSINT claim is promoted from raw collection to an analytic product or shared finding
- When a claim is spreading rapidly across social media, news, or analyst channels and speed is creating pressure to accept it
- When the original source of a claim cannot be independently verified or appears to have been recently created
- When the topic is one where coordinated information operations are known or suspected

## What it produces

- A corroboration tier for the claim: independently confirmed, single-source only, or contradicted
- An origin trace that identifies whether multiple reporting sources derive from a single original claim
- A documented promotion decision that can be reviewed and overturned if new corroborating sources emerge

## Defensive boundary

Use Cross-Source Corroboration only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

## Misuse redirect

If a request asks Cross-Source Corroboration to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Evidence discipline

- For Cross-Source Corroboration, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Cross-Source Corroboration, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Cross-Source Corroboration recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty

- High confidence for Cross-Source Corroboration: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Cross-Source Corroboration: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Cross-Source Corroboration: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Cross-Source Corroboration cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Cross-Source Corroboration should collect to separate the live alternatives.

## Privacy, legal, and harm constraints

- For Cross-Source Corroboration, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Cross-Source Corroboration, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Cross-Source Corroboration, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cross-Source Corroboration failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Cross-Source Corroboration failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Cross-Source Corroboration failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Cross-Source Corroboration to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cross-Source Corroboration into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cross-Source Corroboration to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Independence is defined by origin, not by number — ten outlets repeating one wire report is one source, not ten
- Trace each source's claim back to its original assertion; corroboration requires independent origination, not independent repetition
- Coordinated amplification (bot networks, state media ecosystems, astroturfing) is designed to defeat corroboration — look for identical phrasing, synchronized timing, and shared network infrastructure
- A hold decision is not a rejection — it is a documented waiting state pending additional independent evidence
