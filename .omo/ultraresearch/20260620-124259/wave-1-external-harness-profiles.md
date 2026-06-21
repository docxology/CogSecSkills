# Wave 1 - External Harness Profiles

Worker: `019ee68f-5f40-71e1-8b8c-40b74c8d0e0c`

Access date: 2026-06-20

## Key Findings

- Gemini CLI context files are product-specific, commonly `GEMINI.md`, with
  configurable context filenames including `AGENTS.md`.
- GitHub Copilot has multiple instruction and agent surfaces, not one universal
  profile: repository instructions, path-specific instructions, agent
  instructions, custom agents, CLI/cloud-agent surfaces, and code review.
- Cursor, Cline, Roo-style tools, JetBrains AI, and Continue each use
  product-specific rule/instruction surfaces.
- OpenAI Agents SDK, LangGraph, AutoGen, CrewAI, Pydantic AI, and Microsoft
  Agent Framework are application/framework integration targets.
- MCP is a tool/context protocol, not a standalone model harness.
- Perplexity is best documented as a research companion unless wrapped by an
  application that loads local files, tools, and adapters.

## Expansion

- Closed by implementation: clarify optional profile classes in harness docs,
  skill contract, and manuscript methods/system-context prose.

