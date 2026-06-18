# Codex adapter — Key Assumptions Check

Binds the neutral `skill.yaml` tool verbs to a Codex / `codex exec` agent's
tool surface. Follow `../workflow.md`; map each step's verb as below.

| Neutral verb | Codex binding | Notes |
|--------------|---------------|-------|
| `read`   | `shell` (`cat`, `sed`, `rg`) on provided files | The judgment and analytic line are passed as files or stdin. |
| `reason` | private model reasoning | Surface unstated assumptions, interrogate each, classify, run collapse test. |
| `write`  | `apply_patch` / stdout | Write the assumptions table, key flags, and revised judgment to an output file or stdout. |

## Invocation
Provide this file plus `../workflow.md` and `../skill.yaml` in the task context.
Codex runs the six steps non-interactively and writes the Key Assumptions Check
product to the path given by the caller (default: stdout as Markdown).

## Output contract
Identical to the neutral spec: assumptions table (assumption · stated/unstated ·
rationale · contrary conditions · confidence class · load-bearing?), the key
assumptions with collapse analysis and the collection that would test each, and
a revised judgment that exposes its dependence on the key assumptions.
Deterministic given the same inputs.
