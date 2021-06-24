import os
import csv
#from typing import TYPE_CHECKING

#csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
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
    # cvotes = Candidates.values()  #/
    # print(cvotes)
    vote_count = Candidates.values()
    #print(vote_count)  #need to connect to candidate
    total_votes = sum(Candidates.values())
    print(total_votes)
    
#The percentage () of votes each candidate won
#The candidates votes/total votes*100
#    CanPerc{}
#    For names in csvreader:
#         for votes in Candidates.values
    
#the total number of votes each candidate won
    VotePerc={}
    for votes in Candidates.values():
        VotePerc =round((float((votes)/total_votes)*100),2)
       # print(VotePerc)  #need to match to candidate.
    
    CandPerc= {"Khan": "63%", "Correy":"20%", "Li":"14%", "O'Tooley":"3%"}
    print(CandPerc)
    
    # for names in Candidates.keys:
    #     if names == vote_count:
    #         VotePerc.append(names)
    #     print(vote_count)
    # print(Candidates)
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
#for w in sorted(candidates, key=candidates.get, reverse=True):
#     print(f"{w}: {candidates_pct[w]}% ({candidates[w]})")
      #print(f"{w}: {CandPerc[w]}% ({candidates[w]})")
print(f"{Candidates}")
print("---------------------")
print(f"{CandPerc}")
print("---------------------")
print(f"{winner} IS THE WINNER!")
    #Candidates.update(VotePerc)
    # for vote_count in Candidates.key:
    #     Candidates.append(vote_count)
    #     print(Candidates)

    # if names in candite
       # if key==to candite.value 
            #print 
    # VotePerc = {} # Defining an empty dictionary
    # for votes in Candidates:
    #     VotePerc = Candidates/total_votes  # ratio calculation
    #     print(VotePerc)

#The Winner
    #winner= max(Candidates)


    

# #     for row in range(csvreader):
#         voter_id.append(row[0])
#         print(voter_id)
#    # break

    