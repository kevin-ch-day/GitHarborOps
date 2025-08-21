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

## Theming

GitHarborOps menus use a Harbor Navy theme. The foreground color can be
customised by setting the ``GITHARBOROPS_MENU_COLOR`` environment variable.
Invalid colors fall back to the default ``ansibrightcyan``.

Example:

```bash
export GITHARBOROPS_MENU_COLOR=ansibrightgreen
```

### Supported ANSI Colors

| Color Name         | Description    |
|--------------------|----------------|
| ansiblack          | black          |
| ansired            | red            |
| ansigreen          | green          |
| ansiyellow         | yellow         |
| ansiblue           | blue           |
| ansimagenta        | magenta        |
| ansicyan           | cyan           |
| ansiwhite          | white          |
| ansibrightblack    | bright black   |
| ansibrightred      | bright red     |
| ansibrightgreen    | bright green   |
| ansibrightyellow   | bright yellow  |
| ansibrightblue     | bright blue    |
| ansibrightmagenta  | bright magenta |
| ansibrightcyan     | bright cyan    |
| ansibrightwhite    | bright white   |

## License

MIT

