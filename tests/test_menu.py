import questionary

from githarborops.utils.display_utils import menu


class DummyQuestion:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def ask(self):
        return "choice"


def test_menu_select_uses_anchor_and_style(monkeypatch):
    captured = {}

    def mock_select(message, **kwargs):
        captured["message"] = message
        captured["kwargs"] = kwargs
        return DummyQuestion(**kwargs)

    monkeypatch.setattr(questionary, "select", mock_select)

    assert menu.menu_select("Title", ["a"]) == "choice"
    assert captured["kwargs"]["qmark"] == menu.ANCHOR_ICON
    assert captured["kwargs"]["style"] is menu.MENU_STYLE


def test_menu_confirm_uses_anchor_and_style(monkeypatch):
    captured = {}

    def mock_confirm(message, **kwargs):
        captured["message"] = message
        captured["kwargs"] = kwargs
        return DummyQuestion(**kwargs)

    monkeypatch.setattr(questionary, "confirm", mock_confirm)

    assert menu.menu_confirm("Proceed?")
    assert captured["kwargs"]["qmark"] == menu.ANCHOR_ICON
    assert captured["kwargs"]["style"] is menu.MENU_STYLE


def test_githarborops_menu_calls_select(monkeypatch):
    called = {}

    def mock_select(message, **kwargs):
        called["message"] = message
        return DummyQuestion(**kwargs)

    monkeypatch.setattr(questionary, "select", mock_select)

    menu.githarborops_menu(["opt"])
    assert called["message"] == "GitHarborOps Menu"
