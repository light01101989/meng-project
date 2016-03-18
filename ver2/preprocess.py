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

#Parsing the xml file
def get_list(cmd):
    #p = subprocess.Popen(['./get-post-owner-user-id.sh'], shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
    #byte_output = p.communicate()[0]
    
    byte_output = subprocess.check_output([cmd])
    #print(byte_output)
    out_list = byte_output.decode('ascii','ignore').split('\n')
    out_list.remove('')
    return out_list

lappy = 1
pflag = 0   # Flag to enable verbose printing
newFiles = 0    # Flag to read from new cleaned up files

## Get list for postid:post_type:ownerid:parentid(onlyforans):score:AcceptedAnswerId
if lappy == 1:
    if newFiles == 1:
        plist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-newpost-owner-user-id.sh')
    else:
        plist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-post-owner-user-id.sh')
else:
    if newFiles == 1:
        plist = get_list('/home/molnargroup/Music/project/scripts/get-newpost-owner-user-id.sh')
    else:
        plist = get_list('/home/molnargroup/Music/project/scripts/get-post-owner-user-id.sh')
## Remove all the owner less posts
for i in range(len(plist)):
    temp = plist[i].split(':')
    if temp[2] == '':
        temp[2] = '-2'
        inback = ':'.join(temp)
        plist[i] = inback

pdb.set_trace()
if pflag == 1:
    print(plist)

## Get list for Userid:displayname:Reputation
if lappy == 1:
    if newFiles == 1:
        ulist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-newuser-id-name.sh')
    else:
        ulist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-user-id-name.sh')
else:
    if newFiles == 1:
        ulist = get_list('/home/molnargroup/Music/project/scripts/get-newuser-id-name.sh')
    else:
        ulist = get_list('/home/molnargroup/Music/project/scripts/get-user-id-name.sh')
## Insert a Dummy user with Id '-2'
ulist.append('-2:Dummy:0')
if pflag == 1:
    print(ulist)
udict = {v.split(':')[0]:v.split(':')[1] for v in ulist}
Unq = {v.split(':')[0]:0 for v in ulist}
Una = {v.split(':')[0]:0 for v in ulist}

## Get list for VoteId:PostId:VoteTypeId:CreationDate
if lappy == 1:
    if newFiles == 1:
        vlist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-newuser-id-name.sh')
        print "change file"
    else:
        vlist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-vote-full.sh')
else:
    if newFiles == 1:
        vlist = get_list('/home/molnargroup/Music/project/scripts/get-newuser-id-name.sh')
        print "change file"
    else:
        vlist = get_list('/home/molnargroup/Music/project/scripts/get-user-id-name.sh')
        print "change file"
## Creating dict for storing cumulative votes(value) for each question(key)
qcvotesdict = {}
avotesdict = {}
uqualdict = {}

f_acc = {}
Na = {}
vq = {}

qla = {}    # ques:list of answers
atc = {}    # ans:time dictionary
qlt = {}    # ques:list of answers time
qpat = {}   # Ques: previous answer time
qcl = {}    # Ques: choice list
qtcl = {}   # Ques: time, choice list
pluvt = {}  # post:list of upvote time

# create ques:list of answers dictionary --> qla
# create ans:time dictionary --> atc
# create ques:list of answers time dictionary --> qlt
# temp def: [postid,post_type(poped),ownerid,parentid,score,AcceptedAnswerId,CreationDate]
for post in plist:
    temp = post.split(':')
    post_type = temp.pop(1)
    pluvt[temp[0]] = []
    if post_type == '1':
        # question
        qla[temp[0]] = []
        qlt[temp[0]] = []
        qpat[temp[0]] = []
        qcl[temp[0]] = []
        qtcl[temp[0]] = []
    elif post_type == '2':
        ansTime = date(temp[5].split('T')[0])
        qla[temp[2]].append(temp[0])
        qlt[temp[2]].append(ansTime)
        atc[temp[0]] = ansTime
        if not qpat[temp[2]]:
            qpat[temp[2]].append(ansTime)
            qcl[temp[2]].append([0])
            ####
            newEntry = [ansTime, [0]]
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
for vote in vlist:
    temp = vote.split(',')
    # FIXME: Only upvote being considered
    if temp[2] == '2':
        if temp[1] in pluvt: 
            pluvt[temp[1]].append(date(temp[3].split('T')[0]))

pdb.set_trace()

# create observations: qobs
qobs = {}
# datastructure used are
# qtcl and pluvt, qla
for key in qla:
    qobs[key] = []
    ansNum = 0
    for ans in qla[key]:
        for evote in pluvt[ans]:
            # do binary search in qpat to find the index
            idx = np.searchsorted(qpat[key],evote,side='right')-1
            newObs = [ansNum,qcl[key][idx]]
            qobs[key].append(newObs)
        ansNum += 1

pdb.set_trace()
