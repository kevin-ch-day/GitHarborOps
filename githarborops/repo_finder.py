import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Union


@dataclass
class RepoFinderStatus:
    """Information about why repository discovery failed."""

    base: Path
    reason: str


def find_git_repos(
    base_dir: str | None = None,
) -> Union[List[Tuple[str, str]], RepoFinderStatus]:
    """
    Recursively search for Git repositories under a base directory.

    Args:
        base_dir (str | None): Path to the directory to search. If None,
                               will use $GITHARBOROPS_REPOS or current working dir.

    Returns:
        Either a list of ``(repo_name, absolute_path)`` tuples or a
        :class:`RepoFinderStatus` object if the base directory is invalid.
    """
    # Resolve base path
    if base_dir is None:
        base_dir = os.environ.get("GITHARBOROPS_REPOS", Path.cwd())

    base = Path(base_dir).expanduser().resolve()
    repos: List[Tuple[str, str]] = []

    if not base.exists() or not base.is_dir():
        return RepoFinderStatus(base, "Base directory not found")

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

    return repos
