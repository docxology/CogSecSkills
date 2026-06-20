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

## Failure modes
- Cross-Source Corroboration: treating candidate claim as complete when characterize the claim and current source set and trace origins and assess source independence checks or contradictory evidence are missing.
- Cross-Source Corroboration: producing advice that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Cross-Source Corroboration: reporting the corroboration assessment without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Cross-Source Corroboration outputs to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the corroboration assessment from Cross-Source Corroboration into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Cross-Source Corroboration to verify supplied claims, media, sources, or datasets with documented public-source methods with candidate claim, source list, and source metadata' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not treat multiple outlets reporting the same claim as independent corroboration if they can be traced to a single originating source
- Do not promote a claim simply because pressure, timing, or volume creates a sense of consensus — manufactured consensus is a standard influence operation technique
- Do not conflate corroboration of the existence of a report with corroboration of the underlying factual claim

## AGEINT upstream
`docs/ageint/osint-integrity.md`
