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

## Failure modes and negative controls

- Code Security Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Code Security Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Code Security Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.
- Unsafe: 'Use Code Security Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Code Security Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Code Security Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Silent failure is often more dangerous than visible failure — code that swallows exceptions or suppresses error signals converts security-relevant events into invisible no-ops; hunt these first
- Unsafe fallback: when a security control fails (auth check, crypto op, rate limit), the system must fail closed, not fall back to permissive behavior — verify every fallback path
- Input validation must be applied at trust boundaries, not assumed from upstream callers — trace data from the outermost input surface to each usage site
- Severity = exploitability × impact; a critical-severity unauthenticated remote code execution with no known exploit path is still critical
- Supply-chain risk is a first-class finding: a dependency with a known CVE, an unpinned dependency, or a dependency pulled from an untrusted registry is a security defect
