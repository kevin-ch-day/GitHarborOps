"""List repository branches with tracking information."""

from githarborops.git_utils import run_git_command
from githarborops.utils.display_utils import formatter, notifications, tables


def show(repo_path: str) -> None:
    """Display local branches with upstream and ahead/behind counts."""

    result = run_git_command(
        repo_path,
        [
            "for-each-ref",
            "--format=%(refname:short)|%(upstream:short)|%(ahead)|%(behind)",
            "refs/heads",
        ],
    )

    lines = [l for l in result.stdout.strip().splitlines() if l]
    if not lines:
        notifications.notify_warn("No branches found.")
        return

    rows = [line.split("|") for line in lines]
    table = tables.branches_table(rows)
    formatter.print_table(table)
