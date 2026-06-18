# Workflow — Project Critical Review

Harness-neutral agentic procedure. Each step names the **tool verb(s)** it uses
(see `skill.yaml` → `tools`). A harness adapter binds each verb to concrete
tools; the logic here is identical across harnesses. The spine is
**adversarial first, constructive second, evidence always**.

## Step 1 — Scope the review (read, reason)
Pin down three things before reading anything else:
- **Artifact** — what exactly is under review (repo root, manuscript, subsystem).
- **Decision** — what call this review informs (ship / merge / fund / publish).
  The decision sets the bar: a research-preview bar is not a production bar.
- **Success criteria** — what "good enough" means for *this* decision. If the
  caller did not supply them, infer them, state them explicitly, and proceed.
Out-of-scope must be named too, so the review cannot be blamed for missing it.

## Step 2 — MAP the project (read, search)
Build a factual map with no judgement yet:
- **Purpose** — what problem it claims to solve.
- **Load-bearing claims** — the handful of assertions the project's value rests
  on ("X is correct", "Y is fast", "Z is secure", "all gates pass"). List them.
- **Architecture & deliverables** — the real components, entry points, outputs,
  and where the tests/gates live. Record file paths now; you will cite them later.

## Step 3 — ADVERSARIAL pass (reason, search, read)
For **each load-bearing claim**, attack it on four axes. Bind every hit to
evidence (file:line, config value, or command output):
- **Strongest reason it's wrong** — the most credible failure of the claim, not
  a strawman.
- **Missing evidence** — what would have to be true for the claim to hold, and
  whether that evidence actually exists in the repo. Absence is a finding.
- **Silent-failure risk** — code/paths that swallow errors, fall back quietly,
  or pass when they should fail (`except: pass`, `|| true`, `2>/dev/null`,
  vacuous/empty-scan gates, green-by-construction tests).
- **Dual-use / misuse risk** — how a correct-looking capability could be turned
  to harm or be abused, and whether anything constrains it.
Record each as a candidate finding with a draft severity and a draft confidence.

## Step 4 — CONSTRUCTIVE pass (reason)
Now switch stance. For the same project:
- **Genuine strengths** — what is actually solid and must be preserved (do not
  invent these; a thin project gets a short list).
- **Cheapest fix per top risk** — for each high/critical finding, the smallest
  change that retires or de-risks it. Prefer fixes that add teeth (a failing
  test, a fail-closed guard) over fixes that only add prose.
The constructive pass produces remedies; it must not rewrite or soften any
finding's severity.

## Step 5 — Classify findings (reason)
Assign every finding a **severity** and a **confidence** using the rubric below.
Keep them independent — a finding can be critical-severity / low-confidence.

**Severity**
- **Critical** — blocks the decision; failure causes data loss, security breach,
  invalid headline result, or a false "it works" claim shipping.
- **High** — likely to cause real harm or rework; not an automatic blocker but
  must be addressed before the decision or explicitly accepted in writing.
- **Medium** — real defect/gap with bounded blast radius; schedule a fix.
- **Low** — minor, cosmetic, or stylistic; note and move on.

**Confidence**
- **High** — reproduced; evidence is direct (failing run, file:line proof).
- **Medium** — strong inference from evidence, not yet reproduced.
- **Low** — plausible hypothesis; flag as *needs verification*, never as fact.

## Step 6 — Verify-the-verifier (exec, read)
Do not trust "all passing." **Run the project's own tests/gates** and confirm
they have teeth:
- Execute the suite / gate and capture the real output (not the README's claim).
- **Inject one realistic defect** into a load-bearing path (flip a constant,
  break an assertion's target, corrupt one input) and re-run — a real gate must
  now **fail**. If it stays green, the gate is vacuous: that is itself a
  **critical** finding. Revert the injection.
- Note any gate that is skipped, tolerated, or reports `skipped`/empty-scan as
  "clean" — those are unverified, not passing.

## Step 7 — Deliver the BLUF report (write)
Lead with the bottom line. Emit, in order:
1. **BLUF** — one paragraph: the recommendation and why, up front.
2. **Recommendation** — **GO / NO-GO / GO-WITH-CONDITIONS**, calibrated, with
   the conditions made explicit if conditional.
3. **Top 3 to fix first** — ranked, each with its cheapest fix.
4. **Findings table** — severity, confidence, evidence (file:line / command),
   and remedy for each.
5. **Strengths** — what to preserve.
6. **Verify-the-verifier result** — did the injected defect get caught?
7. **Scope & success criteria** — what was and was not reviewed.

## Severity / confidence rubric (quick reference)

| Axis | Levels | Meaning |
|------|--------|---------|
| Severity | Critical / High / Medium / Low | how bad if the finding is true |
| Confidence | High / Med / Low | how sure the finding is true (evidence strength) |

Report `Severity × Confidence` per finding. Critical/High findings drive the
recommendation; Low/Medium inform the fix backlog.

## Anti-criteria (must NOT happen)
- Vague "looks good" / "seems solid" praise with no evidence behind it.
- Asserting a defect without binding it to file:line or reproduced output.
- Letting the constructive pass soften, merge away, or bury a critical finding.
- Trusting a self-reported "all passing" without running the gate yourself.
- Reporting a gate as a safeguard without checking it fails on an injected defect.
- Conflating severity with confidence (e.g. downgrading a critical risk just
  because it is not yet reproduced — re-verify it instead).

## AGEINT upstream
`docs/ageint/` → adversarial-assurance (claims-vs-evidence audit, verify-the-
verifier, calibrated go/no-go). This skill is the project-level instantiation of
that family.
