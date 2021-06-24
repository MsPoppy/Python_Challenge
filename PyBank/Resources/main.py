import os
import csv

#Create the Path and open it
file= r"C:\Users\lanis\Documents\Bootcamp\Homework\Python_Challenge\PyBank\Resources\budget_data.csv"
csvpath = file
with open(csvpath, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   print(csvreader)
   header= next(csvreader)
   print(header)

    #Create a list for each column and print them
   dates=[]
   Prof_loss=[]
   for row in csvreader:
      dates.append(row[0])
      Prof_loss.append(float(row[1]))
   print(dates)
   print(Prof_loss)
      #find the Total Months
   print(len(dates))
   Net_total= round(sum(Prof_loss),2)
   print("$", sum(Prof_loss))

      #Find the Average Change
      #change is b-a, need a list to average
       # newchange=sum(Prof_loss(x) - Prof_loss(x-1))

   changes=[]
   for x in range(1,len(dates)):
      change = Prof_loss[x]-Prof_loss[x-1]
      changes.append(change)

   avg_change=round(sum(changes)/len(changes),2)
   print(avg_change)

# The greatest increase in profits (date and amount) over the entire period
# Need to find the date connected to make Change.
# We need to find the index. 
   maxchange= round(max(changes),2)
   print(maxchange)
   datemax =dates[changes.index(maxchange)]
   print(datemax)
   minchange= round(min(changes),2)
   print(minchange)
   datemin =dates[changes.index(minchange)]
   print(datemin)
#minmonth= data[minindex + 1][0]
   print("--------------------------------")
   print("Financial Analysis")
   print("--------------------------------")
   print("Total Months: "+ str(len(dates)))
   print("Total: $ "+ str(Net_total))
   print("Average Change: "+ "$ "+ str(avg_change))
   print("Greatest Increase in Profits: " + str(datemax) + "  " + "$" + str(maxchange) )
   print("Greatest Decrease in Profits: " + str(datemin) + "  " + "$"+ str(minchange) )
   
output_path = os.path.join("..","Analysis", "PyBankAnalysis.txt")

with open(output_path, 'w') as csvfile:
    text_file.write:("---------------------\n")
    text_file.write:(f"Financial Analysis\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"Total Months: "+ str(len(dates))"\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"Total: $ "+ str(Net_total))"\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"Average Change: "+ "$ "+ str(avg_change))"\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"Greatest Increase in Profits: " + str(datemax) + "  " + "$" + str(maxchange)"\n")
    text_file.write:(f"Greatest Decrease in Profits: " + str(datemin) + "  " + "$"+ str(minchange))