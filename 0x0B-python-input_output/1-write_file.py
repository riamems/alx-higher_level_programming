#!/usr/bin/python3


"""Writes a string to s text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file

    Args:
        filename (str, optional): The name of the file.
        text (str): The string to be written to the file.

    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
