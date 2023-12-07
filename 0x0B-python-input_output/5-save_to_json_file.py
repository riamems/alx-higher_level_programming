#!/usr/bin/python3

"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
