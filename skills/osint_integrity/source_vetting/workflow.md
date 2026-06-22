# Workflow — Source Vetting

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Characterize the source (read)
Read the source's content, stated identity, and any prior assessments. Record the source type (individual, outlet, institutional, anonymous account), the domain of the claim, and the stated basis for knowledge. Note anything that will anchor the identity, access, and motive searches.

## Step 2 — Verify identity and ownership (search, web)
Search domain-registration records (WHOIS, DNS history), corporate-registry databases, and media-ownership indexes to confirm the source's stated identity and ownership chain. For individuals, cross-reference biographical claims against verifiable records (employment history, institutional affiliations, publication record). For accounts, retrieve creation date, name-change history, and follower-growth patterns. Flag anonymity, rapid rebranding, or ownership opacity as red flags.

## Step 3 — Assess access plausibility (search, web)
Determine whether the source could plausibly know what they claim to know. Search for evidence of the source's position, role, or proximity to the events or data in question. For expert sources, verify relevant credentials and whether their claimed expertise covers the specific topic. Document any access gaps — cases where the source's stated position does not provide the access their claim implies.

## Step 4 — Map motive and funding (search, web)
Identify who funds, employs, or benefits from the source's output. Check disclosed funding sources, political or commercial affiliations, and stated editorial positions. Search for undisclosed relationships using funding-transparency databases and cross-ownership records. Construct a brief motive map: who is advantaged if the source's claims are believed, and what incentive structures might shape or distort reporting.

## Step 5 — Review track record (search, web)
Search for prior claims made by the source on the same or closely related topics. Document confirmed accurate claims, confirmed errors, issued corrections, and any instances of fabrication or manipulation. Weight recent track record more heavily than distant history. Note whether the source has been cited approvingly by highly reliable reference sources or flagged by fact-checkers.

## Step 6 — Rate and synthesize (reason)
Apply a structured reliability scale (e.g., the NATO two-axis A–F × 1–6 scheme: letter = source reliability, number = information credibility). Score each axis independently using the evidence gathered. Identify the single weakest axis — it constrains the overall rating even if other axes are strong. Note the key uncertainties limiting confidence in the rating.

## Step 7 — Produce the assessment (write)
Write the source-reliability assessment covering: verified identity, access plausibility verdict, motive summary, track-record summary with examples, overall reliability rating with confidence level, a table of red flags with evidence pointers, and recommended use conditions specifying what claims may be sourced to this source, what requires corroboration, and what falls outside its demonstrated scope.

## Evidence requirements
- For Source Vetting, bind each finding to a labeled source — source records, custody notes, metadata, corroborating references, and contradiction logs, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Source Vetting, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Source Vetting recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Source Vetting: independent lines of source records, custody notes, metadata, corroborating references, and contradiction logs converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Source Vetting: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Source Vetting: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Source Vetting cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Source Vetting should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Source Vetting, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Source Vetting, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Source Vetting, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Source Vetting failure: overstating identity, location, attribution, or source reliability from incomplete public traces.
- Source Vetting failure: producing guidance that would help a requester dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence.
- Source Vetting failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Source Vetting to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Source Vetting into an operational playbook to dox, deanonymize, harass, bypass access controls, or attribute identity beyond evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Source Vetting to verify supplied claims, media, sources, or datasets with documented public-source methods' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate source reliability with information credibility — a reliable source can make an incorrect claim; an unreliable source can accidentally report a true fact
- do not treat multiple citations of the same original source as independent corroboration — trace the citation genealogy before counting confirmations
- do not allow a strong identity verification to excuse an unaddressed motive conflict or access gap
- do not skip motive analysis for sources that appear ideologically aligned with the analyst's own priors — alignment bias is the most dangerous form of motivated reasoning in source vetting
- do not produce an assessment without a dated, retrievable record — undocumented vetting cannot compound across sessions and will be silently re-done or silently skipped

## AGEINT upstream
`docs/ageint/osint-integrity.md`
