from argparse import ArgumentParser
import sys

def main() -> None:
    parser = ArgumentParser(description="Klickbrick CLI")
    parser.add_argument("hello", metavar="hello", type=str, default="")
    args = parser.parse_args()

    print('Helo World')

if __name__ == "__main__":
    main()