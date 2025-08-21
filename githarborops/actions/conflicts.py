"""Detect merge conflicts in the repository."""

import subprocess
from rich.console import Console
from rich.table import Table

from githarborops.git_utils import run_git_command


console = Console()


def show(repo_path: str) -> None:
    """Display unmerged paths and conflict markers."""

    unmerged = run_git_command(
        repo_path, ["diff", "--name-only", "--diff-filter=U"]
    ).stdout.strip()
    if unmerged:
        table = Table(title="Unmerged paths")
        table.add_column("Path", style="yellow")
        for path in unmerged.splitlines():
            table.add_row(path)
        console.print(table)
    else:
        console.print("[green]No unmerged paths.[/]")

    try:
        rg = subprocess.run(
            ["rg", "<<<<<<<"],
            cwd=repo_path,
            text=True,
            capture_output=True,
            check=False,
        )
        if rg.stdout.strip():
            table = Table(title="Conflict markers")
            table.add_column("Location", style="red")
            for line in rg.stdout.strip().splitlines():
                table.add_row(line)
            console.print(table)
        else:
            console.print("[green]\nNo conflict markers detected.[/]")
    except FileNotFoundError:
        console.print("[red]ripgrep (rg) not installed.[/]")
