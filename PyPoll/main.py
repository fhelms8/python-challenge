print("PyPoll Homework")

#Election Results/ PyPoll
import os
import csv

#Set path for file 
csvpath = os.path.join("..", "Resources", "election_data.csv")
file_to_analyze = "C:/Users/User/python-challenge/PyPoll/electiondata.csv"
file_to_output = "C:/Users/User/python-challenge/PyPoll/Analysis2.txt"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#Total number of votes cast
tot_votes = []
#Complete list of candidates who received votes
candidates = []

#The percentage of votes each candidate won
perc_votes = []
#Total number of votes each candidate won
num_candidate_won = 0
#Winner of the election based on popular vote
winner = []

for row in csvreader:
    tot_votes += 1