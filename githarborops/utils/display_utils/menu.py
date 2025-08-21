"""Interactive menu helpers built on questionary."""

from typing import Iterable, Optional

import questionary


def select_repo(repos: Iterable[str]) -> Optional[str]:
    """Prompt the user to choose a repository from *repos*."""
    return questionary.select("Select repository", choices=list(repos)).ask()


def select_action(actions: Iterable[str]) -> Optional[str]:
    """Prompt the user to choose an action from *actions*."""
    return questionary.select("Select action", choices=list(actions)).ask()


def confirm(message: str) -> bool:
    """Yes/No confirmation prompt."""
    return bool(questionary.confirm(message).ask())
