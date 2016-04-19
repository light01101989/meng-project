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

user_histogram()
