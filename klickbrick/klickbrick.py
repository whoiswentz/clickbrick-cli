from argparse import ArgumentParser
import sys


def main() -> None:
    parser = ArgumentParser(description="Klickbrick CLI")
    parser.add_argument("hello", metavar="hello", type=str, default="")
    parser.add_argument("--name", "-n", metavar="name",
                        type=str, default="world")
    args = parser.parse_args()

    print(f'{args.hello} {args.name}')


if __name__ == "__main__":
    main()
