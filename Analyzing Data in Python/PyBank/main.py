import os
import csv

path = os.path.join("Resources", "budget_data.csv")

# Tracking various parameters used in calculations
total_months = 0
total_profit = 0
change_total = 0
net_change_list = []
month_of_change_list = []

# reads csv file with financial data
with open(path, "r") as datafile:
    reader = csv.reader(datafile, delimiter=",")
    header = next(reader)

    first_row = next(reader)
    prev_num = int(first_row[1])

    for row in reader:

        # Getting total number of months
        total_months += 1

        # Getting total profit from the period
        total_profit += int(row[1])

        # creating the list of monthly changes and the months they occur in
        net_change = int(row[1]) - int(prev_num)
        net_change_list.append(net_change)
        month_of_change_list.append(row[0])
        prev_num = row[1]

    # Getting average change between months
    for num in net_change_list:
        change_total += num
    average = change_total/total_months

    # Locating index number of highest increase and decrease
    max_index = net_change_list.index(max(net_change_list))
    min_index = net_change_list.index(min(net_change_list))

    # creates a aggregate list with month and change
    agg_change_list = list(zip(month_of_change_list, net_change_list))

    max_increase = agg_change_list[max_index]
    max_decrease = agg_change_list[min_index]

    output = (f"""
    Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${total_profit}
    Average Change: ${average}
    Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})
    Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})""")

    print(output)

# exporting results into a text file
export_path = os.path.join("analysis", "analysis.txt")

with open(export_path, 'w') as report_file:
    report_file.write(output)
