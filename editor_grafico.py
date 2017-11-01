#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
Program that reads a sequence of commands to handle a MxN matrix of pixels.
"""

import re

class Image(object):
    """
    Matrix of pixels.

    Its indexes are from 1 up to its dimensions (inclusive ranges).
    """
    _BLANK_COLOR = 'O'

    __INIT_COMMAND_KEY = 'I'
    __AVAILABLE_CLI = {
        'I': r'^I (?P<M>[0-9]+) (?P<N>[0-9]+)$',
        'C': r'^C$',
        'L': r'^L (?P<X>[0-9]+) (?P<Y>[0-9]+) (?P<C>[A-Z])$',
        'V': r'^V (?P<X>[0-9]+) (?P<Y1>[0-9]+) (?P<Y2>[0-9]+) (?P<C>[A-Z])$',
        'H': r'^H (?P<X1>[0-9]+) (?P<X2>[0-9]+) (?P<Y>[0-9]+) (?P<C>[A-Z])$',
        'K': r'^K (?P<X1>[0-9]+) (?P<Y1>[0-9]+) (?P<X2>[0-9]+) (?P<Y2>[0-9]+) (?P<C>[A-Z])$',
        'F': r'^F (?P<X>[0-9]+) (?P<Y>[0-9]+) (?P<C>[A-Z])$',
        'S': r'^S (?P<Name>.*)$',
        'X': r'^X$'
    }


    def __init__(self, cols_qtt: int, rows_qtt: int):
        """Create a new matrix with blank pixels."""
        pass


    def clear(self):
        """Leave all pixels blank."""
        pass


    def set_color(self, col: int, row: int, color: str):
        """Update a single pixel value."""
        pass


    def draw_vertical(self, col: int, begining_row: int, ending_row: int, color: str):
        """Update an entire vertical line."""
        pass


    def draw_horizontal(self, row: int, begining_col: int, ending_col: int, color: str):
        """Update an entire horizontal line."""
        pass


    def draw_rect(self, l_col: int, l_row: int, r_col: int, r_row: int, color: str):
        """Draw a rectangle from a upper left coordinate up to a right bottom coordinate."""
        pass


    def fill(self, ref_col: int, ref_row: int, color: str):
        """Paint a whole homogeneous area starting by an initial reference coordinate."""
        pass


    def save(self, filename: str):
        """Save all matrix data on a given filename."""
        pass


    def cli_exec(self, raw_command_line: str):
        """Interpret a command line and, if it's valid, apply such command on this object.

        For good practices reasons, this eval function will not create another instance
        of image nor replace the instance itself, i.e., the self pointer will remain constant.
        That said, static method init_by_cli(str) may be useful.

        Return True if could find a valid command and its parameters, otherwise False.
        """
        line = raw_command_line.strip()

        cmd_match = re.match(r'^(?P<cmd>[A-Z]) .*', line)
        if cmd_match is None:
            return False
        cmd = cmd_match.group('cmd')
        if (cmd == Image.__INIT_COMMAND_KEY) or (cmd not in Image.__AVAILABLE_CLI):
            return False

        argsm = re.match(Image.__AVAILABLE_CLI[cmd], line)
        if argsm is None:
            return False

        if cmd == 'C':
            self.clear()
        elif cmd == 'L':
            self.set_color(
                col=int(argsm.group('X')),
                row=int(argsm.group('Y')),
                color=argsm.group('C')
            )
        elif cmd == 'V':
            self.draw_vertical(
                col=int(argsm.group('X')),
                begining_row=int(argsm.group('Y1')),
                ending_row=int(argsm.group('Y2')),
                color=argsm.group('C')
            )
        elif cmd == 'H':
            self.draw_horizontal(
                row=int(argsm.group('X1')),
                begining_col=int(argsm.group('X2')),
                ending_col=int(argsm.group('Y')),
                color=argsm.group('C')
            )
        elif cmd == 'K':
            self.draw_rect(
                l_col=int(argsm.group('X1')),
                l_row=int(argsm.group('Y1')),
                r_col=int(argsm.group('X2')),
                r_row=int(argsm.group('Y2')),
                color=argsm.group('C')
            )
        elif cmd == 'F':
            self.fill(
                ref_col=int(argsm.group('X')),
                ref_row=int(argsm.group('Y')),
                color=argsm.group('C')
            )
        elif cmd == 'S':
            self.save(
                filename=argsm.group('Name')
            )
        elif cmd == 'X':
            exit(0)

        return True


    @staticmethod
    def init_by_cli(raw_command_line):
        """Automate (only the) constructor by a command line interface.

        For other domain commands, use cli_exec non-static method.
        """
        line = raw_command_line.strip()
        pattern = Image.__AVAILABLE_CLI[Image.__INIT_COMMAND_KEY]

        cmd = re.match(pattern, line)
        if cmd is None:
            return False

        return Image(cmd.group('M'), cmd.group('N'))



def main():
    """Start and run CLI execution."""
    matrix = Image.init_by_cli(input())
    while True:
        matrix.cli_exec(input())


if __name__ == '__main__':
    main()
