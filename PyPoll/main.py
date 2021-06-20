import os
import csv

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
# #The Total Number of Votes cast
    Candidates= {}
    for names in csvreader:
        if names[2] in Candidates.keys():
            Candidates[names[2]] += 1
        else:
            Candidates[names[2]] = 1
    print(Candidates)

    total_votes = sum(Candidates.values())
    print(total_votes)

#     voterid=[]
#     for row in csvreader:
#         voterid.append(Row[0])
#         print(len(voterid)

#      #dict=candidate name
     # value is total vote name for the candiate
     #    
#A complete list of candidate who recieved votes

#The percentage () of votes each candidate won

#the total number of votes each candidate wom

#The Winner



    
#     for row in csvreader:
#         print(row[0])
#         print("---------------------------------------------------------------------------------")
#         Print("----------------------------------------------------")
#         print("---------------------------------------------------------------------------")
# #     voter_id=[]


# #     for row in range(csvreader):
#         voter_id.append(row[0])
#         print(voter_id)
#    # break

    #Total Votes Cast
    #print(Len)
    #
    # county=[]
    # candidate=[]
    # 
    #     county.append(row[1])
    #     candidate.append(row[2])
    #     #print(voter_id)
    #     #print(county)
    #     print(candidate)