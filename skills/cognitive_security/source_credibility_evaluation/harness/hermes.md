# Harness Adapter — Hermes

Adapter mapping the neutral workflow verbs to Hermes tools for the
Source Credibility Evaluation skill.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| read | fs.read | Read the source material, claim text, and corroborating documents. |
| search | web.search | Find independent corroboration and the source's track record. |
| reason | (model) | Internal weighing of proximity, motive, independence, and corroboration. |
| write | fs.write | Emit the A–F / 1–6 grade pair and the usage bound. |

## Invocation

Call the Hermes skill runner with the source identity and the specific claim.
Use fs.read for the material and any corroboration, web.search for independent
confirmation, reason through the two axes, then fs.write the result.

## Output contract

- `reliability_grade`: letter A–F with justification.
- `credibility_grade`: number 1–6 with justification.
- `usage_bound`: how the combined grade (e.g. `B2`) bounds downstream use.
- Reliability and credibility are reported as a pair; A1 only with independent
  confirmation.
