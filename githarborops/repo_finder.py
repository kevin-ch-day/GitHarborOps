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
        # prune excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        if ".git" in dirs:
            repo_path = Path(root).resolve()
            repos.append(str(repo_path))
            # do not descend further once a repo is found
            dirs[:] = []

    return repos


def find_git_repos(base_dir: str | None = None) -> Union[List[str], Dict[str, Union[str, List[str]]]]:
    """Search for Git repositories with a sensible default path.

    If ``base_dir`` is provided, only that path is searched. When ``base_dir``
    is ``None`` the search is attempted in two stages:

    1. The directory two levels up from this file
       (``Path(__file__).resolve().parent.parent``).
    2. ``Path.cwd()`` if the first search yields no results.

    Directories named ``venv``, ``.venv``, ``__pycache__`` and ``node_modules``
    are excluded from traversal.

    Returns either a list of repository paths or a dictionary with an
    explanatory message when no repositories are found.
    """

    exclude_dirs = {"venv", ".venv", "__pycache__", "node_modules"}

    def _try(path: Path) -> List[str]:
        return _scan(path, exclude_dirs)

    if base_dir is not None:
        base_path = Path(base_dir).expanduser().resolve()
        repos = _try(base_path)
        if repos:
            return repos
        return {"repos": [], "message": f"No Git repositories found in {base_path}"}

    default_base = Path(__file__).resolve().parent.parent
    repos = _try(default_base)
    if repos:
        return repos

    cwd_base = Path.cwd().resolve()
    repos = _try(cwd_base)
    if repos:
        return repos

    return {
        "repos": [],
        "message": f"No Git repositories found in {default_base} or {cwd_base}",
    }
