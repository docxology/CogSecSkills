# Workflow — Ethics & Harms Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Ingest and scope (read)
Read the artifact, its stated purpose, deployment context, and any prior ethics documentation. Extract the capability boundaries: what can the artifact do at maximum capability and what happens when it is misused or combined with other tools?

## Step 2 — Multi-framework harm identification (reason)
Apply at least two ethical frameworks systematically. Consequentialist pass: list plausible harm scenarios, estimate likelihood (rare/possible/likely) and severity (minor/moderate/severe/catastrophic) for each affected party including third parties and society. Deontological pass: identify rights violations, consent failures, or duties breached. Rights-based pass: flag protected-characteristic impacts. Cross-reference discipline-specific codes (Menlo, Belmont, or relevant professional code).

## Step 3 — Dual-use and misuse path analysis (reason)
For each high-likelihood or high-severity harm, trace the misuse path: who would do it, what capability or access is required, what barriers exist, and whether the artifact meaningfully lowers those barriers relative to existing alternatives. Differentiate meaningful uplift from marginal uplift.

## Step 4 — Mitigation design and residual-risk assessment (reason, write)
For each material harm, propose specific, enforceable mitigations (access controls, disclosure requirements, watermarking, staged release, use-case restrictions). Assess residual risk after mitigations. Flag harms that cannot be adequately mitigated for escalation.

## Step 5 — Produce harm register and recommendation (write)
Compile the structured harm register table. Write the ethics assessment narrative covering framework analysis, dual-use findings, and consent/transparency gaps. Issue a go/no-go recommendation with explicit conditions (e.g., 'release with access controls and responsible-disclosure policy; re-review if capability is extended to X').

## Anti-criteria (must NOT happen)
- do not produce a harm register that lists only harms to direct users — third-party and societal harms are typically the most serious and must be enumerated
- do not conflate a low-probability harm with a negligible harm — catastrophic low-probability risks require explicit treatment
- do not issue a blanket go recommendation without stating specific mitigation conditions
- do not treat 'others are already doing this' as an ethical justification — marginal uplift still requires assessment

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
