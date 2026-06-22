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
- For Analytic Confidence Assessment, bind each finding to a labeled source — study designs, source quality, reproducibility artifacts, and uncertainty records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Analytic Confidence Assessment, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Analytic Confidence Assessment recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Analytic Confidence Assessment: independent lines of study designs, source quality, reproducibility artifacts, and uncertainty records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Analytic Confidence Assessment: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Analytic Confidence Assessment: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Analytic Confidence Assessment cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Analytic Confidence Assessment should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Analytic Confidence Assessment, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Analytic Confidence Assessment, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Analytic Confidence Assessment, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Analytic Confidence Assessment failure: collapsing heterogeneous evidence into an unsupported single confident conclusion.
- Analytic Confidence Assessment failure: producing guidance that would help a requester cherry-pick sources, fabricate citations, or overstate certainty from weak evidence.
- Analytic Confidence Assessment failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Analytic Confidence Assessment to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Analytic Confidence Assessment into an operational playbook to cherry-pick sources, fabricate citations, or overstate certainty from weak evidence' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Analytic Confidence Assessment to synthesize supplied or authorized sources with explicit confidence and uncertainty labels' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not assign confidence based on how comfortable the analyst feels with the conclusion rather than on evidence and assumption load
- do not treat corroboration from sources sharing a common origin (e.g., all from the same reporting chain) as independent confirmation
- do not omit a confidence statement because the judgment is preliminary — a low-confidence label is informative, not a failure

## AGEINT upstream
`docs/ageint/research-methods.md`
