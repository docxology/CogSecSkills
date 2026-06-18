# Workflow — Information Provenance Tracing

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Define and fingerprint the artifact (read)
State the claim precisely. For text: identify the key invariant phrase(s) to use as search strings. For images/video: note distinctive visual features, metadata, or hashes. Record the artifact as first encountered (date, platform, account/outlet).

## Step 2 — Search backward through the chain (search, web)
Query databases (news archives, social media search, Google Cache, archive.org Wayback Machine, reverse image/video tools such as TinEye, Google Images, or InVID-WeVerify) for earlier instances. Work from the currently-known instance toward earlier dates. Record each discovered instance with its date, source, platform, and URL.

## Step 3 — Assess source authenticity and type (reason)
For the earliest-found instances, assess: Is the account/outlet real, established, and consistent with its claimed identity? Is the claimed primary source (study, official, witness) verifiable? Check domain registration dates (WHOIS), account creation dates, and cross-references to other reliable sources. Flag anonymous, newly-created, or suspicious source accounts.

## Step 4 — Map mutations across the chain (reason)
Compare each link's version of the claim to adjacent links. Note where: key qualifications were dropped, attributions changed (e.g., 'anonymous source' became 'official'), statistics were misquoted, context was stripped (decontextualization), or the meaning of authentic content inverted. Classify each mutation: corruption, decontextualization, or framing shift.

## Step 5 — Emit provenance chain and origin assessment (write)
Produce the provenance table (earliest to latest) with source type ratings and mutation notes. Write a narrative identifying the earliest verifiable or probable origin, summarizing the mutation history, and stating a confidence-rated origin verdict. Where origin is ambiguous, enumerate the most plausible hypotheses and the evidence for each.

## Anti-criteria (must NOT happen)
- Do not treat 'earliest found' as 'original' without noting that the true origin may predate accessible records — state 'earliest recoverable instance' explicitly
- Do not skip source authenticity assessment for the origin node — a fabricated account publishing first is still fabrication
- Do not conflate provenance tracing (origin and chain of custody) with fact-checking (truth of the claim) — a claim may be old, well-sourced, and still false
- Do not omit the mutation log — provenance without mutation tracking fails to capture how meaning degrades or inverts across republications

## AGEINT upstream
`docs/ageint/cognitive-security.md`
