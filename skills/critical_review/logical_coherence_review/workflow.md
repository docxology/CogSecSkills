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
- For Logical Coherence Review, bind each mapped premise, inferential step, and named fallacy to concrete textual evidence showing where it occurs, and assess the validity of the inference separately from the truth of the premises so that weak evidence for a premise is never confused with an invalid inference.
- For Logical Coherence Review, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the argument map.
- Before recommending any Logical Coherence Review action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Logical Coherence Review: each entry in the argument map and fallacy register is tied to a specific passage and a named formal or informal fallacy, the coherence verdict and its validity-versus-soundness separation hold when hidden premises are made explicit, and no unresolved contradiction in the inferential chain would change whether the conclusion is judged to follow from its premises.
- Medium for Logical Coherence Review: the argument map is plausible, but one important argument text source, comparison case, or alternative explanation remains incomplete.
- Low for Logical Coherence Review: the argument map rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Logical Coherence Review cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating critical_review evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Logical Coherence Review, use only authorized argument text, and key claims, public or source-approved records, and caller-provided context needed for the defensive task.
- For Logical Coherence Review, minimize person-level detail in the argument map; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Logical Coherence Review, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Logical Coherence Review: judging an argument coherent when its hidden premises were never surfaced or the inferential steps were never tested for formal validity, so a narrative that carries through rhetorical momentum or equivocation on a key term is mistaken for sound deductive or inductive reasoning.
- Logical Coherence Review: producing advice that would help a requester launder weak claims, fabricate review findings, or produce exploit guidance without mitigation.
- Logical Coherence Review: reporting the argument map without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Logical Coherence Review outputs to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the argument map from Logical Coherence Review into an operational playbook to launder weak claims, fabricate review findings, or produce exploit guidance without mitigation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Logical Coherence Review to review supplied artifacts for defects, evidence gaps, safety risks, or reproducibility failures with argument text, and key claims' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not conflate the argument being false with it being logically invalid — a valid argument can have false premises, and a sound conclusion can be reached by bad inference
- do not list rhetorical weaknesses as formal fallacies — distinguish formal invalidity from persuasive weaknesses
- do not assess logical coherence while simultaneously adjudicating the truth of the premises — keep those steps separate
- do not declare an argument incoherent solely because it conflicts with the reviewer's prior beliefs

## AGEINT upstream
`docs/ageint/adversarial-assurance.md`
