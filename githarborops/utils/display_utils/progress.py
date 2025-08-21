"""Progress indicators for long-running tasks."""

from contextlib import contextmanager
from typing import Iterator

from rich.progress import Progress, SpinnerColumn, TextColumn


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
