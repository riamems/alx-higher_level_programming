#!/usr/bin/python3


"""Checks if the object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """Checks if the given object is an instance

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    """
    return type(obj) == a_class
