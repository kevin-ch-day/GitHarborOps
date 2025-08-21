"""Standardized table layouts."""

from typing import Iterable, Sequence

from rich.table import Table


def branches_table(rows: Iterable[Sequence[str]]) -> Table:
    """Return a table for branch information."""
    table = Table(title="Local Branches")
    table.add_column("Branch", style="cyan")
    table.add_column("Upstream", style="magenta")
    table.add_column("Ahead", style="green")
    table.add_column("Behind", style="red")
    for branch, upstream, ahead, behind in rows:
        table.add_row(branch, upstream or "(none)", ahead or "0", behind or "0")
    return table


def simple_table(title: str, headers: Sequence[str], rows: Iterable[Sequence[str]]) -> Table:
    """Generic helper to construct a table."""
    table = Table(title=title)
    for head in headers:
        table.add_column(head)
    for row in rows:
        table.add_row(*[str(c) for c in row])
    return table
