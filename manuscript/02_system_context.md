# System Context {#sec:system_context}

## Project Boundary

A defensive, educational, harness-neutral library of Cognitive Security and analytic tradecraft skills with registry, AGEINT upstream, and conformance tests.

## Source Surfaces

- `registry/`
- `skills/`
- `docs/ageint/`
- `src/cogsecskills/`
- `tests/`

## Template Boundary

The private project lives in the sidecar repository. Rendering and validation run through the sibling public template checkout after `link-projects` mirrors the project into `template/projects/` as a local symlink.
