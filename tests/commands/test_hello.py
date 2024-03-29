"""Tests for our `pqtools info` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestInfo(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['pqtools', 'info'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hello_world(self):
        output = popen(['pqtools', 'info'], stdout=PIPE).communicate()[0]
        self.assertTrue('Hello, world!' in output)
