import os
from pathlib import Path
from typing import List, Tuple


def find_git_repos(base_dir: str | None = None) -> List[Tuple[str, str]]:
    """
    Recursively search for Git repositories under a base directory.

    Args:
        base_dir (str | None): Path to the directory to search. If None,
                               will use $GITHARBOROPS_REPOS or current working dir.

    Returns:
        list[tuple[str, str]]: List of (repo_name, absolute_path) tuples.
    """
    # Resolve base path
    if base_dir is None:
        base_dir = os.environ.get("GITHARBOROPS_REPOS", Path.cwd())

    base = Path(base_dir).expanduser().resolve()
    repos: List[Tuple[str, str]] = []

    if not base.exists() or not base.is_dir():
        print(f"[X] Base directory not found: {base}")
        return repos

    exclude_dirs = {".venv", "venv", "__pycache__", "node_modules"}

    for root, dirs, files in os.walk(base):
        # Clean excluded dirs in-place
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        if ".git" in dirs:
            repo_path = Path(root).resolve()
            repo_name = repo_path.name
            repos.append((repo_name, str(repo_path)))
            # prevent descending further into this repo
            dirs[:] = []

    if not repos:
        print(f"[X] No Git repositories found in {base}")
    return repos
