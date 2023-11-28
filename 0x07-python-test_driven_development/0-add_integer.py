#!/usr/bin/python3


"""Defines two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
