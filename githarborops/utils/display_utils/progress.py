"""Progress indicators for long-running tasks."""

from contextlib import contextmanager
from typing import Iterator, Sequence, Tuple

from rich.progress import (
    BarColumn,
    Progress,
    ProgressColumn,
    SpinnerColumn,
    Task,
    TextColumn,
)
from rich.text import Text


@contextmanager
def spinner(message: str) -> Iterator[None]:
    """Context manager showing a spinner while a task runs."""
    progress = Progress(SpinnerColumn(), TextColumn("{task.description}"))
    task_id = progress.add_task(message, start=False)
    progress.start()
    progress.start_task(task_id)
    try:
        yield
    finally:
        progress.stop_task(task_id)
        progress.stop()


class _CompletionColumn(ProgressColumn):
    """Render a green check mark when a task finishes."""

    def render(self, task: Task) -> Text:  # type: ignore[override]
        return Text("✔", style="green") if task.finished else Text("")


@contextmanager
def progress_bar(total: int, message: str) -> Iterator[Tuple[Progress, int]]:
    """Context manager providing a styled progress bar.

    The bar shows cyan progress on a navy background and turns green on
    completion with a check mark.
    """

    with Progress(
        TextColumn("{task.description}"),
        BarColumn(
            bar_width=None,
            complete_style="cyan",
            style="navy_blue",
            finished_style="green",
        ),
        TextColumn("{task.percentage:>3.0f}%"),
        _CompletionColumn(),
    ) as progress:
        task_id = progress.add_task(message, total=total)
        yield progress, task_id


def scanning_fleet(repositories: Sequence[str]) -> Iterator[str]:
    """Iterate repositories while displaying a scanning progress bar."""

    with progress_bar(len(repositories), "Scanning fleet...") as (progress, task_id):
        for repo in repositories:
            yield repo
            progress.advance(task_id)
