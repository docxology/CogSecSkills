# Workflow — Analytic Confidence Assessment

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Inventory evidence and assumptions (read)
Read the analytic judgment and all supporting evidence. Catalog each source with its type (human, technical, open, liaison), reliability history, and access freshness. List every assumption the conclusion implicitly requires.

## Step 2 — Score three confidence dimensions (reason)
Score source quality (reliability and credibility of each source), corroboration (number of independent confirming sources and absence of contradictory evidence), and assumption load (how many high-impact assumptions remain untested). Use a consistent three-level rubric: high/moderate/low for each dimension.

## Step 3 — Derive overall confidence tier (reason)
Combine dimension scores using a conservative rule: overall confidence cannot exceed the weakest dimension. Note whether corroboration is genuine independence or from common-origin sources, and flag any single point of failure in the evidence chain.

## Step 4 — Write confidence statement (write)
Produce the confidence assessment: state the tier, provide a one-paragraph justification citing each dimension score, list the two or three conditions that would raise or lower confidence, and note any cognitive biases (availability, anchoring) that may have inflated the initial estimate.

## Evidence requirements
- For Analytic Confidence Assessment, tie each confidence assessment claim to concrete evidence from the specific judgment, evidence set, and key assumptions item, source excerpt, observation, or command result that supports it.
- For Analytic Confidence Assessment, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the confidence assessment.
- Before recommending any Analytic Confidence Assessment action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Analytic Confidence Assessment: the confidence assessment is supported by multiple independent study designs, source quality, reproducibility artifacts, and uncertainty records; inventory evidence and assumptions and score three confidence dimensions checks agree, and no unresolved contradiction would change the result.
- Medium for Analytic Confidence Assessment: the confidence assessment is plausible, but one important judgment source, comparison case, or alternative explanation remains incomplete.
- Low for Analytic Confidence Assessment: the confidence assessment rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Analytic Confidence Assessment cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating research_methods evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Analytic Confidence Assessment, use only authorized judgment, evidence set, and key assumptions, public or source-approved records, and caller-provided context needed for the defensive task.
- For Analytic Confidence Assessment, minimize person-level detail in the confidence assessment; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Analytic Confidence Assessment, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Analytic Confidence Assessment: treating judgment as complete when inventory evidence and assumptions and score three confidence dimensions checks or contradictory evidence are missing.
- Analytic Confidence Assessment: producing advice that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Analytic Confidence Assessment: reporting the confidence assessment without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Analytic Confidence Assessment outputs to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the confidence assessment from Analytic Confidence Assessment into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Analytic Confidence Assessment to synthesize supplied or authorized sources with explicit confidence and uncertainty labels with judgment, evidence set, and key assumptions' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not assign confidence based on how comfortable the analyst feels with the conclusion rather than on evidence and assumption load
- do not treat corroboration from sources sharing a common origin (e.g., all from the same reporting chain) as independent confirmation
- do not omit a confidence statement because the judgment is preliminary — a low-confidence label is informative, not a failure

## AGEINT upstream
`docs/ageint/research-methods.md`
