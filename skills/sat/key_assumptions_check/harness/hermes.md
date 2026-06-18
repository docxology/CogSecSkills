# Hermes adapter — Key Assumptions Check

Binds the neutral `skill.yaml` tool verbs to a Hermes-style tool-calling agent
(JSON function-calling loop). Follow `../workflow.md`.

| Neutral verb | Hermes tool (function call) | Notes |
|--------------|-----------------------------|-------|
| `read`   | `fs.read` / context payload | The judgment and analytic line are supplied in the prompt or via a read tool. |
| `reason` | private model reasoning | Surface unstated assumptions, interrogate each, classify, and report concise rationale. |
| `write`  | `fs.write` or final message | Emit the Markdown assumptions table + key flags + revised judgment. |

`web.search` / `kb.query` are optional aids for reasoning about contrary
conditions; degrade gracefully if unavailable.

## Invocation
Register the six workflow steps as the system/developer instruction. Hermes emits
one `fs.read`/`fs.write` tool call where a tool is needed and reasons inline for
the `reason` steps. If no tools are bound, Hermes runs the entire procedure
in-context from the supplied judgment and analytic line (single-turn fallback).

## Output contract
Same as the neutral spec. When `fs.write` is available, write
`key_assumptions_check.md` containing the assumptions table, the key assumptions
with collapse analysis and testing collection, and the revised judgment;
otherwise return the product in the final assistant message.
