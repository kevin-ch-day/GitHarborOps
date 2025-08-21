"""Color and style definitions for CLI output."""

from rich.style import Style

# Severity and general output styles
#
# DEFAULT   – Bright white, used for general text
# INFO      – Deep navy
# DETAILS   – Sea blue/teal
# SUCCESS   – Harbor green
# WARN      – Yellow
# ERROR     – Bright red
# HIGHLIGHT – Bold cyan

DEFAULT = Style(color="bright_white")
INFO = Style(color="#001f3f")
DETAILS = Style(color="#17a2b8")
SUCCESS = Style(color="#21a179")
WARN = Style(color="yellow")
ERROR = Style(color="#ff4136")
HIGHLIGHT = Style(color="cyan", bold=True)

SEVERITY = {
    "info": INFO,
    "details": DETAILS,
    "success": SUCCESS,
    "warn": WARN,
    "error": ERROR,
    "highlight": HIGHLIGHT,
}

