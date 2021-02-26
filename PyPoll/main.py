import os
import csv 

totalvoters = 0


poll_csv = os.path.join("..", "Resources", "election_data.csv")

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    candidates = {}
    keylist = [] 
    for row in csvreader:
        totalvoters = totalvoters + 1
        pick = row[2]
        if pick not in candidates:
            candidates[pick] = 1
            keylist.append(pick)
        elif pick in candidates:
            candidates[pick] = candidates[pick] + 1

print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(totalvoters))
print("--------------------------------")
x = 0
winner = 0
winnerstr = ""
for person in candidates:
    canvotes = candidates[keylist[x]]
    print(keylist[x] + ": " + str(canvotes/totalvoters) + " (" + str(canvotes) + ") votes")
    if canvotes > winner:
        winner = canvotes
        winnerstr = keylist[x] 
    x = x + 1

print("--------------------------------")

print("Winner: " + winnerstr)

print("--------------------------------")