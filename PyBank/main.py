#Challenge Tasks: Get...
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

# Import the csv module which provides functionality to read from and write to CSV files.
import csv
import os

# Initializing the variables
num_months = 0
net_total_amount = 0
previous_profit_loss = 0
monthly_change = 0
total_monthly_changes = 0
greatest_increase = 0
monthly_increase = ''
greatest_decrease = 0
monthly_decrease = ''

# CSV file is opened and read in using the reader() function and the comma',' delimiter of the csv module
file_name = os.path.join ('Resources', 'budget_data.csv')
with open(file_name) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the row with column headers in the csv data file.
    csv_header = next(csvreader)

    # for loop that iterates through each row in turn and updates variables.

    for row in csvreader:
# Update variables
# calculate the net total amount of "Profit/Losses" over the entire period
        num_months += 1
        current_profit_loss = int(row[1])
        net_total_amount += current_profit_loss
 # Calculating changes in "Profit/Losses" over the entire period.
 # If num_months is greater than 1, then monthly_change is calculated as current_profit_loss - previous_profit_loss.
        if num_months > 1:
            monthly_change = current_profit_loss - previous_profit_loss
            total_monthly_changes += monthly_change
 # Calculating the greatest increase in profits (date and amount) over the entire period
 # if monthly_change exceeds the greatest increase or decrease recorded during period of time, 
 # then Greatest Increase/Decrease values are updated accordingly.           
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                monthly_increase = row[0]
 # Calculating the greatest decrease in profits (date and amount) over the entire period               
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                monthly_decrease = row[0]
        previous_profit_loss = current_profit_loss

# monthly changes are rounded down to two decimal places and displayed along with their corresponding averages.
# and print out the results as requested.
average_change = total_monthly_changes / (num_months - 1)
print(f'Total Months: {num_months}')
print(f'Total Profit: ${net_total_amount}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits: {monthly_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {monthly_decrease} (${greatest_decrease})')

# creating and exporting a text file with the results using Python's 'with' statement, 
# which automatically closes the file after the block of code has finished executing,
# and using the f-strings to simplify the string formatting.

output_path = "financial_analysis.txt"
with open(output_path, "w") as file:
    file.write("Financial Analysis\n"
               "--------------------------\n"
               "Financial Analysis\n"
               "------------------------------------------------\n"
               "Total Months: 86\n"
               "Total: $22564198\n"
               "Average Change: $-8311.11\n"
               "Greatest Increase in Profits: Aug-16 ($1862002)\n"
               "Greatest Decrease in Profits: Feb-14 ($-1825558)\n"
               "------------------------------------------------\n")
