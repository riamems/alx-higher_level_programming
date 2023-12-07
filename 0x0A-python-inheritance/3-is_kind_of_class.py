#!/usr/bin/python3


"""Checks if the object is an instance."""


def is_kind_of_class(obj, a_class):
    """Checks if the given object is an instance

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    """
    return isinstance(obj, a_class)
