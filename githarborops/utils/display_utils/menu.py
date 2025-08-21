"""Interactive menu helpers built on questionary."""

from typing import Iterable, Optional, Union

import questionary
from questionary import Choice, Style


ANCHOR_ICON = "⚓"
MENU_STYLE = Style(
    [
        ("qmark", "fg:#00ffff bold"),
        ("question", "fg:#00ffff bold"),
        ("answer", "fg:#00ffff bold"),
        ("pointer", "fg:#00ffff bold"),
        ("highlighted", "fg:#00ffff bold"),
        ("selected", "fg:#00ffff bold"),
        ("text", "fg:#ffffff"),
        ("disabled", "fg:#888888"),
    ]
)

ChoiceType = Union[str, Choice]


def menu_select(title: str, choices: Iterable[ChoiceType]) -> Optional[str]:
    """Standard menu selection prompt with GitHarborOps styling."""
    return questionary.select(
        title, choices=list(choices), qmark=ANCHOR_ICON, style=MENU_STYLE
    ).ask()


def menu_confirm(message: str) -> bool:
    """Standard confirmation prompt with GitHarborOps styling."""
    return bool(
        questionary.confirm(message, qmark=ANCHOR_ICON, style=MENU_STYLE).ask()
    )


def githarborops_menu(options: Iterable[ChoiceType]) -> Optional[str]:
    """Display the GitHarborOps main menu."""
    return menu_select("GitHarborOps Menu", options)


def select_repo(repos: Iterable[ChoiceType]) -> Optional[str]:
    """Prompt the user to choose a repository from *repos*."""
    return menu_select("Select repository", repos)


def select_action(actions: Iterable[ChoiceType]) -> Optional[str]:
    """Prompt the user to choose an action from *actions*."""
    return menu_select("Select action", actions)


def confirm(message: str) -> bool:
    """Yes/No confirmation prompt."""
    return menu_confirm(message)
