import os
path = os.path.dirname(os.path.realpath(__file__))

csvpath = "budget_data_1.csv"

import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    months_count = 0
    monthsArray = []
    for date in csvreader:
        monthsArray.append(date[0])
        months_count += 1
    del monthsArray[0]
    print("Total Months: " + str(months_count-1))
csvfile.close()

    #csvreader = csv.reader(open(csvpath, newline=''), delimiter=',')
    #csvreader = csv.reader(open(csvpath, newline='')) //must have 'newline' for reader
    
    #csvfile = open(csvpath, 'r')
    #csvreader = csv.reader(csvfile, delimiter=',')
        #csvreader = csvfile.read() //reads everything in file, no delimit sepearation
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #print(csvreader)
    revenue_list = []
    totalRevenue = 0
    for row in csvreader:
        revenue_list.append(row[1])
    for each in revenue_list[1:]:
        totalRevenue += int(each)
    print("Total Revenues: " + str(totalRevenue))
csvfile.close()

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    revDifArray = []
    revDifArrayShift = []
    for each in revenue_list[1:]:
        revDifArray.append(int(each))
    for shift in revenue_list[2:]:
        revDifArrayShift.append(int(shift))

    tupleZipArray = [b-a for a,b in (zip(revDifArray, revDifArrayShift))]
    tupleZipArrayAbs = [abs(y-x) for x,y in zip(revDifArray, revDifArrayShift)]

    totalDifference = 0
    for _ in tupleZipArrayAbs:
        totalDifference += _
    #if-else statement needed for even odd total number of months//

    print("Average Revenue Change: " + str(totalDifference/(months_count - 1)))


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

















