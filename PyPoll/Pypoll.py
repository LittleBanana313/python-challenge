import os
import pandas as pd

# set path for csv
pypollrow = os.path.join('C:/Users/connn/Desktop', ".\\pypoll.csv")

# read csv
df = pd.read_csv(pypollrow)

# Print count of total votes
print("Total votes: ", df['Voter ID'].count())

# count votes per candidate, create new dataframe
newdf = df.groupby("Candidate")["Voter ID"].count().reset_index(name = "Count").sort_values("Count", ascending = False)
newdf

# create percentages per candidate 
newdf['Percent'] = round(newdf.Count/newdf.Count.sum()*100, 5)
newdf

# create a txt file with results
print("Results", file = open("Election.txt", "a"))
print("-------------------------", file = open("Election.txt", "a"))
print ("Total Votes:" ,df['Voter ID'].count(), file=open("Election.txt", "a"))
print("-------------------------", file = open("Election.txt", "a"))
for index, row in newdf.iterrows():
    print (row['Candidate']+": ",str('%.3f'%row['Percent'])+"% ","("+str(row['Count'])+")", file = open("Election.txt", "a"))
print("-------------------------", file = open("Election.txt", "a"))
print("Winner: ", newdf['Candidate'][newdf['Percent'] == newdf['Percent'].max()].iloc[0], file = open("Election.txt", "a"))
print("-------------------------", file = open("Election.txt", "a"))
