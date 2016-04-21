#!usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import pdb

# NOTE: Need to call from datasets/<xyz>/ directory
def user_histogram():
    # open file to read
    u = open('final-Users.csv', 'r')

    # make array of upvotes
    upvotes = []
    # line --> Userid:displayname:Reputation:UpVotes:DownVotes
    for line in u:
        lspl = line.split(':')
        if len(lspl) < 5:
            print lspl
            continue
        temp = int(lspl[3])
        #if temp<100:
        #    continue
        upvotes.append(int(lspl[3]))

    numUsers = len(upvotes)
    print numUsers
    upvotes = np.array(upvotes)

    # do histogram
    #n,bins,patch = plt.hist(upvotes,bins=[100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2300,2600,2900,3200,3500,3800,4100,4400,4700,5000,5300,5900,6500,7100,7700,8300,8900,9500])
    n,bins,patch = plt.hist(upvotes,bins=[0,10,20,30,40,50,60,70,80,90,100],cumulative=True,normed=False,orientation='vertical')
    #n,bins = np.histogram(upvotes,bins=[0,10,20,30,40,50,60,70,80,90,100,upvotes.max()])
    print n
    print bins
    #cumper = (np.cumsum(n)/float(numUsers))*100
    cumper = (n/float(numUsers))*100
    print cumper
    for i in xrange(cumper.size):
        plt.annotate('%.2f'%cumper[i], xy=(bins[i]+1,n[i]))
    #plt.bar(bins[1:12], cumper,log=True)
    # plot
    plt.xlabel("Number of upvotes", size=10, style='italic')
    plt.ylabel("Number of Users", size=10, style='italic')
    plt.title("Cumulative Histogram of Users vs number of upvotes\nNumbers above bars are % of users below right edge of bar")
    plt.style.use('ggplot')
    plt.show()

def post_byuser_hist():
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
    k=0
    status = 5000000
    orphan_postcnt = 0
    for line in p:
        if k > status:
            print "..."
            status += 5000000
        lspl = line.split(',')
        if len(lspl) < 8:
            print lspl
            continue
        try:
            temp = int(lspl[2])
        except ValueError:
            orphan_postcnt += 1
            continue
        ptype = lspl[1]
        if temp in user_pcnt:
            user_pcnt[temp] += 1
            if ptype == '2':
                user_acnt[temp] += 1
            if ptype == '1':
                user_qcnt[temp] += 1
        k += 1

    # do histogram
    #n,bins,patch = plt.hist(user_pcnt.values(),bins=[0,5,10,15,20,25,30,40,50,60,70,80,90,100],cumulative=True,normed=False,orientation='vertical')
    #n,bins,patch = plt.hist(user_acnt.values(),bins=[0,5,10,15,20,25,30,40,50,60,70,80,90,100],cumulative=True,normed=False,orientation='vertical',color='r')
    n,bins,patch = plt.hist(user_qcnt.values(),bins=[0,5,10,15,20,25,30,40,50,60,70,80,90,100],cumulative=True,normed=False,orientation='vertical',color='g')

    numUsers = len(user_pcnt.keys())

    print "Orphan post count:: %d" % orphan_postcnt
    #print n
    #print bins
    print "Number of Users:: %d" % numUsers

    #cumper = (np.cumsum(n)/float(numUsers))*100
    cumper = (n/float(numUsers))*100
    #print cumper

    for i in xrange(cumper.size):
        plt.annotate('%.2f'%cumper[i], xy=((bins[i]+bins[i+1])/2-1,n[i]/2),rotation='vertical')

    # plot
    plt.xlabel("Number of Questions", size=12, style='italic')
    plt.ylabel("Number of Users", size=12, style='italic')
    plt.title("Cumulative Histogram of Users vs number of Questions\nNumbers above bars are % of users below right edge of bar")
    plt.style.use('ggplot')
    plt.show()

#user_histogram()
post_byuser_hist()
