import os
from pathlib import Path


def find_git_repos(base_dir: str):
    """
    Recursively search for Git repositories under a base directory.

    Args:
        base_dir (str): Path to the directory to search.

    Returns:
        list[str]: A list of absolute paths to Git repositories.
    """
    base = Path(base_dir).expanduser().resolve()
    repos = []

    if not base.exists() or not base.is_dir():
        return repos

    for root, dirs, files in os.walk(base):
        if ".git" in dirs:
            repos.append(str(Path(root).resolve()))
            # prevent descending into this repo's subfolders
            dirs[:] = []

    return repos
