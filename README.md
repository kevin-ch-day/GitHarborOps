# GitHarborOps

GitHarborOps is an interactive command line tool for managing fleets of Git repositories.
It provides a menu-driven interface for common diagnostics and workflows such as
status, branch listings, diffs, conflict detection, log viewing and more.

## Installation

Clone the repository and install with pip:

```bash
pip install .
```

## Usage

Run the CLI and select a repository to manage:

```bash
githarborops
```

The menu offers actions like:

- Repository overview
- Status and changed files
- Branch information
- Fetch / prune remotes
- Diff against a base branch
- Conflict detection
- Log graphs and last commit
- Stash listings

## Development

Run tests with:

```bash
pytest
```

## License

MIT

