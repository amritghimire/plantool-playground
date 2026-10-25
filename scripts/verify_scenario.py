"""Acceptance oracles: baseline passes now; feature scenarios fail until implemented."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def verify(scenario):
    if scenario == "baseline":
        subprocess.run([str(ROOT / "scripts/check.sh")], cwd=ROOT, check=True)
    elif scenario == "slug":
        from playground.text import slugify
        for value, expected in [("Hello World", "hello-world"), (" A__B  C! ", "a-b-c"), ("A---B", "a-b"), ("123", "123")]:
            assert slugify(value) == expected, (value, expected)
        for value in ("", " ", "!!!"):
            try:
                slugify(value)
            except ValueError:
                pass
            else:
                raise AssertionError("empty slug must be rejected")
    elif scenario == "json":
        result = subprocess.run([sys.executable, "-m", "playground", "--json", " Ada "], cwd=ROOT, capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        assert json.loads(result.stdout) == {"name": "Ada", "greeting": "Hello, Ada!"}
        assert not result.stderr
        invalid = subprocess.run([sys.executable, "-m", "playground", "--json", " "], cwd=ROOT, capture_output=True, text=True)
        assert invalid.returncode == 2 and not invalid.stdout
    elif scenario == "docs":
        text = (ROOT / "docs/testing.md").read_text()
        for required in ("./scripts/check.sh", "./scripts/smoke.sh", "PYTHON=", "3.12"):
            assert required in text, f"Missing documentation: {required}"
    print(f"Scenario {scenario}: passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", choices=["baseline", "slug", "json", "docs"])
    args = parser.parse_args()
    try:
        verify(args.scenario)
    except (AssertionError, ImportError, OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Scenario {args.scenario}: FAILED: {error}", file=sys.stderr)
        sys.exit(1)
