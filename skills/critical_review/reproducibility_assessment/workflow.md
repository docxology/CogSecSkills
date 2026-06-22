# Workflow — Reproducibility Assessment

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory stated methods and materials (read)
Read the artifact in full. Extract: the key claims to be verified; the data sources and their access status (public/private/restricted); the code repository or notebook location; the stated environment (OS, language version, library versions); any stated random seeds; and the preprocessing and analysis pipeline as documented.

## Step 2 — Assess data and code availability (reason)
For each required input (data, code, model weights, preprocessing scripts), check availability: is it accessible? is it versioned or pinned? does the described artifact match what is actually provided? Flag discrepancies. If key data or code is missing, mark the relevant claims as 'not assessable' for direct reproduction.

## Step 3 — Attempt direct reproduction (exec)
Where data, code, and environment are available, execute the pipeline following only the documented steps. Record actual outputs and compare to claimed results (numbers, figures, tables). Note any undocumented steps required to get the code to run. Record exact deviations between claimed and reproduced results, including direction and magnitude.

## Step 4 — Classify gaps and assess tiers (reason)
For each key claim, classify reproducibility status at each tier: direct (same data + code), replication (same method + new data), and conceptual (same hypothesis + different operationalization). Identify the root cause of each gap: missing data, missing code, undocumented preprocessing, environment sensitivity, randomness not controlled, or result genuinely differs. Assess whether gaps are remediable (documentation fix) or fundamental (design issue).

## Step 5 — Produce scorecard and recommendations (write)
Compile the reproducibility scorecard table with status and evidence for each criterion. Write the gap report narrative with root causes and recommendations. Assign the overall reproducibility tier. For cognitive-security use, explicitly note whether non-reproducible results should be treated as provisional and what additional evidence would be needed before treating them as reliable.

## Evidence requirements
- For Reproducibility Assessment, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Reproducibility Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Reproducibility Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Reproducibility Assessment: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Reproducibility Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Reproducibility Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Reproducibility Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Reproducibility Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Reproducibility Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Reproducibility Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Reproducibility Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Reproducibility Assessment failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Reproducibility Assessment failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Reproducibility Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Reproducibility Assessment to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Reproducibility Assessment into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Reproducibility Assessment to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not classify a result as reproducible without actually attempting execution — plausibility is not reproducibility
- do not treat unavailable data or code as 'acceptable' without explicitly flagging it as a non-assessable gap
- do not conflate replication (new data, same method) with direct reproduction (same data, same code) — they provide different epistemic assurance
- do not issue recommendations that merely ask authors to assert reproducibility without specifying what artifacts must be provided or what criteria must be met

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
