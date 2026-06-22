# Workflow — Code Security Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Scope and contextualize the review (read)
Read the code, configuration, and dependency manifests. Identify the trust boundaries: where does untrusted input enter the system? What assets (credentials, PII, privileged operations) does this code protect? If a threat model is provided, orient the review toward the most plausible attack vectors. Note the language, framework, and any security-relevant library choices.

## Step 2 — Run automated static analysis and dependency scans (exec)
Execute available static analysis tools (e.g., Bandit for Python, semgrep, CodeQL, cargo-audit) and dependency vulnerability scanners (e.g., pip-audit, npm audit, Dependabot). Collect all findings. Note that automated tools have both false-positive and false-negative rates; they are inputs to the review, not the review itself.

## Step 3 — Manual review: silent failures and unsafe fallbacks (reason)
Conduct a manual pass focused on the defect classes most dangerous and most frequently missed by automated tools: (1) silent failure — bare except clauses, swallowed exceptions, suppressed exit codes, 2>/dev/null patterns; (2) unsafe fallback — what happens when an auth check fails, a crypto operation errors, or a rate limit is exceeded? Does the code fail closed or fall back to permissive behavior? (3) error message leakage — do error paths reveal internal state, stack traces, or secrets to untrusted parties?

## Step 4 — Review security-critical code paths (reason)
Trace each trust boundary input through authentication, authorization, input validation, deserialization, and privilege transitions. Check: Is input validated before use? Are SQL/command/template injections possible? Are cryptographic operations using approved algorithms with proper key management? Are secrets hardcoded or logged? Are file paths traversal-safe? For AI/ML code, check whether model inputs are sanitized, whether model outputs are treated as trusted, and whether failure modes in inference propagate silently into decisions.

## Step 5 — Classify, rate, and consolidate findings (reason, write)
Consolidate automated and manual findings. For each, assess severity (CVSS-informed: critical / high / medium / low / informational), exploitability in the deployment context, and business/mission impact. Identify patterns: are silent failures concentrated in one module? Is unsafe fallback a systemic design problem? Formulate specific, actionable remediations for each finding.

## Step 6 — Produce findings table and security report (write)
Write the findings table with all rated defects. Write the security review narrative covering overall posture, most critical findings with reproduction-level detail, pattern analysis (especially silent failures and unsafe fallbacks), dependency risk summary, and a prioritized remediation roadmap. State explicitly what a reviewer must fix before deployment and what can be deferred to a follow-on sprint.

## Evidence requirements
- For Code Security Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Code Security Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Code Security Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Code Security Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Code Security Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Code Security Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Code Security Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Code Security Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Code Security Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Code Security Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Code Security Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Code Security Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Code Security Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Code Security Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Code Security Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Code Security Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Code Security Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not suppress stderr or swallow exit codes in any command executed during the review — doing so models the very unsafe pattern being audited
- Do not rate severity solely by whether an exploit is currently known — exploitability evolves; rate by worst-case impact in a plausible adversarial scenario
- Do not treat a green automated scan as a clean bill of security health — automated tools miss logic flaws, business-logic authorization errors, and all silent-failure patterns
- Do not recommend 'add a comment explaining the unsafe pattern' as a remediation — fix the underlying defect; comments do not close attack surfaces

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
