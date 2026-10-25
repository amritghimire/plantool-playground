#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
export PYTHONDONTWRITEBYTECODE=1
exec "${PYTHON:-python3}" scripts/verify_scenario.py "$@"
