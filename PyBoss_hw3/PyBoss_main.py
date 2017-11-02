import csv

csvpath = "employee_data1.csv"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    ID_array = []
    name_array = [] 
    date_array = []
    ssn_array = []
    state_array = []
    for each in csvreader:
        ID_array.append(each[0])
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for ee in csvreader:
        name_array.append(ee[1])
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for each in csvreader:
        date_array.append(each[2])
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')        
    for each in csvreader:
        ssn_array.append(each[3])
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for each in csvreader:
        state_array.append(each[4])

    print(ID_array[1:3])
    print(name_array[1:3])

csvfile.close()





        

