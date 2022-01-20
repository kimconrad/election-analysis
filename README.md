# election-analysis
Module 3: PyPoll with Python

Importing election data from .csv file, analysis in Python, writing output to .txt file



In this project, our final Python script will need to be able to deliver the following information when the script is run: 

Total number of votes cast
A complete list of candidates who received votes
Total number of votes each candidate received
Percentage of votes each candidate won
The winner of the election based on popular vote
-----------------------------------------
The general format for opening a file is, file_variable = open(filename, mode).

Let's break down what each component is doing in the general format.

# file_variable is the name of the variable that will reference the file object.
# filename is a string specifying the name of the file.
# mode is a string specifying the mode for reading or writing the file object. The possible modes are:

"r": Open a file to be read.
"w": Open a file to write to it. This will overwrite an existing file and create a file if one does not already exist.
"x": Open a file for exclusive creation. If the file does not exist, it will not create one.
"a": Open a file to append data to an existing file. If a file does not exist, it creates one, if a file has been created the data will be added to the file.
"+": Open a file for reading and writing.
