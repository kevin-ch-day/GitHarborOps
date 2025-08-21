"""Utilities for discovering Git repositories on disk."""

import os
from pathlib import Path
from typing import List, Union, Dict


def _scan(base: Path, exclude_dirs: set[str]) -> List[str]:
    """Return a list of git repositories under ``base``."""
    repos: List[str] = []
    if not base.exists() or not base.is_dir():
        return repos

    for root, dirs, _ in os.walk(base):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        if ".git" in dirs:
            repo_path = Path(root).resolve()
            repos.append(str(repo_path))
            dirs[:] = []  # stop descending further

    return repos


def find_git_repos(base_dir: str | None = None) -> Union[List[str], Dict[str, Union[str, List[str]]]]:
    """
    Search for Git repositories.

    - If `base_dir` is provided, scan there.
    - Otherwise, look in the **parent directory of this project**.
    """

    exclude_dirs = {"venv", ".venv", "__pycache__", "node_modules"}

    def _try(path: Path) -> List[str]:
        try:
            return _scan(path, exclude_dirs)
        except Exception as e:
            print(f"[!] Failed scanning {path}: {e}")
            return []

    if base_dir:
        base_path = Path(base_dir).expanduser().resolve()
    else:
        # default: parent of the project root
        base_path = Path(__file__).resolve().parent.parent.parent  

    repos = _try(base_path)
    if repos:
        return repos

    return {
        "repos": [],
        "message": f"No Git repositories found in {base_path}",
    }
