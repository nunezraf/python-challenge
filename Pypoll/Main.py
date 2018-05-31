# import libraries os and csv 
import os
import csv

# set file path to conect data resource 
csvpath = os.path.join('..','Pypoll', 'election_data_1.csv')

# declaring variables vote count, candidates, candidates %, winner and winner count 
vote_count = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# reading file as csv.reader with open stament 
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    # finding total vote count; finding individual vote counts using a for loop 
    for row in csvreader:
        vote_count += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# percentages for each candidate 
for key, value in candidates.items():
    candidates_percent[key] = round((value/vote_count) * 100, 2)

# finding the winner
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

# tests
# print(total_vote_count)
# print(candidates)
# print(candidates_percent)
# print(winner)

# printing to the terminal
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# creating new text file
new_file = open("Output1.txt", "w")

# writing the new file with the results 
new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(vote_count) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")

