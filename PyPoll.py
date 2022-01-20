#Data Needed
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. Percentage of votes each candidate won
#4. Winner of election based on popular vote

import csv
import os

#Assign variable to load file from path
file_to_load = os.path.join("resources", "election_results.csv")
#Assign variable to save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter + candidate name list + candidate vote dictionary before opening file
total_votes = 0
candidate_options = []
candidate_votes = {}

#Winning candidate name and winning candidate count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read header row
    headers = next(file_reader)

    #Print each row in the csv file
    for row in file_reader:
        #Add to total vote count
        #total_votes = total_votes + 1
        total_votes += 1

        #Get candidate name from each row
        candidate_name = row [2]

        if candidate_name not in candidate_options:
            #Add candidate name to candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

#Save results to text file
with open(file_to_save, "w") as txt_file:
    #Print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print (election_results, end="")

    #Save final vote count to text file
    txt_file.write(election_results)
 
        
    #Determine percentage of votes for each candidate
    for candidate_name in candidate_votes:
        #Retrieve vote count
        votes = candidate_votes[candidate_name]
        #Calculate percentage of total
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print candidate name and percentage to terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #Save candidate results to text file
        txt_file.write(candidate_results)
    
        #Determine winning vote count and winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count, winning_percentage, and winning candidate
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #Print winning candidate, vote count, and percentage to terminal
    winning_candidate_summary = (
       f"-------------\n"
       f"Winner: {winning_candidate}\n"
       f"Winning Vote Count: {winning_count}\n"
       f"Winning Percentage: {winning_percentage:.1f}%\n"
       f"-------------\n")
    print(winning_candidate_summary)
    #Save winning candidate results to text file
    txt_file.write(winning_candidate_summary)


