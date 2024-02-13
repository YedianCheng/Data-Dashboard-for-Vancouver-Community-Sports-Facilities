"""
CS5001
Spring 2023
Final Project -- class Neighbourhood
Author: Yedian Cheng
"""
from validate_data_function import validate_data

class Neighbourhood:
    """
    A class representing a neighbourhood.

    Attributes:
    neighbourhood_name(str): The name of the neighbourhood.
    park_objects(list): A list of park objects in this neighbourhood.

    Methods:
    get_name(): Returns the name of the neighbourhood.
    get_park_objects(): Returns a list of park objects in this neighbourhood
    """

    def __init__(self, neighbourhood_name, park_objects):
        """
        Constructs a new Neighbourhood object.

        Parameters:
        neighbourhood_name(str): The name of the neighbourhood.
        park_objects(list): A list of park objects in this neighbourhood.

        Raises:
        ValueError -- if the neighbourhood name is empty
                   -- if the park_objects list is empty
        TypeError -- if the neighbourhood name is not a string
                  -- if the park_objects is not a list
        """
        validate_data(neighbourhood_name, str)
        validate_data(park_objects, list)

        if neighbourhood_name.strip() == '':
            raise ValueError("The neighbourhood name should not be empty.")
        if not park_objects:
            raise ValueError("The park_objects should not be empty.")


        self.neighbourhood_name = neighbourhood_name
        self.park_objects = park_objects

    def get_name(self):
        """
        Returns the name of the neighbourhood.

        Parameter:
        self: A neighbourhood object

        Returns(str): The name of the neighbourhood.
        """
        return self.neighbourhood_name

    def get_park_objects(self):
        """
        Returns a list of park objects in this neighbourhood.

        Parameter:
        self: A neighbourhood object

        Returns(list): A list of park objects in this neighbourhood
        """
        return self.park_objects
