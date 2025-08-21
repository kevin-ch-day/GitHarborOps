"""Uniform CLI notifications."""

from rich.console import Console

from . import colors

console = Console()


def _notify(message: str, level: str) -> None:
    style = colors.SEVERITY.get(level)
    if style:
        console.print(message, style=style)
    else:
        console.print(message)


def notify_info(message: str) -> None:
    _notify(message, "info")


def notify_warn(message: str) -> None:
    _notify(message, "warn")


def notify_error(message: str) -> None:
    _notify(message, "error")


def notify_success(message: str) -> None:
    _notify(message, "success")
