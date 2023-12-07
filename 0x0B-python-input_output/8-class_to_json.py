#!/usr/bin/python3

"""Representation suitable for JSON serialization."""


def class_to_json(obj):
    """Convert an instance of a class to a dictionary

    Args:
        obj: An instance of a class with serializable attributes.

    """
    json_dict = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
