"""
CS5001
Spring 2023
Final Project -- unittest -- Class TestNeighbourhood
Author: Yedian Cheng
"""


import unittest
from Neighbourhood import Neighbourhood
from Park import Park


class TestNeighbourhood(unittest.TestCase):

    def test_create_neighborhood_with_valid_data(self):
        neighbourhood_name = "Downtown"
        park_objects = [Park("Central Park", "123",  "Main Street", "Downtown",  {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1})]

        neighbourhood1 = Neighbourhood(neighbourhood_name, park_objects)
        self.assertEqual(neighbourhood1.neighbourhood_name, "Downtown")
        self.assertEqual(neighbourhood1.park_objects, park_objects)

    def test_create_neighbourhood_with_empty_neighbourhood_name(self):
        neighbourhood_name = " "
        park_objects = [Park("Central Park", "123", "Main Street", "Downtown",
                             {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1})]

        with self.assertRaises(ValueError):
            neighbourhood1 = Neighbourhood(neighbourhood_name, park_objects)

    def test_create_neighbourhood_with_not_str_neighbourhood_name(self):
        neighbourhood_name = 1
        park_objects = [Park("Central Park", "123", "Main Street", "Downtown",
                             {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1})]

        with self.assertRaises(TypeError):
            neighbourhood1 = Neighbourhood(neighbourhood_name, park_objects)

    def test_create_neighbourhood_with_empty_park_list(self):
        neighbourhood_name = "Downtown"
        park_objects = []

        with self.assertRaises(ValueError):
            neighbourhood1 = Neighbourhood(neighbourhood_name, park_objects)

    def test_create_neighbourhood_with_not_list_park(self):
        neighbourhood_name = "Downtown"
        park_objects = "park"

        with self.assertRaises(TypeError):
            neighbourhood1 = Neighbourhood(neighbourhood_name, park_objects)

    def test_get_name(self):
        neighbourhood_name = "Downtown"
        park_objects = [Park("Central Park", "123", "Main Street", "Downtown",
                             {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1})]

        neighbourhood1 = Neighbourhood(neighbourhood_name, park_objects)
        self.assertEqual(neighbourhood1.get_name(), "Downtown")


    def test_get_park_objects(self):
        neighbourhood_name = "Downtown"
        park_objects = [Park("Central Park", "123", "Main Street", "Downtown",
                             {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1})]

        neighbourhood1 = Neighbourhood(neighbourhood_name, park_objects)
        self.assertEqual(neighbourhood1.get_park_objects(), park_objects )

def main():

    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
