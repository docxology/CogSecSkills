# AGEINT — Educational Upstream for CogSecSkills

CogSecSkills is the *applied* layer: agentic tool-use implementations of analytic
tradecraft, delivered as 100 skills across 7 groups (`sat`,
`cognitive_security`, `critical_review`, `osint_integrity`,
`counterintelligence`, `information_environment`, `research_methods`).
**AGEINT is the educational upstream** — the curriculum that teaches the concepts
each skill operationalizes. This folder vendors the relevant educational material
so every skill can cite its conceptual grounding locally, without a reader having
to leave the repository to learn *why* a procedure is shaped the way it is.

This page is the index for that upstream. Read it to understand what AGEINT is,
how its seven topic primers map onto the seven skill groups, and how to move from
a concept you want to learn to the skill that runs it.

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

AGEINT is the *concept* layer; CogSecSkills is the *practice* layer that turns
those concepts into bounded, inspectable agentic procedures. The relationship is
deliberately one-directional: skills depend on the curriculum for their meaning,
and the curriculum never depends on any single skill's implementation. That
separation is what lets a reviewer audit a skill against the tradecraft it claims
to embody — the primer states the standard, the skill is measured against it.

CogSecSkills inherits AGEINT's defensive, accountable posture: these skills exist
to **recognize, assess, and defend against** cognitive attack — never to author
manipulation or run influence operations. Every primer restates this framing in
its own domain so the boundary travels with the concept, not just with the
top-level disclaimer.

## The seven primers and the groups they ground

Each skill's `skill.yaml` carries an `ageint_topic` that points to one of the
primers below. The pointer is the conceptual reference a skill's workflow draws
on, and the mapping is one primer to one skill group — a clean 7-to-7
correspondence that makes the curriculum and the library navigable as a single
structure.

| Primer | Skill group it grounds | What the group does |
|--------|------------------------|---------------------|
| [`structured-analytic-techniques.md`](structured-analytic-techniques.md) | `skills/sat/` | Externalize and debias the analyst's own reasoning (ACH, Key Assumptions Check, premortem, indicators). |
| [`cognitive-security.md`](cognitive-security.md) | `skills/cognitive_security/` | Characterize and counter cognitive attacks — narrative threats, manipulation techniques, inoculation. |
| [`adversarial-assurance.md`](adversarial-assurance.md) | `skills/critical_review/` | Stress-test claims, analyses, and systems against an explicit adversary model, including the flagship `red_team_review`. |
| [`osint-integrity.md`](osint-integrity.md) | `skills/osint_integrity/` | Keep open-source collection honest — provenance, verification, and chain-of-custody discipline. |
| [`counterintelligence.md`](counterintelligence.md) | `skills/counterintelligence/` | Detect deception, denial, and influence directed at the analyst or the collection process. |
| [`information-environment.md`](information-environment.md) | `skills/information_environment/` | Map and assess the information terrain a decision is being made within. |
| [`research-methods.md`](research-methods.md) | `skills/research_methods/` | Apply rigorous, reproducible method to the evidence base behind every judgment. |

Each primer follows the same internal shape — *what the concept is*, *why it
matters for cognitive security*, *core concepts*, *how CogSecSkills
operationalizes it*, a *defensive & ethical framing*, and *further study* — so a
reader can predict where to look once they have read one. The `critical_review`
group has been deepened most recently: `red_team_review` now carries an explicit
adversary model, an attack-surface taxonomy, an exploitability × impact scoring
rubric, and a go/no-go output, and the
[`adversarial-assurance.md`](adversarial-assurance.md) primer is the conceptual
ground that work is measured against.

## How to move from concept to skill

A reader should travel the upstream in one direction — concept first, then the
procedure that runs it:

1. **Start from the primer.** Pick the [primer](#the-seven-primers-and-the-groups-they-ground)
   for the domain you care about and read its *core concepts* and *defensive &
   ethical framing* sections. This is the *why* — the tradecraft and the bounds
   it must stay inside.
2. **Cross to the catalogue.** Each primer's *how CogSecSkills operationalizes
   this* section names the procedures the group implements. Find the matching
   entries in [`registry/skills.yaml`](../../registry/skills.yaml) by their
   `<group>.<slug>` id (for example `sat.analysis_of_competing_hypotheses`) to
   confirm a skill exists and read its one-line summary.
3. **Open the implementation.** Go to the skill's directory under
   [`skills/`](../../skills/) for the multiharness workflow — the *how*. The
   skill produces a structured, inspectable artifact rather than an opaque
   verdict, so its output can be reviewed against the standard the primer set.
4. **Close the loop back to the concept.** When a skill's output raises a
   question of method or framing, return to its `ageint_topic` primer rather than
   reasoning ad hoc. The primer is the source of truth for what the procedure is
   supposed to mean.

## Plan ↔ build ↔ teach

Three artifacts stay in sync, one per layer of the system:

1. **Teach** — these AGEINT primers (the *why*).
2. **Plan** — [`registry/skills.yaml`](../../registry/skills.yaml), the catalogue of
   all 100 skill areas (the *what*).
3. **Build** — [`skills/`](../../skills/), the multiharness skill implementations
   (the *how*).

The validation gate (`python -m cogsecskills validate`) keeps plan and build
coherent — every catalogued skill must have a real implementation, and every
implementation must be catalogued. Each primer's mapping table keeps teach
aligned to both, so the curriculum, the catalogue, and the code describe the same
100 skills from three angles rather than drifting into three separate stories.
