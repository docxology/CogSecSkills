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

## Procedure

See [`workflow.md`](workflow.md). Harness bindings in [`harness/`](harness/).

## Key discipline

- Silent failure is often more dangerous than visible failure — code that swallows exceptions or suppresses error signals converts security-relevant events into invisible no-ops; hunt these first
- Unsafe fallback: when a security control fails (auth check, crypto op, rate limit), the system must fail closed, not fall back to permissive behavior — verify every fallback path
- Input validation must be applied at trust boundaries, not assumed from upstream callers — trace data from the outermost input surface to each usage site
- Severity = exploitability × impact; a critical-severity unauthenticated remote code execution with no known exploit path is still critical
- Supply-chain risk is a first-class finding: a dependency with a known CVE, an unpinned dependency, or a dependency pulled from an untrusted registry is a security defect
