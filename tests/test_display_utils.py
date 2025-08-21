import re

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
    # ANSI code 36 corresponds to cyan foreground
    assert "\x1b[36" in output


def test_menu_option_styling(monkeypatch):
    """Menu helpers should forward prompts with correct messages and choices."""
    captured = {}

    class DummyQuestion:
        def __init__(self, message, choices, **kwargs):
            captured["message"] = message
            captured["choices"] = choices

        def ask(self):
            return "chosen"

    monkeypatch.setattr(
        menu.questionary,
        "select",
        lambda message, choices, **kwargs: DummyQuestion(message, choices),
    )

    result = menu.select_repo(["a", "b"])
    assert result == "chosen"
    # Updated to match new anchor-prefixed style
    assert captured == {"message": "⚓ Select repository", "choices": ["a", "b"]}


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
