#!/usr/bin/python3


"""Checks if the object is an instance"""


def inherits_from(obj, a_class):
    """Checks if the given object is an instance

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
