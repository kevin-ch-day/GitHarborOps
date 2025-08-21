"""ASCII art banners and section headers."""

from rich.console import Console
from rich.panel import Panel

console = Console()


BANNER_TEXT = "[bold blue]GitHarborOps[/]\nHarbor Control for Your Git Repositories"


def show_banner() -> None:
    """Display the application banner."""
    console.print(Panel(BANNER_TEXT, style="bold blue", border_style="blue"))


def section(title: str) -> None:
    """Render a section header."""
    console.print(f"\n[bold cyan on #001f3f]⚓ {title}[/]\n")
