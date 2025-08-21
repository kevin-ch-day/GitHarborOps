"""Interactive menu helpers built on questionary with Harbor Navy theme."""

from typing import Iterable, Optional, Union

import questionary
from questionary import Choice, Style

# ⚓ Branding
ANCHOR_ICON = "⚓"

# 📝 Default menu instruction
DEFAULT_INSTRUCTION = "Use ↑/↓ to navigate, Enter to select"

# 🌊 Harbor Navy Theme
MENU_STYLE = Style(
    [
        ("qmark", "fg:ansiblue bold"),
        ("question", "fg:ansiblue bold"),
        ("answer", "fg:ansiblue bold"),
        ("pointer", "fg:ansiblue bold"),
        ("highlighted", "fg:ansiblue bold"),
        ("selected", "fg:ansiblue bold"),
        ("text", "fg:#ffffff"),
        ("disabled", "fg:#888888"),
    ]
)

ChoiceType = Union[str, Choice]


def menu_select(
    title: str,
    choices: Iterable[ChoiceType],
    anchor_icon: str = ANCHOR_ICON,
    instruction: str = DEFAULT_INSTRUCTION,
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
    return menu_select(
        f"{anchor_icon} GitHarborOps Menu", options, anchor_icon=anchor_icon
    )


def select_repo(
    repos: Iterable[ChoiceType], anchor_icon: str = ANCHOR_ICON
) -> Optional[str]:
    """Prompt the user to choose a repository from *repos*."""
    return menu_select("Select repository", repos, anchor_icon=anchor_icon)


def select_action(
    actions: Iterable[ChoiceType], anchor_icon: str = ANCHOR_ICON
) -> Optional[str]:
    """Prompt the user to choose an action from *actions*."""
    return menu_select("Select action", actions, anchor_icon=anchor_icon)


def confirm(message: str, anchor_icon: str = ANCHOR_ICON) -> bool:
    """Yes/No confirmation prompt with Harbor Navy styling."""
    return menu_confirm(f"{anchor_icon} {message}", anchor_icon)
