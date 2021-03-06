# # PyBank Data
import csv
import statistics

# #Set variables
tot_months= 0
tot_PL= 0.0
ch_PL = []
increase_prof = ["",0]
decrease_prof = ["",0]
prev_mon_PL= 0
result = []

# #Open the CSV File
with open("Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    for row in csvreader:
        
        # Add Total number of months
        tot_months = tot_months + 1

        #Add profit/loss
        tot_PL = tot_PL + int(row[1])

        #Calculate Changes in PL then average
        if tot_months >1:
            ch_PL.append(int(row[1]) - prev_mon_PL)

        prev_mon_PL = int(row[1])

        #Greatest increase in prof (date and amount)
        if increase_prof[1] < int(row[1]):
            increase_prof[0] = row[0]
            increase_prof[1] = int(row[1])

        #The greatest decrease in profile (date and amount)
        if decrease_prof[1] > int(row[1]):
            decrease_prof[0] = row[0]
            decrease_prof[1] = int(row[1])

        
    result.append('Financial Analysis')
    result.append('--------------------')
    result.append(f'Total Months: {tot_months}')
    result.append(f'Total Profit/Loss: $ {tot_PL}')
    result.append(f'Average Change: $ {round(statistics.mean(ch_PL),2)}')
    result.append(f'Greatest Increase PL:  {increase_prof[0]}, $ {increase_prof[1]} ')
    result.append(f'Greatest Decrease PL:  {decrease_prof[0]}, $ {decrease_prof[1]} ')
    
    #Printing to Python console
    for item in result:
        print(item)
   
    #Print results to Anaylsis txt: 
    with open("Analysis/results.txt", 'w') as text_file:
        for item in result:
            text_file.write(item + "\n")
    