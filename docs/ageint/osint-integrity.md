# OSINT Integrity

OSINT integrity is the discipline of collecting and using open-source information with rigorous provenance, verification, and chain-of-custody so that what an analyst believes is true can be traced back to trustworthy, independent sources. It is the difference between *finding* information and *standing behind* it: an integrity-disciplined finding arrives with its origin, its handling history, and its weakest link already documented, ready to survive an adversarial challenge.

This primer covers the `osint_integrity` group of CogSecSkills — ten skills that turn that discipline into repeatable, auditable steps.

## Contents

- [Why it matters for cognitive security](#why-it-matters-for-cognitive-security)
- [The verification lifecycle](#the-verification-lifecycle)
- [Core concepts](#core-concepts)
- [The skills in this group](#the-skills-in-this-group)
- [How CogSecSkills operationalizes integrity](#how-cogsecskills-operationalizes-integrity)
- [Worked example: a viral video](#worked-example-a-viral-video)
- [Privacy, ethics, and the defensive boundary](#privacy-ethics-and-the-defensive-boundary)
- [Further study](#further-study)

## Why it matters for cognitive security

Open-source intelligence is powerful precisely because it is abundant — and abundance is the adversary's cover. Fabricated images, recycled old footage, and seeded "sources" are designed to launder false claims into credible-looking evidence. A single uncorroborated post, re-shared by a hundred accounts and quoted by three outlets, can manufacture the *appearance* of consensus while resting on nothing. Integrity discipline is the firewall that keeps a defensive analyst from amplifying an adversary's plant or being misled by an information cascade.

The threat model here is specific. Adversaries do not only forge artifacts; they exploit the *structure* of how analysts reason — anchoring a judgment on whoever speaks first, manufacturing false corroboration through circular reporting, and collapsing real media into a false context. Each skill in this group counters a distinct one of those moves, which is why they compose into a layered defense rather than a single check.

## The verification lifecycle

Integrity is not one test applied once. It is a lifecycle, and the skills in this group map onto its stages:

1. **Plan** — decide what is in scope, what is lawful and proportionate, and how data will be protected, *before* collecting (`collection_plan_design`).
2. **Vet the source** — assess identity, access, track record, and motive at intake, before any claim is treated as evidence (`source_vetting`, `sock_puppet_detection`).
3. **Trace the claim** — follow a claim upstream to its primary origin and detect circular reporting (`claim_provenance_verification`).
4. **Examine the artifact** — triage media for reuse and editing, and verify embedded signals (`image_and_media_forensics_triage`, `metadata_integrity_check`, `geolocation_verification`).
5. **Corroborate** — require an independent second origin before promoting a claim to a finding (`cross_source_corroboration`).
6. **Audit inputs** — when a dataset rather than a single item is the input, gate it for origin, licensing, and integrity (`dataset_provenance_audit`).
7. **Preserve custody** — hash and log every artifact and handling step so the chain is tamper-evident (`chain_of_custody_documentation`).

A claim that has passed every stage carries its provenance chain, its corroboration tier, and its custody log with it — which is exactly what lets a finding withstand scrutiny.

## Core concepts

- **The verification mindset** — the core questions for any artifact, drawn from the Bellingcat / First Draft tradition: *provenance* (is this the original?), *source* (who captured it?), *date* (when?), and *location* (where? — geolocation and chronolocation). These four questions are the spine of `image_and_media_forensics_triage` and `geolocation_verification`.
- **Source vs. claim verification** — separating the credibility of a *source* from the verification of a specific *claim*. One credible source does not verify an unsupported assertion, and a low-credibility source can still report a true fact. `source_vetting` rates the source; `claim_provenance_verification` and `cross_source_corroboration` test the claim.
- **Circular reporting** — detecting when multiple "independent" sources actually trace to a single origin, creating false corroboration. Counting outlets is not corroboration; tracing origins is.
- **Source independence** — genuine corroboration requires that two sources do *not* share a common origin, are not controlled by the same actor, and did not derive their claim from the same original report. This is the load-bearing distinction inside `cross_source_corroboration`.
- **Chain of custody** — preserving the path from original artifact to analytic product (archived originals, cryptographic hashes, timestamps, named handlers) so provenance is auditable and tamper-evident. An undocumented handling step is recorded as an explicit *gap*, never papered over as verified custody.
- **Metadata as corroboration, not ground truth** — EXIF, XMP, IPTC, and platform timestamps can be stripped, altered, or spoofed. Consistent metadata raises confidence; inconsistent or absent metadata must be *explained* before any evidential use — the discipline of `metadata_integrity_check`.
- **Context collapse** — real media presented as if it depicts a different event, place, or time. The artifact is authentic; the *claim about it* is false. Triage and geolocation exist largely to catch this.
- **Evidence binding and the weakest link** — every rating, hop, and red flag is tied to a concrete piece of evidence (a dated URL, a registration record, a computed hash, a reverse-image hit), and the single weakest link is named explicitly, so a verdict is never stronger than the chain that supports it.

## The skills in this group

Each skill lives under `skills/osint_integrity/<name>/` and emits a structured, evidence-bound record rather than a bare yes/no.

| Skill | What it does | Headline output |
| --- | --- | --- |
| [`collection_plan_design`](../../skills/osint_integrity/collection_plan_design/) | Turns an intelligence requirement into a scoped, lawful, proportionate collection plan *before* gathering data | An upstream governance document: scope, lawful methods, storage/protection rules, review checkpoints |
| [`source_vetting`](../../skills/osint_integrity/source_vetting/) | Assesses a source's identity, access, track record, and motive at intake | A reliability rating (NATO-style identity × credibility), a motive map, and evidence-linked red flags |
| [`sock_puppet_detection`](../../skills/osint_integrity/sock_puppet_detection/) | Flags inauthentic personas via converging behavioral, temporal, network, and content signals | A coordinated-inauthenticity assessment based on multiple converging indicators, not a single signature |
| [`claim_provenance_verification`](../../skills/osint_integrity/claim_provenance_verification/) | Traces a public claim upstream to its primary source and detects circular reporting | A provenance chain, a circular-reporting assessment, and a graded verdict with the weakest link named |
| [`cross_source_corroboration`](../../skills/osint_integrity/cross_source_corroboration/) | Requires an independent second origin before a claim becomes a finding | A corroboration tier (independently confirmed / single-source / contradicted) and a reviewable promotion decision |
| [`image_and_media_forensics_triage`](../../skills/osint_integrity/image_and_media_forensics_triage/) | Rapidly screens media for reuse, editing, and context collapse | A reuse verdict, editing red flags, a context-collapse assessment, and accept / escalate / reject disposition |
| [`metadata_integrity_check`](../../skills/osint_integrity/metadata_integrity_check/) | Extracts and critically evaluates EXIF/XMP/IPTC and platform metadata, accounting for spoofing | A metadata consistency assessment that treats metadata as a corroborating signal, not ground truth |
| [`geolocation_verification`](../../skills/osint_integrity/geolocation_verification/) | Cross-references terrain, architecture, shadows, and signage against authoritative maps | An independently verifiable anchor for where (and, via sun angle, when) a visual was plausibly captured |
| [`dataset_provenance_audit`](../../skills/osint_integrity/dataset_provenance_audit/) | Audits a dataset's origin, methodology, licensing, sampling frame, and integrity | A due-diligence gate verdict on whether a dataset can be trusted and lawfully used as an analytic input |
| [`chain_of_custody_documentation`](../../skills/osint_integrity/chain_of_custody_documentation/) | Logs collection, transfer, and hashing so evidence integrity is auditable | A per-artifact custody table, a completeness assessment with explicit gaps, and a re-verifiable hash manifest |

## How CogSecSkills operationalizes integrity

Skills in this group encode verification as repeatable agentic steps: capturing and hashing source artifacts, running structured provenance / source / date / location checks, tracing claims to their origin, and flagging likely circular-reporting chains. Three design commitments run through all ten:

- **Every output is evidence-bound.** A reliability score, a provenance hop, or a forensic red flag must be tied to a concrete artifact — a dated URL, a credential confirmation, a computed hash, a reverse-image hit. A rating asserted without such evidence is labeled an assumption, not a verified assessment.
- **Observations are kept separate from inferences.** Each skill labels observations, derived features, assumptions, inferences, contradictions, and missing inputs *before* writing its conclusion, so a reader can see exactly where fact ends and judgment begins.
- **The weakest link is always named.** Before recommending any action, a skill identifies the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check — so a verdict openly carries its own most plausible refutation.

Because each skill emits a verification record tied to the underlying evidence, claims arrive at the analytic product with their custody trail attached, and any downstream reviewer can re-walk the chain.

## Worked example: a viral video

A clip is circulating that purportedly shows a current event, shared with high volume and strong emotional valence. An integrity-disciplined pass composes several skills in this group:

1. **Triage the media** (`image_and_media_forensics_triage`) — reverse-image search returns an earlier upload from an unrelated event two years prior. That single hit reframes everything: the artifact is likely authentic but *context-collapsed*.
2. **Check metadata** (`metadata_integrity_check`) — platform re-encoding has stripped the original EXIF, so timestamps cannot be treated as ground truth; their absence is recorded and explained rather than ignored.
3. **Verify location** (`geolocation_verification`) — architecture and signage in the frame match the *original* location, not the one now claimed, corroborating the reuse finding with an independent anchor.
4. **Trace the claim** (`claim_provenance_verification`) — the outlets repeating the claim all cite one anonymous account, i.e., circular reporting converging on a single unverified origin.
5. **Attempt corroboration** (`cross_source_corroboration`) — no genuinely independent origin exists, so the claim is *held*, not promoted to a finding.
6. **Preserve custody** (`chain_of_custody_documentation`) — the original upload, the reverse-image hits, and the geolocation references are archived and hashed so the assessment can be re-verified later.

The verdict is not "fake" in the abstract; it is a documented chain showing real media, a false context, a single unverified origin, and a named weakest link — exactly the form that survives challenge.

## Privacy, ethics, and the defensive boundary

This group is strictly defensive and accountable. Collection is restricted to genuinely open, lawfully accessible information; no intrusion, deception, access-control bypass, or privacy violation. Every skill carries the same explicit boundary and the same redirect:

> Use these skills only for OSINT integrity and source-verification defense — to recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do **not** use them to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.

If a request bends toward any of those misuses, the skill refuses that path and redirects to the safe defensive form: verify the supplied claims, media, sources, or datasets with documented public-source methods. Two principles make this concrete in practice:

- **Proportionality and minimization start before collection.** `collection_plan_design` is the upstream governance gate: it bounds scope, requires lawful and proportionate methods, and specifies how collected material is stored and protected — preventing scope creep and reducing legal and ethical exposure.
- **Attribution never outruns evidence.** `sock_puppet_detection` assesses *whether* a persona shows coordinated inauthentic behavior; it does not unmask the human behind it. Identity claims are bound to evidence and stop where the evidence stops.

Throughout, skills prioritize accuracy and source protection, operate under human oversight, and respect platform terms and applicable law.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- *The Verification Handbook* (ed. Craig Silverman, European Journalism Centre) — the standard reference for the provenance / source / date / location mindset.
- Bellingcat's online investigation toolkit and First Draft's verification guides — practical tradecraft for reverse-image search, geolocation, and archival capture.
- The skills themselves: read any `skills/osint_integrity/<name>/SKILL.md` for that skill's *When to use*, *What it produces*, *Defensive boundary*, and *Evidence discipline* sections, and the adjacent `workflow.md` for its repeatable steps.
