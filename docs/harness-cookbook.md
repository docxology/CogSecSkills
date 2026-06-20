# Agent Harness Cookbook

This cookbook shows how to hand a CogSecSkills skill to a harness without
inventing a new source of truth. The examples are structural instructions, not
live runtime evaluations.

## Common Pattern

1. Route the user request.
2. Inspect the selected skill.
3. Load `SKILL.md`, `workflow.md`, and `harness/<name>.md`.
4. Produce only the bounded defensive output declared by the skill.
5. Label evidence, inference, confidence, and uncertainty.
6. Use `cogsecskills scenarios --check`, `cogsecskills examples --check`, and
   `cogsecskills dashboard --check` as local drift checks before treating
   fixtures as current.

```bash
PYTHONPATH="src:." python -m cogsecskills route "trace a claim to its earliest source"
PYTHONPATH="src:." python -m cogsecskills show osint_integrity.claim_provenance_verification
```

## Codex

```text
Use the CogSecSkills entry point:
skills/osint_integrity/claim_provenance_verification/SKILL.md

Use the neutral workflow:
skills/osint_integrity/claim_provenance_verification/workflow.md

Use the Codex adapter:
skills/osint_integrity/claim_provenance_verification/harness/codex.md
```

Codex should treat repository reads, local search, and edits according to the
adapter binding table and should preserve the defensive boundary from the skill.

## Claude

```text
Load SKILL.md as the skill instruction.
Load workflow.md as the procedure.
Load harness/claude.md as the tool-binding layer.
```

Claude-facing use should keep chain-of-evidence and uncertainty labels in the
answer and refuse unsafe transformations named by the skill.

## Hermes

```text
Load SKILL.md and workflow.md.
Map neutral verbs through harness/hermes.md.
Return the declared output fields only.
```

Hermes-facing use should keep function/tool bindings explicit and avoid adding
runtime-specific capabilities that the skill did not declare.

## Optional Harness Profiles

Use these as documented external profiles until you deliberately configure one.
The local distinction is:

- default adapters: `claude`, `codex`, and `hermes` ship with the repository;
- configured structural adapters: a profile id appears in `cogsecskills.yaml`
  and all rendered skills carry `harness/<profile-id>.md`;
- documented external profiles: a profile is listed for reader guidance but is
  not a local validation target.

Do not treat the profile list as one interoperable instruction standard. Some
profiles load repository instruction files, some use product-specific rules or
skills, some are application frameworks, and MCP is a tool/context protocol.

```yaml
harnesses: [claude, codex, hermes, gemini_cli]
```

After adding one profile id, regenerate and validate before using the adapter:

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
```

| Profile id | Handoff pattern |
| --- | --- |
| `gemini_cli` | Load the skill files as Gemini CLI context, commonly through `GEMINI.md` or configured context filenames, and map tool verbs to local/MCP actions. |
| `github_copilot` | Put the skill handoff in the supported Copilot surface for the task: repository instructions, path-specific instructions, agent instructions, custom agents, or CLI/cloud-agent context. |
| `devin_local` | Use the profile with Devin Local permissions, skills, sandboxing, and MCP controls. |
| `devin_cascade` | Use AGENTS.md/rules-style handoff for Cascade or Devin Desktop. |
| `cursor` | Convert the handoff into Cursor project, user, or team rules or dynamic skill context. |
| `cline` | Convert the handoff into Cline- or Roo-style rules/skills and configured tool permissions after checking the current product-specific file names. |
| `aider` | Add `SKILL.md`, `workflow.md`, and the adapter as read-only guidance files. |
| `continue` | Convert the handoff into Continue rules for Agent, Chat, or Edit mode. |
| `jetbrains_ai` | Use repository instruction files supported by JetBrains AI Assistant. |
| `openai_agents_sdk` | Implement a wrapper agent that owns orchestration, approvals, state, and tool execution. |
| `langgraph` | Bind the skill workflow into graph nodes, state, and tool policies. |
| `microsoft_agent_framework` | Bind the skill workflow into an agent or explicit workflow with filters and telemetry. |
| `autogen` | Bind the skill workflow into AgentChat/Core agents and tool extensions. |
| `crewai` | Bind the skill workflow into crew agents, tasks, flows, and guardrails. |
| `pydantic_ai` | Bind the skill workflow into typed agents, capabilities, and validated outputs. |
| `mcp_host` | Use only as the host/tool transport layer underneath a real harness; MCP is not itself a model harness. |
| `perplexity_research` | Use only for research support unless a wrapper supplies local file and tool execution. |

## Custom Harness

Create `cogsecskills.yaml`:

```yaml
harnesses: [claude, codex, hermes, custom_harness]
```

Regenerate and validate:

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
```

Generated custom adapters are structural starting points. Review their tool
bindings before using them in a real runtime.
