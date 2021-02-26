import os
import csv 

bank_csv = os.path.join("..","Resources", "budget_data.csv")

#setting variables outside of loops
month = ""
monthnum = 0
totaltotal = 0
changes = []

bigstring = ""
lowstring = ""
greatest = 0
lowest = 0

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
 

    for row in csvreader:
        #not sure if this is necessary but dont want to have
        #to fix indentation
        if row[0] != month:
            #'calculates number of months'
            monthnum = monthnum + 1 

            #'claculates total profit/loss'
            monthprof = int(row[1])
            totaltotal = totaltotal + monthprof            

            #adds each monthh's profit/loss into a list
            changes.append(monthprof)

            #calculates highest/lowest number
            if monthprof > greatest:
                greatest = monthprof
                bigstring = row[0]
            elif monthprof < lowest:
                lowest = monthprof
                lowstring = row[0]

#array that tracks changes



print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(monthnum))
print("Total: $" + str(totaltotal))
print("Average Change: $ " + str(sum(changes)/len(changes)))
print("Greatest increase in Profits: " + bigstring + " $" + str(greatest))
print("Greatest decrease in Profits : " + lowstring + " $" + str(lowest))

bank_output = os.path.join("..", "analysis", "results.txt")

with open(bank_output, 'w', newline='') as csvfile:
    print("Financial Analysis", file=csvfile)
    print("------------------------------", file=csvfile)
    print("Total Months: " + str(monthnum), file=csvfile)
    print("Total: $" + str(totaltotal), file=csvfile)
    print("Average Change: $ " + str(sum(changes)/len(changes)), file=csvfile)
    print("Greatest increase in Profits: " + bigstring + " $" + str(greatest), file=csvfile)
    print("Greatest decrease in Profits : " + lowstring + " $" + str(lowest), file=csvfile)
    