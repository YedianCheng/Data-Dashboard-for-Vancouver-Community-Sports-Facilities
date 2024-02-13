"""
CS5001
Spring 2023
Final Project -- unittest -- test_analysis_functions
Author: Yedian Cheng
"""


import unittest
import pandas as pd
from Park import Park
from Neighbourhood import Neighbourhood
from analysis_functions import get_parks_with_facility, create_park_obj, create_park_dictionary, \
    get_parks_per_neighborhood, create_neighborhood_object, count_facility_by_neighborhood


class TestAnalysisFunctions(unittest.TestCase):

    def test_create_park_dictionary(self):

        park_df = pd.DataFrame(
            {"Name": ["Park A", "Park B"], "StreetNumber": ["123", "456"], "StreetName": ["Main St", "Elm St"],
             "NeighbourhoodName": ["Neighbourhood A", "Neighbourhood B"]})
        facility_df = pd.DataFrame(
            {"Name": ["Park A", "Park B", "Park B"], "FacilityType": ["Tennis", "Swimming Pool", "Tennis"],
             "FacilityCount": ["3", "2", "1"]})
        expected_output = {"Park A": {"StreetNumber": "123", "StreetName": "Main St", "NeighbourhoodName": "Neighbourhood A",
                       "FacilityType": {"Tennis": 3}
                       }, "Park B": {"StreetNumber": "456", "StreetName": "Elm St", "NeighbourhoodName": "Neighbourhood B",
                       "FacilityType": {"Swimming Pool": 2, "Tennis": 1}}}

        self.assertEqual(create_park_dictionary(park_df, facility_df), expected_output)

    def test_empty_park_df(self):
        with self.assertRaises(ValueError):
            park_df = pd.DataFrame()
            facility_df = pd.DataFrame(
                {"Name": ["Park A", "Park B", "Park B"], "FacilityType": ["Tennis", "Swimming Pool", "Tennis"],
                 "FacilityCount": ["3", "2", "1"]})
            create_park_dictionary(park_df, facility_df)

    def test_empty_facility_df(self):
        with self.assertRaises(ValueError):
            facility_df = pd.DataFrame()
            park_df = pd.DataFrame(
                {"Name": ["Park A", "Park B"], "StreetNumber": ["123", "456"], "StreetName": ["Main St", "Elm St"],
                 "NeighbourhoodName": ["Neighbourhood A", "Neighbourhood B"]})

            create_park_dictionary(park_df, facility_df)

    def test_non_park_dataframe_input(self):
        facility_df = pd.DataFrame(
            {"Name": ["Park A", "Park B", "Park B"], "FacilityType": ["Tennis", "Swimming Pool", "Tennis"],
             "FacilityCount": ["3", "2", "1"]})
        with self.assertRaises(TypeError):
            create_park_dictionary(" ", facility_df)

    def test_non_facility_dataframe_input(self):
        park_df = pd.DataFrame(
            {"Name": ["Park A", "Park B"], "StreetNumber": ["123", "456"], "StreetName": ["Main St", "Elm St"],
             "NeighbourhoodName": ["Neighbourhood A", "Neighbourhood B"]})
        with self.assertRaises(TypeError):
            create_park_dictionary(park_df, " ")

    def test_invalid_facility_count(self):
        park_df = pd.DataFrame(
            {"Name": ["Park A", "Park B"], "StreetNumber": ["123", "456"], "StreetName": ["Main St", "Elm St"],
             "NeighbourhoodName": ["Neighbourhood A", "Neighbourhood B"]})
        invalid_facility_df = pd.DataFrame({"Name": ["Park A"], "FacilityType": ["Tennis"], "FacilityCount": ["one"]})
        with self.assertRaises(TypeError):
            create_park_dictionary(park_df, invalid_facility_df)

    def test_empty_dict(self):
        with self.assertRaises(ValueError):
            create_park_obj({})

    def test_not_dict(self):
        with self.assertRaises(TypeError):
            create_park_obj([])
            create_park_obj(1)

    def test_valid_dict(self):
        park_dict ={"Park A": {"StreetNumber": "123", "StreetName": "Main St", "NeighbourhoodName": "Neighborhood A", "FacilityType": {"Tennis": 3}
            }, "Park B": {"StreetNumber": "456","StreetName": "Elm St", "NeighbourhoodName": "Neighborhood B", "FacilityType": {"Tennis": 1,"Swimming Pool": 2}}}
        park_obj_lst = create_park_obj(park_dict)
        self.assertEqual(len(park_obj_lst), 2)
        self.assertEqual(park_obj_lst[0].get_name(), 'Park A')
        self.assertEqual(park_obj_lst[0].get_neighborhood(), 'Neighborhood A')
        self.assertEqual(park_obj_lst[0].get_facility_info(), {"Tennis": 3})
        self.assertEqual(park_obj_lst[1].get_name(), 'Park B')
        self.assertEqual(park_obj_lst[1].get_neighborhood(), 'Neighborhood B')
        self.assertEqual(park_obj_lst[1].get_facility_info(), {"Tennis": 1,"Swimming Pool": 2})


    def test_park_obj_lst_not_list(self):
        with self.assertRaises(TypeError):
            get_parks_with_facility("1", "FacilityName")

    def test_facility_name_not_str(self):
        with self.assertRaises(TypeError):
            get_parks_with_facility([], 1234)

    def test_park_obj_lst_empty(self):
        with self.assertRaises(ValueError):
            get_parks_with_facility([], "FacilityName")

    def test_facility_not_found(self):
        park1 = Park("Park1", "1", "Street1", "Neighborhood1", {"Facility1": 1})
        park2 = Park("Park2", "2", "Street2", "Neighborhood2", {"Facility2": 2})
        park3 = Park("Park3", "3", "Street3", "Neighborhood3", {"Facility3": 3})

        parks = [park1, park2, park3]
        parks_with_facility = get_parks_with_facility(parks, "Facility4")

        self.assertEqual(parks_with_facility, [])

    def test_facility_found(self):
        park1 = Park("Park1", "1", "Street1", "Neighborhood1", {"Facility1": 1, "Facility2": 2})
        park2 = Park("Park2", "2", "Street2", "Neighborhood2", {"Facility2": 2, "Facility3": 3})
        park3 = Park("Park3", "3", "Street3", "Neighborhood3", {"Facility3": 3, "Facility4": 4})

        parks = [park1, park2, park3]
        parks_with_facility = get_parks_with_facility(parks, "Facility2")

        self.assertEqual(parks_with_facility, [park1, park2])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            get_parks_per_neighborhood([])

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            get_parks_per_neighborhood(" ")

    def test_correct_output(self):
        self.park_obj_lst = parks = [
            Park("Park1", "1", "Street1", "Neighborhood1", {"Facility1": 1}),
            Park("Park2", "2", "Street2", "Neighborhood2", {"Facility2": 1}),
            Park("Park3", "3", "Street3", "Neighborhood1", {"Facility1": 1}),
            Park("Park4", "4", "Street4", "Neighborhood2", {"Facility2": 1}),
            Park("Park5", "5", "Street5", "Neighborhood2", {"Facility1": 1})
        ]

        expected_output = {"Neighborhood1": 2, "Neighborhood2": 3}
        self.assertEqual(get_parks_per_neighborhood(parks), expected_output)

    def test_create_neighborhood_object_with_valid_input(self):
        neighborhood_name = "Neighborhood1"
        park1 = Park("Park1", "1", "Street1", "Neighborhood1", {"Facility1": 1})
        park2 = Park("Park2", "2", "Street2", "Neighborhood2", {"Facility2": 1})
        park_obj_lst = [park1, park2]

        neighborhood_obj = create_neighborhood_object(neighborhood_name, park_obj_lst)
        self.assertEqual(neighborhood_obj.get_name(), neighborhood_name)

    def test_create_neighborhood_object_with_empty_park_list(self):
        neighborhood_name = "Neighborhood1"
        with self.assertRaises(ValueError):
            create_neighborhood_object(neighborhood_name, [])

    def test_create_neighborhood_object_with_non_list_park_obj_lst(self):
        neighborhood_name = "Neighborhood1"
        with self.assertRaises(TypeError):
            create_neighborhood_object(neighborhood_name, " ")

    def test_create_neighborhood_object_with_non_string_neighborhood_name(self):
        park1 = Park("Park1", "1", "Street1", "Neighborhood1", {"Facility1": 1})
        park2 = Park("Park2", "2", "Street2", "Neighborhood2", {"Facility2": 1})
        park_obj_lst = [park1, park2]
        with self.assertRaises(TypeError):
            create_neighborhood_object(123, park_obj_lst)

    def test_count_facility_by_neighborhood(self):
        park1 = Park("Park1", "1", "Street1", "Neighborhood1", {"Facility1": 1})
        park2 = Park("Park2", "2", "Street2", "Neighborhood2", {"Facility2": 1})
        park3 = Park("Park3", "3", "Street3", "Neighborhood1", {"Facility1": 1})

        neighborhood = Neighbourhood("Neighborhood1", [park1, park3])
        expected_counts = {"Facility1": 2}
        self.assertEqual(count_facility_by_neighborhood(neighborhood), expected_counts)


def main():

    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()

