# Workflow — Logical Coherence Review

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Extract and segment (read)
Read the full argument text. Identify the main conclusion(s). Segment the text into distinct claim units. Note the explicit premises offered in support of each conclusion.

## Step 2 — Build argument map and surface hidden premises (reason)
Construct the argument map using Toulmin structure (Claim / Data / Warrant / Backing / Qualifier / Rebuttal) or a simpler premise-conclusion schema. Identify every inferential step and make hidden premises explicit — state what must be true for each step to hold that the author did not state.

## Step 3 — Check validity and classify fallacies (reason)
For each inferential step, test formal validity: does the conclusion form follow necessarily from the premises? If not, name the formal fallacy (e.g., affirming the consequent, undistributed middle). Then check for informal fallacies in evidence use and rhetorical moves (ad hominem, strawman, false dilemma, slippery slope, appeal to authority, begging the question, equivocation). Assess severity: does this fallacy alone defeat the argument, or weaken it?

## Step 4 — Assess coherence and produce verdict (reason, write)
Synthesize: does the conclusion follow from the stated premises under valid inference? State the conditions under which the argument would hold and what would have to change. Assign an overall coherence rating (Valid / Valid-with-caveats / Invalid-but-restorable / Invalid). Write specific recommendations: premises to strengthen, inferences to make explicit, or a rejection justification.

## Step 5 — Produce fallacy register and annotated output (write)
Compile the fallacy register table with type, text location, description, and severity. Finalize the argument map with annotations. Write the coherence verdict narrative. If the artifact is a disinformation narrative, note which logical breaks are most rebuttable and most likely to resonate with target audiences.

## Evidence requirements
- For Logical Coherence Review, bind each finding to a labeled source — artifact excerpts, test output, citations, assumptions, and reproducibility records, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Logical Coherence Review, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Logical Coherence Review recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Logical Coherence Review: independent lines of artifact excerpts, test output, citations, assumptions, and reproducibility records converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Logical Coherence Review: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Logical Coherence Review: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Logical Coherence Review cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Logical Coherence Review should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Logical Coherence Review, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Logical Coherence Review, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Logical Coherence Review, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Logical Coherence Review failure: performing theatrical critique without concrete evidence, severity, or remediation path.
- Logical Coherence Review failure: producing guidance that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Logical Coherence Review failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Logical Coherence Review to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Logical Coherence Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Logical Coherence Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate the argument being false with it being logically invalid — a valid argument can have false premises, and a sound conclusion can be reached by bad inference
- do not list rhetorical weaknesses as formal fallacies — distinguish formal invalidity from persuasive weaknesses
- do not assess logical coherence while simultaneously adjudicating the truth of the premises — keep those steps separate
- do not declare an argument incoherent solely because it conflicts with the reviewer's prior beliefs

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
