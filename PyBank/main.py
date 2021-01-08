# Python analysis of financial csv file with 2 columns

# columns are Date as string and Profit/Losses as integer

# import modules
import os
import csv

# initial variables
total_months = 0
total_profit_loss = 0
profit_loss_list = []
month_list = []


# set filepath to csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")

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
        
        # append value for profit/loss into list for later calculations
        profit_loss_list.append(int(row[1]))
        month_list.append(row[0])
        
        
# net change difference calculations

net_change = []
month_change = []

for n in range(1, len(profit_loss_list)):
    change = [profit_loss_list[n] - profit_loss_list[n-1]]
    net_change.append(change)
    month_change.append(month_list[n])
#    print(net_change)  used to for testing, kept for reference  
#    print(month_change)  used to for testing, kept for reference 

# average change
total = 0
for n in net_change:
    total+=sum(n)
avg_change = round(total / len(net_change), 2)
#print(avg_change) 

# maximum changes
max_change = max(net_change)
max_month = month_change[net_change.index(max_change)]
max_change = str(max_change)[1:-1]   # list slicing to remove brackets
#print(max_change)

# minimum changes
min_change = min(net_change)
min_month = month_change[net_change.index(min_change)]
min_change = str(min_change)[1:-1]


# Print results
print("Financial Analysis")
print("-" * 30)

print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")

print(f"Average Change: ${avg_change}") 
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")


#print(f"Greatest Increase in Profits: {max_month} (${max(net_change})")
# print(f"Greatest Decrease in Profits: {min_month} (${min_loss})")


# # Export results to text file in Analysis folder

# # set filepath to txt
# txt_path = os.path.join(".", "Analysis", "analysis.txt")

# # open file to write
# with open(txt_path, "w") as text_file:

#     # write text to file on new lines
#     text_file.write("Financial Analysis\n")   # Using \n adds a new line
#     text_file.write("-----------------------------------------\n")
#     text_file.write(f"Total Months: {total_months}\n")
#     text_file.write(f"Total: ${total_profit_loss}\n")
#     text_file.write(f"Average Change: ${round(total_profit_loss / total_months, 2)}\n")
#     text_file.write(f"Greatest Increase in Profits: {max_month} (${max_profit})\n")
#     text_file.write(f"Greatest Decrease in Profits: {min_month} (${min_loss})\n")
