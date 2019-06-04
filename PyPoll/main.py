import os
import csv

#
# Candidate dictionary
#
candidate_dict = {}

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    header = next(csvreader)
    total_votes = 0

    for row in csvreader:
        current_candidate = row[2]

        if current_candidate not in candidate_dict:
            candidate_dict[current_candidate] = 1
        else:
            candidate_dict[current_candidate] += 1

        total_votes += 1

print("Election Results")
print("------------------")
print("Total Votes: " + str(total_votes))
print("------------------")

highest_count = 0
winner = ""
for person in candidate_dict:
    if (candidate_dict[person] > highest_count):
       highest_count = candidate_dict[person]
       winner = person

    percentage = round(float(candidate_dict[person]/total_votes * 100))
    print(person + " : " + str(percentage) + "% (" + str(candidate_dict[person]) + ")")
print("------------------")
print("Winner: " + winner)
print("------------------")

f = open("result.txt", "w+")
f.write("Election Results\n")
f.write("------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("------------------\n")

for person in candidate_dict:

    percentage = round(float(candidate_dict[person]/total_votes * 100))
    f.write(person + " : " + str(percentage) + "% (" + str(candidate_dict[person]) + ")\n")
f.write("------------------\n")
# 
# already calculated the winner above
#
f.write("Winner: " + winner + "\n")
f.write("------------------\n")
