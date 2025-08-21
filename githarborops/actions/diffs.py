"""Show diffs against a base branch."""

from rich.console import Console
from rich.syntax import Syntax
import questionary

from githarborops.git_utils import run_git_command


console = Console()


def show(repo_path: str) -> None:
    """Display diff against a selected base branch."""

    branches = run_git_command(
        repo_path, ["branch", "--format", "%(refname:short)"]
    ).stdout.splitlines()
    if not branches:
        console.print("[yellow]No branches found.[/]")
        return

    default_base = (
        "main" if "main" in branches else "master" if "master" in branches else branches[0]
    )
    base_branch = questionary.select(
        "Select base branch:", choices=branches, default=default_base
    ).ask()
    if not base_branch:
        return

    result = run_git_command(repo_path, ["diff", base_branch])
    if result.stdout.strip():
        console.print(Syntax(result.stdout, "diff"))
    else:
        console.print("[green]No differences.[/]")
