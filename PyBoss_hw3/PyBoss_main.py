import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

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
    order = [1, 2, 0]
    for each2 in DOB_array:
        each2 = [each2[i] for i in order]
        DOB_array_re.append(each2)
    for each3 in DOB_array_re:
        DOB_array_re2.append("/".join(each3[0:4]))
    
    ssn_array_adj = []
    ssn_array.pop(0)
    for each4 in ssn_array:
        ssn_array_adj.append(each4.split('-'))
    
    state_array.pop(0)
    state_array_adj = []
    for each5 in state_array:
        state_array_adj.append(us_state_abbrev[each5])

    print(state_array_adj[0:5])
    print(ssn_array_adj[0:5])
    print(ssn_array_adj[0][2])
    print(first_last[0:5])
    print(DOB_array[0:5])
    print(DOB_array_re[0:5])
    print(DOB_array_re2[0:5])
    
    emp_dict = {}
    ID_array.pop(0)
    i = 0
    for each in ID_array:
        emp_dict[each] = [first_last[i][1], first_last[i][0], DOB_array_re2[i],
                            "***-**-"+ssn_array_adj[i][2], state_array_adj[i]]
        i += 1

    x = 0
    for key in emp_dict:
        print(key, end=',')
        #print(emp_dict[key][0], end='\n')
        print(emp_dict[key][0], end=',')
        print(emp_dict[key][1], end=',')
        print(emp_dict[key][2], end=',')
        print(emp_dict[key][3], end=',')
        print(emp_dict[key][4], end='\n')
        x += 1
        if x > 5:
            break



    
csvfile.close()





        

