"""Run with python3 -m playground NAME."""
import argparse
from . import greet


def main() -> None:
    parser = argparse.ArgumentParser(description="A tiny PlanTool workflow fixture")
    parser.add_argument("name")
    args = parser.parse_args()
    try:
        print(greet(args.name))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
