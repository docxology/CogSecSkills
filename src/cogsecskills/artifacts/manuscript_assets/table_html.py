"""Escaped HTML counterparts for the supplements' print-specific tables."""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping, Sequence
from html import escape

from .rows import SkillRow, _join


def _table(
    headers: Sequence[str],
    rows: Sequence[Sequence[str]],
    name: str,
    widths: Sequence[int],
) -> str:
    """Wrap internally constructed, escaped cell markup in a raw HTML block."""
    lines = [
        '<div style="overflow-x:auto">',
        f'<table class="{name}" style="width:100%;min-width:52rem;'
        'table-layout:fixed;border-collapse:collapse;overflow-wrap:anywhere">',
        "<colgroup>"
        + "".join(f'<col style="width:{width}%">' for width in widths)
        + "</colgroup>",
        "<thead><tr>"
        + "".join(f'<th scope="col">{escape(header)}</th>' for header in headers)
        + "</tr></thead>",
        "<tbody>",
    ]
    for cells in rows:
        lines.append(
            '<tr><th scope="row" style="font-weight:normal;text-align:left;'
            'vertical-align:top;background:transparent;color:#1d2933">'
            + cells[0]
            + "</th>"
            + "".join(
                f'<td style="vertical-align:top">{cell}</td>' for cell in cells[1:]
            )
            + "</tr>"
        )
    lines.extend(["</tbody></table>", "</div>"])
    payload = "\n".join(lines)
    longest_run = max((len(run) for run in re.findall(r"`+", payload)), default=0)
    fence = "`" * max(3, longest_run + 1)
    return f"{fence}{{=html}}\n{payload}\n{fence}\n"


def _code(value: str) -> str:
    return (
        '<code style="white-space:normal;overflow-wrap:anywhere">'
        + escape(value)
        + "</code>"
    )


def render_html_skill_table(rows: Sequence[SkillRow]) -> str:
    """Retain every catalogue field in the web manuscript without raw TeX."""
    cells = []
    for row in rows:
        metadata = "<br>".join(
            escape(value)
            for value in (
                f"Verbs: {_join(row.verbs)}",
                f"Inputs: {_join(row.inputs)}",
                f"Outputs: {_join(row.outputs)}",
                f"AGEINT: {row.ageint_topic}; refs: {row.references_count}",
                f"Source: {row.source_path}",
            )
        )
        quality = "".join(
            f"<p><strong>{label}:</strong> {escape(value)}</p>"
            for label, value in (
                ("Boundary", row.defensive_boundary),
                ("Evidence", row.evidence_discipline),
                ("Confidence", row.confidence_anchor),
                ("Unsafe redirect", row.unsafe_redirect),
                ("Safe defensive", row.safe_defensive_pattern),
            )
        )
        cells.append(
            (
                _code(row.id) + "<br>" + escape(row.name),
                escape(row.functionality),
                escape(row.use_when),
                metadata,
                quality,
            )
        )
    return _table(
        ("Skill", "Functionality", "Use when", "Metadata", "Quality capsule"),
        cells,
        "skill-catalogue",
        (14, 15, 14, 17, 40),
    )


def render_html_verb_matrix(
    groups: Sequence[str], verbs: Sequence[str], counts: Mapping[str, Counter[str]]
) -> str:
    """Render the same exact group ids and counts as the printed verb matrix."""
    cells = [
        (_code(group), *(str(counts[group].get(verb, 0)) for verb in verbs))
        for group in groups
    ]
    return _table(("Group", *verbs), cells, "verb-matrix", (28, *(9 for _ in verbs)))
