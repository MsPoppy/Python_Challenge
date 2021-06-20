
import os
import csv

file= r"C:\Users\lanis\Documents\Bootcamp\Homework\Python_Challenge\PyBank\Resources\budget_data.csv"
csvpath = file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    header= next(csvreader)
    print(header)
   
    Prof_loss=[]
    dates=[]
    for row in csvreader:
       dates.append(row[0])
       Prof_loss.append(float(row[1]))
    print(dates)
    print(Prof_loss)
    num_months=[]
    print(len(dates))
    Net_total= sum(Prof_loss)
    print("$", sum(Prof_loss))

    