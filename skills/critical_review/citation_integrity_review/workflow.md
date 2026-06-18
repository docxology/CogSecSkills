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

## Anti-criteria (must NOT happen)
- Do not accept a source existing as proof the citation is accurate — always check what the source actually states
- Do not treat accurate quotation as sufficient — check that the quoted passage genuinely supports the specific claim made in context
- Do not stop at the first accessible version of a source; preprints, retractions, and later editions can change what a source says
- Do not rate citation quality solely by journal prestige or author credential — assess what this specific passage actually asserts

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
