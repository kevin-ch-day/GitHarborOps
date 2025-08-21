import re
import importlib

import pytest
from rich.console import Console

from githarborops.utils.display_utils import colors, banners, menu, tables, formatter


def test_severity_color_mappings():
    """SEVERITY should map level names to expected styles."""
    assert colors.SEVERITY["info"] == colors.INFO
    assert colors.SEVERITY["warn"] == colors.WARN
    assert colors.SEVERITY["error"] == colors.ERROR
    assert colors.SEVERITY["success"] == colors.SUCCESS


def test_show_banner_formatting(monkeypatch):
    """Banner should render with bold cyan style."""
    console = Console(force_terminal=True)
    monkeypatch.setattr(banners, "console", console)
    with console.capture() as capture:
        banners.show_banner()
    output = capture.get()
    assert "GitHarborOps" in output
    # ANSI code for bold bright cyan is 1;36
    assert "\x1b[1;36" in output


def test_menu_option_styling(monkeypatch):
    """Menu helpers should forward prompts with correct messages and choices."""
    captured = {}

    class DummyQuestion:
        def __init__(self, message, choices):
            self.message = message
            self.choices = choices

        def ask(self):
            return "chosen"

    def fake_select(message, choices, **kwargs):
        captured["message"] = message
        captured["choices"] = choices
        captured["kwargs"] = kwargs
        return DummyQuestion(message, choices)

    monkeypatch.setattr(menu.questionary, "select", fake_select)

    result = menu.select_repo(["a", "b"])
    assert result == "chosen"
    assert captured["message"] == "⚓ Select repository"
    assert captured["choices"] == ["a", "b"]
    assert "qmark" in captured["kwargs"] and "style" in captured["kwargs"]


@pytest.mark.parametrize(
    "env_color, expected", [
        (None, "ansibrightcyan"),
        ("ansibrightgreen", "ansibrightgreen"),
        ("notacolor", "ansibrightcyan"),
    ]
)
def test_menu_color_override(monkeypatch, env_color, expected, caplog):
    """Environment variable should control menu color with fallback on invalid input."""
    if env_color is not None:
        monkeypatch.setenv("GITHARBOROPS_MENU_COLOR", env_color)
    else:
        monkeypatch.delenv("GITHARBOROPS_MENU_COLOR", raising=False)
    caplog.set_level("WARNING")
    importlib.reload(menu)
    rule_dict = dict(menu.MENU_STYLE._style_rules)
    assert rule_dict["qmark"].startswith(f"fg:{expected}")
    if env_color not in (None, expected):
        assert "Unsupported menu color" in caplog.text
    monkeypatch.delenv("GITHARBOROPS_MENU_COLOR", raising=False)
    importlib.reload(menu)


def test_table_row_alternation(monkeypatch):
    """Alternating row styles should be reflected in rendered output."""
    console = Console(force_terminal=True)
    monkeypatch.setattr(formatter, "console", console)
    table = tables.simple_table("T", ["col"], [["row1"], ["row2"]])
    table.row_styles = ["", "dim"]
    with console.capture() as capture:
        formatter.print_table(table)
    output = capture.get()
    # Rich applies SGR 2 for "dim" style
    assert "\x1b[2m" in output
    # The dim code should precede row2 but not row1
    dim_before_row2 = re.search(r"\x1b\[2m.*row2", output, re.DOTALL)
    dim_before_row1 = re.search(r"\x1b\[2m.*row1", output, re.DOTALL)
    assert dim_before_row2 is not None
    assert dim_before_row1 is None
