import subprocess
import sys
from setuptools import setup, find_packages

# --- Ensure Git is installed ---
def check_git_installed():
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        sys.stderr.write(
            "\n[X] Git is not installed or not found in PATH.\n"
            "Please install Git before using GitHarborOps.\n"
            "  • Linux:   sudo apt install git   (Debian/Ubuntu)\n"
            "             sudo dnf install git   (Fedora)\n"
            "  • macOS:   brew install git\n"
            "  • Windows: https://git-scm.com/download/win\n\n"
        )
        sys.exit(1)

# --- Ensure Questionary is installed ---
def ensure_questionary_installed():
    try:
        import questionary  # noqa: F401
    except ImportError:
        sys.stderr.write("[*] Installing missing dependency: questionary\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "questionary>=2.0"])

check_git_installed()
ensure_questionary_installed()

# --- Package Setup ---
setup(
    name="GitHarborOps",
    version="0.1.0",
    description="Interactive Git management tool for handling multiple repositories.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Kevin Day",
    author_email="you@example.com",
    url="https://github.com/kevin-ch-day/GitHarborOps",
    license="MIT",
    packages=find_packages(include=["githarborops", "githarborops.*"]),
    include_package_data=True,
    install_requires=[
        "questionary>=2.0",
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
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Topic :: Software Development :: Version Control :: Git",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
    keywords="git cli devops version-control",
)
