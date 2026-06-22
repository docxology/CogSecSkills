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

## Evidence requirements
- For Information Provenance Tracing, bind each finding to a labeled source — content, behavioral, narrative, media, and audience-risk evidence, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Information Provenance Tracing, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Information Provenance Tracing recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Information Provenance Tracing: independent lines of content, behavioral, narrative, media, and audience-risk evidence converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Information Provenance Tracing: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Information Provenance Tracing: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Information Provenance Tracing cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Information Provenance Tracing should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Information Provenance Tracing, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Information Provenance Tracing, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Information Provenance Tracing, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Information Provenance Tracing failure: mistaking persuasive resonance for verified harm or intent.
- Information Provenance Tracing failure: producing guidance that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Provenance Tracing failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Information Provenance Tracing to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Information Provenance Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Information Provenance Tracing to assess supplied material for manipulation indicators and recommend resilience measures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat 'earliest found' as 'original' without noting that the true origin may predate accessible records — state 'earliest recoverable instance' explicitly
- Do not skip source authenticity assessment for the origin node — a fabricated account publishing first is still fabrication
- Do not conflate provenance tracing (origin and chain of custody) with fact-checking (truth of the claim) — a claim may be old, well-sourced, and still false
- Do not omit the mutation log — provenance without mutation tracking fails to capture how meaning degrades or inverts across republications

## AGEINT upstream
`docs/ageint/cognitive-security.md`
