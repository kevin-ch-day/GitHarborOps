"""Show repository status information."""

from rich.console import Console
from rich.table import Table

from githarborops.git_utils import run_git_command


console = Console()


def show(repo_path: str) -> None:
    """Display git status, changed files, and untracked files."""

    status = run_git_command(repo_path, ["status", "-sb"])
    console.print(status.stdout.rstrip() or "[green]Clean working tree[/]")

    changed = run_git_command(repo_path, ["diff", "--name-only"]).stdout.strip()
    if changed:
        table = Table(title="Changed files since HEAD")
        table.add_column("Path", style="yellow")
        for path in changed.splitlines():
            table.add_row(path)
        console.print(table)
    else:
        console.print("[green]No changes since HEAD.[/]")

    untracked = run_git_command(
        repo_path, ["ls-files", "--others", "--exclude-standard"]
    ).stdout.strip()
    if untracked:
        table = Table(title="Untracked files")
        table.add_column("Path", style="red")
        for path in untracked.splitlines():
            table.add_row(path)
        console.print(table)
    else:
        console.print("[green]No untracked files.[/]")
