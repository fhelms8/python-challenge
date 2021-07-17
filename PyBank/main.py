# PyBank Data
import os
import csv

# #Set path for file 
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

#Open the CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

#Set variables
tot_months=1
net_total=0
ch_PL = []
increase_prof = ["",0]
decrease_prof = ["",0]
profit = []

# for row in csvreader:
#         tot_months.append(row[0])
#         net_total.append(int(row[1]))
# for p in range(len(profit)-1):
#         ch_PL.append(profit[p+1]-profit[p])

for row in csvreader:
    

#date = column 0
#PL = column 1
#Total # of months in data set; net total of PL over data set
    # for row in csvreader:
    #     tot_months = tot_months + 1
    #     net_total = net_total + int(row[1])

#Changes in PL over data set then average
    
