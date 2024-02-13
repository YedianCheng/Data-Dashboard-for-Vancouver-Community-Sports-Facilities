"""
CS5001
Spring 2023
Final Project -- validate_data_function
Author: Yedian Cheng
"""


# Function: validate_data
def validate_data(data, typename):
    """
    check if the given data is of the specified type, if not, raises a TypeError

    Parameters:
    data: the given data to be checked
    typename: a specified type

    Raises:
    TypeError: if the given data is not of the specified type

    Returns:
    nothing
    """
    data_output = isinstance(data, typename)
    if not data_output:
        raise TypeError(f"{data} is not a {typename}")
