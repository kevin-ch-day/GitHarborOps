#!/usr/bin/env python3
"""
GitHarborOps - Interactive Git management tool.
"""

import os
import sys
from pathlib import Path
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


def main():
    """Entry point for GitHarborOps CLI."""

    # Discover repos from derived search root
    repos = find_git_repos()
    if not repos:
        base_dir = Path(os.environ.get("GITHARBOROPS_REPOS", Path.cwd())).expanduser().resolve()
        sys.stderr.write(
            f"[X] No Git repositories found in {base_dir}. "
            "Add some projects first.\n"
        )
        sys.exit(1)

    # Select a repo
    if len(repos) == 1:
        repo_path = repos[0]
    else:
        repo_path = menu.select_repo(
            repos, instruction="Use arrow keys and press Enter to select"
        )

    if not repo_path:
        print("No repository selected. Exiting.")
        sys.exit(0)

    # Main interactive loop
    while True:
        choice = menu.select_action(
            f"GitHarborOps - {repo_path}",
            [
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
            ],
        )

        if not choice:
            break

        if choice.startswith("1"):
            overview.show(repo_path)

        elif choice.startswith("2"):
            status.show(repo_path)

        elif choice.startswith("3"):
            branches.show(repo_path)

        elif choice.startswith("4"):
            print(run_git_command(repo_path, ["fetch", "--all", "--prune"]).stdout)

        elif choice.startswith("5"):
            diffs.show(repo_path)

        elif choice.startswith("6"):
            conflicts.show(repo_path)

        elif choice.startswith("7"):
            logs.show(repo_path)

        elif choice.startswith("8"):
            logs.last_commit(repo_path)

        elif choice.startswith("9"):
            stashes.show(repo_path)

        else:
            print("Bye 👋")
            break


if __name__ == "__main__":
    main()
