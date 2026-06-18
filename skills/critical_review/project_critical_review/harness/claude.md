# Claude Code adapter — Project Critical Review

Binds the neutral `skill.yaml` tool verbs to Claude Code tools. Invoke this
skill by following `../workflow.md`; use the mappings below for each step. The
`exec` binding is load-bearing — the verify-the-verifier step (Step 6) requires
actually running the project's gates.

| Neutral verb | Claude Code tool(s) | Notes |
|--------------|---------------------|-------|
| `read`   | `Read`, `Grep`      | Read code, manuscript, configs, and test files; record file:line for citations. |
| `search` | `Grep`, `WebSearch`, `Agent` (Explore) | Locate load-bearing claims, gates, and the evidence (or its absence). |
| `exec`   | `Bash`              | Run the project's test suite / gates; inject one defect and re-run to prove the gate fails; revert. |
| `reason` | model reasoning (extended thinking) | Run the adversarial and constructive passes; calibrate severity × confidence. |
| `write`  | `Write`, message output | Emit the BLUF report, findings table, and go/no-go recommendation. |

## Invocation

Authored as a Claude Code skill: `SKILL.md` frontmatter (`name`, `description`)
is the activation surface. When the user's request matches a trigger in
`skill.yaml` (e.g. "critical review", "go/no-go", "red team this project"), run
the seven-step workflow. For Step 6, run the real gate with `Bash` (e.g. the
project's `pytest`/`make test`/CI command), capture genuine output, inject one
realistic defect, confirm a gate fails, then revert — never report a gate as a
safeguard without this check.

## Output contract
- A **BLUF** paragraph leading the report, then a **GO / NO-GO /
  GO-WITH-CONDITIONS** recommendation and the **top 3 fixes first**.
- A GitHub-flavored Markdown **findings table**: severity, confidence,
  evidence (file:line or command output), remedy.
- A **strengths** list and a **verify-the-verifier** result (did the injected
  defect get caught?), plus the scope/success-criteria the review used.
