"""List stashes in the repository."""

from rich.console import Console
from rich.table import Table

from githarborops.git_utils import run_git_command


console = Console()


def show(repo_path: str) -> None:
    """Display git stashes."""

    result = run_git_command(repo_path, ["stash", "list"])
    if result.stdout.strip():
        table = Table(title="Stashes")
        table.add_column("Entry", style="cyan")
        for line in result.stdout.strip().splitlines():
            table.add_row(line)
        console.print(table)
    else:
        console.print("[green]No stashes found.[/]")
