# Codex adapter — Project Critical Review

Binds the neutral `skill.yaml` tool verbs to a Codex / `codex exec` agent's
tool surface. Follow `../workflow.md`; map each step's verb as below. The
`exec` binding carries the verify-the-verifier step (Step 6): Codex must run the
project's gates, not merely read about them.

| Neutral verb | Codex binding | Notes |
|--------------|---------------|-------|
| `read`   | `shell` (`cat`, `sed`, `rg`) on the repo | Read code, manuscript, configs, tests; capture file:line. |
| `search` | `shell` (`rg`, `grep`) + (optional) web tool | Find load-bearing claims and gates; locate or fail to locate evidence. |
| `exec`   | `shell` (run test/gate command) | Execute the suite, inject one defect via `apply_patch`, re-run to prove a gate fails, then revert. |
| `reason` | private model reasoning | Adversarial + constructive passes; severity × confidence calibration. |
| `write`  | `apply_patch` / stdout | Write the BLUF report + findings table to a file or stdout. |

## Invocation
Provide this file plus `../workflow.md` and `../skill.yaml` in the task context,
along with the artifact path. Codex runs the seven steps non-interactively. For
Step 6 it runs the project's real gate via `shell`, applies a one-line defect
with `apply_patch`, confirms the gate fails, and reverts the patch — a gate that
stays green is reported as a critical finding.

## Output contract
Identical to the neutral spec: a BLUF paragraph, a **GO / NO-GO /
GO-WITH-CONDITIONS** recommendation, the top 3 fixes, a Markdown findings table
(severity, confidence, evidence file:line / command, remedy), a strengths list,
and the verify-the-verifier result. Deterministic given the same inputs.
