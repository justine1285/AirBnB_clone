#!/usr/bin/python3
"""Unit Test module for the Console"""


import unittest
import sys
import os
from io import StringIO
from unittest.mock import create_autospec
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """
    Test console.py
    """
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.cli = self.create()
        sys.stdout = StringIO()
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(
            lambda x: x[0][0],
            self.mock_stdout.write.call_args_list[-nr:]))

    def test_do_quit(self):
        self.assertTrue(self.cli.onecmd("EOF"))

    def test_do_help(self):
        self.cli.onecmd("help help")
        string = "List available commands with \"help\" or detailed help with "
        string += "\"help cmd\".\n"
        self.assertEqual(string, self._last_write())
        self.cli.onecmd("help create")
        self.assertTrue(self._last_write())

    def test_do_create(self):
        self.cli.onecmd("create User")
        self.assertTrue(sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("create")
        self.assertEqual("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("create UserModel")
        self.assertEqual("** class doesn't exist **\n", sys.stdout.getvalue())

    def test_do_show(self):
        self.cli.onecmd("show")
        self.assertEqual("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("show UserModel")
        self.assertEqual("** class doesn't exist **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("show BaseModel")
        self.assertEqual("** instance id missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("show BaseModel 112-ahdhdh-23")
        self.assertEqual("** no instance found **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("create BaseModel")
        self.assertTrue(sys.stdout.getvalue())

    def test_do_destroy(self):
        self.cli.onecmd("destroy")
        self.assertEqual("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("destroy UserModel")
        self.assertEqual("** class doesn't exist **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("destroy BaseModel")
        self.assertEqual("** instance id missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("destroy BaseModel 12112-ahdhdh-233")
        self.assertEqual("** no instance found **\n", sys.stdout.getvalue())
        self.flush_buffer()

    def test_do_all(self):
        self.cli.onecmd("all UserModel")
        self.assertEqual("** class doesn't exist **\n", sys.stdout.getvalue())

    def tes_dot_update(self):
        self.cli.onecmd("update")
        self.assertEqual("** class name missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("update UserModel")
        self.assertEqual("** class doesn't exist **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("update BaseModel")
        self.assertEqual("** instance id missing **\n", sys.stdout.getvalue())
        self.flush_buffer()
        self.cli.onecmd("update BaseModel 112-ahdhdh-23")
        self.flush_buffer()
        obj_dict = storage.all()

    def test_do_count_adv(self):
        obj_dict = storage.all()
        count = 0
        for k, v in obj_dict.items():
            if obj_dict[k].__class__.__name__ == "User":
                count += 1
        self.cli.onecmd("User.count()")

    @staticmethod
    def flush_buffer():
        sys.stdout.seek(0)
        sys.stdout.truncate(0)


if __name__ == '__main__':
    unittest.main()
