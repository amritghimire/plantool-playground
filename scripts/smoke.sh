#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python_bin=${PYTHON:-python3}
export PYTHONDONTWRITEBYTECODE=1
actual=$("$python_bin" -m playground Ada)
[ "$actual" = 'Hello, Ada!' ] || { echo 'Greeting smoke failed' >&2; exit 1; }
if "$python_bin" -m playground ' ' >/dev/null 2>&1; then
    echo 'Blank input unexpectedly succeeded' >&2
    exit 1
fi
echo 'Smoke passed'
