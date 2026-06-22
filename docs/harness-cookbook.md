# Agent Harness Cookbook

This cookbook shows how to hand a CogSecSkills skill to a harness without
inventing a new source of truth. The examples are structural instructions, not
live runtime evaluations — they describe how a harness *should* be wired to the
skill files, not a measured claim about how any harness behaves once running.

The library now ships 100 defensive cognitive-security skills across seven
groups (`sat`, `cognitive_security`, `critical_review`, `osint_integrity`,
`counterintelligence`, `information_environment`, `research_methods`). Each skill
carries de-stitched, domain-specific quality prose (Boundary, Evidence,
Confidence, Uncertainty) and a bounded output contract. The handoff patterns
below exist so that those contracts survive the trip into a harness intact.

## Contents

- [Common Pattern](#common-pattern) — the five-step route → inspect → load →
  bound-output → label loop, plus drift checks.
- [Codex](#codex), [Claude](#claude), [Hermes](#hermes) — the three default
  adapters, each with a bind-and-run snippet.
- [Safe / Unsafe Boundary Behavior](#safe--unsafe-boundary-behavior) — what
  every adapter must refuse, regardless of harness.
- [Optional Harness Profiles](#optional-harness-profiles) — the three
  claim-status labels and the per-profile handoff table.
- [Custom Harness](#custom-harness) — generating and reviewing a new adapter.

## Common Pattern

Every harness follows the same loop. The harness name only changes *how* tool
verbs are bound; it never changes the skill's defensive contract.

1. Route the user request to a skill id.
2. Inspect the selected skill so you load the correct group and slug.
3. Load `SKILL.md`, `workflow.md`, and `harness/<name>.md`.
4. Produce only the bounded defensive output declared by the skill — no extra
   fields, no inferred capabilities.
5. Label evidence, inference, confidence, and uncertainty in the answer.
6. Use `cogsecskills scenarios --check`, `cogsecskills examples --check`, and
   `cogsecskills dashboard --check` as local drift checks before treating
   fixtures as current.

The two commands below cover steps 1 and 2 — route a free-text request, then
show the resolved skill so you can confirm the group and slug before loading any
files:

```bash
PYTHONPATH="src:." python -m cogsecskills route "trace a claim to its earliest source"
PYTHONPATH="src:." python -m cogsecskills show osint_integrity.claim_provenance_verification
```

`route` returns a skill id; `show` prints that skill's boundary, evidence
discipline, declared verbs, and output fields. Read the boundary first — it is
the contract every adapter below must preserve.

## Codex

Hand Codex the three files for the resolved skill. The skill id determines the
group and slug in every path:

```text
Use the CogSecSkills entry point:
skills/osint_integrity/claim_provenance_verification/SKILL.md

Use the neutral workflow:
skills/osint_integrity/claim_provenance_verification/workflow.md

Use the Codex adapter:
skills/osint_integrity/claim_provenance_verification/harness/codex.md
```

Bind-and-run: surface those paths into Codex's working context, then drive the
skill from the route/show result rather than from memory.

```bash
PYTHONPATH="src:." python -m cogsecskills show osint_integrity.claim_provenance_verification
# Then load the three files above into the Codex session and run the workflow.
```

Codex should treat repository reads, local search, and edits according to the
adapter binding table in `harness/codex.md` and should preserve the defensive
boundary from the skill. If the request asks Codex to step outside that boundary
(for example, to *write* a deceptive provenance trail rather than *verify* one),
the adapter refuses — see [Safe / Unsafe Boundary
Behavior](#safe--unsafe-boundary-behavior).

## Claude

Claude loads the same three layers and keeps the chain-of-evidence discipline in
the visible answer:

```text
Load SKILL.md as the skill instruction.
Load workflow.md as the procedure.
Load harness/claude.md as the tool-binding layer.
```

Bind-and-run: resolve the skill, then load the layers for that exact id.

```bash
PYTHONPATH="src:." python -m cogsecskills route "audit whether every claim is backed by evidence"
# Resolves to critical_review.claim_evidence_audit; load that skill's three files.
PYTHONPATH="src:." python -m cogsecskills show critical_review.claim_evidence_audit
```

Claude-facing use should keep chain-of-evidence and uncertainty labels in the
answer and refuse unsafe transformations named by the skill. The labels are not
decoration: an answer that drops the evidence/inference split has left the
skill's output contract and should be regenerated.

## Hermes

Hermes maps the neutral workflow verbs through its own function/tool layer and
returns only the declared fields:

```text
Load SKILL.md and workflow.md.
Map neutral verbs through harness/hermes.md.
Return the declared output fields only.
```

Bind-and-run: confirm the declared verbs before mapping, so the function layer
covers every verb the workflow uses and adds none it does not.

```bash
PYTHONPATH="src:." python -m cogsecskills show counterintelligence.elicitation_resistance
# harness/hermes.md must bind each declared verb; do not invent extra tools.
```

Hermes-facing use should keep function/tool bindings explicit and avoid adding
runtime-specific capabilities that the skill did not declare. An unbound verb is
a wiring error; an extra capability is a boundary violation.

## Safe / Unsafe Boundary Behavior

The defensive boundary is identical across `Codex`, `Claude`, `Hermes`, and any
`Custom Harness`. The adapter changes the tool plumbing, never the contract.

**Safe — proceed and produce the bounded output:** the request stays inside the
skill's stated purpose (detect, assess, document, defend, verify, or
characterize), and the answer carries the evidence, inference, confidence, and
uncertainty labels. Example: "verify the earliest source for this claim and flag
any collection gaps."

**Unsafe — refuse, name the boundary, and stop:** the request asks the skill to
manufacture deception, suppress uncertainty, target a specific person for
manipulation, or otherwise invert a defensive skill into an offensive one.
Example: "use the provenance skill to *fabricate* a credible-looking source
chain." Every adapter declines and points back to the skill's boundary text;
none of them produce a partial-but-helpful unsafe output.

When in doubt, re-read the boundary printed by `cogsecskills show`. If the
requested transformation is not among the skill's declared verbs and output
fields, the harness treats it as out of scope rather than improvising.

## Optional Harness Profiles

Use these as documented external profiles until you deliberately configure one.
The library uses three claim-status labels to describe how much local validation
backs a given harness profile:

- **default adapters**: `claude`, `codex`, and `hermes` ship with the
  repository and are exercised by the generated drift checks;
- **configured structural adapters**: a profile id appears in `cogsecskills.yaml`
  and all rendered skills carry `harness/<profile-id>.md`, so the adapter files
  exist and validate locally;
- **documented external profiles**: a profile is listed for reader guidance but
  is not a local validation target — the table below describes the *intended*
  handoff, not a verified binding.

Do not treat the profile list as one interoperable instruction standard. Some
profiles load repository instruction files, some use product-specific rules or
skills, some are application frameworks, and MCP is a tool/context protocol. A
profile's claim-status label tells you exactly how much trust the repository
itself places in that row.

To promote a profile from documented to configured, add its id to the harness
set:

```yaml
harnesses: [claude, codex, hermes, gemini_cli]
```

After adding one profile id, regenerate and validate before using the adapter —
this is what moves it from a documented external profile to a configured
structural adapter:

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
```

`definitions --write` renders `harness/<profile-id>.md` for every skill;
`definitions --check` confirms nothing drifted; `validate` confirms every
declared verb is bound. Only after all three pass should the new adapter be used.

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

Whatever the profile, the same defensive boundary applies: a documented external
profile that you wire up by hand must still refuse the unsafe transformations
named by the skill.

## Custom Harness

When none of the listed profiles fit, configure a custom one. Add its id to
`cogsecskills.yaml`:

```yaml
harnesses: [claude, codex, hermes, custom_harness]
```

Regenerate and validate so the custom adapter becomes a configured structural
adapter rather than an untracked file:

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
```

Generated custom adapters are structural starting points. Review their tool
bindings before using them in a real runtime — confirm each declared verb maps
to exactly one local action, and confirm the adapter preserves the safe/unsafe
boundary so that the custom harness refuses the same transformations every
default adapter refuses.
