import csv

csvpath = "employee_data1.csv"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    ID_array = []
    for each in csvreader:
        
        

