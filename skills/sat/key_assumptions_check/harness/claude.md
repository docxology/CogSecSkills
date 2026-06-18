# Claude Code adapter — Key Assumptions Check

Binds the neutral `skill.yaml` tool verbs to Claude Code tools. Invoke this
skill by following `../workflow.md`; use the mappings below for each step.

| Neutral verb | Claude Code tool(s) | Notes |
|--------------|---------------------|-------|
| `read`   | `Read`, `Grep`      | Read the supplied judgment, analytic line, and cited evidence. |
| `reason` | model reasoning (extended thinking) | Surface unstated assumptions, run the three-question interrogation, classify, and apply the collapse test. |
| `write`  | `Write`, message output | Emit the assumptions table + key-assumption flags + revised judgment. |

`WebSearch`/`Agent` (Explore) are optional aids while reasoning about contrary
conditions, but the core procedure needs only read/reason/write.

## Invocation

This is authored as a Claude Code skill: `SKILL.md` frontmatter (`name`,
`description`) is the activation surface. When the user's request matches a
trigger in `skill.yaml`, run the six-step workflow, rendering the assumptions
inventory as a GitHub-flavored Markdown table.

## Output contract
- A Markdown assumptions table: one row per assumption with columns
  *assumption · stated/unstated · rationale · contrary conditions · confidence
  class · load-bearing?*.
- A `Key assumptions` section, each with its collapse analysis and the
  collection that would test it.
- A `Revised judgment` block stating the conclusion together with the
  assumptions it depends on.
