import os
import csv

# Path to collect CSV file from folder
election_csv = 'Resources/election_data.csv'

# Define function to process CSV
def results(election_csv):
    with open(election_csv, mode='r') as csvfile:
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        data = list(csvreader)

        # Extract candidate
        ballot_id = [int(row[0]) for row in data]
        candidate = [row[2] for row in data]

        # The total number of votes cast
        votes = len(ballot_id)

        # List candidates and how many votes each has
        candidates = list(dict.fromkeys(candidate))  # using dict to keep candidate list in alphabetical order

        # Count votes for each candidate
        candidate_votes = {candidate: 0 for candidate in candidates}
        for c in candidate:
            candidate_votes[c] += 1

        # The percentage of votes each candidate won
        candidate_percentage = {candidate: (vote_count / votes) * 100 for candidate, vote_count in candidate_votes.items()}

        # The winner of the election based on popular vote
        winner = max(candidate_votes, key=candidate_votes.get)

        return votes, candidate_votes, candidate_percentage, winner

# Call the function and print the results
votes, candidate_votes, candidate_percentage, winner = results(election_csv)

# Print the results at the terminal
print("\nElection Results\n")
print("-------------------------\n")
print(f"Total votes: {votes}\n")
print("-------------------------\n")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({votes})\n")   # Format with % and 3 decimals
print("-------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------")

# Output election results to a new csv file
results_list = [
    ["Election Results"],
    ["----------------------------"],
    [f"Total votes: {votes}"],
    ["----------------------------"]
]
for candidate in candidate_votes:
    results_list.append([f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})"])
results_list.append(["----------------------------"])
results_list.append([f"Winner: {winner}"])
results_list.append(["----------------------------"])

# Write to a new csv file
output = 'analysis/election results.csv'
with open(output, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(results_list)
