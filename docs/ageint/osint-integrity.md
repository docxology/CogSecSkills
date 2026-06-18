# OSINT Integrity

OSINT integrity is the discipline of collecting and using open-source information with rigorous provenance, verification, and chain-of-custody so that what an analyst believes is true can be traced back to trustworthy, independent sources.

## Why it matters for cognitive security

Open-source intelligence is powerful precisely because it is abundant — and abundance is the adversary's cover. Fabricated images, recycled old footage, and seeded "sources" are designed to launder false claims into credible-looking evidence. Integrity discipline is the firewall that keeps a defensive analyst from amplifying an adversary's plant or being misled by an information cascade.

## Core concepts

- **The verification mindset** — Bellingcat / First Draft's core questions for any artifact: *provenance* (is this the original?), *source* (who captured it?), *date* (when?), and *location* (where? — geolocation and chronolocation).
- **Source vs. claim verification** — separating the credibility of a *source* from the verification of a specific *claim*; one credible source does not verify an unsupported assertion.
- **Circular reporting** — detecting when multiple "independent" sources actually trace to a single origin, creating false corroboration.
- **Chain of custody** — preserving the path from original artifact to analytic product (archived originals, hashes, timestamps) so provenance is auditable and tamper-evident.
- **Tradecraft tools** — reverse image search, EXIF/metadata analysis, shadow and weather cross-referencing, and archival capture (e.g., the Wayback Machine, archive.today) to fix ephemeral evidence.
- **Documentation discipline** — recording collection method, time, and access conditions for reproducibility.

## How CogSecSkills operationalizes this

Skills in this group encode verification as repeatable agentic steps: capturing and hashing source artifacts, running structured provenance/source/date/location checks, and flagging likely circular-reporting chains. Each emits a verification record tied to the underlying evidence, so claims arrive with their custody trail attached.

## Defensive & ethical framing

Collection is restricted to genuinely open, lawfully accessible information; no intrusion, deception, or privacy violation. Skills prioritize accuracy and source protection, operate under human oversight, and respect platform terms and applicable law.

## Further study

- AGEINT curriculum — github.com/docxology/AGEINT, concept DOI 10.5281/zenodo.20732274.
- *The Verification Handbook* (ed. Craig Silverman, European Journalism Centre).
- Bellingcat's online investigation toolkit and First Draft's verification guides.
