from argparse import ArgumentParser
from typing import Optional, Sequence
import sys


def main() -> None:
    string = process_arguments(sys.argv[1:])
    print(string)


def process_arguments(argv: Optional[Sequence[str]] = None) -> str:
    parser = ArgumentParser(description="Klickbrick CLI")
    parser.add_argument("hello", metavar="hello", type=str, default="")
    parser.add_argument("--name", "-n", metavar="name",
                        type=str, default="world")
    args = parser.parse_args(argv)

    return f'hello {args.name}'


if __name__ == "__main__":
    main()
