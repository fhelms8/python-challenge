#PyPoll
import csv

#Set Variables
tot_votes= 0
candidate = []
perc_votes = 0.0
candidates_votes = {}
candidate_perc = {}
winner = 0
result = ""

# #Open the CSV File
with open("Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    for row in csvreader:
        
        # Add Total number of votes
        tot_votes = tot_votes + 1
        
        #Add list of candidates
        candidate = row[2]

        #Calculate votes per candidate 
        if candidate in candidates_votes:
            candidates_votes[candidate] = candidates_votes[candidate] + 1 
        else:
            candidates_votes[candidate] = 1
        print(candidates_votes)
        
        #Percentage format {:%}
        def percent(x):
            num = x/tot_votes
            percentage = "{:.2%}".format(num)
            print(percentage)

        

    
    #     prev_mon_PL = int(row[1])

    #     #Greatest increase in prof (date and amount)
    #     if increase_prof[1] < int(row[1]):
    #         increase_prof[0] = row[0]
    #         increase_prof[1] = int(row[1])

    #     #The greatest decrease in profile (date and amount)
    #     if decrease_prof[1] > int(row[1]):
    #         decrease_prof[0] = row[0]
    #         decrease_prof[1] = int(row[1])

        
    # result.append('Election Results')
    # result.append('--------------------')
    # result.append(f'Total Votes: {tot_votes}')
    # result.append('--------------------')
    # result.append(f'candidates_votes: $ {tot_PL}')
    # result.append(f'Average Change: $ {round(statistics.mean(ch_PL),2)}')
    # result.append(f'Greatest Increase PL:  {increase_prof[0]}, $ {increase_prof[1]} ')
    # result.append(f'Greatest Decrease PL:  {decrease_prof[0]}, $ {decrease_prof[1]} ')
    
    #Printing to Python console
    for item in result:
        print(item)
   
    # #Print results to Anaylsis txt: 
    # with open("Analysis/results.txt", 'w') as text_file:
    #     for item in result:
    #         text_file.write(item + "\n")