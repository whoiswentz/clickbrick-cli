from unittest import TestCase

from klickbrick import hello_cli


class Klickbrick(TestCase):
    def test_get_hello_name(self):
        string = hello_cli.process_arguments(["hello", "--name", "name"])
        self.assertEqual(string, "hello name")
