# Workflow — Citation Integrity Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract all citations and in-text claims (read)
Read the document and systematically extract every citation, footnote, and reference. For each, record the in-text claim the author makes at that point — the exact assertion the citation is supposed to support. Number each citation-claim pair for tracking.

## Step 2 — Locate and retrieve cited sources (web)
For each citation, attempt to locate the source: search by DOI, title, author, or URL. Record whether the source exists and is accessible. Flag any citations that cannot be located after a reasonable search as potentially fabricated. For accessible sources, retrieve the specific passage cited or the section most relevant to the in-text claim.

## Step 3 — Compare claim against source text (reason)
For each retrievable source, compare what the author claims it says against what it actually says. Classify the match: accurate (source supports the claim faithfully), partial (source partially supports but omits important qualifications), distorted (source is misquoted or taken out of context to reverse or significantly change meaning), or fabricated (source does not exist or contains nothing resembling the claimed content).

## Step 4 — Assess support for the cited point (reason)
Even for citations that accurately represent the source, assess whether the source actually supports the specific point being made in this document at this location. A source can be quoted accurately yet not support the argument — flag these as 'accurate but unsupportive.' Note when a cited source is itself secondary or tertiary, requiring tracing to primary evidence.

## Step 5 — Produce audit table and integrity summary (write)
Compile the citation audit table with one row per citation, including all verdicts and severity ratings. Write the integrity summary identifying overall patterns (systematic distortion, selective citation, occasional error, isolated fabrication), the most serious violations, and a recommendation on the document's reliability as a source.

## Evidence requirements
- For Citation Integrity Review, tie each citation audit table, and integrity summary claim to concrete evidence from the specific document, and citation list item, source excerpt, observation, or command result that supports it.
- For Citation Integrity Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the citation audit table.
- Before recommending any Citation Integrity Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Citation Integrity Review: the citation audit table is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; extract all citations and in-text claims and locate and retrieve cited sources checks agree, and no unresolved contradiction would change the result.
- Medium for Citation Integrity Review: the citation audit table is plausible, but one important document source, comparison case, or alternative explanation remains incomplete.
- Low for Citation Integrity Review: the citation audit table rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Citation Integrity Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Citation Integrity Review, use only authorized document, and citation list, public or source-approved records, and caller-provided context needed for the defensive task.
- For Citation Integrity Review, minimize person-level detail in the citation audit table; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Citation Integrity Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Citation Integrity Review: treating document as complete when extract all citations and in-text claims and locate and retrieve cited sources checks or contradictory evidence are missing.
- Citation Integrity Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Citation Integrity Review: reporting the citation audit table without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Citation Integrity Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the citation audit table from Citation Integrity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Citation Integrity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with document, and citation list' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not accept a source existing as proof the citation is accurate — always check what the source actually states
- Do not treat accurate quotation as sufficient — check that the quoted passage genuinely supports the specific claim made in context
- Do not stop at the first accessible version of a source; preprints, retractions, and later editions can change what a source says
- Do not rate citation quality solely by journal prestige or author credential — assess what this specific passage actually asserts

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
