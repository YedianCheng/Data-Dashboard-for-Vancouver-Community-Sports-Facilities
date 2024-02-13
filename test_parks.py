"""
CS5001
Spring 2023
Final Project -- unittest -- Class TestPark
Author: Yedian Cheng
"""

import unittest
from Park import Park

class testPark(unittest.TestCase):

    def test_create_park_with_valid_data(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        park1 = Park(park_name, address_number, address_road, neighborhood, facility_info)

        self.assertEqual(park1.park_name, "Central Park")
        self.assertEqual(park1.address_number, "123")
        self.assertEqual(park1.address_road, "Main Street")
        self.assertEqual(park1.neighborhood, "Downtown")
        self.assertEqual(park1.facility_info, {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1})

    def test_create_park_with_empty_road_number(self):
        park_name = "Central Park"
        address_number = ""
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(ValueError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_non_numeric_road_number(self):
        park_name = "Central Park"
        address_number = "abc"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(TypeError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_empty_road(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = ""
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(ValueError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_not_string_road(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = 1
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(TypeError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_empty_park_name(self):
        park_name = ""
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(ValueError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_not_string_park_name(self):
        park_name = 1
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(TypeError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_empty_neighborhood(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = ""
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(ValueError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_not_string_neighborhood(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = 1
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        with self.assertRaises(TypeError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_empty_facility_info(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {}

        with self.assertRaises(ValueError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_create_park_with_non_dict_facility_info(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main"
        neighborhood = "Downtown"
        facility_info = ["Tennis Courts", 4]
        with self.assertRaises(TypeError):
            park = Park(park_name, address_number, address_road, neighborhood, facility_info)

    def test_get_name(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        park = Park(park_name, address_number, address_road, neighborhood, facility_info)
        self.assertEqual(park.get_name(), "Central Park")

    def test_get_neighborhood(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        park = Park(park_name, address_number, address_road, neighborhood, facility_info)
        self.assertEqual(park.get_neighborhood(), "Downtown")

    def test_get_facility_info(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        park = Park(park_name, address_number, address_road, neighborhood, facility_info)
        self.assertEqual(park.get_facility_info(), {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1})

    def test_str(self):
        park_name = "Central Park"
        address_number = "123"
        address_road = "Main Street"
        neighborhood = "Downtown"
        facility_info = {"Tennis Courts": 4, "Basketball Courts": 2, "Playgrounds": 1}

        park = Park(park_name, address_number, address_road, neighborhood, facility_info)
        self.assertEqual(str(park), f"{park_name}: located in NO.{address_number} {address_road}, in {neighborhood}.")


def main():

    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()