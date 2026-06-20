# Installing CogSecSkills Into An Agent Harness

CogSecSkills is published at `https://github.com/docxology/CogSecSkills`.
The repository contains the registry, canonical definitions, rendered on-disk
skills, default harness adapters, optional harness configuration, and the
`cogsecskills` CLI.

## Install And Validate

```bash
git clone https://github.com/docxology/CogSecSkills.git
cd CogSecSkills
uv sync
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills doctor
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills dashboard --check
```

If you are not using `uv`, install the package in editable mode:

```bash
python -m pip install -e .
cogsecskills validate
```

## Use A Skill From A Harness

Each skill lives at:

```text
skills/<group>/<slug>/
```

An agent harness should load the human-facing skill entry point, then use the
harness adapter that matches its runtime:

```text
SKILL.md                 skill description and when-to-use guidance
workflow.md              harness-neutral procedure
harness/<harness>.md     concrete adapter binding neutral verbs to tools
```

Default adapters are provided for `claude`, `codex`, and `hermes`.

For a concrete harness handoff, route a task, inspect the selected skill, then
load the three local files together:

```bash
PYTHONPATH="src:." python -m cogsecskills route "verify a viral claim before sharing it" --limit 5
PYTHONPATH="src:." python -m cogsecskills show osint_integrity.claim_provenance_verification
```

The harness should treat `SKILL.md` as the entry-point description,
`workflow.md` as the neutral procedure, and `harness/<name>.md` as the runtime
binding table for the closed tool verbs. The scenario gate above confirms that
curated safe-use and unsafe-redirect fixtures still route to expected skills and
that those fixtures declare the expected defensive response shape and required
quality metadata. It does not execute a live model or connector.

## Harness Status Terms

CogSecSkills uses three distinct labels so portability claims stay bounded:

| Status | Meaning |
| --- | --- |
| default adapters | The repository ships `claude`, `codex`, and `hermes` adapters for every rendered skill. These are the default configured harnesses. |
| configured structural adapters | A harness name is added to `cogsecskills.yaml`, `definitions --write` renders `harness/<name>.md`, and `validate` requires that adapter for every skill. |
| documented external profiles | A named runtime or framework is listed as an integration candidate in `registry/harness_profiles.yaml`; it is not covered by local gates until configured, regenerated, reviewed, and validated. |

The optional profile registry is documentation metadata, not runtime
configuration. It helps readers choose a likely `harnesses:` name while keeping
the local claim boundary intact. Product profiles differ materially: some load
repo instruction files, some use product-specific rules or skills, some are
SDK/framework integration targets, and `mcp_host` is a tool protocol profile
rather than a model harness.

| Profile id | Use as | Notes |
| --- | --- | --- |
| `gemini_cli` | terminal agent | Good first optional configured harness candidate for Gemini CLI-style local use; Gemini CLI context files are product-specific, commonly `GEMINI.md` or configured alternatives such as `AGENTS.md`. |
| `github_copilot` | IDE or cloud agent | Instruction support varies across repository instructions, path-specific instructions, agent instructions, Copilot Chat, cloud agent, CLI, and code-review surfaces. |
| `devin_local` | local agent | Treat generated adapters as reviewable starting points for Devin Local permissions and skills. |
| `devin_cascade` | IDE agent | Use for Cascade/Devin Desktop rule and AGENTS.md-style instruction surfaces. |
| `cursor` | IDE agent | Map the skill files into Cursor project, user, or team rules or skills as local instructions. |
| `cline` | IDE agent | Map the skill files into Cline- or Roo-style rule/skill surfaces after checking the product-specific filenames and deprecations. |
| `aider` | terminal agent | Load conventions or selected skill files read-only into Aider sessions. |
| `continue` | IDE or CLI agent | Map the skill files into Continue rules for Agent, Chat, or Edit mode. |
| `jetbrains_ai` | IDE agent | Use instruction files supported by JetBrains AI Assistant. |
| `openai_agents_sdk` | programmatic runtime | Wrap skills in application-owned agents, tools, approvals, and state. |
| `langgraph` | programmatic runtime | Bind skills into graph nodes, tool policies, and human-in-the-loop controls. |
| `microsoft_agent_framework` | programmatic runtime | Bind skills into .NET or Python agents, workflows, middleware, and filters. |
| `autogen` | programmatic runtime | Bind skills into AgentChat/Core agents and extensions. |
| `crewai` | programmatic runtime | Bind skills into crew, task, flow, guardrail, and knowledge definitions. |
| `pydantic_ai` | programmatic runtime | Bind skills into typed agents, capabilities, and tool definitions. |
| `mcp_host` | protocol host | Treat as a tool/context transport profile, not a standalone model harness or instruction standard. |
| `perplexity_research` | research companion | Treat as research support unless a wrapper loads local files, tools, and adapters. |

## Add A Custom Harness

Create or edit `cogsecskills.yaml`:

```yaml
harnesses: [claude, codex, hermes, your_harness]
```

Then regenerate and validate adapters:

```bash
PYTHONPATH="src:." python -m cogsecskills definitions --write
PYTHONPATH="src:." python -m cogsecskills definitions --check
PYTHONPATH="src:." python -m cogsecskills validate
PYTHONPATH="src:." python -m cogsecskills scenarios --check
PYTHONPATH="src:." python -m cogsecskills examples --check
PYTHONPATH="src:." python -m cogsecskills dashboard --check
```

Unknown harness names are treated as supporting the full closed verb set unless
an explicit support map narrows them in code. Generated fallback adapter rows
are structurally valid but should be reviewed and refined for the real runtime.

## Route To The Right Skill

```bash
PYTHONPATH="src:." python -m cogsecskills route "verify a viral claim before sharing it"
PYTHONPATH="src:." python -m cogsecskills show osint_integrity.claim_provenance_verification
```

The route command helps an operator or harness choose the appropriate skill.
The show command prints the corresponding structured contract.
