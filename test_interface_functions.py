"""
CS5001
Spring 2023
Final Project -- unittest -- test_interface_functions
Author: Yedian Cheng
"""

import matplotlib.pyplot as plt
import unittest
import pandas as pd
from Park import Park


from user_interface_functions import display_park_distribution_piechart, output_park_info, \
    display_facility_proportion_piechart, \
    display_facility_amount_barchart, explore_facility, explore_neighborhood, \
    output_facility_info, display_park_amount_barchart


class TestInterfaceFunctions(unittest.TestCase):

    def test_explore_facility_empty_dataframe(self):
        facility_df = pd.DataFrame()
        with self.assertRaises(ValueError):
            explore_facility(facility_df)

    def test_explore_facility_not_dataframe(self):
        facility_df = []
        with self.assertRaises(TypeError):
            explore_facility(facility_df)

    def test_display_park_distribution_piechart_valid_input(self):
        parks_per_neighborhood = {'Neighborhood1': 5, 'Neighborhood2': 10, 'Neighborhood3': 7}
        facility_name = 'Tennis'

        # Asserts no error is raised and that the pie chart is displayed
        self.assertIsNone(display_park_distribution_piechart(parks_per_neighborhood, facility_name))
        self.assertTrue(plt.gcf().number > 0)

    def test_empty_parks_per_neighborhood(self):
        parks_per_neighborhood = {}
        facility_name = 'Basketball'

        with self.assertRaises(ValueError):
            display_park_distribution_piechart(parks_per_neighborhood, facility_name)

    def test_not_dict_parks_per_neighborhood(self):
        parks_per_neighborhood = ['Neighborhood1', 5]
        facility_name = 'Basketball'

        with self.assertRaises(TypeError):
            display_park_distribution_piechart(parks_per_neighborhood, facility_name)

    def test_parks_per_neighborhood_negative_values(self):
        parks_per_neighborhood = {'Neighborhood1': 5, 'Neighborhood2': -10, 'Neighborhood3': 7}
        facility_name = 'Swimming'

        with self.assertRaises(ValueError):
            display_park_distribution_piechart(parks_per_neighborhood, facility_name)

    def test_display_park_amount_barchart_valid_input(self):
        parks_per_neighborhood = {"neighborhood1": 2, "neighborhood2": 3, "neighborhood3": 5}
        facility_name = "parking"
        self.assertIsNone(display_park_amount_barchart(parks_per_neighborhood, facility_name))

    def test_display_park_amount_barchart_empty_neighborhood_input(self):
        parks_per_neighborhood = {}
        facility_name = 'Tennis'

        with self.assertRaises(ValueError):
            display_park_amount_barchart(parks_per_neighborhood, facility_name)

    def test_display_park_amount_barchart_not_dict_neighborhood_input(self):
        parks_per_neighborhood = ['Neighborhood 1', -1]
        facility_name = 'Tennis'

        with self.assertRaises(TypeError):
            display_park_amount_barchart(parks_per_neighborhood, facility_name)

    def test_display_park_amount_barchart_invalid_facility_name_input(self):
        parks_per_neighborhood = {'Neighborhood 1': -1, 'Neighborhood 2': 3, 'Neighborhood 3': 8}
        facility_name = 123

        with self.assertRaises(TypeError):
            display_park_amount_barchart(parks_per_neighborhood, facility_name)

    def test_display_park_amount_barchart_negative_values(self):
        parks_per_neighborhood = {'Neighborhood1': 5, 'Neighborhood2': -10, 'Neighborhood3': 7}
        facility_name = 'Swimming'

        with self.assertRaises(ValueError):
            display_park_amount_barchart(parks_per_neighborhood, facility_name)

    def test_output_park_info_with_empty_list(self):
        with self.assertRaises(ValueError):
            output_park_info([])

    def test_output_park_info_with_invalid_input_type(self):
        with self.assertRaises(TypeError):
            output_park_info("not a list")

    def test_output_park_info_with_invalid_list_element_type(self):
        park_obj_lst = [Park("Park1", "1", "Street1", "Neighborhood1", {"Facility1": 1}),
                        "not a Park object",
                        Park("Park2", "2", "Street2", "Neighborhood2", {"Facility2": 1})]
        with self.assertRaises(TypeError):
            output_park_info(park_obj_lst)

    def test_explore_neighborhood_invalid_input_dataframe_is_empty(self):
        with self.assertRaises(ValueError):
            explore_neighborhood(pd.DataFrame())

    def test_explore_neighborhood_invalid_input_dataframe_is_not_dataframe(self):
        with self.assertRaises(TypeError):
            explore_neighborhood("not a dataframe")

    def test_display_facility_amount_barchart_valid_input(self):
        neighborhood_facility_amount_dic = {'Basketball Court': 5, 'Playground': 7, 'Tennis Court': 3}
        neighbourhood_name = 'Kitsilano'

        self.assertIsNone(display_facility_amount_barchart(neighborhood_facility_amount_dic, neighbourhood_name))

    def test_display_facility_amount_barchart_empty_dic(self):
        neighborhood_facility_amount_dic = {}
        neighbourhood_name = 'Kitsilano'

        with self.assertRaises(ValueError):
            display_facility_amount_barchart(neighborhood_facility_amount_dic, neighbourhood_name)

    def test_display_facility_amount_barchart_not_dic(self):
        neighborhood_facility_amount_dic = ['Basketball Court', 5]
        neighbourhood_name = 'Kitsilano'

        with self.assertRaises(TypeError):
            display_facility_amount_barchart(neighborhood_facility_amount_dic, neighbourhood_name)

    def test_display_facility_amount_barchart_invalid_input(self):
        neighborhood_facility_amount_dic = {'Basketball Court': 5, 'Playground': 7, 'Tennis Court': 3}
        neighbourhood_name = 1234

        with self.assertRaises(TypeError):
            display_facility_amount_barchart(neighborhood_facility_amount_dic, neighbourhood_name)


    def test_display_facility_amount_barchart_valid_input(self):
        neighborhood_facility_amount_dic = {'Basketball Court': 5, 'Playground': 7, 'Tennis Court': 3}
        neighbourhood_name = 'Kitsilano'

        self.assertIsNone(display_facility_proportion_piechart(neighborhood_facility_amount_dic, neighbourhood_name))

    def test_display_facility_amount_barchart_empty_dic(self):
        neighborhood_facility_amount_dic = {}
        neighbourhood_name = 'Kitsilano'

        with self.assertRaises(ValueError):
            display_facility_proportion_piechart(neighborhood_facility_amount_dic, neighbourhood_name)

    def test_display_facility_amount_barchart_not_dic(self):
        neighborhood_facility_amount_dic = ['Basketball Court', 5]
        neighbourhood_name = 'Kitsilano'

        with self.assertRaises(TypeError):
            display_facility_proportion_piechart(neighborhood_facility_amount_dic, neighbourhood_name)

    def test_display_facility_amount_barchart_invalid_input(self):
        neighborhood_facility_amount_dic = {'Basketball Court': 5, 'Playground': 7, 'Tennis Court': 3}
        neighbourhood_name = 1234

        with self.assertRaises(TypeError):
            display_facility_proportion_piechart(neighborhood_facility_amount_dic, neighbourhood_name)

    def test_output_facility_empty_dict(self):
        with self.assertRaises(ValueError):
            output_facility_info({})

    def test_output_facility_not_dict(self):
        with self.assertRaises(TypeError):
            output_facility_info(['Basketball Court', 5])


def main():

    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()




