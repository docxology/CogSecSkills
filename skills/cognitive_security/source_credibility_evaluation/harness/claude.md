# Harness Adapter — Claude Code

Adapter mapping the neutral workflow verbs to Claude Code tools for the
Source Credibility Evaluation skill.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| read | Read | Read the source material, claim text, and corroborating documents. |
| search | Grep / WebSearch | Grep local evidence; WebSearch for independent corroboration and track record. |
| reason | (model) | Internal weighing of proximity, motive, independence, and corroboration. |
| write | Write | Emit the A–F / 1–6 grade pair and the usage bound. |

## Invocation

Invoke from Claude Code with the source identity and the specific claim. Read
the supplied material and any corroboration, run WebSearch for independent
confirmation where allowed, reason through the two axes, then Write the result.

## Output contract

- `reliability_grade`: letter A–F with justification.
- `credibility_grade`: number 1–6 with justification.
- `usage_bound`: how the combined grade (e.g. `B2`) bounds downstream use.
- Reliability and credibility are reported as a pair; A1 only with independent
  confirmation.
