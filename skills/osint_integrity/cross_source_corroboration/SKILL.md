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

- For Cross-Source Corroboration, tie each corroboration assessment, and promotion decision claim to concrete evidence from the specific candidate claim, source list, and source metadata item, source excerpt, observation, or command result that supports it.
- For Cross-Source Corroboration, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the corroboration assessment.
- Before recommending any Cross-Source Corroboration action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Cross-Source Corroboration: the corroboration assessment is supported by multiple independent source records, custody notes, metadata, corroborating references, and contradiction logs; characterize the claim and current source set and trace origins and assess source independence checks agree, and no unresolved contradiction would change the result.
- Medium for Cross-Source Corroboration: the corroboration assessment is plausible, but one important candidate claim source, comparison case, or alternative explanation remains incomplete.
- Low for Cross-Source Corroboration: the corroboration assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Cross-Source Corroboration cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Cross-Source Corroboration, use only authorized candidate claim, source list, and source metadata, public or source-approved records, and caller-provided context needed for the defensive task.
- For Cross-Source Corroboration, minimize person-level detail in the corroboration assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Cross-Source Corroboration, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Cross-Source Corroboration: treating candidate claim as complete when characterize the claim and current source set and trace origins and assess source independence checks or contradictory evidence are missing.
- Cross-Source Corroboration: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Cross-Source Corroboration: reporting the corroboration assessment without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Cross-Source Corroboration outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the corroboration assessment from Cross-Source Corroboration into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cross-Source Corroboration to verify supplied claims, media, sources, or datasets with documented public-source methods with candidate claim, source list, and source metadata' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Independence is defined by origin, not by number — ten outlets repeating one wire report is one source, not ten
- Trace each source's claim back to its original assertion; corroboration requires independent origination, not independent repetition
- Coordinated amplification (bot networks, state media ecosystems, astroturfing) is designed to defeat corroboration — look for identical phrasing, synchronized timing, and shared network infrastructure
- A hold decision is not a rejection — it is a documented waiting state pending additional independent evidence
