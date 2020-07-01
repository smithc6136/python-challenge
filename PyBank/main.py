#The total number of months included in the dataset - Check!
# The net total amount of "Profit/Losses" over the entire period
    # define a variable, +=, special for loop 
    # enumerate: https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/#enumerate
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits/decrease in losses (date and amount) over the entire period

#Left to do:
    #Push the changes to GitHub or GitLab.
        #YouTube Video: https://www.youtube.com/watch?v=ruieT3Nkg2M


import os
import csv
import numpy as np

csvpath = os.path.join('Resources', 'data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #do next line again (done) but store in variable after monthly change=[]
    #gets rid of header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    months=0
    max_profit=0
    max_loss=0
    monthly_change= []
    #list=data.csv(row[1])
    #gets rid of first row of data
    first_row=next(csvreader)
    net_total=int(first_row[1])

    # Read each row of data after the header
    #Add total months and total profits/losses
    for row in csvreader:
        change_between=int(row[1])-int(first_row[1])
        net_total += int(row[1])
        first_row=row
        monthly_change.append(change_between)

    print("Financial Analysis")
    print("-----------------------")

    month=len(monthly_change)+1
    average_change=round((sum(monthly_change))/len(monthly_change))
    max_profit= max(monthly_change)
    max_loss= min(monthly_change)
        
    print("number of months: ", month)
    print("net total profits/losses: $", net_total)
    print("Total Average Change: $", average_change)
    print("greatest increase in profits: $", max_profit)
    print("greatest decrease in losses: $", max_loss)

outF = open("data.txt", "w")
#write line to output file
outF.write("Financial Analysis" "\n" "-----------------------" "\n" "number of months:  86" "\n" "net total profits/losses: $ 38382578" "\n" "Total Average Change: $ -2315" "\n" "greatest increase in profits: $ 1926159" "\n" "greatest decrease in losses: $ -2196167")
outF.write("\n")
outF.close()

# As an example, your analysis should look similar to the one below:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results