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
    for each in csvreader:
        name_array.append(each[1])
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

    #print(ID_array[1:3])
    #print(name_array[1:3])

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    first_last = []
    name_array.pop(0)
    for _ in name_array:
        first_last.append(_.split(' '))

    DOB_array = []
    DOB_array_re = []
    DOB_array_re2 = []
    date_array.pop(0)
    for each in date_array:
        #DOB_array.append(''.join(each.split('-')))
        DOB_array.append(each.split('-'))
    order = [2, 1, 0]
    for each2 in DOB_array:
        each2 = [each2[i] for i in order]
        DOB_array_re.append(each2)
    for each3 in DOB_array_re:
        DOB_array_re2.append("/".join(each3[0:4]))


    print(first_last[0:5])
    print(DOB_array[0:5])
    print(DOB_array_re[0:5])
    print(DOB_array_re2[0:5])
    
    emp_dict = {}
    ID_array.pop(0)
    i = 0
    for each in ID_array:
        emp_dict[each] = [first_last[i][1], first_last[i][0]]
        i += 1

    x = 0
    for key in emp_dict:
        while x <5:
            print(key, emp_dict[key])
            x += 1



    
csvfile.close()





        

