# Symbols and Skill-System Glossary {#sec:symbols_glossary}

## AGEINT

Agentic Intelligence educational material used here as the teaching upstream for
cognitive-security skill topics. Each skill records its teaching topic in the
`ageint_topic` field of its specification, which is the crosswalk between an
implemented skill and the AGEINT primer that explains why it exists.

## Harness

A model or agent runtime interface. CogSecSkills currently targets Claude,
Codex, and Hermes adapters from one neutral skill specification.

## Skill Specification

The `skill.yaml` file in each skill directory. It declares identity, status,
summary, AGEINT topic, tags, triggers, allowed neutral tool verbs, inputs,
outputs, references, workflow path, and harness adapter paths.

## Tool Verb

One of the closed, harness-neutral capability labels accepted by the validator:
`read`, `search`, `write`, `exec`, `reason`, `web`, `delegate`, and `ask`.

## Plan/Build/Teach

The project architecture: `registry/` plans the catalogue, `skills/` builds the
implemented library, and `docs/ageint/` teaches the defensive analytic context.

## Defensive Boundary

The per-skill statement of what the skill is for (recognize, assess, document, or
defend) and what it must not be used for. Enforced as a required field on every
skill specification.

## Misuse Redirect

The per-skill clause that refuses an offensive or manipulative request and points
back to the safe defensive form of the same technique. Required on every skill.

## Negative Control

A paired example that states an unsafe request and the safe defensive response it
should be redirected to. The quality linter rejects reused or boilerplate
negative controls so each skill carries technique-specific ones.

## Scenario Fixture

A curated, deterministic safe-use or unsafe-redirect case in
`scenarios/defensive_readiness.yaml`. Fixtures are local route-and-contract
checks, not live model evaluations.

## Worked Example

A source-owned, expected-answer-shape example for a skill, one per skill,
regenerated into the worked-examples view. It illustrates expected output
structure, not a live model transcript.

## Reference Density

A metadata measure of how many references a skill declares in its specification.
It indicates declared source backing, not evidence quality, citation authority,
or operational validity.
