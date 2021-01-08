# Python analysis of csv file with 3 columns (election_data.csv)

# columns are Voter ID, County, and Candidate

# import modules
import os
import csv

# initial variables
vote_count = 0
candidates = []

# set filepath to csv
csvpath = os.path.join(".", "Resources", "election_data.csv")

# read data from csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header and save as variable
    csv_header = next(csvreader)
    
# # Kept for reverece, used to see data
#     print(csv_header)
#     for row in csvreader:
#         print(row)
        
    # iterate through rows
    for row in csvreader:
    
        # Total mnumber of votes cast (count of voter ID)
        vote_count += 1

        # complete list of candidates who received votes (count unique candidates)
        if row[2] not in candidates:
            candidates.append(row[2])

        # Percentage of votes each candidate won


        # total number of votes each candidate won


        # winner of election based on popular vote
        
    
    
# print results to terminal
print("Election Results")
print("----------------------------")

print(f"Total Votes: {vote_count}")
print("----------------------------")

# for loop to print each candidate
for name in candidates:
    print(f"{name}: ")

print("----------------------------")


# export results to text file
