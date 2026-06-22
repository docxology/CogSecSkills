# Workflow — Cross-Source Corroboration

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the claim and current source set (read)
State the claim precisely. List all sources asserting it, with publication timestamps and outlet identities. Identify the earliest known instance of the claim in the public record.

## Step 2 — Trace origins and assess source independence (search, reason)
For each source, attempt to identify where that outlet obtained the claim — wire service, official statement, social media post, prior report. Map the dependency graph. Flag sources that share a common origin as a single corroboration unit, not independent confirmations. Search for sources that emerged independently of the identified chain.

## Step 3 — Assess corroboration quality and detect amplification (reason)
Determine whether any genuinely independent sources (different origin, different network, different time) confirm the claim. Check for coordinated amplification signals: near-simultaneous posting, identical phrasing across outlets, or accounts/outlets created near the time of the claim. Assign a corroboration tier: confirmed (2+ independent origins), single-source, or contradicted.

## Step 4 — Document assessment and promotion decision (write)
Write the corroboration assessment table and the promotion decision with tier, rationale, confidence level, and — if held — the specific evidence that would warrant promotion. Record conditions under which the hold should be revisited.

## Evidence requirements
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

## Failure modes
- Cross-Source Corroboration failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Cross-Source Corroboration failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Cross-Source Corroboration failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Cross-Source Corroboration to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Cross-Source Corroboration into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Cross-Source Corroboration to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat multiple outlets reporting the same claim as independent corroboration if they can be traced to a single originating source
- Do not promote a claim simply because pressure, timing, or volume creates a sense of consensus — manufactured consensus is a standard influence operation technique
- Do not conflate corroboration of the existence of a report with corroboration of the underlying factual claim

## AGEINT upstream
`docs/ageint/osint-integrity.md`
