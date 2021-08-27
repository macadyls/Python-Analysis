# Dependencies 
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("PyBank","Resources","budget_data.csv")

# Initial variables
total_months = 0
net_total = 0
net_monthly_avg = 0
greatest_increase = [0,0]
greatest_decrease = [0,0]
net_change_list = []
month_of_change = []

# Open and read csv
with open(budget_csv) as financial_data:
    read = csv.reader(financial_data, delimiter=",")

    # Extract the header row first 
    header = next(read)
    print(f"Header: {header}")

    # Extract first row for net change and add to months
    first_row = next(read)
    prev_net = int(first_row[1])
    total_months = total_months + 1


    # Read through each row of data after the header
    for row in read:
        # Keep track of number of months, also the row
        total_months = total_months + 1
        
        # Keep track of net total
        net_total = net_total + int(row[1])

        # Calculate net change and keep track of month it occurred
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        #Test with revenue variable
        #revenue = revenue + int(row[1])

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change 
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total:,}\n"
    f"Average Change: ${net_monthly_avg:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,})\n"
    )

# Print the output (to terminal)
print(output)

# Export results into text file 
# Set variable for output file
output_file = os.path.join("PyBank", "analysis","budget_analysis.txt")

# Open the output file
with open(output_file, "w", newline="") as txt_file:
    
    # Write results into file
    txt_file.write(output)
