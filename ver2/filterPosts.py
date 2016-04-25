#!usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import argparse
import pdb

def filterPosts(minPosts,minUsers):
    # open file to read
    p = open('final-Posts.csv', 'r')
    u = open('final-Users.csv', 'r')

    # make array of upvotes
    user_pcnt = {}
    user_acnt = {}
    user_qcnt = {}
    # line --> Userid:displayname:Reputation:UpVotes:DownVotes
    for line in u:
        lspl = line.split(':')
        if len(lspl) < 5:
            print lspl
            continue
        user_pcnt[int(lspl[0])] = 0
        user_acnt[int(lspl[0])] = 0
        user_qcnt[int(lspl[0])] = 0

    ## Get list for postid:post_type:ownerid:parentid(onlyforans):score:AcceptedAnswerId:CreationDate:CAnswerCount
    c=0
    status = 5000000
    orphan_postcnt = 0
    # First pass to get set of filtered users
    for line in p:
        if c > status:
            print "..."
            status += 5000000
        lspl = line.split(',')
        if len(lspl) < 8:
            print lspl
            continue
        try:
            oid = int(lspl[2])
        except ValueError:
            orphan_postcnt += 1
            continue
        ptype = lspl[1]
        if oid in user_pcnt:
            user_pcnt[oid] += 1
            if ptype == '2':
                user_acnt[oid] += 1
            if ptype == '1':
                user_qcnt[oid] += 1
        c += 1

    numUsers = len(user_pcnt.keys())

    # set of filtered users
    filteredUsers = set([k for (k,v) in user_pcnt.items() if v >= minPosts])

    print "Total Number of Users:: %d" % numUsers
    print "Number of filtered Users: %d" % len(filteredUsers)
    print "Orphan post count:: %d" % orphan_postcnt

    p.seek(0)
    c=0
    status = 5000000
    ## Get list for postid:post_type:ownerid:parentid(onlyforans):score:AcceptedAnswerId:CreationDate:CAnswerCount
    # Second pass to get set of filtered Questions
    qid = {}
    for line in p:
        if c > status:
            print "..."
            status += 5000000
        lspl = line.split(',')
        if len(lspl) < 8:
            print lspl
            continue
        try:
            oid = int(lspl[2])
        except ValueError:
            orphan_postcnt += 1
            continue
        ptype = lspl[1]
        pid = lspl[0]

        if ptype == '1':
            # Create entry
            qid[pid] = 0
        if ptype == '2':
            # Check if owner of answer is in filteredUsers
            if oid in filteredUsers:
                parentid = lspl[3]
                # parent might be orphan i.e. owner less parent(dont need such
                # posts
                if parentid in qid:
                    qid[parentid] += 1
        c += 1

    # set of filtered questions
    filteredQues = set([k for (k,v) in qid.items() if v >= minUsers])

    print "Total Number of Ques:: %d" % len(qid.keys())
    print "Number of filtered Ques:: %d" % len(filteredQues)

    print "Filtering Now......................"
    # Open new files for writing
    wp = open('filterPosts.csv', 'w')
    wu = open('filterUsers.csv', 'w')

    p.seek(0)
    c=0
    status = 5000000
    ## Get list for postid:post_type:ownerid:parentid(onlyforans):score:AcceptedAnswerId:CreationDate:CAnswerCount
    # Third pass to actually filter posts
    for line in p:
        if c > status:
            print "..."
            status += 5000000
        lspl = line.split(',')
        if len(lspl) < 8:
            print lspl
            continue

        ptype = lspl[1]
        pid = lspl[0]

        if ptype == '1':
            # Check id
            if pid in filteredQues:
                wp.write(line)
        if ptype == '2':
            # Check if parent id is in filteredQues
            parentid = lspl[3]
            if parentid in filteredQues:
                wp.write(line)
        c += 1

    # Filter users file
    # line --> Userid:displayname:Reputation:UpVotes:DownVotes
    u.seek(0)
    for line in u:
        lspl = line.split(':')
        if len(lspl) < 5:
            print lspl
            continue
        uid = int(lspl[0])
        if uid in filteredUsers:
            wu.write(line)

    wp.close()
    wu.close()
    p.close()
    u.close()

parser = argparse.ArgumentParser(description='Script to filter Users and Posts based on minPosts and minUsers')
parser.add_argument('-p','--minpost', help='Minimum number of post for user to qualify(inclusive)',required=True)
parser.add_argument('-u','--minuser', help='Minimum number of qualified user in a Q/A pair(inclusive)', required=True)
args = parser.parse_args()

## show values ##
#print ("minPosts: %s" % args.minpost )
#print ("minUsers: %s" % args.minuser )
filterPosts(int(args.minpost),int(args.minuser))
