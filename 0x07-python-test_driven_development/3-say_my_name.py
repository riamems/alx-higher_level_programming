#!/usr/bin/python3


"""Function that prints my name is."""


def say_my_name(first_name, last_name=""):
    """Prints a formatted message with the provided names."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
