"""Color and style definitions for CLI output."""

from rich.style import Style

# Base colors
BLUE = Style(color="blue")
CYAN = Style(color="cyan")
GREEN = Style(color="green")
YELLOW = Style(color="yellow")
RED = Style(color="red")
MAGENTA = Style(color="magenta")

# Severity styles
INFO = CYAN
WARN = Style(color="yellow", bold=True)
ERROR = Style(color="red", bold=True)
SUCCESS = Style(color="green", bold=True)

SEVERITY = {
    "info": INFO,
    "warn": WARN,
    "error": ERROR,
    "success": SUCCESS,
}
