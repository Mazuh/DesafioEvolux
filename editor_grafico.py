#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
Program that reads a sequence of commands to handle a MxN matrix of pixels.
"""

class Image(object):
    """
    Matrix of pixels.

    Its indexes are from 1 up to its dimensions (inclusive ranges).
    """
    _BLANK = 'O'

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


def main():
    """TODO: implement main routines."""
    print('hello there!')

if __name__ == '__main__':
    main()
