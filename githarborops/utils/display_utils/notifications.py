"""Uniform CLI notifications."""

from rich.console import Console

from . import colors

console = Console()


NAUTICAL_PREFIXES = {
    "success": "Anchors aweigh! ",
    "warn": "Batten down the hatches! ",
    "error": "Mayday! ",
    "info": "Captain's log: ",
}


def _notify(message: str, level: str, style=None) -> None:
    """Render a styled notification with a nautical flavor."""
    prefix = NAUTICAL_PREFIXES.get(level, "")
    style = style or colors.SEVERITY.get(level)
    if style:
        console.print(f"{prefix}{message}", style=style)
    else:
        console.print(f"{prefix}{message}")


def notify_info(message: str) -> None:
    _notify(message, "info", colors.HARBOR_NAVY)


def notify_warn(message: str) -> None:
    _notify(message, "warn", colors.HARBOR_NAVY)


def notify_error(message: str) -> None:
    _notify(message, "error", colors.HARBOR_NAVY)


def notify_success(message: str) -> None:
    _notify(message, "success", colors.HARBOR_NAVY)
