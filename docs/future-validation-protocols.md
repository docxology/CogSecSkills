# Future Validation Protocols

These protocols define future work. They are not completed validation and must
not be cited as evidence of field effectiveness, live connector support, or
publication readiness.

## Exploratory Baseline Comparison

Purpose: compare CogSecSkills-guided answers against unstructured prompting on
the same defensive fixtures.

Minimum design:

- Use the existing scenario ids and expected-answer sections as the fixture set.
- Run one CogSecSkills-guided answer and one unstructured-prompt answer per
  scenario.
- Score both with `docs/analyst-output-review.md`.
- Report results as exploratory internal evaluation unless independently
  reviewed.

Disallowed claims: superiority, benchmark status, or field effectiveness.

## Analyst Usability Pilot

Purpose: check whether analysts can find, load, and apply the right skill.

Minimum design:

- Recruit reviewers who understand the defensive-use boundary.
- Give each reviewer the quickstart, harness cookbook, and a fixed scenario.
- Record friction points, selected skill, missing information, and output
  clarity.
- Keep notes anonymized and separate from private operational data.

Disallowed claims: organization-wide usability, training efficacy, or operational
readiness.

## Live Connector Readiness

Purpose: prepare for optional OSINT/web connector integration without creating
privacy or misuse debt.

Minimum design:

- Name the connector, data class, terms-of-use constraints, rate limits, and
  custody fields.
- Add tests that prove connector outputs preserve source URL, timestamp,
  collection method, and uncertainty.
- Require privacy/legal review for people, accounts, location, or platform data.
- Keep connector failures explicit rather than filling gaps with inference.

Disallowed claims: complete collection, legal sufficiency, attribution certainty,
or live platform coverage.

## Publication And DOI Readiness

Purpose: prepare release metadata without inventing archive status.

Minimum design:

- Run `docs/release-checklist.md`.
- Verify citation metadata and generated manuscript outputs.
- Confirm repository URL, license, version, and source revision.
- Add DOI or archive fields only after a real external archive exists.

Disallowed claims: peer review, archive DOI, or public release until those
artifacts are real.
