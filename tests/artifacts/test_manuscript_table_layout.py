"""Layout and content regressions for both manuscript output formats."""

import re
from collections import Counter
from dataclasses import replace
from html.parser import HTMLParser
from pathlib import Path

from cogsecskills.artifacts.manuscript_assets import (
    FIGURES,
    collect_skill_rows,
    render_metadata_matrix,
    render_skill_catalogue,
)
from cogsecskills.core.spec import ToolVerb


class _TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = []
        self.table = None
        self.row = None
        self.cell = None
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.table = []
            self.tables.append(self.table)
        elif tag == "tbody":
            self.in_body = True
        elif tag == "tr" and self.in_body:
            self.row = []
            self.table.append(self.row)
        elif tag in {"th", "td"} and self.in_body:
            self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag in {"th", "td"} and self.cell is not None:
            self.row.append(" ".join(self.cell))
            self.cell = None
        elif tag == "tbody":
            self.in_body = False
        elif tag == "table":
            self.table = None


def _html_blocks(markdown):
    return [
        match["payload"]
        for match in re.finditer(
            r"(?P<fence>`{3,})\{=html\}\n(?P<payload>.*?)\n(?P=fence)",
            markdown,
            re.DOTALL,
        )
    ]


def _parse_html_blocks(markdown):
    parser = _TableParser()
    for block in _html_blocks(markdown):
        parser.feed(block)
    return parser


def test_catalogue_metadata_can_wrap_between_identifier_words():
    rows = collect_skill_rows(Path(__file__).resolve().parents[2])
    aims = next(row for row in rows if row.id == "sat.customer_aims_checklist")
    catalogue = render_skill_catalogue([aims])

    # These names previously overflowed the narrow Metadata column and obscured
    # adjacent evidence text. Keep the complete identifiers and permit breaks.
    assert r"Inputs: product\_\allowbreak{}or\_\allowbreak{}outline" in catalogue
    assert (
        r"gap\_\allowbreak{}and\_\allowbreak{}misalignment\_\allowbreak{}report"
        in catalogue
    )
    assert r"\scriptsize" in catalogue
    assert aims.evidence_discipline in catalogue


def test_figure_inventory_paths_resolve_from_manuscript_source():
    root = Path(__file__).resolve().parents[2]
    manuscript = root / "docs" / "manuscript"
    for figure in FIGURES:
        assert (manuscript / figure.source).resolve() == (
            root / "output" / "figures" / figure.filename
        ).resolve()
        assert (manuscript / figure.source).is_file()


def test_web_catalogue_retains_every_skill_and_evidence_field():
    rows = collect_skill_rows(Path(__file__).resolve().parents[2])
    catalogue = render_skill_catalogue(rows)
    parser = _parse_html_blocks(catalogue)
    web_rows = [row for table in parser.tables for row in table]
    assert len(web_rows) == len(rows) == 100
    assert len(parser.tables) == 7
    for source, cells in zip(rows, web_rows, strict=True):
        assert len(cells) == 5
        assert source.id in cells[0]
        assert source.name in cells[0]
        assert cells[1] == source.functionality
        assert cells[2] == source.use_when
        assert all(value in cells[3] for value in (*source.inputs, *source.outputs))
        assert source.source_path in cells[3]
        assert source.evidence_discipline in cells[4]
        assert source.safe_defensive_pattern in cells[4]


def test_web_catalogue_escapes_source_text_as_data():
    source = collect_skill_rows(Path(__file__).resolve().parents[2])[0]
    literal = '<script>alert("example")</script> & source'
    source = replace(source, name=literal, evidence_discipline=literal)
    catalogue = render_skill_catalogue([source])
    block = _html_blocks(catalogue)[0]
    assert "<script>" not in block
    assert "&lt;script&gt;" in block
    cells = _parse_html_blocks(catalogue).tables[0][0]
    assert literal in cells[0]
    assert literal in cells[4]


def test_multiline_source_cannot_close_the_raw_html_block():
    source = collect_skill_rows(Path(__file__).resolve().parents[2])[0]
    literal = "before\n```\n\n# table-cell-breakout\n\n```{=html}\nafter"
    source = replace(source, evidence_discipline=literal)
    catalogue = render_skill_catalogue([source])
    blocks = _html_blocks(catalogue)
    assert len(blocks) == 1
    assert literal in blocks[0]
    assert "````{=html}\n" in catalogue
    assert catalogue.rstrip().endswith("````")


def test_print_and_web_verb_matrix_preserve_exact_ids_and_counts():
    rows = collect_skill_rows(Path(__file__).resolve().parents[2])
    matrix = render_metadata_matrix(rows)
    verbs = tuple(verb.value for verb in ToolVerb)
    groups = tuple(dict.fromkeys(row.group for row in rows))
    counts = {
        group: Counter(verb for row in rows if row.group == group for verb in row.verbs)
        for group in groups
    }
    web_rows = _parse_html_blocks(matrix).tables[0]
    assert len(web_rows) == len(groups) == 7
    for group, cells in zip(groups, web_rows, strict=True):
        assert cells[0] == group
        assert cells[1:] == [str(counts[group][verb]) for verb in verbs]
        assert " & ".join(cells[1:]) + r"\\" in matrix
    assert r"p{0.27\linewidth}" in matrix
    assert r"\texttt{critical\_\allowbreak{}review}" in matrix
