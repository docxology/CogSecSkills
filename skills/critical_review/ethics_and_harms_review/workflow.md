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
- For Ethics & Harms Review, tie each harm scenario, mitigation, and residual-risk rating to concrete evidence from the artifact's capability boundaries, stated intended use, and deployment context, and treat a claimed mitigation as effective only when the evidence shows it is enforceable rather than aspirational.
- For Ethics & Harms Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the harm register.
- Before recommending any Ethics & Harms Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Ethics & Harms Review: each scenario in the harm register names a concrete affected party with likelihood and severity grounded in the artifact and its deployment context, at least two incommensurable ethical frameworks converge on the assessment, and no unresolved contradiction about a dual-use misuse path would change the go/no-go recommendation.
- Medium for Ethics & Harms Review: the harm register is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Ethics & Harms Review: the harm register rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Ethics & Harms Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Ethics & Harms Review, use only authorized artifact, intended use, and deployment context, public or source-approved records, and caller-provided context needed for the defensive task.
- For Ethics & Harms Review, minimize person-level detail in the harm register; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Ethics & Harms Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Ethics & Harms Review: issuing a go recommendation when the harm register enumerated only harms to direct users and the dual-use misuse paths to third parties and society were never traced, so diffuse low-probability high-severity risks and meaningful capability uplift to adversaries are silently omitted from the assessment.
- Ethics & Harms Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Ethics & Harms Review: reporting the harm register without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Ethics & Harms Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the harm register from Ethics & Harms Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Ethics & Harms Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, intended use, and deployment context' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not produce a harm register that lists only harms to direct users — third-party and societal harms are typically the most serious and must be enumerated
- do not conflate a low-probability harm with a negligible harm — catastrophic low-probability risks require explicit treatment
- do not issue a blanket go recommendation without stating specific mitigation conditions
- do not treat 'others are already doing this' as an ethical justification — marginal uplift still requires assessment

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
