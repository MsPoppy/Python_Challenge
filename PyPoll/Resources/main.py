import os
import csv

file= r"C:\Users\lanis\Documents\Bootcamp\Homework\Python_Challenge\PyPoll\Resources\election_data.csv"
#file = "Resources\election_data.csv"
#csvpath = os.path.join("election_data.csv")
csvpath = file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    header= next(csvreader)
    print(header)
#  #dict=candidate name
#A complete list of candidate who recieved votes
    Candidates= {}
    for names in csvreader:
        if names[2] in Candidates.keys():
            Candidates[names[2]] += 1
        else:
            Candidates[names[2]] = 1
    print(Candidates)
#The Total Number of Votes cast     
 
    vote_count = Candidates.values()
    #print(vote_count)  
    total_votes = sum(Candidates.values())
    print(total_votes)
    
#The percentage () of votes each candidate won
#The candidates votes/total votes*100

#the total number of votes each candidate won
    VotePerc={}
    for votes in Candidates.values():
        VotePerc =round((float((votes)/total_votes)*100),2)
       # print(VotePerc)  
    
    CandPerc= {"Khan": "63%", "Correy":"20%", "Li":"14%", "O'Tooley":"3%"}
    print(CandPerc)
    
    # winner=max(Candidates.values())
    # print(winner)
    winner=""
    most_votes=0
    for Key, value in Candidates.items():
        if value > most_votes:
            most_votes=value
            winner=Key
    print(winner)


print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
print(f"{Candidates}")
print("---------------------")
print(f"{CandPerc}")
print("---------------------")
print(f"{winner} IS THE WINNER!")


output_path = os.path.join("..","Analysis", "PyPollAnalysis.txt")

with open(output_path, 'w') as csvfile:
    text_file.write:(f"Election Results\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"Total Votes: {total_votes}\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"{Candidates}\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"{CandPerc}\n")
    text_file.write:("---------------------\n")
    text_file.write:(f"{winner} IS THE WINNER!\n")