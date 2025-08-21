import subprocess
from pathlib import Path


def run_git_command(repo_path: str, args: list[str]):
    """
    Run a Git command inside a repository and return the completed process.

    Args:
        repo_path (str): Path to the repository root.
        args (list[str]): Git arguments, e.g., ["status", "-sb"]

    Returns:
        subprocess.CompletedProcess: Contains stdout, stderr, returncode.
    """
    repo = Path(repo_path).expanduser().resolve()

    if not repo.exists():
        raise FileNotFoundError(f"Repository path does not exist: {repo}")

    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=str(repo),
            text=True,
            capture_output=True,
            check=False,   # don’t raise automatically, let caller inspect
        )
        return result
    except Exception as e:
        raise RuntimeError(f"Error running git command: {e}")


def get_current_branch(repo_path: str) -> str:
    """Return the current branch name."""
    result = run_git_command(repo_path, ["rev-parse", "--abbrev-ref", "HEAD"])
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def get_repo_root(repo_path: str) -> str:
    """Return the absolute path to the repo root."""
    result = run_git_command(repo_path, ["rev-parse", "--show-toplevel"])
    return result.stdout.strip() if result.returncode == 0 else repo_path


def get_last_commit(repo_path: str) -> str:
    """Return the last commit info (hash + message)."""
    result = run_git_command(repo_path, ["log", "-1", "--oneline"])
    return result.stdout.strip() if result.returncode == 0 else "(no commits)"
