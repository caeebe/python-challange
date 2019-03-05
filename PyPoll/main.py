# PyPoll part of Homework #3
# authored by Clara Eberhardy

# Instructions:
""" 
The dataset is composed of three columns: Voter ID, County, and Candidate. 
Your task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.
"""

# First we'll import the needed modules
import os
import csv

# the path to the dataset we are using
election_path = os.path.join('election_data.csv')

#initialize some variables that need to start with 0
num_votes_total = 0
most_votes = 0

# we will store the information into a dictionary with each entry in the form of "name":int(# of votes)
# and we will create a second dictionary with the percentage values "name": float(percentage)
candidates = {}
cand_percent = {}


with open(election_path, newline='') as election_file:
    # create the object with the election data
    election_reader = csv.reader(election_file, delimiter=',')

    # Read the header row first to get to the next row, we may not use this though
    election_header = next(election_reader)

    # Read each row of data after the header
    for row in election_reader:
        # count up the total votes cast by everyone
        num_votes_total +=1
        # check if this is a new candidate is in the candidate dictionary, if so add a new dictionary entry, 
        #otherwise just update the vote value in that candidates dict entry.
        if row[2] in candidates:
            # add a vote to the candidate dictionary entry
            candidates[row[2]] += 1
        else:
            # create a new key entry to the candidate dict and put one vote in the value
            candidates[row[2]] = 1
    
# add the percentage for each candidate to the candidate dictionary, and find the candidate with the most votes
for c in candidates:
        percentage = 100 * candidates[c] / num_votes_total
        cand_percent[c] = round(percentage, 3)
        if most_votes < candidates[c]:
            most_votes = candidates[c]
            winner = c

      

#out of FOR loops and out of the cvs reader file with all variables defined by the file


textfile = 'election_results.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(textfile, 'w+') as text:
    text.write("------------------\n")
    text.write("Election Results\n")
    text.write("------------------\n")
    text.write(f"Total Votes: {num_votes_total}\n")
    text.write("------------------\n")
    #loop through all the candidates with votes
    for c in candidates:
        text.write(f"""{c}: {cand_percent[c]}% ({candidates[c]})\n""")
    text.write("------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("------------------\n")

with open(textfile, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)