"""Generated Markdown supplements, data exports, and the LaTeX cell helpers.

Renders the all-skill catalogue and the metadata matrix, serializes the rows to
JSON and CSV, and computes the canonical expected text for each generated file
used by both the writer and the drift checker.
"""

from __future__ import annotations

import csv
import io
import json
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Iterable

from cogsecskills.core.spec import ToolVerb

from .figures import FIGURES
from .paths import (
    CATALOGUE_PATH,
    DATA_CSV_PATH,
    DATA_JSON_PATH,
    GENERATED_HEADER,
    MATRIX_PATH,
)
from .rows import (
    SkillRow,
    _clean_cell,
    _group_ids,
    _group_title,
    _join,
    collect_skill_rows,
)


def _latex_escape(value: object) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in str(value).strip())


def _latex_lines(values: Iterable[object]) -> str:
    return r"\newline ".join(
        _latex_escape(value) for value in values if str(value).strip()
    )


def _latex_labeled(label: str, value: object) -> str:
    return rf"\textbf{{{label}:}} {_latex_escape(value)}"


def _latex_breakable_path(value: object) -> str:
    escaped = _latex_escape(value)
    return escaped.replace("/", r"/\allowbreak{}").replace(r"\_", r"\_\allowbreak{}")


def render_skill_catalogue(rows: list[SkillRow]) -> str:
    """Render the generated all-skill supplemental catalogue."""
    lines = [
        GENERATED_HEADER,
        "",
        "# Supplemental 100-Skill Catalogue {#sec:supplemental_skill_catalogue}",
        "",
        "This generated supplement lists the live CogSecSkills library by taxonomy "
        "group. Each row is derived from `registry/skills.yaml` and the matching "
        "`skills/<group>/<slug>/skill.yaml` file, so the catalogue can be checked "
        "for drift with `python -m cogsecskills manuscript-assets --check`.",
        "",
    ]

    for group_id in _group_ids(rows):
        group_rows = [row for row in rows if row.group == group_id]
        title = group_rows[0].group_title if group_rows else group_id
        lines.extend(
            [
                f"## {title} (`{group_id}`)",
                "",
                f"{len(group_rows)} skills in this group.",
                "",
                r"\begingroup",
                r"\scriptsize",
                r"\setlength{\tabcolsep}{1.8pt}",
                r"\renewcommand{\arraystretch}{1.02}",
                r"\begin{longtable}{@{}"
                r">{\raggedright\arraybackslash}p{0.105\linewidth}"
                r">{\raggedright\arraybackslash}p{0.13\linewidth}"
                r">{\raggedright\arraybackslash}p{0.095\linewidth}"
                r">{\raggedright\arraybackslash}p{0.135\linewidth}"
                r">{\raggedright\arraybackslash}p{0.455\linewidth}@{}}",
                r"\toprule",
                (
                    r"\textbf{Skill} & \textbf{Functionality} & "
                    r"\textbf{Use when} & \textbf{Metadata} & "
                    r"\textbf{Quality capsule}\\"
                ),
                r"\midrule",
                r"\endfirsthead",
                r"\toprule",
                (
                    r"\textbf{Skill} & \textbf{Functionality} & "
                    r"\textbf{Use when} & \textbf{Metadata} & "
                    r"\textbf{Quality capsule}\\"
                ),
                r"\midrule",
                r"\endhead",
                r"\bottomrule",
                r"\endfoot",
            ]
        )
        for row in group_rows:
            metadata = r"\newline ".join(
                (
                    _latex_escape(f"Verbs: {_join(row.verbs)}"),
                    _latex_escape(f"Inputs: {_join(row.inputs)}"),
                    _latex_escape(f"Outputs: {_join(row.outputs)}"),
                    _latex_escape(
                        f"AGEINT: {row.ageint_topic}; refs: {row.references_count}"
                    ),
                    rf"Source: {_latex_breakable_path(row.source_path)}",
                )
            )
            quality = r"\par\smallskip ".join(
                (
                    _latex_labeled("Boundary", row.defensive_boundary),
                    _latex_labeled("Evidence", row.evidence_discipline),
                    _latex_labeled("Confidence", row.confidence_anchor),
                    _latex_labeled("Unsafe redirect", row.unsafe_redirect),
                    _latex_labeled("Safe defensive", row.safe_defensive_pattern),
                )
            )
            skill = (
                rf"\texttt{{{_latex_escape(row.id)}}}"
                + r"\newline "
                + _latex_escape(row.name)
            )
            lines.append(
                " & ".join(
                    (
                        skill,
                        _latex_escape(row.functionality),
                        _latex_escape(row.use_when),
                        metadata,
                        quality,
                    )
                )
                + r"\\"
            )
        lines.extend([r"\end{longtable}", r"\endgroup", ""])

    return "\n".join(lines).rstrip() + "\n"


