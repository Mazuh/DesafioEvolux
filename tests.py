#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
Unit testing.
"""

from unittest import TestCase, main
from filecmp import cmp
from os import remove

from editor_grafico import Image


class ImageTest(TestCase):
    """Test the Image class."""

    def test_1(self):
        """First expected behaviour."""

        matrix = Image.init_by_cli('I 5 6')
        matrix.cli_exec('L 2 3 A')
        matrix.cli_exec('S one.bmp')
        self.assertTrue(
            cmp('one.bmp', 'tests_outputs/test_1/one.bmp', shallow=0),
            'Unexpected file content for one.bmp.'
        )
        remove('one.bmp')

        matrix.cli_exec('G 2 3 J')
        matrix.cli_exec('V 2 3 4 W')
        matrix.cli_exec('H 3 4 2 Z')
        matrix.cli_exec('F 3 3 J')
        matrix.cli_exec('S two.bmp')
        self.assertTrue(
            cmp('two.bmp', 'tests_outputs/test_1/two.bmp', shallow=0),
            'Unexpected file content for two.bmp.'
        )
        remove('two.bmp')

        with self.assertRaises(SystemExit):
            matrix.cli_exec('X')

    def test_2(self):
        """Second expected behaviour."""

        matrix = Image.init_by_cli('I 10 9')
        matrix.cli_exec('L 5 3 A')
        matrix.cli_exec('G 2 3 J')
        matrix.cli_exec('V 2 3 4 W')
        matrix.cli_exec('H 1 10 5 Z')
        matrix.cli_exec('F 3 3 J')
        matrix.cli_exec('K 2 7 8 8 E')
        matrix.cli_exec('F 9 9 R')
        matrix.cli_exec('S one.bmp')
        self.assertTrue(
            cmp('one.bmp', 'tests_outputs/test_2/one.bmp', shallow=0),
            'Unexpected file content for one.bmp.'
        )
        remove('one.bmp')

        with self.assertRaises(SystemExit):
            matrix.cli_exec('X')


if __name__ == '__main__':
    main()
