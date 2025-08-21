#!/usr/bin/env bash
# GitHarborOps run script
# This script lets you run the CLI directly in dev mode.

set -euo pipefail

# Ensure we’re in the project root
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$ROOT_DIR"

# Activate virtualenv if one exists
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# Run GitHarborOps CLI
python -m githarborops.main "$@"
