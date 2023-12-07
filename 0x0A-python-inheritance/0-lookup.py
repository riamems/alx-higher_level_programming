#!/usr/bin/python3


"""A function for attributes and obj methods"""


def lookup(obj):
    """Returns a list of available attributes and methods of the given object.

    Args:
        obj (object): The object to inspect.
    """
    return dir(obj)
