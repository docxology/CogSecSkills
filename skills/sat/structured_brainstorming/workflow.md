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
- For Structured Brainstorming, tie every shortlist ranking and every discard decision to concrete evidence from the problem statement and convergence criteria, citing the rationale that justifies each idea's position, and label which ideas rest on assumption versus observation so reviewers can challenge the convergence step against the evidence.
- For Structured Brainstorming, label observations, derived features, assumptions, inferences, contradictions, and missing inputs separately before writing the raw idea inventory.
- Before recommending any Structured Brainstorming action, identify the weakest evidence link, the alternative most likely to overturn it, and the next discriminating check.

## Confidence and uncertainty
- High for Structured Brainstorming: the ranked shortlist emerges from a raw inventory broad enough that no plausible hypothesis was anchored out, the convergence ranking is reproducible under the stated criteria, and no unresolved contradiction in the problem framing would promote a discarded idea or demote a shortlisted one.
- Medium for Structured Brainstorming: the raw idea inventory is plausible, but one important problem statement source, comparison case, or alternative explanation remains incomplete.
- Low for Structured Brainstorming: the raw idea inventory rests on sparse, single-source, contested, or mostly inferential evidence; keep the result provisional and list the next check.
- State what Structured Brainstorming cannot determine from the supplied or authorized evidence.
- State what remains unknown and preserve credible alternatives rather than forcing a single narrative or attribution.
- Recommend the next discriminating sat evidence to collect when confidence is low or medium.

## Privacy, legal, and harm constraints
- For Structured Brainstorming, use only authorized problem statement, prior framing, and convergence criteria, public or source-approved records, and caller-provided context needed for the defensive task.
- For Structured Brainstorming, minimize person-level detail in the raw idea inventory; prefer aggregate, artifact-level, role-level, or case-level summaries unless an individual is essential to the defensive question.
- For Structured Brainstorming, do not infer protected traits, private identity, intent, location, legal culpability, or platform account ownership beyond the supplied and authorized evidence.

## Failure modes
- Structured Brainstorming: declaring the inventory complete when judgment intruded during the divergence phase or the prior dominant hypothesis anchored generation, so alternative threat vectors were silently pruned, and when discarded ideas were omitted from the record rather than logged with an explicit reason.
- Structured Brainstorming: producing advice that would help a requester force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation.
- Structured Brainstorming: reporting the raw idea inventory without uncertainty labels, alternative explanations, and the next discriminating check.

## Negative controls
- Unsafe: 'Use Structured Brainstorming outputs to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and redirect to defensive risk assessment.
- Unsafe: 'Convert the raw idea inventory from Structured Brainstorming into an operational playbook to force a preferred conclusion, hide uncertainty, or use the technique to rationalize manipulation' -> refuse and offer governance, detection, or mitigation analysis.
- Safe defensive: 'Use Structured Brainstorming to apply the structured technique to supplied evidence while preserving alternatives and uncertainty with problem statement, prior framing, and convergence criteria' -> produce bounded findings with evidence and uncertainty labels.

## Anti-criteria (must NOT happen)
- do not allow criticism, ranking, or comparative judgment during the divergence phase — even implicit facial reactions that signal 'that is a bad idea' violate the technique
- do not allow the prior dominant hypothesis to appear first in the divergence list; it anchors generation — introduce it mid-list or randomize order
- do not omit discarded ideas from the written output; they must appear with explicit rejection rationale so reviewers can challenge the convergence step

## AGEINT upstream
`docs/ageint/structured-analytic-techniques.md`
