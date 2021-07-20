#PyPoll
import csv

#Set Variables
tot_votes= 0
candidate_choices = []
candidates_votes = {}
winner = 0
result = ""
name_list = []
count_list = 0

with open("Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# # #Open the CSV File

    header = next(csvreader)

    for row in csvreader:
        name_list.append(row[2])

        # Add Total number of votes (*Correct*)
        tot_votes = tot_votes + 1      
        
        #Add list of candidates (row 2)
    
        candidate_choices.append(row[2])

    for candidate in set(candidate_choices):
        name_list.append(candidate)

    Tooley = (candidate_choices.count)("O'Tooley")
    Khan = (candidate_choices.count)("Khan")
    Correy = (candidate_choices.count)("Correy")
    Li = (candidate_choices.count)("Li")
    

    #Set percentage functions 
    Tooley_percentage = (Tooley/tot_votes) * 100
    Khan_percentage = (Khan/tot_votes) * 100
    Correy_percentage = (Correy/tot_votes) * 100
    Li_percentage = (Li/tot_votes) * 100

    Tooley_percentage = "{0:.2f}%".format(Tooley_percentage)
    Khan_percentage = "{0:.2f}%".format(Khan_percentage)
    Correy_percentage = "{0:.2f}%".format(Correy_percentage)
    Li_percentage = "{0:.2f}%".format(Li_percentage)


    #Calcuate winner function
    if Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"
    elif Khan > Correy > Li > Tooley:
       Winner = "Khan"
    elif Correy > Khan > Li > Tooley:
       Winner = "Correy"
    elif Li > Khan > Correy > Tooley:
       Winner = "Li"
    
    
#Print functions
    print("Election Results")
    print('-----------------')
    print(f'Total Votes: {tot_votes}')
    print('------------------')
    print(f"Khan: {Khan_percentage}% ({Khan})")
    print(f"Correy: {Correy_percentage}% ({Correy})")
    print(f"Li: {Li_percentage}% ({Li})")
    print(f"O'Tooley: {Tooley_percentage}% ({Tooley})")
    print(f'Winner: {Winner}')

   
    #Print results to Anaylsis via txt: 
    with open("Analysis/results.txt", 'w') as text_file:
        for item in result:
            text_file.write(item + "\n")