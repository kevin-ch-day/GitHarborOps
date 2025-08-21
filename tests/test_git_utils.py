import subprocess

from githarborops.git_utils import run_git_command, get_current_branch


def test_run_git_command(tmp_path):
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, stdout=subprocess.PIPE)

    result = run_git_command(str(repo_dir), ["rev-parse", "--is-inside-work-tree"])
    assert result.returncode == 0
    assert result.stdout.strip() == "true"


def test_get_current_branch(tmp_path):
    repo_dir = tmp_path / "repo2"
    repo_dir.mkdir()
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, stdout=subprocess.PIPE)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_dir, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "--allow-empty", "-m", "init"], cwd=repo_dir, check=True, stdout=subprocess.PIPE)
    branch = get_current_branch(str(repo_dir))
    assert branch in {"master", "main"}
