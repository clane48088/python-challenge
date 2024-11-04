import csv
import os

# file to  load
file_to_load = os.path.join("..", "Resources", "budget_data.csv")

# out file path
file_to_output = os.path.join("..","analysis", "budget_analysis.txt")

totalMonths = 0     # variable for total number of months starting at 0
total = 0           # initialize the total of profits / loses to 0
monthlyChanges = [] # initialize the list of monthly net changes
months = []         # initialized the list of months

#read the csv file
with open(file_to_load) as financial_data:

    # creating a csv reader
    csv_reader = csv.reader(financial_data)

     # read the header row
    header = next(csv_reader)
   
    # move top the first row
    firstRow = next(csv_reader)

   
    # increment the count of the total months
    totalMonths += 1 # same as totalMonths = totalMonths + 1

    # add on to the total profit/loses
    total += float(firstRow[1])

   
    # establish previous month's profit or lose
        # add on to the previous month's profit/loses
    previousProfitLosses = float(firstRow[1])


    for row in csv_reader:
        # increment the count of the total months
        totalMonths += 1 # same as totalMonths = totalMonths + 1

        # add on to the total profit/loses
        total += float(row[1])

        # calculate the next changes
        netchange = float(row[1]) - previousProfitLosses
        # add on to the list of monthly changes
        monthlyChanges.append(netchange)

        #add the first month that a change occured
            # months is in index 0
        months.append(row[0])

        # update the previous profit/loss
        previousProfitLosses = float(row[1])

# calculate the average net change per month
averageChangePerMonth = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]] # reflects the month of the value of the greatest increase
greatestDecrease = [months[0], monthlyChanges[0]] # reflects the month of the value of the greatest decrease

# use loop to calculate the index of the greatest and least monthly changes 
for m in range(len(monthlyChanges)):
    # calculate the greatest increase and decrease
    if(monthlyChanges[m] > greatestIncrease[1]):
        # if the value is greater than the greatest increase, that value becomes the largest increase
        greatestIncrease[1] = monthlyChanges[m]        # update the month
        greatestIncrease[0] = months[m]

    if(monthlyChanges[m] < greatestDecrease[1]):
        # if the value is less than the greatest decrease, that value becomes the largest decrease
        greatestDecrease[1] = monthlyChanges[m]
        # update the month
        greatestDecrease[0] = months[m]
 
# start calculating the output
output = (
    f"Financial Analysis \n"
""    f"----------------------------\n"
    f"Total Months: {totalMonths} \n"
    f"Total:  ${total:.0f} \n"
    f"Average Change = ${averageChangePerMonth:,.2f} \n"
    f"Greatest Increase in Profits : {greatestIncrease[0]} (${greatestIncrease[1]:.0f}) \n"   
    f"Greatest Decrease in Profits : {greatestDecrease[0]} (${greatestDecrease[1]:.0f}) \n" 
    )

#print the output to the console / terminal
print(output)

# export output to the tesxt file
with open(file_to_output, "w") as textfile:
    textfile.write(output)





