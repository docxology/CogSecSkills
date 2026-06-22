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
- For Claim Provenance Verification, tie every hop in the chain and the final verdict to concrete evidence — a dated URL, an outlet citation, or a primary-source excerpt showing its actual scope — and name the single weakest link, because a chain resting on uncorroborated repetition is a hypothesis, not a verified claim.
- For Claim Provenance Verification, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the provenance chain.
- Before recommending any Claim Provenance Verification action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Claim Provenance Verification: the provenance chain traces the atomic claim back to a reachable primary source whose scope genuinely supports it, at least one non-derivative source corroborates it independently of that origin, the chain is free of circular reporting, and no unresolved weak link would overturn the verdict.
- Medium for Claim Provenance Verification: the provenance chain is plausible, but one important claim source, comparison case, or alternative explanation remains incomplete.
- Low for Claim Provenance Verification: the provenance chain rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Claim Provenance Verification cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating osint_integrity evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Claim Provenance Verification, use only authorized claim, and starting sources, public or source-approved records, and caller-provided context needed for the defensive task.
- For Claim Provenance Verification, minimize person-level detail in the provenance chain; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Claim Provenance Verification, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Claim Provenance Verification: declaring a claim verified when repetition across many outlets was mistaken for corroboration, when tracing stopped at a secondary source that merely cited another secondary, or when scope drift from the primary source was never examined, so apparent confirmation reflects an incomplete trace rather than independent support.
- Claim Provenance Verification: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Claim Provenance Verification: reporting the provenance chain without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Claim Provenance Verification outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the provenance chain from Claim Provenance Verification into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Claim Provenance Verification to verify supplied claims, media, sources, or datasets with documented public-source methods with claim, and starting sources' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- **Do not treat volume of repetition as corroboration.** N outlets citing one
- **Do not stop at a secondary source that merely cites another secondary.**
- **Do not collapse scope silently.** If the claim drifted from the primary
- **Do not count derivative sources as independent.** Shared wire copy, shared
- **Do not issue a verdict without naming the single weakest link.**

## AGEINT upstream
`docs/ageint/osint-integrity.md`
