"""
CS5001
Spring 2023
Final Project -- unittest -- test_validate_functions
Author: Yedian Cheng
"""


import unittest
from validate_data_function import validate_data


class TestValidateData(unittest.TestCase):

    def test_validate_string(self):
        # Test with a string
        self.assertIsNone(validate_data("hello", str))

    def test_validate_int(self):
        # Test with an integer
        self.assertIsNone(validate_data(42, int))

    def test_validate_float(self):
        # Test with a float
        self.assertIsNone(validate_data(3.14, float))

    def test_validate_list(self):
        # Test with a list
        self.assertIsNone(validate_data([1, 2, 3], list))

    def test_validate_dict(self):
        # Test with a dictionary
        self.assertIsNone(validate_data({"name": "Alice", "age": 30}, dict))

    def test_validate_tuple(self):
        # Test with a tuple
        self.assertIsNone(validate_data(("apple", "banana", "cherry"), tuple))

    def test_validate_wrong_type(self):
        # Test with a wrong type
        with self.assertRaises(TypeError):
            validate_data(42, str)
