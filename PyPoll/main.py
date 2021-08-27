# Dependencies 
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("PyPoll","Resources","election_data.csv")

# Initial variables
total_votes = 0
vote_counts = []
candidates = []

#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

# Open and read csv
with open(election_csv) as election_data:
    read = csv.reader(election_data, delimiter=",")

    # Extract the header row first 
    header = next(read)
    #print(f"Header: {header}")

    for row in read:
        
        # Add to total votes
        total_votes = total_votes + 1
        
        # Collect candidate 
        candidate = row[2]

        # If candidate is in the list, add to vote total
        if candidate in candidates:
            
            # Set candidate index according to candiate list
            candidate_index = candidates.index(candidate)

            # Add to vote count list using same index
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

        # If candiate is not in the list, add into list
        else:
            candidates.append(candidate)
            vote_counts.append(1)

# Variables for calculations
percentages = []
max_index = 0
max_vote = vote_counts[0]

# Add percentage of total votes according to number of candidates
for i in range(len(candidates)):
    
    # Calculate vote_percentage and add to list
    vote_percentage = (vote_counts[i] / total_votes) * 100
    percentages.append(vote_percentage)
    
    # Finding the max_votes
    if vote_counts[i] > max_vote:
        max_votes = vote_counts[i]
        max_index = i

# Choose winning candiate according to index
winner = candidates[max_index]

# Output election results
vote_summary = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------")
print(vote_summary)

for i in range(len(candidates)):
    print(f"{candidates[i]}: {percentages[i]:.3f}% ({vote_counts[i]})")
    
winning_candidate_summary = (
    "---------------------------\n"  
    f"Winner: {winner}\n"
    "---------------------------\n")
print(winning_candidate_summary)

# Export results into text file 
# Set variable for output file
output_file = os.path.join("PyPoll", "analysis","election_results.txt")

# Path to output file
with open(output_file, "w", newline="") as txt_file:
    
    # Write results into file
    txt_file.write(vote_summary)
    
    for i in range(len(candidates)):
        txt_file.write(f"\n{candidates[i]}: {percentages[i]:.3f}% ({vote_counts[i]})")
    txt_file.write("\n")
    txt_file.write(winning_candidate_summary)
