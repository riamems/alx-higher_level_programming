#!/usr/bin/python3


"""Appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file

    Args:
        filename (str, optional): The name of the file.
        text (str): The string to be appended to the file.

    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
