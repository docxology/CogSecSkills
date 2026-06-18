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

## Anti-criteria (must NOT happen)
- Do not treat multiple outlets reporting the same claim as independent corroboration if they can be traced to a single originating source
- Do not promote a claim simply because pressure, timing, or volume creates a sense of consensus — manufactured consensus is a standard influence operation technique
- Do not conflate corroboration of the existence of a report with corroboration of the underlying factual claim

## AGEINT upstream
`docs/ageint/osint-integrity.md`
