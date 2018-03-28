import os
path = os.path.dirname(os.path.realpath(__file__))

csvpath = "election_data_2.csv"

import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

################################################################################
# Finding out the total number of votes cast
################################################################################

    totalVotes = 0
    for each in csvreader:
        totalVotes += 1
csvfile.close()

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
##################################################################################
# Creating a list of candidate names, then pop the title row, call 'set' to find
# unique candidates.  Since set is not a iterrable list, we type cast to a list.  The
# list will be different every time, so we use a dictionary to call those key variables
##################################################################################   
    candidateArray = []
    for candidate in csvreader:
        candidateArray.append(candidate[2])
    
    candidateArray.pop(0)
    unique_candidates = list(set(candidateArray))

##################################################################################
# To count the total votes per candidate, we call each item in the unique_candidate list
# if the name in the candidateArray matches to the item in the unique_candidate list,
# then we add a +1 to the count.  So each candidate will have a total vote count associated with
# their key(name).  Empty dictionary created to store keys and respective values.
###################################################################################

    mydict = {}

    for each_uniq in unique_candidates:
        votes = 0
        for aa in candidateArray:
            if aa == each_uniq:
                votes += 1
            mydict[each_uniq] = votes
            
####################################################################################
# This for-loop will loop through the keys (names) and associated values (total votes).  Then
# appending another value (percentage of total votes) to the key, in the second position of the list,
# next to the total votes.
####################################################################################

    for key, value in mydict.items():
        percent_of = mydict[key]/(totalVotes-1)
        #mydict[key] = [value, percent_of]
        mydict[key] = [value]
        mydict[key].append(percent_of)

    print("--------------------\n")
    print("Election Results\n")
    print("--------------------")
    print("Total Votes: " + str(totalVotes-1))
    print("--------------------")

    for key, value in mydict.items():
        print(str(key) + ": " + str(mydict[key][1]*100) + "% " + "(" + str(mydict[key][0]) + ")")
        winner = str(key)
        winningVote = int(mydict[key][0])

    for key, value in mydict.items():
        if winningVote < int(mydict[key][0]):
            winner = key
    print("--------------------\n")
    print("Winner: " + str(winner))
    print("\n--------------------")
csvfile.close()
     
with open("Output_PyPoll.txt", "w") as txt_file:
    txt_file.write("--------------------\n")
    txt_file.write("Election Results\n")
    txt_file.write("--------------------\n")
    txt_file.write("Total Votes: " + str(totalVotes-1))
    txt_file.write("\n--------------------\n")
    for key, value in mydict.items():
        txt_file.write(str(key) + ": " + str(mydict[key][1]*100) + "% " + "(" + str(mydict[key][0]) + ")\n")
        winner = key
        winningVote = mydict[key][0]
    for key, value in mydict.items():
        if winningVote < mydict[key][0]:
            winner = key
    txt_file.write("\n--------------------\n")
    txt_file.write("Winner: " + str(winner))
    txt_file.write("\n--------------------\n")
txt_file.close()
