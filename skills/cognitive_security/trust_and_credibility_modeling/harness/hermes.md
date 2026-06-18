# Hermes adapter — Trust & Credibility Modeling

Binds the neutral `skill.yaml` tool verbs to Hermes tools. Follow `../workflow.md`; the logic is identical across harnesses.

| Neutral verb | Hermes tool | Notes |
| --- | --- | --- |
| `read` | `fs.read` / context payload | Read supplied files or prompt payload. |
| `reason` | chain-of-thought | Reason through the steps in-turn. |
| `search` | `web.search` / `kb.query` | Query the web or a knowledge base. |
| `write` | `fs.write` / final message | Write the product or return it. |

## Invocation

Run the workflow steps in order with the caller's context as the source of truth. If a required tool is unavailable, state the limitation and downgrade the tool-dependent claim to unverified rather than fabricating evidence.

## Output contract

Return the `skill.yaml` outputs (trust_model, exploitation_vulnerability_audit) as Markdown, with a calibrated confidence statement. Keep the product defensive and accountable.
