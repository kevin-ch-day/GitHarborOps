"""Standardized table layouts."""

from typing import Iterable, Sequence

from rich.table import Table


def branches_table(rows: Iterable[Sequence[str]]) -> Table:
    """Return a table for branch information."""
    table = Table(
        title="Local Branches",
        header_style="bold navy_blue",
        row_styles=["black on white", "white on #008080"],
    )
    table.add_column("Branch", style="cyan")
    table.add_column("Upstream", style="magenta")
    table.add_column("Ahead", style="green")
    table.add_column("Behind", style="red")
    table.add_column("Status")
    for branch, upstream, ahead, behind in rows:
        ahead = ahead or "0"
        behind = behind or "0"
        ahead_int = int(ahead)
        behind_int = int(behind)
        if ahead_int == 0 and behind_int == 0:
            status = "✅"
        elif ahead_int > 0 and behind_int > 0:
            status = "❌"
        else:
            status = "⚠️"
        table.add_row(branch, upstream or "(none)", ahead, behind, status)
    return table


def simple_table(title: str, headers: Sequence[str], rows: Iterable[Sequence[str]]) -> Table:
    """Generic helper to construct a table."""
    table = Table(
        title=title,
        header_style="bold navy_blue",
        row_styles=["black on white", "white on #008080"],
    )
    for head in headers:
        table.add_column(head)
    for row in rows:
        table.add_row(*[str(c) for c in row])
    return table
