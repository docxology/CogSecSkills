# Harness Adapter — Codex

Adapter mapping the neutral workflow verbs to Codex tools for the
Source Credibility Evaluation skill.

| Neutral verb | Codex tool | Notes |
| --- | --- | --- |
| read | shell (cat/rg) | Read the source material, claim text, and corroborating files. |
| search | shell + web | rg over local evidence; web for independent corroboration and track record. |
| reason | (model) | Internal weighing of proximity, motive, independence, and corroboration. |
| write | apply_patch | Write the A–F / 1–6 grade pair and the usage bound to disk. |

## Invocation

Run under Codex with the source identity and the specific claim. Use shell to
read the material and any corroboration, use web to find independent
confirmation, reason through the two axes, then apply_patch to record the result.

## Output contract

- `reliability_grade`: letter A–F with justification.
- `credibility_grade`: number 1–6 with justification.
- `usage_bound`: how the combined grade (e.g. `B2`) bounds downstream use.
- Reliability and credibility are reported as a pair; A1 only with independent
  confirmation.
