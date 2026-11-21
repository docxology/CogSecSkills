# CogSec Evidence

CogSec Evidence helps analysts, editors, and researchers assess how well public claims are supported. Paste a claim and the public excerpts needed to assess it. Claude explains what each source supports, identifies gaps or shared origins, and ties its conclusions to the evidence you supplied.

## Try it

Install CogSec Evidence through Claude's plugin interface and start a new conversation. The skills need no accounts, credentials, connectors, or additional software. You can ask in plain language or invoke a skill by name in Claude Code.

| Task | Skill | Example prompt |
| --- | --- | --- |
| Grade a source and its claim separately | `/cogsec-evidence:source-credibility` | “Assess the reliability of this transit agency bulletin and the credibility of its claim that ridership increased by 12%. I’ve pasted the bulletin and the ridership table. Show what the table independently establishes.” |
| Trace how a claim was repeated | `/cogsec-evidence:claim-provenance` | “Trace the claim that the museum doubled annual attendance. Here are dated excerpts from two articles and the original press release. Identify which articles draw on the same source and what the release actually measures.” |
| Check whether a citation supports a sentence | `/cogsec-evidence:citation-integrity` | “Audit this sentence against the abstract and table I’ve pasted. Does the cited study support a claim about all adults, or only the population it sampled? Draft a supported revision if possible.” |

## Data handling

The skills use only excerpts pasted in the conversation. Paste the relevant portions of public sources and remove personal or sensitive details first. The skills do not request credentials, open uploads or links, read local files, search the web, or send material to another service. The plugin has no scripts, hooks, servers, telemetry, or storage of its own. Pasted inputs and the resulting analysis are part of the Claude conversation and are subject to its normal data handling. The plugin is intended for adults doing evidence review.

## Troubleshooting

- **A finding is unverified.** Paste the relevant original passage, its date, and the text the later source attributes to it. If two reports cite the same original, supply an independent excerpt to test corroboration.
- **A citation supplied only as a URL can't be checked.** Paste the cited sentence, bibliographic details, and the relevant source passage. The skill can compare supplied text and identify what it cannot establish from that text.
- **A skill does not appear in Claude Code.** Confirm the plugin is enabled, reload plugins with `/reload-plugins`, and look for the `cogsec-evidence` namespace.

## Source and support

These are portable adaptations of three [CogSecSkills methods](https://github.com/docxology/CogSecSkills): Source Credibility Evaluation, Claim Provenance Verification, and Citation Integrity Review. The adaptations limit the workflows to supplied public excerpts. The plugin is licensed under [Apache 2.0](LICENSE).

Report usage or compatibility issues on [GitHub](https://github.com/docxology/CogSecSkills/issues). Use a short example with public text and omit identifying details.

Report vulnerabilities through [GitHub's private security reporting form](https://github.com/docxology/CogSecSkills/security/advisories/new).
