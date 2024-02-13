"""
CS5001
Spring 2023
Final Project -- user_interface_functions
Author: Yedian Cheng
"""

from constants import NEIGHBOURHOOD, FACILITYTAPE, TOP_ADJUSTMENT, X_LIMIT_LEFT, X_LIMIT_RIGHT, X_LABEL_ALIGNMENT, \
    CENTER, BOTTOM_ADJUSTMENT, X_LABEL_ROTATION, FACILITYNUM, PARK_NUM, PCT_DISTANCE, ATUOPCT, YES, NO
import matplotlib.pyplot as plt
import pandas as pd
from validate_data_function import validate_data
from Park import Park


# Function1: explore_facility
def explore_facility(facility_df):
    """
    Prompts the user to input the name of their favorite sports facility
    and returns the name if it exists in the provided facilities DataFrame.

    Parameters:
    facility_df (pandas.DataFrame): A DataFrame containing sports facility information.

    Raise:
    ValueError: If facility_df is empty.
    TypeError: If facility_df is not a dataframe

    Returns:
    facility_name(str): The name of the facility
    """

    validate_data(facility_df, pd.DataFrame)

    if facility_df.empty:
        raise ValueError("facility_df is empty")

    print("Welcome to explore parks and sports facilities in Vancouver!\n")
    print("May I kindly ask you to provide the name of your favorite sports facility? \n")
    print("I can assist you in finding the parks that have it, as well as their address.\n")

    facility_list = list(set(facility_df[FACILITYTAPE]))

    print("Here are the facilities you can choose:\n")
    print(facility_list)

    is_valid_input = False
    while not is_valid_input:
        facility_name = input("Please enter the name of the facility:\n")
        if not facility_name in facility_list:
            print(
                f"I'm sorry, but {facility_name} is not found in any parks in Vancouver. Please enter another facility name:\n")
        elif facility_name.isspace():
            print("You entered only white spaces. Please enter a valid facility name:\n")
        else:
            print(f"\n Here is the distribution of {facility_name} in various neighborhoods in Vancouver.\n")
            print(f"Here are the parks that contain {facility_name}:\n")

            return facility_name


# Function2: display_park_distribution_piechart
def display_park_distribution_piechart(parks_per_neighborhood, facility_name):
    """
    Displays a pie chart for the given data dictionary.

    Parameters:
    parks_per_neighborhood(dict): A dictionary containing the count of all parks which has the facility in the neighbourhood
    facility_name(str): the name of the facility

    Raise:
    ValueError: If parks_per_neighborhood dictionary is empty.
                If parks_per_neighborhood values is negative integers.
    TypeError: If parks_per_neighborhood is not a dictionary.
               If facility_name is not a string.

    Returns:
    Nothing
    """
    validate_data(parks_per_neighborhood, dict)
    validate_data(facility_name, str)

    if not parks_per_neighborhood:
        raise ValueError("parks_per_neighborhood dictionary is empty")

    for value in parks_per_neighborhood.values():
        if not isinstance(value, int) or value < 0:
            raise ValueError("parks_per_neighborhood values must be non-negative integers")


    labels = list(parks_per_neighborhood.keys())
    values = list(parks_per_neighborhood.values())

    plt.pie(values, labels=labels, autopct=ATUOPCT, pctdistance=PCT_DISTANCE)
    plt.title(f'{facility_name} Facility Distribution by Neighbourhood')

    plt.show()


# Function3: display_facility_distribution_barchart
def display_park_amount_barchart(parks_per_neighborhood, facility_name):
    """
    Displays a pie chart for the given data dictionary.

    Parameters:
    parks_per_neighborhood(dict): A dictionary containing the count of all parks which has the facility in the neighbourhood
    facility_name(str): the name of the facility

    Raise:
    ValueError: If parks_per_neighborhood dictionary is empty.
                If parks_per_neighborhood values is negative integers.
    TypeError: If parks_per_neighborhood is not a dictionary.
               If facility_name is not a string.
    Returns:
    Nothing
    """
    validate_data(parks_per_neighborhood, dict)
    validate_data(facility_name, str)

    if not parks_per_neighborhood:
        raise ValueError("parks_per_neighborhood dictionary is empty")

    for value in parks_per_neighborhood.values():
        if not isinstance(value, int) or value < 0:
            raise ValueError("parks_per_neighborhood values must be non-negative integers")


    plt.bar(range(len(parks_per_neighborhood)), list(parks_per_neighborhood.values()), align='center')
    plt.xticks(range(len(parks_per_neighborhood)), list(parks_per_neighborhood.keys()))

    plt.xlim(X_LIMIT_LEFT, len(facility_name) - X_LIMIT_RIGHT)
    plt.xticks(rotation=X_LABEL_ROTATION, ha=X_LABEL_ALIGNMENT)

    plt.xlabel(NEIGHBOURHOOD)
    plt.ylabel(PARK_NUM)
    plt.title(f'Amount of parks contains {facility_name} in Different Neighborhoods')

    plt.subplots_adjust(bottom=BOTTOM_ADJUSTMENT)

    plt.show()


