#!usr/bin/python
import subprocess
import pprint
import numpy as np
import matplotlib.pyplot as plt
import operator
from datetime import datetime
import pdb

# Create date datatype
def date(token):
    return datetime.strptime(token, "%Y-%m-%d")

# open file to read
pfile = open('filterPosts.csv', 'r')
ufile = open('filterUsers.csv', 'r')
vfile = open('final-Votes.csv', 'r')

print "Data Loaded!!!"
print "Processing..."

qla = {}    # ques:list of answers
atc = {}    # ans:time dictionary(not used)
qlt = {}    # ques:list of answers time(not used)
qpat = {}   # Ques: previous answer time
qcl = {}    # Ques: choice list
qtcl = {}   # Ques: time, choice list(not used)
pluvt = {}  # post:list of upvote time
pldvt = {}  # post:list of downvote time

# create ques:list of answers dictionary --> qla
# create ans:time dictionary --> atc
# create ques:list of answers time dictionary --> qlt
# temp def: [postid,post_type(poped),ownerid,parentid,score,AcceptedAnswerId,CreationDate,CAnswerCount]
for post in pfile:
    temp = post.split(',')
    post_type = temp.pop(1)
    pluvt[temp[0]] = []
    pldvt[temp[0]] = []
    if post_type == '1':
        # question
        qla[temp[0]] = []
        qlt[temp[0]] = []
        qpat[temp[0]] = []
        qcl[temp[0]] = []
        qtcl[temp[0]] = []
    elif post_type == '2':
        ansTime = date(temp[5].split('T')[0])
        if temp[2] not in qla:
            continue
        qla[temp[2]].append(temp[0])
        qlt[temp[2]].append(ansTime)
        atc[temp[0]] = ansTime
        if not qpat[temp[2]]:
            qpat[temp[2]].append(ansTime)
            # 0 is for fake answer(DownVote)
            qcl[temp[2]].append([0, 1])
            ####
            newEntry = [ansTime, [0, 1]]
            qtcl[temp[2]].append(newEntry)
        else:
            if qpat[temp[2]][-1] == ansTime:
                # one more answer at same date
                # no update in qpat
                # qcl just add one more choice in the same list
                pc = qcl[temp[2]][-1][-1]
                qcl[temp[2]][-1].append(pc+1)
                ####
                pc = qtcl[temp[2]][-1][1][-1]
                qtcl[temp[2]][-1][1].append(pc+1)
            else:
                # update time
                # append new list of choices
                qpat[temp[2]].append(ansTime)
                pc = qcl[temp[2]][-1][-1]
                newList = list(xrange(0,pc+2))
                qcl[temp[2]].append(newList)
                ####
                pc = qtcl[temp[2]][-1][1][-1]
                newList = list(xrange(0,pc+2))
                newEntry = [ansTime, newList]
                qtcl[temp[2]].append(newEntry)

pdb.set_trace()
## Get list for VoteId:PostId:VoteTypeId:CreationDate
# create post:list of upvote time dictionary --> pluvt
for vote in vfile:
    temp = vote.split(',')
    # FIXME: Only upvote being considered
    if temp[2] == '2':
        if temp[1] in pluvt:
            pluvt[temp[1]].append(date(temp[3].split('T')[0]))
    if temp[2] == '3':
        # DownVote
        if temp[1] in pldvt:
            pldvt[temp[1]].append(date(temp[3].split('T')[0]))

# create observations: qobs
qobs = {}
ansFake = 0     # 0 corresponds to fake answer which
                # distuinguish between wrong and right
# datastructure used are
# qcl and pluvt, qla, qpat
maxVoteQues = 0
for key in qla:
    qobs[key] = []
    ansNum = 1
    maxAnsNum = 0
    maxUpvote = 0
    for ans in qla[key]:
        cntUpvote = 0
        # UpVote
        for evote in pluvt[ans]:
            # do binary search in qpat to find the index
            idx = np.searchsorted(qpat[key],evote,side='right')-1
            newObs = [ansNum,qcl[key][idx]]
            qobs[key].append(newObs)
            cntUpvote += 1

        # Answer with maxUpvote
        if maxUpvote < cntUpvote:
            maxUpvote = cntUpvote
            maxAnsNum = ansNum

        # DownVote
        for edvote in pldvt[ans]:
            newObs = [ansFake, [ansFake, ansNum]]
            qobs[key].append(newObs)
            #print "downvote in key ", key
        ansNum += 1

    # Print keys where last answer rocks
    #if maxAnsNum == ansNum-1 and maxAnsNum > 2:
    #    print key
    # Max
    if len(qobs[key]) > maxVoteQues:
        maxVoteQues = len(qobs[key])
        maxKey = key

pdb.set_trace()
print maxVoteQues
print maxKey
print qobs
