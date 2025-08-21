"""Formatting helpers for CLI and report output."""

from __future__ import annotations

import json
from typing import Any, Iterable

from rich.console import Console
from rich.table import Table

console = Console()


def print_table(table: Table) -> None:
    """Render a Rich table to the console."""
    console.print(table)


def to_json(data: Any) -> str:
    """Return *data* as a pretty-printed JSON string."""
    return json.dumps(data, indent=2, sort_keys=True)


def to_markdown(headers: Iterable[str], rows: Iterable[Iterable[str]]) -> str:
    """Render a Markdown table from *headers* and *rows*."""
    header_line = " | ".join(headers)
    sep_line = " | ".join(["---"] * len(list(headers)))
    data_lines = [" | ".join(map(str, r)) for r in rows]
    return "\n".join([header_line, sep_line, *data_lines])
