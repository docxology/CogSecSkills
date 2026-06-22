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
- For Citation Integrity Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Citation Integrity Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Citation Integrity Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Citation Integrity Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Citation Integrity Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Citation Integrity Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Citation Integrity Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Citation Integrity Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Citation Integrity Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Citation Integrity Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Citation Integrity Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Citation Integrity Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Citation Integrity Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Citation Integrity Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Citation Integrity Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Citation Integrity Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Citation Integrity Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do not accept a source existing as proof the citation is accurate — always check what the source actually states
- Do not treat accurate quotation as sufficient — check that the quoted passage genuinely supports the specific claim made in context
- Do not stop at the first accessible version of a source; preprints, retractions, and later editions can change what a source says
- Do not rate citation quality solely by journal prestige or author credential — assess what this specific passage actually asserts

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
