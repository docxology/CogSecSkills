# Workflow — Source Credibility Evaluation

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Identify the source and its proximity (read)
Determine who or what the source is, how close it sits to the events, what access it had, and whether it is primary, secondary, expert, or merely relaying others.

## Step 2 — Assess track record, motive, and independence (read, search)
Check past accuracy, incentives to mislead, funding or affiliation signals, and whether the source is independent enough to corroborate anything.

## Step 3 — Assign the source-reliability letter (reason, write)
Map proximity, track record, motive, and independence to A through F, then justify the letter in evidence-bound language.

## Step 4 — Assess the specific claim independently (read, search, reason)
Check whether the exact claim is confirmed by independent sources, plausible, and consistent with known facts. Distinguish confirmation from repetition.

## Step 5 — Assign the information-credibility number (reason, write)
Map corroboration and plausibility to 1 through 6, naming confirming, contradicting, or absent evidence.

## Step 6 — Preserve the two-axis distinction (write)
State that the letter grades the source and the number grades this specific claim, then report the combined pair such as B2.

## Step 7 — Bound downstream use (reason, write)
Translate the combined grade into practical constraints, including whether the claim can be used, requires more corroboration, or should be withheld.

## Evidence requirements
- For Source Credibility Evaluation, bind the reliability letter, the credibility number, and the usage bound to concrete evidence, naming the confirming, contradicting, or absent independent sources for the specific claim and keeping the source-judging evidence separate from the claim-judging evidence rather than letting one stand in for the other.
- For Source Credibility Evaluation, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the reliability grade.
- Before recommending any Source Credibility Evaluation action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Source Credibility Evaluation: the source-reliability letter and the information-credibility number are each justified by distinct evidence — proximity, track record, motive, and independence for the letter; independent confirmation, plausibility, and consistency for the number — and no unresolved contradiction would change the combined grade or the bound it places on downstream use.
- Medium for Source Credibility Evaluation: the reliability grade is plausible, but one important source source, comparison case, or alternative explanation remains incomplete.
- Low for Source Credibility Evaluation: the reliability grade rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Source Credibility Evaluation cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating cognitive_security evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Source Credibility Evaluation, use only authorized source, claim, and corroboration, public or source-approved records, and caller-provided context needed for the defensive task.
- For Source Credibility Evaluation, minimize person-level detail in the reliability grade; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Source Credibility Evaluation, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Source Credibility Evaluation: declaring a claim graded when source reliability was collapsed into claim credibility, prestige was allowed to substitute for corroboration, or repetition of the same originating report was counted as independent confirmation, yielding an unwarranted grade such as A1.
- Source Credibility Evaluation: producing advice that would help a requester increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation.
- Source Credibility Evaluation: reporting the reliability grade without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Source Credibility Evaluation outputs to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the reliability grade from Source Credibility Evaluation into an operational playbook to increase persuasive impact, exploit audience vulnerabilities, or optimize narrative manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Source Credibility Evaluation to assess supplied material for manipulation indicators and recommend resilience measures with source, claim, and corroboration' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- Do **not** conflate source reliability with claim credibility — never collapse
- Do **not** let prestige, fame, or authority substitute for corroboration of
- Do **not** assign **A1** without genuine independent confirmation — A1
- Do **not** treat repetition or re-syndication of the same originating claim as

## AGEINT upstream
`docs/ageint/cognitive-security.md`
