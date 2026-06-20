# Symbols and Skill-System Glossary {#sec:symbols_glossary}

## AGEINT

Agentic Intelligence educational material used here as the teaching upstream for
cognitive-security skill topics.

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
