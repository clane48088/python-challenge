import csv
import os

# load the file to read election data
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# variables
total_Votes = 0     # variable for total number of votes
candidates = []     # list of candidates in the election
candidate_Votes = {} # dictionary that will hold the votes each candidate receives
winningCount= 0     # variable hold the winning count
winningCandidate = "" # variable to hold teh winning candidate

# read the csv file 
with open(file_to_load) as election_data:
    #create csv reader
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # rows will be lists
        # index 0 is the ballot ID
        # index 2 is the candidate

    # for each row
    for row in reader:
        # add on the total votes
        total_Votes += 1 # same as total_Votes + 1

        # to see if the candidate is in the list of candidates
        if row[2] not in candidates:
            # if the candidate is not in the list, add the candidate to the list of candidates
            candidates.append(row[2])

            # add the candidate to the dictionary also
            # {"key"= value }
            # start the count at 1 for the votes
            candidate_Votes[row[2]] = 1
        else:
            # the candidate is in the list of candidates
            # add a vote to that candidate count
            candidate_Votes[row[2]] += 1

# print(candidate_Votes)
voteOutput = ""

for candidates in candidate_Votes:
    # get the vote count and percentage of the votes
    votes = candidate_Votes.get(candidates)
    votePct = (float(votes) / float(total_Votes)) * 100.00
    voteOutput += f"\n{candidates}: {votePct:.3f}% ({votes}) \n"

    # compare the votes to the winning count
    if votes > winningCount:
        # udate the votes to the new winning count
        winningCount = votes
        # update the winning candidate
        winningCandidate = candidates

winningCandidateOutput = f"Winner: {winningCandidate}"
#print(winningCandidateOutput)
# create an output variable to hold the output
output = (
    f"Election Results\n"
    f"--------------------------------\n"
    f"Total Votes: {total_Votes:.0f} \n"
    f"--------------------------------\n"
    f"{voteOutput}\n"
    f"--------------------------------\n"
    f"{winningCandidateOutput} \n"
    f"--------------------------------\n"
    
)
# print the output to the console/terminal
print(output)

# export the output to a text file
with open(file_to_output, "w") as textfile:
    textfile.write(output)