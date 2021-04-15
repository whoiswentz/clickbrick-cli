from argparse import ArgumentParser
from typing import Optional, Sequence
import sys


def main() -> None:
    string = process_arguments(sys.argv[1:])
    print(string)


def process_arguments(argv: Optional[Sequence[str]] = None) -> str:
    parser = ArgumentParser(description="Klickbrick CLI")
    subparsers = parser.add_subparsers()

    hello_group = subparsers.add_parser('hello')
    hello_group.add_argument(
        "--name", "-n", metavar="name", type=str, default="world")

    onboard_group = subparsers.add_parser('onboard')
    onboard_group.add_argument(
        '--test', '-t', metavar="test", type=str, default=None)

    args = parser.parse_args(argv)

    return f'hello {args.name}'


if __name__ == "__main__":
    main()
