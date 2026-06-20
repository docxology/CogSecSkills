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
- For Information Provenance Tracing, tie each provenance chain, and origin assessment claim to concrete evidence from the specific artifact, known context, and scope item, source excerpt, observation, or command result that supports it.
- For Information Provenance Tracing, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the provenance chain.
- Before recommending any Information Provenance Tracing action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Information Provenance Tracing: the provenance chain is supported by multiple independent content, behavioral, narrative, media, and audience-risk evidence; define and fingerprint the artifact and search backward through the chain checks agree, and no unresolved contradiction would change the result.
- Medium for Information Provenance Tracing: the provenance chain is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Information Provenance Tracing: the provenance chain rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Information Provenance Tracing cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Information Provenance Tracing, use only authorized artifact, known context, and scope, public or source-approved records, and caller-provided context needed for the defensive task.
- For Information Provenance Tracing, minimize person-level detail in the provenance chain; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Information Provenance Tracing, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Information Provenance Tracing: treating artifact as complete when define and fingerprint the artifact and search backward through the chain checks or contradictory evidence are missing.
- Information Provenance Tracing: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Information Provenance Tracing: reporting the provenance chain without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Information Provenance Tracing outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the provenance chain from Information Provenance Tracing into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Information Provenance Tracing to assess supplied material for manipulation indicators and recommend resilience measures with artifact, known context, and scope' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat 'earliest found' as 'original' without noting that the true origin may predate accessible records — state 'earliest recoverable instance' explicitly
- Do not skip source authenticity assessment for the origin node — a fabricated account publishing first is still fabrication
- Do not conflate provenance tracing (origin and chain of custody) with fact-checking (truth of the claim) — a claim may be old, well-sourced, and still false
- Do not omit the mutation log — provenance without mutation tracking fails to capture how meaning degrades or inverts across republications

## AGEINT upstream
`docs/ageint/cognitive-security.md`
