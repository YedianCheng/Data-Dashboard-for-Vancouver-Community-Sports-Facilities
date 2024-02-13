"""
CS5001
Spring 2023
Final Project -- analysis_functions
Author: Yedian Cheng
"""

from constants import NEIGHBOURHOOD, FACILITYTAPE, FACILITYNUM, NAME, STREETNUM, STREETNAME
from Park import Park
from Neighbourhood import Neighbourhood
from validate_data_function import validate_data
import pandas as pd


# Function1 create_park_dictionary
def create_park_dictionary(park_df, facility_df):
    """
    Given a park dataframe and a facility dataframe, returns a dictionary where
    the keys are the park names and the values are dictionaries containing the
    park's street number, street name, neighborhood name, and a dictionary of the
    park's facilities and their counts.

    Parameters:
    park_df (pandas dataframe): dataframe containing information about parks
    facility_df (pandas dataframe): dataframe containing information about facilities

    Raises:
    ValueError: if park_df is empty
                if facility_df is empty

    TypeError: if FacilityCount is not digit
               if park_df is not a dataframe
               if facility_df is not a dataframe

    Returns:
    park_dict(dict): A dictionary where the keys are park names and the values are dictionaries
    containing the park's street number, street name, neighborhood name, and a dictionary of
    the park's facilities and their counts.
    """

    validate_data(facility_df, pd.DataFrame)
    validate_data(park_df, pd.DataFrame)

    if park_df.empty:
        raise ValueError("park_df is empty")
    elif facility_df.empty:
        raise ValueError("facility_df is empty")

    park_dict = {}

    for index, row in park_df.iterrows():
        name = row[NAME]
        street_number = row[STREETNUM]
        street_name = row[STREETNAME]
        neighbourhood_name = row[NEIGHBOURHOOD]

        facilities_dict = {}
        for index2, row2 in facility_df.iterrows():
            if row2[NAME] == name:
                if not row2[FACILITYNUM].isdigit():
                    raise TypeError("FacilityCount is not digit.")
                facilities_dict[row2[FACILITYTAPE]] = int(row2[FACILITYNUM])

        park_dict[name] = {STREETNUM: street_number, STREETNAME: street_name, NEIGHBOURHOOD: neighbourhood_name, FACILITYTAPE:facilities_dict}

    return park_dict


# Function2 create_park_obj
def create_park_obj(park_dict):
    """
    Given a dictionary of parks and their information, returns a list of Park objects.

    Parameters:
    park_dict (dictionary): dictionary containing information about parks

    Raises:
    ValueError: if park_dict is empty
    TypeError: if park_dict is not dictionary

    Returns:
    A list of Park objects.
    """
    validate_data(park_dict, dict)

    if not park_dict:
        raise ValueError("park_dict is empty")

    park_obj_lst = []
    for park_name, park_info in park_dict.items():
        park_obj = Park(park_name, park_info[STREETNUM], park_info[STREETNAME], park_info[NEIGHBOURHOOD], park_info[FACILITYTAPE])
        park_obj_lst.append(park_obj)
    return park_obj_lst


# Function3 get_parks_with_facility
def get_parks_with_facility(park_obj_lst, facility_name):
    """
    Given a list of Park objects and a facility name, returns a list of Park objects
    that have the specified facility.

    Parameters:
    park_obj_lst (list): list of Park objects
    facility_name (str): name of the facility to search for

    Raises:
    ValueError: if park_obj_lst is empty
    TypeError: if park_obj_lst is a list
               if facility_name is a string


    Returns:
    A list of Park objects that have the specified facility.
    """

    validate_data(park_obj_lst, list)
    validate_data(facility_name, str)

    if not park_obj_lst:
        raise ValueError("park_obj_lst is empty")

    parks_with_facility = []
    for park in park_obj_lst:
        facilities = park.get_facility_info()
        if facility_name in facilities.keys():
            parks_with_facility.append(park)
    return parks_with_facility


# Function4 get_parks_per_neighborhood
def get_parks_per_neighborhood(filter_park_obj_lst):
    """
    Given a list of park objects that have a 'neighborhood' attribute,
    returns a dictionary where the keys are the neighborhood names and the
    values are the number of parks in that neighborhood that have the specified facility.

    Parameters:
    parks_with_facility（list): a list of park objects that have a 'neighborhood' attribute

    Raises:
    ValueError: if filter_park_obj_lst is empty
    TypeError:  if filter_park_obj_lst is a list

    Returns:
    A dictionary where the keys are neighborhood names and the values are integers
    representing the number of parks in that neighborhood that have the specified facility.
    """
    validate_data(filter_park_obj_lst, list)

    if not filter_park_obj_lst:
        raise ValueError("filter_park_obj_lst is empty")

    parks_per_neighborhood = {}
    for park in filter_park_obj_lst:
        neighborhood = park.get_neighborhood()
        if neighborhood in parks_per_neighborhood:
            parks_per_neighborhood[neighborhood] += 1
        else:
            parks_per_neighborhood[neighborhood] = 1

    return parks_per_neighborhood


# Function5 create_neighborhood_object
def create_neighborhood_object(neighborhood_name, park_obj_lst):
    """
    Given a list of park objects and a neighborhood name, returns a Neighbourhood object that contains only the
    park objects in the specified neighborhood.

    Parameters:
    neighborhood_name (str): The name of the neighborhood to filter parks by.
    park_obj_lst (list): A list of Park objects.

    Raises:
    TypeError: if park_obj_lst is a list
               if neighborhood_name is a string

    Returns:
    A Neighbourhood object containing only the park objects in the specified neighborhood.
    """

    validate_data(neighborhood_name, str)
    validate_data(park_obj_lst, list)

    if not park_obj_lst:
        raise ValueError("park_obj_lst is empty")

    filter_park_obj_lst = []
    for park in park_obj_lst:
        if park.get_neighborhood() == neighborhood_name:
            filter_park_obj_lst.append(park)

    neighborhood_obj = Neighbourhood(neighborhood_name, filter_park_obj_lst)
    return neighborhood_obj


# Function6 count_facility_by_neighborhood
def count_facility_by_neighborhood(neighborhood_obj):
    """
    Given a Neighbourhood object, returns a dictionary where the keys are the facility names and the values are
    the number of facilities of that type in the neighborhood.

    Parameters:
    neighborhood_obj (Neighbourhood): A Neighbourhood object.

    Raises:
    ValueError: If neighborhood_obj is empty.

    Returns:
    A dictionary where the keys are facility names and the values are integers representing the number of
    facilities of that type in the neighborhood.
    """

    if not neighborhood_obj:
        raise ValueError("neighborhood_obj is empty")

    facility_counts = {}
    for park in neighborhood_obj.get_park_objects():
        facilities = park.get_facility_info()
        for facility_name, count in facilities.items():
            if facility_name not in facility_counts:
                facility_counts[facility_name] = count
            else:
                facility_counts[facility_name] += count
    return facility_counts

