import os
import csv
budget_data_csv = os.path.join("budget_data.csv")

totalmonth = 0

totalnet = 0

previous_profit_loss = 0

netchange_list = []


with open(budget_data_csv) as csvfile:
   
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        totalmonth = totalmonth +1
        profitloss = int(row[1])
        totalnet = totalnet + profitloss
       
        if totalmonth>1:
            
            netchange=profitloss-previous_profit_loss
            netchange_list.append(netchange)
        previous_profit_loss=profitloss
    average_netchange=sum(netchange_list)/len(netchange_list)



print(totalmonth)
print(totalnet)
print(average_netchange)