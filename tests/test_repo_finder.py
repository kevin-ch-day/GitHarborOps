import subprocess

from githarborops.repo_finder import RepoFinderStatus, find_git_repos


def test_find_git_repos(tmp_path, capsys):
    repo_dir = tmp_path / "myrepo"
    repo_dir.mkdir()
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, stdout=subprocess.PIPE)

    result = find_git_repos(str(tmp_path))
    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""
    assert isinstance(result, list)
    assert ("myrepo", str(repo_dir.resolve())) in result


def test_missing_base_dir(tmp_path, capsys):
    missing = tmp_path / "missing"
    result = find_git_repos(str(missing))
    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""
    assert isinstance(result, RepoFinderStatus)
    assert result.base == missing.resolve()


def test_no_repos(tmp_path, capsys):
    result = find_git_repos(str(tmp_path))
    captured = capsys.readouterr()

    assert captured.out == ""
    assert captured.err == ""
    assert result == []
