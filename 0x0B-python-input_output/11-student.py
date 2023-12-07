#!/usr/bin/python3


"""Defines a class Student"""


class Student:
    """Represents a class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
        """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for attr, value in json.items():
            setattr(self, attr, value)
