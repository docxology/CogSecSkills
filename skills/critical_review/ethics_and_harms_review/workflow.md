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

## Evidence requirements
- For Ethics & Harms Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Ethics & Harms Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Ethics & Harms Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Ethics & Harms Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Ethics & Harms Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Ethics & Harms Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Ethics & Harms Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Ethics & Harms Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Ethics & Harms Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Ethics & Harms Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Ethics & Harms Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Ethics & Harms Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Ethics & Harms Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Ethics & Harms Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Ethics & Harms Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Ethics & Harms Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Ethics & Harms Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not produce a harm register that lists only harms to direct users — third-party and societal harms are typically the most serious and must be enumerated
- do not conflate a low-probability harm with a negligible harm — catastrophic low-probability risks require explicit treatment
- do not issue a blanket go recommendation without stating specific mitigation conditions
- do not treat 'others are already doing this' as an ethical justification — marginal uplift still requires assessment

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
