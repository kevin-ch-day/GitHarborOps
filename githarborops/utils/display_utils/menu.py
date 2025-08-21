"""Interactive menu helpers built on questionary with Harbor Navy theme."""

from typing import Iterable, Optional, Union

import questionary
from questionary import Choice, Style

# ⚓ Branding
ANCHOR_ICON = "⚓"

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


def menu_select(title: str, choices: Iterable[ChoiceType]) -> Optional[str]:
    """Standard menu selection prompt with GitHarborOps Harbor Navy styling."""
    return questionary.select(
        title,
        choices=list(choices),
        qmark=ANCHOR_ICON,
        style=MENU_STYLE,
    ).ask()


def menu_confirm(message: str) -> bool:
    """Standard confirmation prompt with GitHarborOps styling."""
    return bool(
        questionary.confirm(message, qmark=ANCHOR_ICON, style=MENU_STYLE).ask()
    )


def githarborops_menu(options: Iterable[ChoiceType]) -> Optional[str]:
    """Display the GitHarborOps main menu."""
    return menu_select(f"{ANCHOR_ICON} GitHarborOps Menu", options)


def select_repo(repos: Iterable[ChoiceType]) -> Optional[str]:
    """Prompt the user to choose a repository from *repos*."""
    return menu_select(f"{ANCHOR_ICON} Select repository", repos)


def select_action(actions: Iterable[ChoiceType]) -> Optional[str]:
    """Prompt the user to choose an action from *actions*."""
    return menu_select(f"{ANCHOR_ICON} Select action", actions)


def confirm(message: str) -> bool:
    """Yes/No confirmation prompt with Harbor Navy styling."""
    return menu_confirm(f"{ANCHOR_ICON} {message}")
