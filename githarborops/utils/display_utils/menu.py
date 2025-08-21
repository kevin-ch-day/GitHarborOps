"""Interactive menu helpers built on questionary."""

from typing import Iterable, Optional

import questionary
from questionary import Style


HARBOR_NAVY_STYLE = Style(
    [
        ("qmark", "fg:ansiblue"),
        ("question", "bold"),
        ("answer", "fg:ansiblue"),
        ("pointer", "fg:ansiblue bold"),
        ("highlighted", "fg:ansiblue bold"),
        ("selected", "fg:ansiblue"),
    ]
)

ANCHOR = "⚓ "


def select_repo(repos: Iterable[str]) -> Optional[str]:
    """Prompt the user to choose a repository from *repos* using Harbor Navy styling."""
    return questionary.select(
        f"{ANCHOR}Select repository",
        choices=list(repos),
        style=HARBOR_NAVY_STYLE,
    ).ask()


def select_action(message: str, actions: Iterable[str]) -> Optional[str]:
    """Prompt the user to choose an action from *actions* using Harbor Navy styling."""
    return questionary.select(
        f"{ANCHOR}{message}",
        choices=list(actions),
        style=HARBOR_NAVY_STYLE,
    ).ask()


def confirm(message: str) -> bool:
    """Yes/No confirmation prompt."""
    return bool(questionary.confirm(message, style=HARBOR_NAVY_STYLE, qmark=ANCHOR.strip()).ask())
