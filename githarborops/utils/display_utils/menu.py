"""Interactive menu helpers built on questionary with Harbor Navy theme."""

from typing import Iterable, Optional, Union, Dict, Any

import os
import logging

import questionary
from questionary import Choice, Style

# ⚓ Branding
ANCHOR_ICON = "⚓"

# 📝 Default menu instruction
DEFAULT_INSTRUCTION = "Use ↑/↓ to navigate, Enter to select"

# 🌊 Harbor Navy Theme
# Theme can be customized via environment variables.  For now only the
# foreground color is exposed publicly, but the structure allows future
# extension for background and highlight styles.

logger = logging.getLogger(__name__)

DEFAULT_THEME: Dict[str, Any] = {
    "color": "ansibrightcyan",
    "background": None,
    "highlight": "bold",
}


def _validate_color(color: str) -> str:
    """Return *color* if supported, otherwise fall back to default with warning."""
    try:
        Style([("check", f"fg:{color}")])
        return color
    except Exception:
        logger.warning(
            "Unsupported menu color '%s'; falling back to '%s'", color, DEFAULT_THEME["color"]
        )
        return DEFAULT_THEME["color"]


def _load_theme() -> Dict[str, Any]:
    color = os.getenv("GITHARBOROPS_MENU_COLOR", DEFAULT_THEME["color"])
    background = os.getenv("GITHARBOROPS_MENU_BG", DEFAULT_THEME["background"])
    highlight = os.getenv("GITHARBOROPS_MENU_HIGHLIGHT", DEFAULT_THEME["highlight"])
    return {
        "color": _validate_color(color),
        "background": background,
        "highlight": highlight,
    }


def _compose_style(theme: Dict[str, Any]) -> str:
    parts = [f"fg:{theme['color']}"]
    if theme.get("background"):
        parts.append(f"bg:{theme['background']}")
    if theme.get("highlight"):
        parts.append(theme["highlight"])
    return " ".join(parts)


MENU_THEME = _load_theme()

_STYLE_STR = _compose_style(MENU_THEME)

MENU_STYLE = Style(
    [
        ("qmark", _STYLE_STR),
        ("question", _STYLE_STR),
        ("answer", _STYLE_STR),
        ("pointer", _STYLE_STR),
        ("highlighted", _STYLE_STR),
        ("selected", _STYLE_STR),
        ("text", "fg:#ffffff"),
        ("disabled", "fg:#888888"),
    ]
)

ChoiceType = Union[str, Choice]


def menu_select(
    title: str,
    choices: Iterable[ChoiceType],
    anchor_icon: str = ANCHOR_ICON,
    instruction: Optional[str] = DEFAULT_INSTRUCTION,
) -> Optional[str]:
    """Standard menu selection prompt with GitHarborOps Harbor Navy styling."""
    return questionary.select(
        title,
        choices=list(choices),
        qmark=anchor_icon,
        instruction=instruction,
        style=MENU_STYLE,
    ).ask()


def menu_confirm(message: str, anchor_icon: str = ANCHOR_ICON) -> bool:
    """Standard confirmation prompt with GitHarborOps styling."""
    return bool(
        questionary.confirm(message, qmark=anchor_icon, style=MENU_STYLE).ask()
    )


def githarborops_menu(
    options: Iterable[ChoiceType], anchor_icon: str = ANCHOR_ICON
) -> Optional[str]:
    """Display the GitHarborOps main menu."""
    return menu_select(f"{anchor_icon} GitHarborOps Menu", options, anchor_icon)


def select_repo(
    repos: Iterable[ChoiceType],
    anchor_icon: str = ANCHOR_ICON,
    instruction: Optional[str] = DEFAULT_INSTRUCTION,
) -> Optional[str]:
    """Prompt the user to choose a repository from *repos*."""
    return menu_select(
        f"{anchor_icon} Select repository", repos, anchor_icon, instruction
    )


def select_action(
    actions: Iterable[ChoiceType], anchor_icon: str = ANCHOR_ICON
) -> Optional[str]:
    """Prompt the user to choose an action from *actions*."""
    return menu_select(f"{anchor_icon} Select action", actions, anchor_icon)


def confirm(message: str, anchor_icon: str = ANCHOR_ICON) -> bool:
    """Yes/No confirmation prompt with Harbor Navy styling."""
    return menu_confirm(f"{anchor_icon} {message}", anchor_icon)