# Function4: output_park_info
def output_park_info(park_obj_lst):
    """
    print the information of the park

    Parameters:
    park_obj_lst (list): A list of park objects

    Raise:
    ValueError: If park_obj_lst is empty.
    TypeError: If park_obj_lst is not a list
               If park_obj_lst not only contain Park objects

    Returns:
    nothing
    """
    validate_data(park_obj_lst, list)

    if not park_obj_lst:
        raise ValueError("park_obj_lst is empty")

    for park in park_obj_lst:
        if not isinstance(park, Park):
            raise TypeError("park_obj_lst should only contain Park objects")
        print(park.__str__())


# Function5: explore_the_neighbourhood
def explore_neighborhood(park_df):
    """
    Prompts the user to input the name of their neighbourhood
    and returns the name if it exists in the provided park DataFrame.

    Parameters:
    park_df (pandas.DataFrame): A DataFrame containing park information.

    Raise:
    ValueError: If park_df is empty.
                If neighbourhood_list is empty
    TypeError: If park_df is not a dataframe

    Returns:
    neighbourhood_name(str): The name of the neighbourhood
    """

    validate_data(park_df, pd.DataFrame)

    if park_df.empty:
        raise ValueError("park_df is empty")

    print("May I ask which neighborhood you reside in? \n")
    print("I would be happy to inform you about the number of sports facilities in your area.\n")

    neighbourhood_list = list(set(park_df[NEIGHBOURHOOD]))
    if not neighbourhood_list:
        raise ValueError("neighbourhood_list is empty")

    print("Here are the neighbourhood you can choose:\n")
    print(neighbourhood_list)

    is_valid_input = False
    while not is_valid_input:
        neighbourhood_name = input("Please enter the name of your neighbourhood:\n")

        if not neighbourhood_name in neighbourhood_list:
            print(
                f"I'm sorry, but {neighbourhood_name} does not seem to be one of Vancouver's neighborhoods.\nPlease try again with a different neighbourhood name:\n")
        elif neighbourhood_name.isspace():
            print("You only entered white spaces. Please enter a valid neighbourhood name:")
        else:
            print(
                f"Here is a bar chart and a pie chart discribing the distribution of different facilities in {neighbourhood_name}.\n")
            print(f"Here is the amount of different facilities in {neighbourhood_name}\n")
            return neighbourhood_name


# Function6: display_facility_amount_barchart
def display_facility_amount_barchart(neighborhood_facility_amount_dic, neighbourhood_name):
    """
    Display a bar chart of the amount of each facility in the given neighbourhood.

    Parameters:
    neighborhood_facility_amount_dic (dict): A dictionary containing the number of each facility in the neighbourhood.
    neighbourhood_name（str): the name of the neighbourhood

    Raise:
    ValueError: If neighborhood_facility_amount_dic is empty.
    TypeError: If neighborhood_facility_amount_dic is not a dictionary
               If neighbourhood_name is not a string

    Returns:
    Nothing
    """
    validate_data(neighborhood_facility_amount_dic, dict)
    validate_data(neighbourhood_name, str)

    if not neighborhood_facility_amount_dic:
        raise ValueError("neighborhood_facility_amount_dic is empty")

    # display the barchart of facility and amount

    # Extract the facility names and amounts from facility_dict
    facility_names = list(neighborhood_facility_amount_dic.keys())
    facility_amounts = list(neighborhood_facility_amount_dic.values())

    # Create a bar chart
    plt.bar(facility_names, facility_amounts)

    # Add the number of facilities on top of each bar, with adjusted vertical position
    for i, v in enumerate(facility_amounts):
        plt.text(i, float(v) + TOP_ADJUSTMENT, str(v), ha=CENTER)

    # Set the x-axis limits to adjust the position of the labels
    plt.xlim(X_LIMIT_LEFT, len(facility_names) - X_LIMIT_RIGHT)

    # Rotate the x-axis labels by 45 degrees and align them to the right
    plt.xticks(rotation=X_LABEL_ROTATION, ha=X_LABEL_ALIGNMENT)

    # Set the title and axis labels
    plt.title(f"Facilities in the {neighbourhood_name}")
    plt.xlabel(FACILITYTAPE)
    plt.ylabel(FACILITYNUM)

    # Adjust the figure position by adding space to the bottom
    plt.subplots_adjust(bottom=BOTTOM_ADJUSTMENT)
    # Display the chart
    plt.show()


