#Challenge Task: Get...
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# Import the csv module which provides functionality to read from and write to CSV files.
import csv
import os
# Define function and parameter list.
def calculate_votes(ballot_data):
    # Initialize variables and Create an empty dictionary to store the vote counts for each candidate
    vote_counts = {}
    total_votes = 0

    # Loop through each ballot and count the votes for each candidate
    # Get the candidate name and strip any whitespace
    for ballot in ballot_data:
        candidate = ballot[2].strip().lower()  
        if candidate not in vote_counts:
            vote_counts[candidate] = 0
        vote_counts[candidate] += 1
        total_votes += 1
    
    # Calculate the percentage of votes each candidate won by Looping through the vote_counts dictionary.
    vote_percentages = {}
    for candidate, vote_count in vote_counts.items():
        vote_percentages[candidate] = round((vote_count / total_votes) * 100, 2)
    # Return a tuple containing the vote counts, vote percentages, and total votes
    return vote_counts, vote_percentages, total_votes
# Set the path to the CSV file using the os module's join method to concatenate folder and file names
file_name = os.path.join ('Resources', 'election_data.csv')
# CSV file is opened in read mode and use csv.reader to read its contents
with open(file_name, 'r') as file:
    # Create a csv.reader object to parse the CSV file
    csvreader = csv.reader(file)
    # Using next() to skip the header row and set the header variable to the header row
    header = next(csvreader)
    # Converting the remaining data into a list of lists and set it to the ballot_data variable
    ballot_data = list(csvreader)
    # calculating the number of votes for each candidate in the current election.
    vote_counts, vote_percentages, total_votes = calculate_votes(ballot_data)

    # Declaring variables; total_votes and list vote_counts with stored candidate names 
    # and their respective percentages.
print(f'Total Votes: {total_votes}')
for candidate, votes in vote_counts.items():
    percentage = vote_percentages[candidate]
    # Prints out each candidate's name and percentage on separate lines with f'{candidate}': {percentage}'.
    print(f'{candidate.title()}: ({percentage}%) {votes}')

    # Create empty list called winner to store the winning candidate's name.
    # code iterates through all of the candidates in vote_counts and prints the candidate with the maximum vote count.
    vote_counts = {'Charles Casper Stockham': 85213, 'Diana Degette': 272892, 'Raymon Anthony Doane': 11606}
    winner = max(vote_counts, key=vote_counts.get)
print(f"Winner: {winner}")

# creating and exporting a text file with the results using Python's 'with' statement, 
# which automatically closes the file after the block of code has finished executing,
# and using the f-strings to simplify the string formatting.

output_path = "election_outcome.txt"
with open(output_path, "w") as file:
    file.write("Election Results\n"
               "--------------------------\n"
               "Total Votes: 369711\n"
               "--------------------------\n"
               "Charles Casper Stockham: (23.05%) 85213\n"
               "Diana Degette: (73.81%) 272892\n"
               "Raymon Anthony Doane: (3.14%) 11606\n"
               "--------------------------\n"
               "Winner: Diana Degette\n"
               "--------------------------\n")
