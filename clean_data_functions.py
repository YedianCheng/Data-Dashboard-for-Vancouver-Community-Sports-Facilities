"""
CS5001
Spring 2023
Final Project -- clean_data_functions
Author: Yedian Cheng
"""


import requests
import pandas as pd
from constants import ENCODING, CSV_DELIMITER, HEADER, UPPER_YES, FACILITIES, NAME, STREETNUM, STREETNAME, NEIGHBOURHOOD, FACILITYTAPE, FACILITYNUM, START_DATA1, START_DATA0
from validate_data_function import validate_data

# Function1: read_url
def read_url(url):
    """
    read data from the given URL and return as a list of lines.

    Parameters:
    url (str): The URL to read data from

    Raises:
    HTTPError: raise HTTPError for status codes is not 200

    Returns:
    lines(list): List of lines read from the given URL
    """
    try:
        lines = []
        response = requests.get(url)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f"HTTP Error {response.status_code}")
        content = response.content.decode(ENCODING)
        lines = content.splitlines()

    except requests.exceptions.ConnectionError as ex:
        print("Failed to connect to the server", ex)

    except requests.exceptions.Timeout as ex:
        print("Request timed out", ex)

    except requests.exceptions.HTTPError as ex:
        print("HTTP error occurred", ex)
        raise requests.exceptions.HTTPError("HTTP error occurred")

    except requests.exceptions.TooManyRedirectsError as ex:
        print("TooManyRedirectsError occurred", ex)

    except requests.exceptions.RequestException as ex:
        print("An error occurred while making the request:", ex)

    return lines


# Function2: pull_and_clean_data_parks
def clean_data_parks(lines):
    """
    Read park  data from the given list of lines, cleans it, and returns it as a DataFrame.

    Parameters:
    lines(list): List of lines

    Raises:
    ValueError: if Park Data is empty
                if Park DataFrame is empty after cleaning
    TypeError: if Park Data is not a list

    Returns:
    pandas.DataFrame: DataFrame of cleaned park data
    """
    validate_data(lines,list)
    # check if the line is empty
    if not lines:
        raise ValueError("Park Data is empty")

    heads = lines[HEADER].split(CSV_DELIMITER)
    rows = []
    for line in lines:
        row = line.split(CSV_DELIMITER)
        # filter that data
        if row[heads.index(FACILITIES)] == UPPER_YES:
            row = [row[heads.index(NAME)], row[heads.index(STREETNUM)], row[heads.index(STREETNAME)],
                   row[heads.index(NEIGHBOURHOOD)]]
            rows.append(row)
    park_df = pd.DataFrame(rows[START_DATA0:], columns=[NAME, STREETNUM, STREETNAME, NEIGHBOURHOOD])
    # delete rows that contain null values.
    park_df.dropna(inplace=True)
    if park_df.empty:
        raise ValueError("Park DataFrame is empty after cleaning")
    return park_df


# Function3: clean_data_facility
def clean_data_facility(lines):
    """
    Read park facility data from the given list of lines , cleans it, and returns it as a DataFrame.

    Parameters:
    lines(list): List of lines

    Raises:
    ValueError: if facility Data is empty
                if facility DataFrame is empty after cleaning
    TypeError: if facility Data is not a list

    Returns:
    pandas.DataFrame: DataFrame of cleaned park facility data

    """
    validate_data(lines, list)

    # check if the line is empty
    if not lines:
        raise ValueError("Facility Data is empty")

    heads = lines[HEADER].split(CSV_DELIMITER)
    rows = []
    for line in lines:
        row = line.split(CSV_DELIMITER)
        # filter that data
        row = [row[heads.index(FACILITYNUM)], row[heads.index(FACILITYTAPE)], row[heads.index(NAME)]]
        rows.append(row)

    facility_df = pd.DataFrame(rows[START_DATA1:], columns=[FACILITYNUM, FACILITYTAPE, NAME])
    # delete rows that contain null values.
    facility_df.dropna(inplace=True)
    if facility_df.empty:
        raise ValueError("Facility DataFrame is empty after cleaning")

    return facility_df