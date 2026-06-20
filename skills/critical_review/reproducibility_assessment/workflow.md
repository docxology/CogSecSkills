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
- For Reproducibility Assessment, tie each reproducibility scorecard, and gap report claim to concrete evidence from the specific artifact, key claims, and environment spec item, source excerpt, observation, or command result that supports it.
- For Reproducibility Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the reproducibility scorecard.
- Before recommending any Reproducibility Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Reproducibility Assessment: the reproducibility scorecard is supported by multiple independent artifact excerpts, test output, citations, assumptions, and reproducibility records; inventory stated methods and materials and assess data and code availability checks agree, and no unresolved contradiction would change the result.
- Medium for Reproducibility Assessment: the reproducibility scorecard is plausible, but one important artifact source, comparison case, or alternative explanation remains incomplete.
- Low for Reproducibility Assessment: the reproducibility scorecard rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Reproducibility Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Reproducibility Assessment, use only authorized artifact, key claims, and environment spec, public or source-approved records, and caller-provided context needed for the defensive task.
- For Reproducibility Assessment, minimize person-level detail in the reproducibility scorecard; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Reproducibility Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Reproducibility Assessment: treating artifact as complete when inventory stated methods and materials and assess data and code availability checks or contradictory evidence are missing.
- Reproducibility Assessment: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Reproducibility Assessment: reporting the reproducibility scorecard without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Reproducibility Assessment outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the reproducibility scorecard from Reproducibility Assessment into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Reproducibility Assessment to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with artifact, key claims, and environment spec' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not classify a result as reproducible without actually attempting execution — plausibility is not reproducibility
- do not treat unavailable data or code as 'acceptable' without explicitly flagging it as a non-assessable gap
- do not conflate replication (new data, same method) with direct reproduction (same data, same code) — they provide different epistemic assurance
- do not issue recommendations that merely ask authors to assert reproducibility without specifying what artifacts must be provided or what criteria must be met

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
