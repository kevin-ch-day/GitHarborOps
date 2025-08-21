"""Show repository logs and commit information."""

from rich.console import Console
from rich.syntax import Syntax

from githarborops.git_utils import run_git_command


console = Console()


def show(repo_path: str) -> None:
    """Display a git log graph of the last 30 commits."""

    result = run_git_command(
        repo_path,
        ["log", "--oneline", "--graph", "--decorate", "--color", "-n", "30"],
    )
    if result.stdout.strip():
        console.print(Syntax(result.stdout, "ansi"))
    else:
        console.print("[yellow]No commits to display.[/]")


def last_commit(repo_path: str) -> None:
    """Display details of the last commit."""

    result = run_git_command(repo_path, ["show", "--stat", "-1", "--color"])
    if result.stdout.strip():
        console.print(Syntax(result.stdout, "ansi"))
    else:
        console.print("[yellow]No commits found.[/]")
