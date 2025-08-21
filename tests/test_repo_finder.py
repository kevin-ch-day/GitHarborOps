import subprocess
from pathlib import Path

from githarborops.repo_finder import find_git_repos


def test_find_git_repos(tmp_path):
    repo_dir = tmp_path / "myrepo"
    repo_dir.mkdir()
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, stdout=subprocess.PIPE)

    repos = find_git_repos(str(tmp_path))

    assert str(repo_dir) in repos
