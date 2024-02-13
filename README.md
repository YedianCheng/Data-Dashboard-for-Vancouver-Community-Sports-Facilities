# Data-Dashboard-for-Vancouver-Community-Sports-Facilities
Data sets
I will use the data sets of parks and parks facilities to analyze.
URL : https://opendata.vancouver.ca/explore/dataset/parks-facilities/analyze/?disjunctive.facilitytype&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InBhcmtzLWZhY2lsaXRpZXMiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLmZhY2lsaXR5dHlwZSI6dHJ1ZX19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJmYWNpbGl0eWNvdW50Iiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzAyNzlCMSJ9XSwieEF4aXMiOiJmYWNpbGl0eXR5cGUiLCJtYXhwb2ludHMiOjUwLCJzb3J0IjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D
URL：https://opendata.vancouver.ca/explore/dataset/parks/table/

Analysis

I will use two datasets for the following analysis:

I will ask the user to input the name of a sports facility she likes,
then calculate the amount of park which has this sports facility in each neighbourhood,
and proportion of park which has this sports in each neighbourhood


Then I will ask the user to input a neighbourhood that interests her,
then calculate the sports facilities and corresponding quantities are available in this neighbourhood.
and proportion of each sports facility in this neighbourhood

Data Structure:

They will be stored in lists and dictionaries:

a dictionary where the keys are the park names and the values are dictionaries containing the
park's street number, street name, neighborhood name, and a dictionary of the park's facilities and their counts.

a list of park instances
a list of neighborhood instances

Visualization:

When the user selects a sports facility,
there will be a pie chart representing the proportion of park which has this sports in each neighbourhood，
and a bar chart representing the amount of park which has this sports facility in each neighbourhood
present which neighbourhood has more of this sports facility and which has less of this sports facility.

When the user selects a neighbourhood,
there will be a pie chart representing the proportion of each sports facility in this neighbourhood,
a bar chart representing the amount of each sports facility in this neighbourhood.
