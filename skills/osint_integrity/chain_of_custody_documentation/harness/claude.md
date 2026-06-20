# Claude Code adapter — Chain-of-Custody Documentation

Binds the neutral `skill.yaml` tool verbs to Claude Code tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Claude Code tool | Notes |
| --- | --- | --- |
| `read` | `Read` / `Grep` | Read supplied material and locate local evidence. |
| `exec` | `Bash` | Run commands or the project's own gates. |
| `write` | `Write` / final response | Emit the structured product. |
| `reason` | private model reasoning | Apply the technique; expose concise rationale. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. Enforce the defensive boundary: Use Chain-of-Custody Documentation only for OSINT integrity and source-verification defense: recognize, assess, document, or defend source provenance, privacy, chain of custody, and public-source accountability. Do not use this skill to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence. If the caller asks for prohibited manipulation, deception, targeting, evasion, or operational influence guidance, apply this redirect: If a request asks Chain-of-Custody Documentation to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence, refuse that path and redirect to the safe defensive form: verify supplied claims, media, sources, or datasets with documented public-source methods.

## Output contract

Return the `skill.yaml` outputs (custody_log, integrity_summary) as Markdown, with a calibrated confidence statement, evidence labels, uncertainty notes, and any relevant privacy/legal constraints. Keep the product defensive and accountable.
