#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

 
    def __init__(self, size=0):
        """Initialize a new squar"""
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""

        return self.__size

    @size.setter
    def size(self, size):
        """Set size of square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.size * self.size)
