# election-analysis
Module 3: PyPoll with Python

Importing election data from .csv file, analysis in Python, writing output to .txt file


------------------------------
# Overview of Election Audit Project
A Colorado Board of Elections employee has requested an analysis and audit of a recent local congressional election. 

## Audit Tasks
The analysis will determine:

1. Total number of votes cast
2. Total number of votes by county
3. Total votes per county as percentage of overall total votes
4. County with highest turnout (largest number of votes cast)
5. Complete list of candidates who received votes
6. Total number of votes each candidate received
7. Percentage of votes each candidate won
8. The winner of the election based on popular vote

## Resources
-- Data Source: election_results.csv

-- Software: Python, VS Code


-------------------------------


# Election Audit Results
-- Analysis Output: election_results.txt


>
>Total Votes: 369,711
>-------------------------
>
>County Votes:
>
>Jefferson: 10.5% (38,855)
>
>Denver: 82.8% (306,055)
>
>Arapahoe: 6.7% (24,801)
>
>-------------------------
>
>Largest County Turnout: Denver
>
>-------------------------
>
>Charles Casper Stockham: 23.0% (85,213)
>
>Diana DeGette: 73.8% (272,892)
>
>Raymon Anthony Doane: 3.1% (11,606)
>
>-------------------------
>Winner: Diana DeGette
>
>Winning Vote Count: 272,892
>
>Winning Percentage: 73.8%
>
-------------------------


# Election Audit Summary

This analysis script can be easily utilized for future election audits. As written, the code has been designed to accomodate any number of candidates or counties, and could be used in a local or statewide capacity. 

This script could also easily be modified to include any number of parameters, such as total votes and/or vote percentages by district or zip code, assuming these data points are included in the original dataset. 

