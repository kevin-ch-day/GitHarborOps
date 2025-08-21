import io
import os
import subprocess
import sys
from setuptools import setup, find_packages


# --- Pre-flight Checks ---
def check_git_installed():
    """Ensure Git is installed on the system."""
    try:
        subprocess.run(
            ["git", "--version"], check=True, capture_output=True, text=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        sys.stderr.write(
            "\n[X] Git is not installed or not found in PATH.\n"
            "Please install Git before using GitHarborOps:\n"
            "  • Linux:   sudo apt install git   (Debian/Ubuntu)\n"
            "             sudo dnf install git   (Fedora)\n"
            "  • macOS:   brew install git\n"
            "  • Windows: https://git-scm.com/download/win\n\n"
        )
        sys.exit(1)


def check_python_version():
    """Ensure Python version compatibility (>=3.8)."""
    if sys.version_info < (3, 8):
        sys.stderr.write("[X] Python 3.8 or higher is required to run GitHarborOps.\n")
        sys.exit(1)


def read_long_description() -> str:
    """Read README.md for PyPI long description."""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if not os.path.exists(readme_path):
        return "GitHarborOps – Interactive Git management tool for handling multiple repositories."
    with io.open(readme_path, encoding="utf-8") as f:
        return f.read()


# Run checks
check_git_installed()
check_python_version()


# --- Package Setup ---
setup(
    name="GitHarborOps",
    version="0.1.1",
    description="Interactive Git management tool for handling multiple repositories.",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Kevin Day",
    author_email="you@example.com",
    url="https://github.com/kevin-ch-day/GitHarborOps",
    license="MIT",
    packages=find_packages(include=["githarborops", "githarborops.*"]),
    include_package_data=True,
    install_requires=[
        "questionary>=2.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "githarborops=githarborops.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Topic :: Software Development :: Version Control :: Git",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
    keywords="git cli devops version-control automation",
    zip_safe=False,
)
