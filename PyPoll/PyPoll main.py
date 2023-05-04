import csv

with open("Pypoll/Resources/election_data.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    total_votes = 0
    candidates = {}

    for row in reader:

        total_votes += 1

        if row[2] not in candidates:
            candidates[row[2]] = 0

        candidates[row[2]] += 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

winner = ""
max_votes = 0

for candidate, votes in candidates.items():

    vote_percentage = round((votes / total_votes) * 100, 3)
    
    print(f"{candidate}: {vote_percentage}% ({votes})")
    
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open('Election Results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    
    for candidate, votes in candidates.items():
        vote_percentage = round((votes / total_votes) * 100, 3)
        file.write(f"{candidate}: {vote_percentage}% ({votes})\n")
        
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

