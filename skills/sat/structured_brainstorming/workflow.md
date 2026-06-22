# Workflow — Structured Brainstorming

Harness-neutral agentic procedure. Each step names the tool verb(s) it uses (see `skill.yaml` → `tools`); a harness adapter binds each verb.

## Step 1 — Frame the problem and set aside prior framing (read)
Read the problem statement. If prior analytic framing exists, note it explicitly and declare it suspended for the divergence phase. Doing so acknowledges the anchor without being constrained by it.

## Step 2 — Diverge: unconstrained idea generation (reason, ask)
Generate every plausible idea, hypothesis, threat vector, or option, including low-probability ones. Defer all judgment. If idea flow is drying up early, ask the analyst: 'What would an adversary want us not to think of here?' and 'What assumption would have to be wrong for a completely different hypothesis to be correct?'

## Step 3 — Cluster and apply convergence criteria (reason)
Group ideas by theme or type. Apply the convergence criteria to rank clusters and individual ideas. Explicitly flag ideas that are novel but low-probability — they belong in the output even if not in the shortlist.

## Step 4 — Produce raw inventory and ranked shortlist (write)
Emit the complete raw idea inventory (divergence output) and the ranked shortlist table (convergence output). For every idea excluded from the shortlist, write a one-line reason. Note any idea suppressed by social or hierarchical pressure that re-emerged during the structured process.

## Evidence requirements
- For Structured Brainstorming, bind each finding to a labeled source — hypotheses, assumptions, indicators, evidence tables, and confidence notes, a cited reference, or an explicitly marked inference — and never present inference as observed evidence.
- For Structured Brainstorming, keep observations, assumptions, inferences, and missing information in separate labeled categories.
- Before issuing any Structured Brainstorming recommendation, name the weakest evidentiary link and the highest-impact missing observation.

## Confidence and uncertainty
- High confidence for Structured Brainstorming: independent lines of hypotheses, assumptions, indicators, evidence tables, and confidence notes converge, credible alternatives have been tested, and the conclusion would survive removing any single source.
- Medium confidence for Structured Brainstorming: the evidence supports the conclusion, but one important input, comparison class, or alternative explanation is still incomplete.
- Low confidence for Structured Brainstorming: the evidence is sparse, single-source, contested, or mostly inferential, so competing explanations must be preserved in the output.
- State plainly what Structured Brainstorming cannot determine from the supplied or authorized evidence.
- Preserve credible alternatives and unresolved unknowns instead of forcing a single narrative or attribution.
- When confidence is not high, name the next discriminating piece of evidence Structured Brainstorming should collect to separate the live alternatives.

## Privacy, legal, and harm constraints
- For Structured Brainstorming, use only data the caller is authorized to analyze, drawn from public or source-approved records.
- For Structured Brainstorming, protect privacy by preferring aggregate, role-level, or artifact-level summaries over individual targeting unless an individual is essential to the defensive question.
- For Structured Brainstorming, do not infer protected traits, private identity, intent, location, or legal culpability beyond the supplied and authorized evidence.

## Failure modes
- Structured Brainstorming failure: using the method as a checklist while skipping diagnostic evidence and disconfirming tests.
- Structured Brainstorming failure: producing guidance that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Brainstorming failure: hiding uncertainty behind generic confidence language instead of stating the evidence limits.

## Negative controls
- Unsafe: 'Use Structured Brainstorming to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Turn Structured Brainstorming into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis instead.
- Safe defensive: 'Use Structured Brainstorming to apply the structured technique to supplied evidence while preserving alternatives and uncertainty' -> produce bounded findings with explicit evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow criticism, ranking, or comparative judgment during the divergence phase — even implicit facial reactions that signal 'that is a bad idea' violate the technique
- do not allow the prior dominant hypothesis to appear first in the divergence list; it anchors generation — introduce it mid-list or randomize order
- do not omit discarded ideas from the written output; they must appear with explicit rejection rationale so reviewers can challenge the convergence step

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
