# Codex adapter — Rumor & Virality Assessment

Binds the neutral `skill.yaml` tool verbs to Codex tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Codex tool | Notes |
| --- | --- | --- |
| `read` | `shell` (`cat`, `rg`) | Read supplied files or stdin. |
| `reason` | private model reasoning | Apply the technique with concise rationale. |
| `search` | `shell` + optional web | Search the workspace or the web if available. |
| `write` | `apply_patch` / stdout | Persist the product or return Markdown. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence.

## Output contract

Return the `skill.yaml` outputs (virality_assessment, factor_table) as Markdown, with a calibrated confidence statement. Keep the product defensive and accountable.
