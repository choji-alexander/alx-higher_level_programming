#!/usr/bin/python3
"""This program define a class Square."""

class Square:
    """This program represents a square."""
    pass

    def __init__(self, size=0):
        """Initialize a new Square."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
