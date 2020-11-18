# Assignment-1

This program will use as its primary resource a file of mask use behaviors based upon data compiled by the NY Times in the Summer of 2020. The program will read that in (as well as an auxiliary file, described below). The program will then present a simple interface to the user. This will allow the user to ask for statistics for the entire country, or for a specified US State-level entity (i.e. the 50 States, plus the District of Columbia and Puerto Rico). The program will repeat this until the user chooses to quit.
The input files
o Mask data by county: https://github.com/nytimes/covid-19-
data/tree/master/mask-use
o State FIPS codes: State-geocodes-v2018.csv (Available on Blackboard)
o State names and abbreviations: State_abbreviations.csv (Available on Blackboard) The mask data file is explained on the Github page.
The FIPS code is the key to identifying counties and states. The FIPS code for which state a county is in is the first two characters of that county’s FIPS identifier (e.g. 17009 is a county in State “17” which is Illinois).
Specific Program Behavior
1. The program will read in the three files listed above. This will give it the data it
needs to answer the different types of user queries.
2. The program will then operate in a loop. In the loop, the user can specify three
different types of queries.
a. Whole US data.
b. Data for a specified US State
c. Exit the program
The queries are detailed as follows: o Whole US data:
  INF 405
v 2020 09 01 Fall 2020
o o
By aggregating the data for all the counties, give the nationwide average of each of the mask wearing category percentages.
For every State, calculate and give
§ The statistics for each of the mask wearing category percentages in that state
§ The County with the highest best mask wearing percentage in that State. Best mask wearing percentage is the sum of the FREQUENTLY and ALWAYS percentages.
§ The County with the highest worst mask wearing percentage in that State. Worst mask wearing percentage is the sum of the NEVER and RARELY percentages.
o Using the same method just described, output
§ the State with the highest best mask wearing percentage (aggregated)
§ the State with the highest worst mask wearing percentage
(aggregated).
o Specified State Data
o The user specifies a state by its two letter code (e.g. “NY” for “New York”) and the program gives the same State data as is supplied for it for the nationwide
query. o Exit
o If the user requests the program exit, the program terminates.
o Otherwise it goes back into the loop prompting the user for its query.
