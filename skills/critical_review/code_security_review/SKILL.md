---
name: critical_review.code_security_review
description: Review code for security defects, silent failures, and unsafe fallback behavior.
---

# Code Security Review

Code Security Review is a structured audit of source code for security defects, silent failure modes, unsafe fallback behavior, and patterns that can be exploited by adversaries. Grounded in secure-code review methodology (OWASP, NIST SSDF), it examines authentication, authorization, input validation, error handling, secrets management, dependency risk, and supply-chain integrity. In cognitive-security contexts, code review extends to detecting logic that silently degrades or manipulates AI-system behavior, suppresses failure signals, or creates covert channels for adversarial influence.

## When to use

- Before deploying code that handles authentication, authorization, sensitive data, or external inputs
- When reviewing a pull request or code change that touches security-sensitive paths (auth, crypto, network, file I/O, deserialization)
- When a codebase includes AI/ML components where adversarial inputs or silent model failures could propagate into decisions
- When auditing third-party dependencies or supply-chain components for known vulnerabilities or suspicious behavior
- When investigating an incident or near-miss and tracing whether silent failure modes or unsafe fallbacks contributed
- When reviewing code that suppresses errors (bare except, 2>/dev/null, swallowed exceptions) that could mask security-relevant failures

## What it produces

- A severity-rated inventory of security defects in the reviewed code
- Identification of silent failure modes — code paths where errors are swallowed without alerting the system or operator
- Unsafe fallback pattern detection — cases where an error or unexpected condition causes the system to fall back to a less secure or unauthenticated state
- Dependency risk summary with known CVEs and supply-chain concerns
- A prioritized remediation roadmap ordered by exploitability and impact

## Defensive boundary

Use Code Security Review only for critical review and assurance: recognize, assess, document, or defend evidence quality, implementation integrity, and decision accountability. Do not use this skill to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.

## Misuse redirect

If a request asks Code Security Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation, refuse that path and redirect to the safe defensive form: review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures.

## Evidence discipline

- For Code Security Review, bind every finding to concrete evidence — a specific file-and-line excerpt, a dependency manifest entry, or captured scanner or static-analysis command output — and name the trust boundary and adversary action that would turn that evidence into an exploit, never suppressing stderr or exit codes while gathering it.
- For Code Security Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the findings table.
- Before recommending any Code Security Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty

- High for Code Security Review: each finding in the table is pinned to a specific file and line and corroborated by both manual tracing and automated scanner output, the severity and exploitability ratings hold when the trust-boundary path is re-traced, and no unresolved contradiction about a silent-failure or unsafe-fallback path would change the deployment recommendation.
- Medium for Code Security Review: the findings table is plausible, but one important code source, comparison case, or alternative explanation remains incomplete.
- Low for Code Security Review: the findings table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Code Security Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints

- For Code Security Review, use only authorized code, threat model, and review scope, public or source-approved records, and caller-provided context needed for the defensive task.
- For Code Security Review, minimize person-level detail in the findings table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Code Security Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes and negative controls

- Code Security Review: treating a green automated scan as a clean bill of health when the manual pass for silent failures, unsafe fallbacks, and trust-boundary input validation was never performed, so swallowed exceptions and fail-open fallback paths that no tool detects propagate into a deployed system as invisible attack surface.
- Code Security Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Code Security Review: reporting the findings table without uncertainty labels, alternative explanations, and the next discriminating check.
- Unsafe: 'Use Code Security Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the findings table from Code Security Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Code Security Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with code, threat model, and review scope' -> produce bounded findings with evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Silent failure is often more dangerous than visible failure — code that swallows exceptions or suppresses error signals converts security-relevant events into invisible no-ops; hunt these first
- Unsafe fallback: when a security control fails (auth check, crypto op, rate limit), the system must fail closed, not fall back to permissive behavior — verify every fallback path
- Input validation must be applied at trust boundaries, not assumed from upstream callers — trace data from the outermost input surface to each usage site
- Severity = exploitability × impact; a critical-severity unauthenticated remote code execution with no known exploit path is still critical
- Supply-chain risk is a first-class finding: a dependency with a known CVE, an unpinned dependency, or a dependency pulled from an untrusted registry is a security defect
