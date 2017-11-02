import os
path = os.path.dirname(os.path.realpath(__file__))

csvpath = "election_data_2.csv"

import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    totalVotes = 0
    for each in csvreader:
        totalVotes += 1
csvfile.close()

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    candidateArray = []
    for candidate in csvreader:
        candidateArray.append(candidate[2])
    
    candidateArray.pop(0)
    unique_candidates = list(set(candidateArray))

    mydict = {}
    for each_uniq in unique_candidates:
        votes = 0
        for aa in candidateArray:
            if aa == each_uniq:
                votes += 1
            mydict[each_uniq] = votes

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
