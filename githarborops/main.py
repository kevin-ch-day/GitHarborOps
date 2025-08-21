#!/usr/bin/env python3
"""
GitHarborOps - Interactive Git management tool.
"""

import os
import sys
from pathlib import Path
from typing import List, Optional

from githarborops.repo_finder import find_git_repos
from githarborops.git_utils import run_git_command
from githarborops.actions import (
    overview,
    status,
    branches,
    diffs,
    logs,
    conflicts,
    stashes,
)
from githarborops.utils.display_utils import menu


# -------------------------
# Repo discovery & selection
# -------------------------

def discover_repositories() -> List[Path]:
    """Return a list of available Git repositories."""
    repos = find_git_repos()
    if not repos:
        base_dir = Path(os.environ.get("GITHARBOROPS_REPOS", Path.cwd())).expanduser().resolve()
        sys.stderr.write(
            f"[X] No Git repositories found in {base_dir}. Add some projects first.\n"
        )
        sys.exit(1)

    return [Path(r) for r in repos]


def select_repository(repos: List[Path]) -> Optional[Path]:
    """Allow user to select a repository. Returns None if canceled."""
    if len(repos) == 1:
        return repos[0]

    repo_strs = [str(r) for r in repos]
    selected = menu.select_repo(
        repo_strs, instruction="Use arrow keys and press Enter to select"
    )
    return Path(selected) if selected else None


# -------------------------
# Action Dispatcher
# -------------------------

def run_action(choice: str, repo_path: Path) -> bool:
    """
    Dispatch the selected action.
    Returns False if the loop should exit, True otherwise.
    """
    if choice.startswith("1"):
        overview.show(str(repo_path))

    elif choice.startswith("2"):
        status.show(str(repo_path))

    elif choice.startswith("3"):
        branches.show(str(repo_path))

    elif choice.startswith("4"):
        print(run_git_command(str(repo_path), ["fetch", "--all", "--prune"]).stdout)

    elif choice.startswith("5"):
        diffs.show(str(repo_path))

    elif choice.startswith("6"):
        conflicts.show(str(repo_path))

    elif choice.startswith("7"):
        logs.show(str(repo_path))

    elif choice.startswith("8"):
        logs.last_commit(str(repo_path))

    elif choice.startswith("9"):
        stashes.show(str(repo_path))

    else:
        print("Bye 👋")
        return False

    return True


# -------------------------
# Main Program
# -------------------------

def main():
    """Entry point for GitHarborOps CLI."""
    repos = discover_repositories()
    repo_path = select_repository(repos)

    if not repo_path:
        print("No repository selected. Exiting.")
        sys.exit(0)

    actions = [
        "1) Repo overview",
        "2) Status & changed files",
        "3) Branches",
        "4) Fetch --all --prune",
        "5) Diff vs base",
        "6) Conflicts",
        "7) Log graph (last 30)",
        "8) Last commit",
        "9) Stashes",
        "Quit",
    ]

    while True:
        choice = menu.select_action(actions)
        if not choice:
            break
        if not run_action(choice, repo_path):
            break


if __name__ == "__main__":
    main()
