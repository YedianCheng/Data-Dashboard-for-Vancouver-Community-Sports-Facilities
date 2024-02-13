"""
CS5001
Spring 2023
Final Project -- driver
Author: Yedian Cheng

This program reads and cleans data from two URL addresses,
extracts the data that need, and generates two dataframes.

Then, the user will see a menu panel,
ask the user if they want to explore Vancouver's neighbourhoods, parks, and sports facilities:

1. The user can choose to explore Vancouver's sports facilities.
When the user enters the name of a sports facility she likes,
if the sports facility cannot be found in Vancouver's sports facilities,
he will be prompted to re-enter.
If it can be found,
he will be told which parks have these sports facilities and their addresses.

2. The user can choose to enter a neighbourhood he is interested in.
If the community cannot be found among Vancouver's neighbourhoods,
he will be prompted to re-enter.
If it can be found,
he will be told what sports facilities are available in the neighbourhood and their corresponding quantities.
3. The user can also choose to exit.

When this is over,
the user will be asked if they want to continue exploring.
If yes, they will return to the main menu. If not, they will exit.

"""

from constants import PARK_URL, FACILITY_URL, EXPLORE_FACILITY, EXPLORE_NEIGHBOURHOOD, EXIT
from clean_data_functions import clean_data_facility, clean_data_parks, read_url
from analysis_functions import get_parks_with_facility, create_park_obj, create_park_dictionary, \
    get_parks_per_neighborhood, create_neighborhood_object, count_facility_by_neighborhood
from user_interface_functions import display_park_distribution_piechart, output_park_info, \
    display_facility_proportion_piechart, \
    display_facility_amount_barchart, display_menu, explore_facility, explore_neighborhood, explore_system_again, \
    output_facility_info, display_park_amount_barchart, output_invalid_input_message


def main():
    try:

        # pull and clean the data
        facility_data = read_url(FACILITY_URL)
        facility_df = clean_data_facility(facility_data)
        park_data = read_url(PARK_URL)
        park_df = clean_data_parks(park_data)

        # combine the data
        park_dict = create_park_dictionary(park_df, facility_df)

        explore_again = True

        while explore_again:
            # display the menu and ask the user to make a choice
            user_choice = display_menu()

            if not user_choice in [EXPLORE_FACILITY, EXPLORE_NEIGHBOURHOOD, EXIT]:
                output_invalid_input_message()

            elif user_choice == EXPLORE_FACILITY:

                # ask the user to enter the facility name
                facility_name = explore_facility(facility_df)

                # make analyse
                park_obj_lst = create_park_obj(park_dict)
                filter_park_obj_lst = get_parks_with_facility(park_obj_lst, facility_name)
                parks_per_neighborhood = get_parks_per_neighborhood(filter_park_obj_lst)

                # display the amount of parks contains this facility in each neighborhoods
                display_park_amount_barchart(parks_per_neighborhood, facility_name)
                # display the distribution of parks contains this facility across neighborhoods
                display_park_distribution_piechart(parks_per_neighborhood, facility_name)

                # output park information which contains the facility
                output_park_info(filter_park_obj_lst)

                # ask the user if he wants to explore again
                explore_again = explore_system_again()

            elif user_choice == EXPLORE_NEIGHBOURHOOD:

                # ask the user to enter the facility name
                neighborhood_name = explore_neighborhood(park_df)

                # make analyse
                park_obj_lst = create_park_obj(park_dict)
                neighborhood_obj = create_neighborhood_object(neighborhood_name, park_obj_lst)
                neighborhood_facility_amount_dic = count_facility_by_neighborhood(neighborhood_obj)

                # display amount and proportion  of various facilities within a neighborhood
                display_facility_amount_barchart(neighborhood_facility_amount_dic, neighborhood_name)
                display_facility_proportion_piechart(neighborhood_facility_amount_dic, neighborhood_name)
                output_facility_info(neighborhood_facility_amount_dic)

                # ask the user if he wants to explore again
                explore_again = explore_system_again()

            elif user_choice == EXIT:
                explore_again = False

    except TypeError as ex:
        print("Invalid types", type(ex), ex)

    except ValueError as ex:
        print("Invalid value", type(ex), ex)

    except NameError as ex:
        print("The name is not defined", type(ex), ex)

    except IndexError as ex:
        print("Invalid index", type(ex), ex)

    except AttributeError as ex:
        print("Invalid attribute", type(ex), ex)


main()
