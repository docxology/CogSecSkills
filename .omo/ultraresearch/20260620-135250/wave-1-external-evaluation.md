# Wave 1 External Evaluation Digest

Worker: `019ee6d0-1999-7d20-b6a8-fff0708c9398`

Key source-backed findings:
- OpenAI official docs distinguish ordinary tests from evaluations for variable model outputs, and recommend task definition, test inputs, analysis, iteration, traces for agent workflows, graders, and red-team cases.
- OpenAI safety guidance supports adversarial testing, human oversight, and prompt-injection/break-it inputs.
- NIST AI RMF and the Generative AI Profile support lifecycle risk framing, representative evaluation, documentation of measures, and avoidance of extrapolation from narrow anecdotal assessments.
- ISO AI risk/management/impact-assessment standards support governance language but should not be cited as proof of CogSecSkills effectiveness.
- Stanford HAI benchmark guidance supports the key claim-boundary question: what was claimed, what was tested, and whether those match.

Planning implications:
- The next CogSecSkills layer should separate deterministic fixture checks, optional offline model-output evals, human review protocols, and live harness smoke runs as distinct evidence levels.
- Any benchmark/eval language must name the task, setting, scored product, grader, and limitations.
- Red-team fixtures should remain scoped to authorized defensive scenarios and should document assumptions and failure criteria.

Worker EXPAND:
- OpenAI deprecations page and current migration guidance for Evals / Agent Builder.
- NIST AI 800-2 final publication if it replaces the draft.
- More formal inter-rater reliability and rubric-calibration sources for human review design.
- Additional government guidance on AI impact assessment and evaluation documentation, especially if jurisdiction-specific policy language is needed.
- External benchmark-quality research on contamination, dataset leakage, and construct validity if a stricter claims rubric is wanted.

## EXPAND
- LEAD: Eval harness evidence-level taxonomy — WHY: external guidance separates traces, datasets, graders, human review, and red-team fixtures — ANGLE: plan separate local/offline/live lanes.
- LEAD: Rubric calibration protocol — WHY: human review quality depends on anchors and agreement — ANGLE: plan rubric examples, reviewer count, adjudication, and claim limits.

