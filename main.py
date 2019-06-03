import os
import csv

csvpath = os.path.join("","budget_data.csv")

with open(csvpath,'r',encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    #print(f"csvheader = {csvheader}")

    months = [] #stores list of months
    changelist = [] #stores difference between months
    currval = 0 
    change = 0
    profitlosssum = 0 #to compute sum of profits & losses

    for row in csvreader:
        months.append(row[0])      
        #print(int(row[1]))
        #print(currval)
        change = int(row[1]) - int(currval)
        changelist.append(change)
        currval = row[1]
        profitlosssum = profitlosssum + int(row[1])

    #avgprofits = sum(profits)/len(profits)
    #avglosses = sum(losses)/len(losses)
    monthcount = len(months)
    profitlosssum = '${:,.2f}'.format(profitlosssum) # format as USD with 2 decimal places
    changelist.pop(0) #remving first element of the list as we require the differences only from second month onwards
    avgchange = '${:,.2f}'.format(round(sum(changelist)/len(changelist),2))
    greatestincrease =  '${:,.2f}'.format(max(changelist))
    greatestdecrease = '${:,.2f}'.format(min(changelist))
    greatestincreasemonth = months[changelist.index(max(changelist)) + 1]  # geting index of greatest change and finding the month. adding 1 since the month list has all months while the change list has only from second month onwards
    greatestdecreasemonth = months[changelist.index(min(changelist)) + 1]  # geting index of smallest change and finding the month. adding +1 since the month list has all months while the change list has only from second month onwards
    
    #avglosses = losses.mean()
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {monthcount}")
    print(f"Total: {profitlosssum}")
    print(f"Average  Change: : {avgchange}")
    print(f"Greatest Increase in Profits: {greatestincreasemonth} {greatestincrease}")
    print(f"Greatest Decrease in Profits: {greatestdecreasemonth} {greatestdecrease}")


    filetowrite = os.path.join("","", "BankOutput.txt")
    with open(filetowrite, 'w' , newline = '\n')  as textfile:
        #csvwriter = csv.writer(csvfile)
        textfile.write("Financial Analysis\n")
        textfile.write("----------------------------\n")
        textfile.write(f"Total Months: {monthcount}\n")
        textfile.write(f"Total: {profitlosssum}\n")
        textfile.write(f"Average  Change: : {avgchange}\n")
        textfile.write(f"Greatest Increase in Profits: {greatestincreasemonth} {greatestincrease}\n")
        textfile.write(f"Greatest Decrease in Profits: {greatestdecreasemonth} {greatestdecrease}\n")
    textfile.close()