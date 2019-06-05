import os
import csv

csvpath = os.path.join("","election_data.csv")
CandidateVotes = {}

with open(csvpath,'r',encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    #print(f"csvheader = {csvheader}")

    TotalVotes = 0

    for row in csvreader:
        TotalVotes = TotalVotes + 1 #To store total number of votes
        #candidates.append(row[2])
        k = row[2]
        v = row[0]
        if k not in CandidateVotes:     #search for the key in Candidate column. If not present create a key in dictionary
            CandidateVotes[k] = []
            CandidateVotes[k].append(v)     # include the voter ID in the list of voters for the candidate
        else:            
            CandidateVotes[k].append(v)     # include the voter ID in the list of voters for the candidate

votecount = 0

    
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"-------------------------")


filetowrite = os.path.join("","", "PollOutput.txt")
with open(filetowrite, 'w' , newline = '\n')  as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Total Votes: {TotalVotes}\n")
    textfile.write(f"-------------------------\n")


    for keys in CandidateVotes:
        #numvotes = 0
        #for values in CandidateVotes[keys]:
        #    numvotes = numvotes + 1
        #winner = keys
        votepercent = "{0:.3%}".format(len(CandidateVotes[keys])/TotalVotes)
        if votecount <= len(CandidateVotes[keys]):              # TO find the key which has the highest length(ie most votes)
            votecount = len(CandidateVotes[keys])
            winner = keys
        print(f"{keys} {votepercent} {len(CandidateVotes[keys])}")
        textfile.write(f"{keys} {votepercent}  {len(CandidateVotes[keys])}\n")

        #print(len(CandidateVotes[key]))
    textfile.write(f"-------------------------\n")    
    textfile.write(f"Winner: {winner}\n")
    textfile.write(f"-------------------------\n")
print(f"-------------------------\n")
print(f"Winner: {winner}")
print(f"-------------------------\n")




