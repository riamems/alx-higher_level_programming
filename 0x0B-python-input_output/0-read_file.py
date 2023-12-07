#!/usr/bin/python3


"""Reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read and print the contents of a UTF-8 text file to stdout.

    Args:
        filename (str, optional): The name of the file to be read.

    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
