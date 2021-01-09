# Python analysis of election csv file with 3 columns

# columns are Voter ID, County, and Candidate

# import modules
import os
import csv

# initial variables
vote_count = 0
candidates = []
vote_candidates = {}
winner = ""
winner_count = 0

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
    
        # Total number of votes cast (count of rows)
        vote_count += 1

        # complete list of candidates who received votes
        # total number of votes each candidate won
        if row[2] not in candidates:
            candidates.append(row[2]) # append unique candidates to list
            vote_candidates[row[2]] = 1  # add candidate to dictionary as key with value 1
        else:
            vote_candidates[row[2]] +=1  # increase value in dictionary by 1
            
            
        # Percentage of votes each candidate won


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




