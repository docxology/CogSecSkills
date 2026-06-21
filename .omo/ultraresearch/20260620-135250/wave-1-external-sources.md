# Wave 1 External Source Digest

Access date: 2026-06-20.

Sources opened directly:
- OpenAI evals guide: https://developers.openai.com/api/docs/guides/evals
- OpenAI evaluation best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- NIST AI RMF / GenAI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST AI RMF page: https://www.nist.gov/itl/ai-risk-management-framework
- FORCE11 software citation principles: https://force11.org/info/software-citation-principles-published-2016/
- Zenodo CITATION.cff help: https://help.zenodo.org/docs/github/describe-software/citation-file/
- Zenodo GitHub/software help: https://help.zenodo.org/docs/github/
- GitHub citing/Zenodo docs: https://docs.github.com/repositories/archiving-a-github-repository/referencing-and-citing-content
- GitHub Copilot CLI custom instructions and AGENTS.md: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
- Gemini context files: https://geminicli.com/docs/cli/gemini-md/
- Cursor rules: https://cursor.com/docs/rules
- MCP intro: https://modelcontextprotocol.io/docs/getting-started/intro

Key findings:
- OpenAI frames evals as tests of model outputs against style/content criteria and notes that traditional software tests are insufficient for variable generative systems.
- NIST AI RMF/GenAI Profile supports risk-management framing for generative AI systems, but does not by itself validate CogSecSkills effectiveness.
- FORCE11 and Zenodo/GitHub guidance support release/provenance metadata and citable software, but a DOI or archive claim must not be invented before the archive exists.
- GitHub Copilot, Gemini, Cursor, and MCP all support local instruction/context/tool surfaces, but they are not interchangeable harness certifications.

Expansion markers:
- LEAD: Add a future eval harness that explicitly labels deterministic fixture checks, offline scored model-output evals, and live harness smoke runs as separate evidence levels.
- LEAD: Add release-readiness tasks for `.zenodo.json`/CITATION.cff/code metadata review, but leave DOI blank until a real archive exists.

## EXPAND
- LEAD: Evidence ladder v2 with offline model-output scoring — WHY: external eval guidance distinguishes software tests from model-output evals — ANGLE: plan local fixtures + optional provider adapters.
- LEAD: Release provenance pack — WHY: software citation guidance needs version/archive identifiers without inventing DOI — ANGLE: plan metadata validation and release checklist.

