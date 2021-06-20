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
   Net_total= sum(Prof_loss)
   print("$", sum(Prof_loss))

      #Find the Average Change
   changes=[]
   for x in range(1,len(dates)):
      change = Prof_loss[x]-Prof_loss[x-1]
      changes.append(change)

   avg_change=round(sum(changes)/len(changes),2)
   print(avg_change)
            #change is b-a, need a list to average
       # newchange=sum(Prof_loss(x) - Prof_loss(x-1))

# The greatest increase in profits (date and amount) over the entire period
# Need to find the date connected to make Change.
# We need to find the index. 
   maxchange=max(changes)
   print(maxchange)
   datemax = dates[changes.index(maxchange)]
   # print(datemax)
   # minchange=min(changes)
   # print(minchange)


#

   



       #Find the total of Prof/loss column.  
       #sum(Prof_loss.values)
    #    total =float(0.0)
    #    print(total + (sum(Prof_loss)))
      
    # for values in Prof_loss(1,86):
    #    sum(Prof_loss)
    # for value in Prof_loss:
    #     value = total =+ len(Prof_loss)
    #     print(value)



#         for i in range(1, len(total)): 
#         change.append(total[i] - total[i-1])
#  The average of the changes in "Profit/Losses" over the entire period
#         avg_chng = round(sum(change) / len(change),2)
# The greatest increase in profits (date and amount) over the entire period
#         max_chng = max(change)
#  The greatest decrease in losses (date and amount) over the entire period
#         min_chng = min(change)
#  Through index get location of the date and get date value from dates array 
#         max_dt_chng = dates[change.index(max_chng)]
#         min_dt_chng = dates[change.index(min_chng)]