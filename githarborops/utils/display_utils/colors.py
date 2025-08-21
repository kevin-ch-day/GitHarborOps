"""Color and style definitions for GitHarborOps CLI output (Harbor Navy theme)."""

from rich.style import Style

# 🌊 Harbor Navy Theme Colors
HARBOR_NAVY = Style(color="#001f3f")   # Deep navy (primary identity)
SEA_BLUE = Style(color="#17a2b8")      # Teal / details
HARBOR_GREEN = Style(color="#21a179")  # Success
BRIGHT_WHITE = Style(color="bright_white")
WARNING_YELLOW = Style(color="yellow")
DANGER_RED = Style(color="#ff4136")
HIGHLIGHT_CYAN = Style(color="cyan", bold=True)

# Semantic / Severity Styles
DEFAULT = BRIGHT_WHITE
INFO = HARBOR_NAVY
DETAILS = SEA_BLUE
SUCCESS = HARBOR_GREEN
WARN = WARNING_YELLOW
ERROR = DANGER_RED
HIGHLIGHT = HIGHLIGHT_CYAN

# Centralized lookup table for convenience
SEVERITY = {
    "default": DEFAULT,
    "info": INFO,
    "details": DETAILS,
    "success": SUCCESS,
    "warn": WARN,
    "error": ERROR,
    "highlight": HIGHLIGHT,
}
