---
name: critical_review.project_critical_review
description: >-
  Adversarial-then-constructive critical review of a project — codebase,
  research project, or initiative. Audits load-bearing claims against evidence,
  inventories risks and gaps, surfaces silent assumptions, verifies that the
  project's own gates have teeth, and delivers a calibrated go/no-go
  recommendation. Use before you ship, merge, fund, or publish — when being
  wrong is expensive and "it looks good" is not enough.
---

# Project Critical Review

This is the flagship critical-review skill. It takes a project and asks the only
question that matters before a high-stakes decision: **do the claims survive
contact with the evidence?** The review is deliberately two-faced. First it
attacks — for every load-bearing claim it hunts the strongest reason the claim
could be wrong, the evidence that is missing, and the failure modes that stay
silent. Then it builds — it names what is genuinely strong and the cheapest fix
for each top risk. The constructive pass never softens a real critical finding;
it only tells you what to do about it.

## When to use

- A decision is imminent — ship, merge, fund, publish, deprecate — and a wrong
  call is costly or hard to reverse.
- A project reports "all tests passing / everything works" and you need to know
  whether that claim has teeth.
- You inherited a codebase, manuscript, or initiative and must form an honest
  view of its risks and gaps fast.

**Not for** vague reassurance or a pat on the back, and not for line-by-line
code style review (that is a linter's job). This skill adjudicates whether the
project is *defensible*, not whether it is *tidy*.

## What it produces

1. A **project map** — purpose, load-bearing claims, architecture, deliverables.
2. An **adversarial findings table** — each risk/gap with severity, confidence,
   and **evidence bound to file:line or command output**.
3. A **strengths inventory** — what is genuinely solid and should be preserved.
4. A **verify-the-verifier result** — did the project's own gates actually catch
   an injected defect, or do they stay green regardless?
5. A **BLUF report** with a calibrated **go / no-go / go-with-conditions**
   recommendation and the **top three things to fix first**.

## Procedure

Run the seven-step loop in [`workflow.md`](workflow.md): scope → map →
adversarial pass → constructive pass → classify → verify-the-verifier →
deliver. The harness-specific tool bindings are in [`harness/`](harness/).

## Key discipline

- **Bind every finding to evidence.** A claimed defect with no file:line or no
  reproduced command output is a hypothesis, not a finding — label it as such or
  go get the evidence. No evidence, no assertion.
- **Verify-the-verifier.** A green test suite that stays green when you inject a
  defect proves nothing. Run the project's gates; inject one realistic defect;
  confirm a gate fails. An untested gate is a finding, not a safeguard.
- **Calibrate severity and confidence separately.** Severity is "how bad if
  true"; confidence is "how sure it is true." A high-severity / low-confidence
  finding is a *re-verify now* item, not a blocker — say so explicitly.
- **The constructive pass does not launder the critical pass.** Strengths are
  listed alongside, never on top of, critical findings. A go/no-go that buries
  a critical finding under praise is a failed review.
- **Distrust self-report.** "All passing" is a claim about a process; reproduce
  the process or downgrade the claim to unverified.
