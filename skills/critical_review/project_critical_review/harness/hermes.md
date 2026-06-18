# Hermes adapter — Project Critical Review

Binds the neutral `skill.yaml` tool verbs to a Hermes-style tool-calling agent
(JSON function-calling loop). Follow `../workflow.md`. The `exec` binding is
required for the verify-the-verifier step (Step 6); if no shell is bound, the
review must downgrade every "passing" gate to **unverified**.

| Neutral verb | Hermes tool (function call) | Notes |
|--------------|-----------------------------|-------|
| `read`   | `fs.read` / context payload | Read code, manuscript, configs, tests; record file:line. |
| `search` | `web.search` / `kb.query` / `fs.grep` | Find load-bearing claims and gates; surface missing evidence. |
| `exec`   | `shell` / `exec` function | Run the project's gate, inject one defect, re-run to prove it fails, then revert. |
| `reason` | private model reasoning | Adversarial + constructive passes; report concise severity × confidence rationale. |
| `write`  | `fs.write` or final message | Emit the BLUF report + findings table. |

## Invocation
Register the seven workflow steps as the system/developer instruction. Hermes
emits one tool call per step where a tool is needed and reasons inline for
`reason` steps. For Step 6 it calls the `shell` / `exec` function to run the
real gate and to inject + revert a defect. If no shell is bound, Hermes proceeds
on read-only evidence and explicitly marks every gate-based claim as
**unverified** rather than passing — it never fabricates a gate run.

## Output contract
Same as the neutral spec: a BLUF paragraph, a **GO / NO-GO /
GO-WITH-CONDITIONS** recommendation, the top 3 fixes, a Markdown findings table
(severity, confidence, evidence, remedy), a strengths list, and the
verify-the-verifier result. When `fs.write` is available, write
`critical_review.md`; otherwise return the product in the final assistant message.