# Function7: display_facility_piechart
def display_facility_proportion_piechart(neighborhood_facility_amount_dic, neighbourhood_name):
    """
    Display a pie chart of the proportion of each facility in the given neighbourhood.

    Parameters:
    neighborhood_facility_amount_dic(dict): A dictionary containing the number of each facility in the neighbourhood.
    neighbourhood_name（str): the name of the neighbourhood

    Raise:
    ValueError: If neighborhood_facility_distribution_dic is empty.
    TypeError: If neighborhood_facility_amount_dic is not a dictionary
               If neighbourhood_name is not a string

    Returns:
    Nothing
    """
    validate_data(neighborhood_facility_amount_dic, dict)
    validate_data(neighbourhood_name, str)

    if not neighborhood_facility_amount_dic:
        raise ValueError("neighborhood_facility_distribution_dic is empty")

    # Extract the facility names and amounts from facility_dict
    facility_names = list(neighborhood_facility_amount_dic.keys())
    facility_amounts = list(neighborhood_facility_amount_dic.values())

    # Set up the figure and the axes
    fig, ax = plt.subplots()

    plt.pie(facility_amounts, labels=facility_names,autopct=ATUOPCT, pctdistance=PCT_DISTANCE)

    # Set the title
    ax.set_title(f"Facility Proportion in {neighbourhood_name}")

    # Display the chart
    plt.show()


# Function8: output_facility_data
def output_facility_info(neighborhood_facility_amount_dic):
    """
    print the information of the facilities

    Parameters:
    neighborhood_facility_amount_dic(dict): A dictionary containing the number of each facility in the neighbourhood.

    Raise:
    ValueError: If neighborhood_facility_distribution_dic is empty.
    TypeError: If neighborhood_facility_amount_dic is not a dictionary

    Returns:
    Nothing
    """
    validate_data(neighborhood_facility_amount_dic, dict)

    if not neighborhood_facility_amount_dic:
        raise ValueError("neighborhood_facility_distribution_dic is empty")

    for key, value in neighborhood_facility_amount_dic.items():
        print(f"It has {value} {key}(s).")


# Function9:explore_system_again
def explore_system_again():
    """
    This function prompts the user to decide if they would like to continue
    exploring the system or not.

    Parameters:
    Nothing

    Returns:
    bool: True if the user wants to explore again, False otherwise.
    """

    valid_explore_again_input = False
    while not valid_explore_again_input:
        explore_again = input("\nWould you like to continue exploring?\nEnter 'y' for yes, 'n' for no:\n")

        if explore_again == YES:
            return True
        elif explore_again == NO:
            print("Thank you for using the system. Have a great day!")
            return False
        else:
            print("I'm sorry, but I didn't understand your input. \n")
            print("Please enter 'y' if you would like to explore again, or 'n' if you would like to exit the system.\n")


# Function10: display_menu
def display_menu():
    """
    Displays the main menu for the Vancouver parks and sports facilities exploration system.

    Parameters:
    Nothing

    Returns:
    Nothing
    """
    choice = input(
        "What do you want to explore?\nPlease make a choice:\n1. Sports facility\n2. Neighbourhood\n3. Exit\n")
    return choice


# Function11: output_invalid_input_message
def output_invalid_input_message():
    """
    output invalid input message.

    Parameters:
    Nothing

    Returns:
    Nothing
    """
    print("I'm sorry, but I didn't understand your input. \n")
    print(
        "Please enter '1' to explore sports facilities,\n'2' to explore neighborhoods,\nor '3' to exit the system.\n")


