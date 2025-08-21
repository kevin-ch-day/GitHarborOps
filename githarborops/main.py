#!/usr/bin/env python3
"""
GitHarborOps - Interactive Git management tool.
"""

import sys
from pathlib import Path
import questionary

from githarborops.repo_finder import find_git_repos
from githarborops.git_utils import run_git_command
from githarborops.actions import overview, status, branches, diffs, logs, conflicts


def main():
    """Entry point for GitHarborOps CLI."""

    # Base directory where repos are stored (default: ~/Github_Repos)
    base_dir = Path.home() / "Github_Repos"

    # Discover repos
    repos = find_git_repos(str(base_dir))
    if not repos:
        sys.stderr.write(
            f"[X] No Git repositories found in {base_dir}. "
            "Add some projects first.\n"
        )
        sys.exit(1)

    # Select a repo
    repo_path = questionary.select(
        "Select a Git repository:",
        choices=repos,
    ).ask()

    if not repo_path:
        print("No repository selected. Exiting.")
        sys.exit(0)

    # Main interactive loop
    while True:
        choice = questionary.select(
            f"⚓ GitHarborOps - {repo_path}",
            choices=[
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
        ).ask()

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
            print(run_git_command(repo_path, ["show", "--stat", "-1"]).stdout)

        elif choice.startswith("9"):
            print(run_git_command(repo_path, ["stash", "list"]).stdout)

        else:
            print("Bye 👋")
            break


if __name__ == "__main__":
    main()
