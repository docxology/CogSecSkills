# Ethics, Dual-Use, and Responsible Use {#sec:ethics_responsible_use}

Cognitive-security tradecraft is dual-use. The same techniques that let a defender recognize a coordinated influence operation, grade a source, or triage synthetic media can, if inverted, describe how to run such an operation. This section states the project's ethical posture explicitly so that reviewers and adopters do not have to infer it.

## Dual-Use Stance

CogSecSkills is scoped to the *defensive recognition, assessment, documentation, and mitigation* side of every technique it implements. The library contains no offensive playbooks: it does not author manipulation campaigns, fabricate personas, optimize emotional pressure, plan harassment or doxing, or remove human review from high-impact action. Each skill carries an explicit defensive boundary, a misuse-redirect clause that refuses the offensive inverse and points back to the defensive form, and negative-control examples that pair an unsafe request with the safe defensive pattern it should be redirected to. These are not manuscript assertions; they are fields enforced per skill by the quality linter (`doctor`) and visible in the generated worked examples and quality dashboard.

## Defensive by Contract and Review

The defensive boundary is held by two mechanisms working together. The first is structural: the validator proves file and schema conformance, verb legality, adapter coverage, and the presence of the defensive quality bundle on every skill. The second is human review: the governance rule-set in @sec:limitations_next_steps defines, per risk surface, the disallowed output, the allowed defensive transformation, and the review-failure condition, and any skill or adapter that crosses those lines should fail review even when it passes structural validation. The structural gate can prove that the defensive bundle exists; it cannot prove future defensive intent [@ageint2026]. Responsibility for that judgment stays with the maintainers and with anyone who adapts the library to a new organization or runtime.

## Human-Subjects and Institutional Scope

This work is open-source software with no human-subjects component. The scenario fixtures are curated, deterministic route-and-contract checks, and the worked examples are expected-answer shapes; neither is a live model evaluation, a study of human participants, or a record of operational use. No institutional review was required, and no personal data was collected or processed in producing the library, the manuscript, or its generated supplements.

## Responsibilities of Adopters

The library is provided under the Apache License 2.0, on an as-is basis, for defensive analytic work. Adopters remain responsible for using it within applicable law and platform terms, for keeping human review on dual-use and high-impact steps, for not repurposing defensive recognition skills into influence, surveillance, or harassment workflows, and for re-running the conformance and quality gates whenever skills are modified or extended. Distribution of the skills to a new harness does not transfer the defensive judgment those gates cannot encode; that judgment travels with the operator.

## What This Section Does Not Claim

Stating a defensive posture is not the same as proving safety. The gates and the review rule-set reduce the risk that the library ships offensive content or silently drifts; they do not guarantee that every downstream use remains defensive, nor do they make any claim about field effectiveness, which is out of scope for the current local evidence base (see @sec:limitations_next_steps).
