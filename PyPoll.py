# Data we need to retrieve
# 1. total number of vites cast
# 2. A complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. total number of votes each candidate won
# 5. the winner of the election based on popular votes

import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:


  #write three counties to the file
    txt_file.write("Counties in the Election\n-----\nArapahoe\nDenver\nJefferson")

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)
    header = next(csvreader)
    # To do: perform analysis.
    for row in csvreader:
        print(row)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
# Open the election results and read the file.
candidate_options = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
# Print each row in the CSV file.
    for row in file_reader:
       total_votes += 1
       candidate_name = row[2]
       if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        
        candidate_votes[candidate_name] = 0
    
       candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_votes)

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    #calculate percentage of votes
    vote_percentage = float(votes)/ float(total_votes) * 100
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        #set the winning_candidate equal to candidate_name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-----------\n"
    f"Winner:{winning_candidate}\n"
    f"winning count:{winning_count:,}\n"
    f"winning percentage:{winning_percentage:.1f}%\n"
    f"--------------\n")
print(winning_candidate_summary)