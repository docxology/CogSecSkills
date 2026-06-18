# Claude Code adapter — Analysis of Competing Hypotheses

Binds the neutral `skill.yaml` tool verbs to Claude Code tools. Invoke this
skill by following `../workflow.md`; use the mappings below for each step.

| Neutral verb | Claude Code tool(s) | Notes |
|--------------|---------------------|-------|
| `read`   | `Read`, `Grep`      | Read supplied evidence files / pasted material. |
| `search` | `WebSearch`, `Grep`, `Agent` (Explore) | Gather more evidence / surface missing hypotheses. |
| `reason` | model reasoning (extended thinking) | Build and score the matrix; do the sensitivity pass. |
| `write`  | `Write`, message output | Emit the matrix as a Markdown table + ranking. |

## Invocation

This is authored as a Claude Code skill: `SKILL.md` frontmatter (`name`,
`description`) is the activation surface. When the user's request matches a
trigger in `skill.yaml`, run the eight-step workflow, rendering the matrix as a
GitHub-flavored Markdown table.

## Output contract
- A Markdown matrix table: rows = evidence, columns = hypotheses, cells = C/I/N.
- A ranked list with inconsistency scores.
- An `Indicators` section and a one-line calibrated confidence judgment.
