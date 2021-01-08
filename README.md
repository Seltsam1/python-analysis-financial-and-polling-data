# python-analysis-financial-and-polling-data
Contains two sample python scripts to read csv data and output aggregate metrics to a text file

## Getting Started

Download folder structure

There are two folders: PyBank and PyPoll
- Both contain a Resources folder with a csv file and an Analysis folder with an example output text file
- There is a "main.py" python script file in each folder
- Run the "main.py" script from the appropriate folder to read the csv file and produce the output text file ("analysis.txt")

## Features

PyBank
- Contains a python script to calculate aggregate metrics
- The csv file "budget_data.csv" is a simplified finacial file with only two columns (date and profit/losses)
- "main.py" python script will read in the data from the csv file and produce the following metrics to an output text file:
1. Total months
2. Total profit/losses
3. Average net change of profit/losses (difference from month to month)
4. Greatest net increase in profits (difference from month to month)
5. Greatest net descrease in profits (difference from month to month)

PyRoll
- Contains a python script to calculate aggregate metrics
- The csv file "election_data" contains 3 columns (Voter ID, County, Candidate)
- "main.py" python script will read in the data from the cvs file and produce the following to an output text file:
1. Total number of votes cast
2. List of candidates that received votes
3. Percentage of votes each candidate won
4. Number of total votes per candidate
5. Winnder of election based on popular vote

## Licensing

The code in this project is licensed under MIT license.
