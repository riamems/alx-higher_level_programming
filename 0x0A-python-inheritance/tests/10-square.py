#!/usr/bin/python3


"""Write a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """
        Initialize a Square instance with a specified size.

        Args:
            size (int): The size of the square (positive integer).

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
