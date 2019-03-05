# PyBank part of Homework #3
# authored by Clara Eberhardy

# Instructions:
""" 
The dataset is composed of two columns: Date and Profit/Losses. 
Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The average of the changes in "Profit/Losses" over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period
"""

# First we'll import the needed modules
import os
import csv

# the path to the dataset we are using
budget_path = os.path.join('budget_data.csv')

#initialize variables that need to start with 0
month = 0
months_total = 0
net_total = 0
num_values = 0
great_inc = 0
great_dec = 0

with open(budget_path, newline='') as budget_file:
    # create the object with the budget data
    budget_reader = csv.reader(budget_file, delimiter=',')

    # Read the header row first to get to the next row
    budget_header = next(budget_reader)

    # Read each row of data after the header
    for row in budget_reader:

        # count up the months
        months_total +=1

        # sum up the values of the profit/loss column
        net_total += float(row[1])
        # count the rows
        num_values += 1
        # check if this value is bigger than the previous greatest value
        if float(row[1]) > great_inc:
            great_inc = float(row[1])
            great_inc_date = row[0]

        # check if this value is lower than the previous lowest value
        if float(row[1]) < great_dec:
            great_dec = float(row[1])
            great_dec_date = row[0]

#out of FOR loops and out of the cvs reader file with all variables defined by the file

total_average = net_total / num_values

textfile = 'financial_analysis.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(textfile, 'w+') as text:

    text.write("Financial Analysis\n")
    text.write("------------------\n")
    text.write(f"Total Months: {months_total}\n")
    text.write(f"Total Profit/loss: ${net_total}\n")
    text.write(f"Average Profit/loss: {total_average}\n")
    text.write(f"The greatest increase in profits happened on {great_inc_date} with ${great_inc} in profit\n")
    text.write(f"The greatest decrease in profits happened on {great_dec_date} with ${great_dec} in loss\n")

with open(textfile, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)