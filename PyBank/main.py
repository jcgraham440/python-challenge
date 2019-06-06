import math
import os
import csv

#
# Borrowed this truncate function from StackOverflow:
#     https://stackoverflow.com/a/37697840
# 
def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper

greatestIncrease = 0
greatestDecrease = 0
averageChange = 0

# The size of the following arrays is only ever going to be 2
# and their entries are going to be overwritten

greatestIncreaseRow = ["1", "2"]
greatestDecreaseRow = ["1", "2"]

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    header = next(csvreader)
    i = 0
    NetPL = 0
    currentProfit = 0
    for row in csvreader:
        if (i > 0):
            # subtract the difference between this month and last month, 
            # and add it to the averageChange
            averageChange += (int(row[1]) - currentProfit)

        currentProfit = int(row[1])
        NetPL = NetPL + currentProfit
        if (currentProfit > greatestIncrease):
            greatestIncrease = currentProfit
            greatestIncreaseRow[0] = row[0]
            greatestIncreaseRow[1] = row[1]
        if (currentProfit < greatestDecrease):
            greatestDecrease = currentProfit
            greatestDecreaseRow[0] = row[0]
            greatestDecreaseRow[1] = row[1]
        i = i + 1

print("Financial Analysis")
print("------------------")
print("Total Months: " + str(i))
print("Total: $" + str(NetPL))
print("Average Change: " + str(truncate(float(averageChange/(i-1)), 2)))
print(f"Greatest Increase in Profits: {greatestIncreaseRow[0]} ({greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecreaseRow[0]} ({greatestDecrease})")

f = open("result.txt", "w+")
f.write("Financial Analysis\n")
f.write("------------------\n")
f.write("Total Months: " + str(i) + "\n")
f.write("Total: $" + str(NetPL) + "\n")
f.write("Average Change: " + str(truncate(float(averageChange/(i-1)), 2)) + "\n")
f.write(f"Greatest Increase in Profits: {greatestIncreaseRow[0]} ({greatestIncrease})\n")
f.write(f"Greatest Decrease in Profits: {greatestDecreaseRow[0]} ({greatestDecrease})\n")

