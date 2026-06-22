# Workflow — Claim Provenance Verification

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — State the claim atomically (read, reason)
Strip framing and reduce the claim to one precise, falsifiable proposition with explicit scope. Preserve both the encountered wording and the atomic restatement.

## Step 2 — Anchor the point of encounter (read)
Record where the requester encountered the claim, including URL, outlet, date, author, and what that source cites.

## Step 3 — Trace citations upstream to the origin (search, web)
Follow each citation hop toward the earliest reachable primary source or a documented dead end, recording every hop in the chain.

## Step 4 — Detect circular reporting (reason)
Collapse the chain to distinct origins and flag cases where many reports repeat one unverified source rather than independently corroborating it.

## Step 5 — Assess the primary source directly (web, read, reason)
Inspect the origin for scope match, caveats, error bars, sample limits, or conditional language that may have been lost in retelling.

## Step 6 — Seek independent corroboration (search, web, reason)
Look for non-derivative sources such as a separate primary document, measurement, or witness. Do not count shared wire copy or press releases twice.

## Step 7 — Record the provenance chain (write)
Write the ordered chain from point of encounter back to origin, including links, timestamps, and chain-of-custody notes.

## Step 8 — Issue the verdict (reason, write)
Grade the claim, state confidence, and name the single weakest link most responsible for remaining uncertainty.

## Evidence requirements
- For Claim Provenance Verification, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Claim Provenance Verification, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Claim Provenance Verification recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Claim Provenance Verification: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Claim Provenance Verification: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Claim Provenance Verification: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Claim Provenance Verification cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Claim Provenance Verification should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Claim Provenance Verification, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Claim Provenance Verification, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Claim Provenance Verification, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Claim Provenance Verification failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Claim Provenance Verification failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Claim Provenance Verification failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Claim Provenance Verification to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Claim Provenance Verification into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Claim Provenance Verification to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- **Do not treat volume of repetition as corroboration.** N outlets citing one
- **Do not stop at a secondary source that merely cites another secondary.**
- **Do not collapse scope silently.** If the claim drifted from the primary
- **Do not count derivative sources as independent.** Shared wire copy, shared
- **Do not issue a verdict without naming the single weakest link.**

## AGEINT upstream
`docs/ageint/osint-integrity.md`
