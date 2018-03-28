import os
path = os.path.dirname(os.path.realpath(__file__))

csvpath = "budget_data_1.csv"

import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

###########################################################################################
# Counting number of months in the csv file, then adjust the count (-1) for the title row
# Then prints out the total number of months
###########################################################################################
    months_count = 0
    monthsArray = []
###########################################################################################
# Reading in each row ("date") in csvreader, then append column 0 (date column) to monthsArray.
# Then delete column name in first row.
###########################################################################################
    for date in csvreader:
        monthsArray.append(date[0])
        months_count += 1
    del monthsArray[0]
    print("Total Months: " + str(months_count-1))
csvfile.close()

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#############################################################################################
# Creating a new list for calculating total revenues, a list is created to store the list
# of revenues starting at row[1] (that is where the revenue numbers are stored in the CSV file)
# First for loop appends the revenue values, then the second for-loop iterates through each
# item to sum each item.  Then prints the total revenue values.
##############################################################################################
    revenue_list = []
    totalRevenue = 0
###########################################################################################
# Reading in each row ("revenue") in csvreader, then append column 1 (revenue column).
# Used bracket notation to avoid first row (column name), keep running total in totalRevenue.
###########################################################################################
    for row in csvreader:
        revenue_list.append(row[1])
    for each in revenue_list[1:]:
        totalRevenue += int(each)
    print("Total Revenues: " + str(totalRevenue))
csvfile.close()


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
############################################################################################
# Creating two lists; one holds a list of revenues, and the other holds a the same list
# but it is shifted by one cell.  This will create the two lists which will be zipped
# together to form pairs of numbers.  The pairs will be used to calculate the difference.
# Used bracket notation to specify start point within the column.
############################################################################################
    revDifArray = []
    revDifArrayShift = []
    for each in revenue_list[1:]:
        revDifArray.append(int(each))
    for shift in revenue_list[2:]:
        revDifArrayShift.append(int(shift))
###########################################################################################
# Two lists are created, one will calculate the change in revenues between two months.  
# The other, will be used to calculate the total change (fluctuation) of revenues.
# The idea is that, if revenues at month 1 is 1 dollar, and month 2 is 10 dollars, then
# if month 3 is back to 1 dollar again, then the average change considered to be 9 dollars,
# and NOT 0 (-9 + 9).  Hence ABSOLUTE VALUE is required.
###########################################################################################
    tupleZipArray = [b-a for a,b in (zip(revDifArray, revDifArrayShift))]
    tupleZipArrayAbs = [abs(y-x) for x,y in zip(revDifArray, revDifArrayShift)]

    totalDifference = 0
    for _ in tupleZipArrayAbs:
        totalDifference += _

    print("Average Revenue Change: " + str(totalDifference/(months_count - 1)))
##########################################################################################
# Searching for the high and low values
##########################################################################################
    hiValue = tupleZipArray[0]
    hiValueDate = monthsArray[1]
    loValue = tupleZipArray[0]
    loValueDate = monthsArray[1]
    i = 1
    while i < len(tupleZipArray):
        if hiValue < tupleZipArray[i]:
            hiValue = tupleZipArray[i]
            hiValueDate = monthsArray[tupleZipArray.index(hiValue)+1]
        i+=1
    k = 1
    while k < len(tupleZipArray):
        if loValue > tupleZipArray[k]:
            loValue = tupleZipArray[k]
            loValueDate = monthsArray[tupleZipArray.index(loValue)+1]
        k += 1
    print("Greatest Increase in Revenue: " + str(hiValueDate) + " " + "($" + str(hiValue) + ")")
    print("Greatest Decrease in Revenue: " + str(loValueDate) + " " + "($" + str(loValue) + ")")
csvfile.close()

















