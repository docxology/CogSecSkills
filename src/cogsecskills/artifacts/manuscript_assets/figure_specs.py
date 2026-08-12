"""The figure registry: what each generated figure is and what it answers.

``FIGURES`` is the single source of truth for figure filenames, so the drift
gate in ``assets_io`` and the manuscript tables agree on the set by construction.
"""

from __future__ import annotations

from dataclasses import dataclass

from .paths import COVER_IMAGE_NAME


@dataclass(frozen=True)
class FigureMetadata:
    filename: str
    source: str
    reader_question: str
    semantic_labels: tuple[str, ...]
    mirrored: bool = False


FIGURES = (
    FigureMetadata(
        "cogsecskills_taxonomy_counts.png",
        "../output/figures/cogsecskills_taxonomy_counts.png",
        "How are skills distributed across the seven taxonomy groups?",
        ("Taxonomy", "skill counts", "share"),
    ),
    FigureMetadata(
        "cogsecskills_skill_grid.png",
        "../output/figures/cogsecskills_skill_grid.png",
        "Can the reader scan all 100 skills as one compact library surface?",
        ("100 skills", "library atlas", "group"),
    ),
    FigureMetadata(
        "cogsecskills_verb_heatmap.png",
        "../output/figures/cogsecskills_verb_heatmap.png",
        "Which groups exercise which neutral tool verbs most often?",
        ("verb", "heatmap", "group"),
    ),
    FigureMetadata(
        "cogsecskills_ageint_network.png",
        "../output/figures/cogsecskills_ageint_network.png",
        "How do skill groups connect to AGEINT teaching topics?",
        ("AGEINT", "teaching", "topic"),
    ),
    FigureMetadata(
        "cogsecskills_plan_build_teach_flow.png",
        "../output/figures/cogsecskills_plan_build_teach_flow.png",
        "How do plan, build, teach, validation, and manuscript generation fit together?",
        ("Plan", "Build", "Teach", "Run"),
    ),
    FigureMetadata(
        "cogsecskills_reference_density.png",
        "../output/figures/cogsecskills_reference_density.png",
        "Which groups carry the deepest declared source-reference backing per skill?",
        ("Reference Density", "references", "metadata"),
    ),
    FigureMetadata(
        "cogsecskills_harness_contract.png",
        "../output/figures/cogsecskills_harness_contract.png",
        "Does each group maintain configured harness adapter coverage?",
        ("Harness Contract", "adapter", "coverage"),
    ),
    FigureMetadata(
        COVER_IMAGE_NAME,
        "../output/figures/cogsecskills_cover_installation.png",
        "How does a reader install CogSecSkills from GitHub into an agent harness?",
        ("GitHub", "install", "harness"),
        mirrored=True,
    ),
)

FIGURE_NAMES = tuple(figure.filename for figure in FIGURES)
