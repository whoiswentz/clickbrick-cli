from argparse import ArgumentParser
import sys


def main() -> None:
    string = process_arguments(sys.argv[1:])
    print(string)


def process_arguments(args) -> str:
    parser = ArgumentParser(description="Klickbrick CLI")
    parser.add_argument("hello", metavar="hello", type=str, default="")
    parser.add_argument("--name", "-n", metavar="name",
                        type=str, default="world")
    args = parser.parse_args(args)

    return f'{args.hello} {args.name}'


if __name__ == "__main__":
    main()
