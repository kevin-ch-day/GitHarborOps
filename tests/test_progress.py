from githarborops.utils.display_utils import progress
from rich.progress import BarColumn


def test_progress_bar_styling():
    with progress.progress_bar(1, "Test") as (p, task_id):
        bar_col = next(col for col in p.columns if isinstance(col, BarColumn))
        assert bar_col.complete_style == "cyan"
        assert bar_col.style == "navy_blue"
        assert bar_col.finished_style == "green"
        assert any(isinstance(col, progress._CompletionColumn) for col in p.columns)


def test_scanning_fleet_iterates():
    repos = ["a", "b", "c"]
    assert list(progress.scanning_fleet(repos)) == repos
