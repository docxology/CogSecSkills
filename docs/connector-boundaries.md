# Connector Boundary Notes

Some skills declare `search` or `web` because defensive analysis may need
external source lookup. The current repository does not wire live OSINT,
browser, platform, or paid-data connectors into the validation gates.

## Allowed Connector Roles

- Retrieve public sources for provenance, corroboration, and citation checks.
- Preserve source URLs, timestamps, collection method, and uncertainty.
- Support defensive review of public claims, media, narratives, and datasets.
- Enforce rate limits, terms of service, and privacy/legal constraints.

## Required Review Checks

- Confirm the request is defensive, authorized, and proportionate.
- Avoid private personal data unless the user supplies lawful authorization and
  the skill explicitly supports that context.
- Label source material separately from inference.
- Preserve unknowns, conflicts, missing data, and confidence limits.
- Refuse requests to target, manipulate, harass, evade safeguards, or expose
  private identity/location information.

## Out Of Scope For This Repo

- Live account scraping or platform automation.
- Private-person identification, doxing, or location exposure.
- Influence-operation optimization.
- Connector performance benchmarks.
- Claims that a connector output is complete, authentic, or legally sufficient.

Connector integration should add its own tests and documentation before being
described as supported.

Use `future-validation-protocols.md` before adding any live connector readiness
claim.
