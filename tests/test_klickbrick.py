from unittest import TestCase

from clickbrick_cli import hello


class Klickbrick(TestCase):
    def test_get_hello_name(self) -> None:
        string = hello.process_arguments(["hello", "--name", "name"])
        self.assertEqual(string, "hello name")
