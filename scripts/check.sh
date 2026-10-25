#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
PYTHONDONTWRITEBYTECODE=1
export PYTHONDONTWRITEBYTECODE
python_bin=${PYTHON:-python3}
"$python_bin" -c 'import sys; assert sys.version_info >= (3, 12), "Python 3.12+ required"'
"$python_bin" -m unittest discover -s tests -p 'test_*.py' -v
./scripts/smoke.sh
