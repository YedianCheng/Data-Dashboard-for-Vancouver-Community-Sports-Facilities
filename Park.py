"""
CS5001
Spring 2023
Final Project -- Milestone1--class Park
Author: Yedian Cheng
"""
from validate_data_function import validate_data

class Park:
    """
    A class representing a park.

    Attributes:
    park_name(str): The name of the park.
    address_number(str): The number of the park's address.
    address_road(str):The road of the park's address.
    neighborhood(str):The neighborhood in which the park is located.
    facility_info (dict): A dictionary containing the name and number of each facility in the park.


    Methods:
    get_name(): Returns the name of the park.
    get_neighborhood(): Returns the name of the neighborhood in which the park is located.
    get_facility_info(): Returns the dictionary containing the name and number of each facility in the park.
    __str__(): Returns a string representation of the park.
    """

    def __init__(self, park_name, address_number, address_road, neighborhood, facility_info):
        """
        Constructs a new Park object.

        Parameters:
        park_name(str): The name of the park.
        address_number(str): The number of the park's address.
        address_road(str):The road of the park's address.
        neighborhood(str):The neighborhood in which the park is located.
        facility_info (dict): A dictionary containing the name and number of each facility in the park.

        Raises:
        ValueError -- if the road number is empty
                   -- if the road is empty
                   -- if the park name is empty
                   -- if the neighborhood is empty
                   -- if the facility_info list is empty
        TypeError  -- if the road number is not a number
                   -- if the road street is not a string
                   -- if the park name is not a string
                   -- if the facility_info is not a dictionary
        """
        validate_data(park_name, str)
        validate_data(neighborhood, str)
        validate_data(address_road, str)
        validate_data(facility_info, dict)

        if address_number.strip() == '':
            raise ValueError("The road number should not be empty.")
        elif not address_number.isdigit():
            raise TypeError("The road number should be a number.")
        elif address_road.strip() == '':
            raise ValueError("The road shouldn't be empty.")
        elif park_name.strip() == '':
            raise ValueError("The park name shouldn't be empty.")
        elif neighborhood.strip() == '':
            raise ValueError("The neighborhood shouldn't be empty.")
        elif not facility_info:
            raise ValueError("The facility_info list is empty")

        validate_data(park_name, str)
        validate_data(neighborhood, str)
        validate_data(address_road, str)
        validate_data(facility_info, dict)


        self.address_number = address_number
        self.address_road = address_road
        self.park_name = park_name
        self.neighborhood = neighborhood
        self.facility_info = facility_info

    def get_name(self):
        """
        Returns the name of the park.

        Parameter:
        self: A park object

        Returns(str): The name of the park.
        """
        return self.park_name

    def get_neighborhood(self):
        """
        Returns the neighborhood of the park.

        Parameter:
        self: A park object

        Returns(str): The neighborhood of the park.
        """
        return self.neighborhood

    def get_facility_info(self):
        """
        Returns a dictionary containing the name and number of each facility in the park.

        Parameter:
        self: A park object

        Returns(dict): A dictionary containing the name and number of each facility in the park.
        """
        return self.facility_info

    def __str__(self):
        """
        Returns a string representation of the park.

        Parameter:
        self: A park object

        Returns(str): A string in the format "{park_name}: located in NO.{address_number} {address_road}, in {neighborhood}."
        """

        return f"{self.park_name}: located in NO.{self.address_number} {self.address_road}, in {self.neighborhood}."
