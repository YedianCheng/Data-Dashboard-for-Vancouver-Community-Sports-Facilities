"""
CS5001
Spring 2023
Final Project -- unittest -- test_cleandata_functions
Author: Yedian Cheng
"""
import requests
import unittest
import pandas as pd
from clean_data_functions import clean_data_facility, clean_data_parks, read_url
from constants import PARK_URL

class TestCleanDataFunctions(unittest.TestCase):

    def test_http_error(self):
        url = 'https://sss.com/404'
        with self.assertRaises(requests.exceptions.HTTPError):
            read_url(url)

    def test_success(self):
        # Test if function returns a non-empty list for a valid URL
        lines = read_url(PARK_URL)
        self.assertTrue(len(lines) > 0)

    def test_clean_data_parks(self):
        lines = [
            "Name,StreetNumber,StreetName,NeighbourhoodName,Facilities",
            "Park 1,789,Third St,Neighbourhood C,N",
            "Park 2,1011,Fourth St,Neighbourhood D,Y"
        ]

        expected_output = pd.DataFrame({
            "Name": ["Park 2"],
            "StreetNumber": ['1011'],
            "StreetName": ["Fourth St"],
            "NeighbourhoodName": ["Neighbourhood D"]
        })

        result = clean_data_parks(lines)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_empty_input(self):
        lines = []
        with self.assertRaises(ValueError):
            clean_data_parks(lines)

    def test_empty_dataframe(self):
        lines = [
            "Name,Street Number,Street Name,Neighbourhood,Facilities",
            "Park 1,123,Main St,Neighbourhood A,No"
        ]

        with self.assertRaises(ValueError):
            clean_data_parks(lines)

    def test_invalid_input(self):
        lines = "invalid input"

        with self.assertRaises(TypeError):
            clean_data_parks(lines)

    def test_clean_data_facility_valid_input(self):
        lines = [
            "FacilityCount,FacilityType,Name",
            "1,Facility1,Park1",
            "2,Facility2,Park2",
            "3,Facility3,Park3",
        ]
        result = clean_data_facility(lines)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 3)

    def test_clean_data_facility_empty_lines(self):
        with self.assertRaises(ValueError):
            clean_data_facility([])

    def test_clean_data_facility_empty_dataframe(self):
        with self.assertRaises(ValueError):
            clean_data_facility(["FacilityCount,FacilityType,Name"])

    def test_clean_data_facility_invalid_input(self):
        with self.assertRaises(TypeError):
            clean_data_facility("not a list")

        with self.assertRaises(TypeError):
            clean_data_facility(123)


def main():

    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()

