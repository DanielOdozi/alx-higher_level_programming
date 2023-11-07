#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Set the property of student.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple data structure,
        (list, dictionary, string, integer and boolean) for JSON serialization,
        of an object.

        Args:
            self:

        Returns:
            dict: dictionary.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
