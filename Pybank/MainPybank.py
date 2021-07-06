import os
import csv
import pandas as pd

# set path for csv
pybankrow = os.path.join('C:/Users/connn/Desktop', ".\\pybank.csv")

# create variables and initialize
totalprofit = 0
count = 0 
deltaprofit = 0
currentprofit = 0
monthlychange = []
profit = []
date =[]

#Open csv w/ pybankrow
with open(pybankrow, newline = "") as csvfile:
    # delimit
    csv_reader = csv.reader(csvfile, delimiter = ",")
    # read header row first
    header = next(csv_reader)
    
    for row in csv_reader:

        # count months
        count = count +1
        
        date.append(row[0])
        
        # find total profit
        profit.append(row[1])
        totalprofit = totalprofit + int(row[1])
        
        # find delta profit month to month
        finalprofit = int(row[1])

        if count != 1: 
            monthlydelta = finalprofit - currentprofit
        
            # store delta profit month values in a list
            monthlychange.append(monthlydelta)
        
        # find total change in profit
            deltaprofit = deltaprofit + monthlydelta
        currentprofit = finalprofit
    avgDprofit = (deltaprofit/(count-1))
        
    # find min and max change in profit, related dates
    GreatIncrProfit = max(monthlychange)
    GreatDecrProfit = min(monthlychange)
        
    Maxdate = date[monthlychange.index(GreatIncrProfit)]
    Mindate = date[monthlychange.index(GreatDecrProfit)]
        
# Terminal output
print ("Financial Analysis")
print ( '-------------------------------------------------')
print ("Total months: " + str(count))
print ("Total profit: " + "$" + str(totalprofit))
print ("Average change: " + "$" + str(avgDprofit))
print ("Greatest increase in profit: " + str(Maxdate) + ", " + "$" + str(GreatIncrProfit))
print ("Greatest decrease in profit: " + str(Mindate) + ", " + "$" + str(GreatDecrProfit))
print ( '-------------------------------------------------')


# make a text file
with open('Pybank.txt', 'w') as text:
    text.write ("Financial Analysis" + "\n")
    text.write ('-------------------------------------------------\n')
    text.write ("Total months: " + str(count)+ "\n")
    text.write ("Total profit: " + "$" + str(totalprofit)+ "\n")
    text.write ("Average change: " + "$" + str(int(avgDprofit))+ "\n")
    text.write ("Greatest increase in profit: " + str(Maxdate) + ", " + "$" + str(GreatIncrProfit)+ "\n")
    text.write ("Greatest decrease in profit: " + str(Mindate) + ", " + "$" + str(GreatDecrProfit)+ "\n")
    text.write ('-------------------------------------------------')
