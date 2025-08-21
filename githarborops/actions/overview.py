"""Show repository overview information."""

from rich.console import Console
from rich.table import Table

from githarborops.git_utils import (
    get_current_branch,
    get_repo_root,
    run_git_command,
)

console = Console()


def show(repo_path: str) -> None:
    """Display basic information about the repository.

    Args:
        repo_path: Path to the git repository.
    """

    try:
        repo_root = get_repo_root(repo_path)

        branch_raw = get_current_branch(repo_path)
        branch = "(detached HEAD)" if branch_raw in {"HEAD", "unknown"} else branch_raw

        upstream_proc = run_git_command(
            repo_path,
            ["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
        )
        upstream_branch = (
            upstream_proc.stdout.strip() if upstream_proc.returncode == 0 else "(none)"
        )

        name_proc = run_git_command(repo_path, ["config", "user.name"])
        email_proc = run_git_command(repo_path, ["config", "user.email"])
        user_name = name_proc.stdout.strip() if name_proc.returncode == 0 else "(unset)"
        user_email = email_proc.stdout.strip() if email_proc.returncode == 0 else ""
        user = f"{user_name} <{user_email}>" if user_email else user_name

        remotes_proc = run_git_command(repo_path, ["remote", "-v"])
        remote_lines = (
            remotes_proc.stdout.strip().splitlines()
            if remotes_proc.returncode == 0 and remotes_proc.stdout.strip()
            else []
        )

        conflict_proc = run_git_command(repo_path, ["config", "merge.conflictstyle"])
        conflict_style = (
            conflict_proc.stdout.strip()
            if conflict_proc.returncode == 0 and conflict_proc.stdout.strip()
            else "merge"
        )

        table = Table(title="Repository Overview", show_header=False)
        table.add_column("Property", style="cyan", no_wrap=True)
        table.add_column("Value", style="green")

        table.add_row("Repo root", repo_root)
        table.add_row("Branch", branch)
        table.add_row("Upstream", upstream_branch)
        table.add_row("User", user)

        if remote_lines:
            table.add_row("Remote(s)", remote_lines[0])
            for line in remote_lines[1:]:
                table.add_row("", line)
        else:
            table.add_row("Remote(s)", "(none)")

        table.add_row("Conflict style", conflict_style)

        console.print(table)
    except Exception as exc:  # pragma: no cover - defensive
        console.print(f"[red]Error:[/] {exc}")
