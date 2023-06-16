#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square."""
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets Position of square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.size * self.size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
