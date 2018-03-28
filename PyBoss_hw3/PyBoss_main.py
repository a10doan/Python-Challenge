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
#####################################################################
# STORING ALL THE DIFFERENT COLUMNS INTO DIFFERENT ARRAYS
#####################################################################
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


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#####################################################################################
# SETTING UP THE NAME ARRAY, AND SPLITTING THE FIRST AND LAST NAMES INTO A NEW ARRAY,
# THEREBY FORMING A LIST (FIRST, LAST) WITHIN A LIST
#####################################################################################
    first_last = []
    name_array.pop(0)
    for _ in name_array:
        first_last.append(_.split(' '))
#####################################################################################
# ADJUSTING THE DOB ARRAY, HAD TO USE 3 DIFFERENT ARRAYS: ONE FOR THE SPLIT,
# ANOTHER FOR ADJUSTING THE ORDER, AND A THIRD ARRAY FOR ADDING THE '/'
#####################################################################################
    DOB_array = []
    DOB_array_re = []
    DOB_array_re2 = []
    date_array.pop(0)
    for each in date_array:
        DOB_array.append(each.split('-'))
    order = [1, 2, 0]
    for each2 in DOB_array:
        each2 = [each2[i] for i in order]
        DOB_array_re.append(each2)
    for each3 in DOB_array_re:
        DOB_array_re2.append("/".join(each3[0:4]))
#####################################################################################
# ADJUSTING THE SSN FOR EACH EMPLOYEE, USING TWO ARRAYS (ONE IS ORIGINAL, ANOTHER IS ADJUSTED)
#####################################################################################
    ssn_array_adj = []
    ssn_array.pop(0)
    for each4 in ssn_array:
        ssn_array_adj.append(each4.split('-'))

#####################################################################################
# ADJUST THE STATE ARRAY, CALLING THE ABBREV DICTIONARY FROM *HINTS*
# "each5" IS KEY THAT CALLS THE VALUE FROM DICTIONARY, STORES IN ANOTHER ARRAY
#####################################################################################
    state_array.pop(0)
    state_array_adj = []
    for each5 in state_array:
        state_array_adj.append(us_state_abbrev[each5])
######################################################################################
# CREATING THE DICTIONARY AND STORING ALL INFORMATION, USING EMPLOYEE ID NUMBER AS THE KEY
# "each" IN "ID_array" IS THE EMPLOYEE ID NUMBER.  VALUES ARE ASSIGNED TO THE KEY AS A LIST
######################################################################################
    emp_dict = {}
    ID_array.pop(0)
    i = 0
    for each in ID_array:
        emp_dict[each] = [first_last[i][0], first_last[i][1], DOB_array_re2[i],
                            "***-**-"+ssn_array_adj[i][2], state_array_adj[i]]
        i += 1
csvfile.close()

###############################################################################
# WRITING TO TEXT FILE (CSV)
###############################################################################

with open("Output_PyBoss.txt", "w") as txt_file:
    txt_file.write('Emp ID')
    txt_file.write(',')
    txt_file.write('First Name')
    txt_file.write(',')
    txt_file.write('Last Name')
    txt_file.write(',')
    txt_file.write('DOB')
    txt_file.write(',')
    txt_file.write('SSN')
    txt_file.write(',')
    txt_file.write('State')
    txt_file.write('\n')
    for key in emp_dict:
        txt_file.write(key)
        txt_file.write(',')
        txt_file.write(emp_dict[key][0])
        txt_file.write(',')
        txt_file.write(emp_dict[key][1])
        txt_file.write(',')
        txt_file.write(emp_dict[key][2])
        txt_file.write(',')
        txt_file.write(emp_dict[key][3])
        txt_file.write(',')
        txt_file.write(emp_dict[key][4])
        txt_file.write('\n')



        

