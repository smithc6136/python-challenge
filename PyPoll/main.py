#The total number of votes cast - Check!
#A complete list of candidates who received votes - Check!
#The percentage of votes each candidate won - Check!
#The total number of votes each candidate won - Check!
#The winner of the election based on popular vote - Check!
#youtube video: https://www.youtube.com/watch?v=dt4JCYtc1dE

#left to do:
    #Push the changes to GitHub or GitLab.
        #YouTube Video: https://www.youtube.com/watch?v=ruieT3Nkg2M

import os
import csv

import sys 

csvpath = os.path.join('Resources', 'poll_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Line below gets rid of row with titles so "Candidate" isn't included in the list of candidates/votes
    next(csvreader)
    print(csvreader)

    #set lists/dictionary
    candidate=[]
    candidate_amount={}
    candidate_percent=[]
    votes=0
    candidate_names=[]
    d={}

    #add total votes
    for row in csvreader:   
        votes += 1
        candidate.append(row[2])

    #make dictionary (d) with candidate names
    for candidate_names in row[2]:
        key=candidate_names
        if key not in d:
            d[key]=[]
        d[key].append(candidate_names)

    #counting the candidates
    #YouTube Video: https://www.youtube.com/watch?v=dt4JCYtc1dE
    from collections import Counter
    candidate_amount=Counter(candidate)


    print("Election Results:")
    print("-----------------------")
    print("Total Votes: ", votes)
    print("-----------------------")

    #Percentages
    #key=types of data in a dictionary
    List =list(candidate_amount.keys())
    for key in List:
        candidate_percent=round(((candidate_amount[key])/votes)*100)
        #"get takes a maximum of two parameters"
        #https://www.programiz.com/python-programming/methods/dictionary/get
        max_key=max(candidate_amount, key=candidate_amount.get)
        print(key, candidate_percent, "%", "(", candidate_amount[key], ")")
    print("-----------------------")
    print("Winner: ", max_key)
    print("-----------------------")

outF = open("poll_data.txt", "w")
#write line to output file
outF.write("Election Results:" "\n" "-----------------------" "\n" "Total Votes:  3521001" "\n" "-----------------------" "\n" "Khan 63 % ( 2218231" "\n" "Correy 20 % ( 704200 )" "\n" "Li 14 % ( 492940 )" "\n" "O'Tooley 3 % ( 105630 )" "\n" "-----------------------" "\n" "Winner:  Khan" "\n" "-----------------------")
outF.write("\n")
outF.close()

#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.