def render_metadata_matrix(rows: list[SkillRow]) -> str:
    """Render compact generated matrices over the skill metadata."""
    verbs = tuple(v.value for v in ToolVerb)
    group_counts = Counter(row.group for row in rows)
    ageint_counts = Counter(row.ageint_topic for row in rows)
    harness_counts = Counter(h for row in rows for h in row.harnesses)

    lines = [
        GENERATED_HEADER,
        "",
        "# Supplemental Skill Metadata and Figure Matrix {#sec:supplemental_skill_metadata_matrix}",
        "",
        "This generated matrix view summarizes group sizes, tool-verb coverage, "
        "AGEINT crosswalks, and harness adapter coverage across the same skill rows "
        "used in the supplemental catalogue.",
        "",
        "## Group Counts",
        "",
        "| Group | Title | Skills |",
        "| --- | --- | ---: |",
    ]
    for group_id in _group_ids(rows):
        lines.append(
            f"| `{group_id}` | {_clean_cell(_group_title(rows, group_id))} | "
            f"{group_counts[group_id]} |"
        )

    lines.extend(
        [
            "",
            "## Tool Verb Usage By Group",
            "",
            "| Group | " + " | ".join(f"`{verb}`" for verb in verbs) + " |",
            "| --- | " + " | ".join("---:" for _ in verbs) + " |",
        ]
    )
    by_group_verb: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        for verb in row.verbs:
            by_group_verb[row.group][verb] += 1
    for group_id in _group_ids(rows):
        counts = by_group_verb[group_id]
        lines.append(
            f"| `{group_id}` | "
            + " | ".join(str(counts.get(verb, 0)) for verb in verbs)
            + " |"
        )

    lines.extend(
        [
            "",
            "## AGEINT Crosswalk",
            "",
            "| AGEINT topic | Groups represented | Skills |",
            "| --- | --- | ---: |",
        ]
    )
    for topic, count in sorted(
        ageint_counts.items(), key=lambda item: (-item[1], item[0])
    ):
        groups = sorted({row.group for row in rows if row.ageint_topic == topic})
        lines.append(f"| `{topic}` | {_clean_cell(_join(groups))} | {count} |")

    lines.extend(
        [
            "",
            "## Harness Coverage",
            "",
            "| Harness | Skills declaring adapter |",
            "| --- | ---: |",
        ]
    )
    for harness in sorted(harness_counts):
        lines.append(f"| `{harness}` | {harness_counts[harness]} |")

    quality_capsule_count = sum(
        1
        for row in rows
        if row.defensive_boundary != "not declared"
        and row.evidence_discipline != "not declared"
        and row.confidence_anchor != "not declared"
        and row.unsafe_redirect != "not declared"
        and row.safe_defensive_pattern != "not declared"
    )
    lines.extend(
        [
            "",
            "## Quality Capsule Coverage",
            "",
            "| Capsule field set | Skills with complete generated capsule |",
            "| --- | ---: |",
            (
                "| boundary + evidence + confidence + unsafe redirect + safe defensive pattern | "
                f"{quality_capsule_count} |"
            ),
        ]
    )

    lines.extend(
        [
            "",
            "## Generated Figure Inventory",
            "",
            "| Figure source | Reader question answered |",
            "| --- | --- |",
        ]
    )
    for figure in FIGURES:
        lines.append(f"| `{figure.source}` | {figure.reader_question} |")

    return "\n".join(lines).rstrip() + "\n"


def _rows_as_json(rows: list[SkillRow]) -> str:
    return json.dumps([asdict(row) for row in rows], indent=2, sort_keys=True) + "\n"


def _rows_as_csv(rows: list[SkillRow]) -> str:
    fields = tuple(asdict(rows[0]).keys()) if rows else tuple(SkillRow.__annotations__)
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        payload = asdict(row)
        for field, value in tuple(payload.items()):
            if isinstance(value, tuple):
                payload[field] = "; ".join(value)
        writer.writerow(payload)
    return stream.getvalue()


def _expected_texts(root: Path | None = None) -> dict[Path, str]:
    rows = collect_skill_rows(root)
    return {
        CATALOGUE_PATH: render_skill_catalogue(rows),
        MATRIX_PATH: render_metadata_matrix(rows),
        DATA_JSON_PATH: _rows_as_json(rows),
        DATA_CSV_PATH: _rows_as_csv(rows),
    }
