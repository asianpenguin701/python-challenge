import os
import csv

# Path to collect csv file from folder
budget_csv = 'Resources/budget_data.csv'

# Define function to process CSV
def bank(budget_csv):
    with open(budget_csv, mode='r') as csvfile:
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        data = list(csvreader)
        
        # Extract dates and profit/losses
        dates = [row[0] for row in data]
        profit_losses = [int(row[1]) for row in data]

    # The total number of months included in the dataset
    months = len(dates)

    # The net total amount of "Profit/Losses" over the entire period
    net = sum(profit_losses)

    # The changes in "Profit/Losses" over the entire period
    changes = [profit_losses[i] - profit_losses[i-1] for i in range(1, months)]
    average = sum(changes) / len(changes) #  Average of changes 
    
    # The greatest increase in profits over the entire period
    greatest_increase = max(changes)
    greatest_increase_index = changes.index(greatest_increase) + 1  # +1 to correct for changes index
    greatest_increase_date = dates[greatest_increase_index]

    # The greatest decrease in profits over the entire period
    greatest_decrease = min(changes)
    greatest_decrease_index = changes.index(greatest_decrease) + 1  # +1 to correct for changes index
    greatest_decrease_date = dates[greatest_decrease_index]

    # Print the analysis at the terminal
    print("\nFinancial Analysis\n")
    print("----------------------------\n")
    print(f"Total Months: {months}\n")
    print(f"Net Total Amount of Profit/Losses: ${net}\n")
    print(f"Average Change in Profit/Losses: ${average:.2f}\n")  # Format with $ and 2 decimals
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

    # Output analysis to a new cvs file
    analysis = [
        ["Financial Analysis"],
        ["----------------------------"],
        ["Total Months", months],
        ["Net Total Amount of Profit/Losses", f"${net}"],
        ["Average Change in Profit/Losses", f"${average:.2f}"],
        ["Greatest Increase in Profits", f"{greatest_increase_date} (${greatest_increase})"],
        ["Greatest Decrease in Profits", f"{greatest_decrease_date} (${greatest_decrease})"]
    ]

    return analysis

# Run the analysis
analysis = bank(budget_csv)

# Write to a new csv file
output = 'analysis/financial analysis.csv'
with open(output, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(analysis)
