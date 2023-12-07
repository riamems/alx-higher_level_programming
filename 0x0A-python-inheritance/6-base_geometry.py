#!/usr/bin/python3


"""Writes a class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raises an Exception with the message "area() is not implemented"

        This method is intended to be overridden

        Raises:
            Exception: Always raises an Exception
        """
        raise Exception("area() is not implemented")
