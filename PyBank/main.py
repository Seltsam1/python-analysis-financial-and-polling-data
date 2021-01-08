# Python analysis of csv file with 2 columns

# columns are Date as string and Profit/Losses as integer

# import modules
import os
import csv

# set filepath to csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# initial variables
total_months = 0
total_profit_loss = 0
max_profit = 0
min_loss = 0

# read data from csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header and save as variable
    csv_header = next(csvreader)
    
# # Kept for reverece, used to see data
#     print(csv_header)
#     for row in csvreader:
#         print(row)

    # interate through rows
    for row in csvreader:

        # Total number of months in the dataset
        total_months += 1

        # Net total of Profit/Losses
        total_profit_loss += int(row[1])

        # Greatest increase in profits (date and amount)
        if max_profit < int(row[1]):
            max_profit = int(row[1])
            max_month = row[0]

        # Greatest decrease in losses (date and amount)
        if min_loss > int(row[1]):
            min_loss = int(row[1])
            min_month = row[0]

# Print results
print("Financial Analysis")
print("-" * 30)

print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")

# average change calculation with rounding
print(f"Average Change: ${round(total_profit_loss / total_months, 2)}")
print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_month} (${min_loss})")


# Export results to text file in Analysis folder

# set filepath to txt
txt_path = os.path.join(".", "Analysis", "analysis.txt")

# open file to write
with open(txt_path, "w") as text_file:

    # write text to file on new lines
    text_file.write("Financial Analysis\n")   # Using \n adds a new line
    text_file.write("-----------------------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total_profit_loss}\n")
    text_file.write(f"Average Change: ${round(total_profit_loss / total_months, 2)}\n")
    text_file.write(f"Greatest Increase in Profits: {max_month} (${max_profit})\n")
    text_file.write(f"Greatest Decrease in Profits: {min_month} (${min_loss})\n")
