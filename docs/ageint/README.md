# AGEINT — Educational Upstream for CogSecSkills

CogSecSkills is the *applied* layer: agentic tool-use implementations of analytic
tradecraft. **AGEINT is the educational upstream** — the curriculum that teaches
the concepts each skill operationalizes. This folder vendors the relevant
educational material so every skill can cite its conceptual grounding locally.

## What AGEINT is

> AGEINT — *Agentic Intelligence: A Modular Atlas, Library, Course, Textbook,
> Cookbook, and Playbook* (Daniel Ari Friedman, Active Inference Institute).
> It teaches intelligence tradecraft, the IC cycle, OSINT/GEOINT integrity,
> FININT/economic security, declassified intelligence history, agentic-AI
> governance, cognitive security, counterintelligence, cyber defense, and ICS/OT
> readiness — all **educational, synthetic, accountable, defensive, and bounded
> by legal and human-oversight constraints.**

- **Repository:** <https://github.com/docxology/AGEINT>
- **Concept DOI:** [10.5281/zenodo.20732274](https://doi.org/10.5281/zenodo.20732274)
- **License:** text CC BY 4.0; code Apache-2.0

CogSecSkills inherits AGEINT's defensive, accountable posture: these skills exist
to **recognize, assess, and defend against** cognitive attack — never to author
manipulation or run influence operations.

## Topic primers

Each skill's `skill.yaml` carries an `ageint_topic` that points to one of these
primers. They are the conceptual reference a skill's workflow draws on.

| Primer | Skill group it grounds |
|--------|------------------------|
| [`structured-analytic-techniques.md`](structured-analytic-techniques.md) | `skills/sat/` |
| [`cognitive-security.md`](cognitive-security.md) | `skills/cognitive_security/` |
| [`adversarial-assurance.md`](adversarial-assurance.md) | `skills/critical_review/` |
| [`osint-integrity.md`](osint-integrity.md) | `skills/osint_integrity/` |
| [`counterintelligence.md`](counterintelligence.md) | `skills/counterintelligence/` |
| [`information-environment.md`](information-environment.md) | `skills/information_environment/` |
| [`research-methods.md`](research-methods.md) | `skills/research_methods/` |

## Plan ↔ build ↔ teach

Three artifacts stay in sync:

1. **Teach** — these AGEINT primers (the *why*).
2. **Plan** — [`registry/skills.yaml`](../../registry/skills.yaml), the catalogue of
   all 100 skill areas (the *what*).
3. **Build** — [`skills/`](../../skills/), the multiharness skill implementations
   (the *how*).

The validation gate (`python -m cogsecskills validate`) keeps plan and build
coherent; each primer's mapping table keeps teach aligned to both.
