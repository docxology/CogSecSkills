# Hermes adapter — Analysis of Competing Hypotheses

Binds the neutral `skill.yaml` tool verbs to a Hermes-style tool-calling agent
(JSON function-calling loop). Follow `../workflow.md`.

| Neutral verb | Hermes tool (function call) | Notes |
|--------------|-----------------------------|-------|
| `read`   | `fs.read` / context payload | Evidence supplied in the prompt or via a read tool. |
| `search` | `web.search` / `kb.query`   | Optional; degrade gracefully if unavailable. |
| `reason` | private model reasoning | Build/score the matrix and report concise rationale. |
| `write`  | `fs.write` or final message | Emit Markdown matrix + ranking. |

## Invocation
Register the eight workflow steps as the system/developer instruction. Hermes
emits one tool call per step where a tool is needed, and reasons inline for
`reason` steps. If no tools are bound, Hermes runs the entire procedure in-context
from the supplied evidence (single-turn fallback).

## Output contract
Same as the neutral spec. When `fs.write` is available, write
`ach_matrix.md`; otherwise return the product in the final assistant message.
