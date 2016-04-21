#!usr/bin/python
import subprocess
import pprint
import numpy as np
import matplotlib.pyplot as plt
import operator
from datetime import datetime
import os
from os.path import expanduser
import pdb

# NOTE: Need to call from datasets/<xyz>/ directory
#Parsing the xml file
def get_list(cmd):
    #p = subprocess.Popen(['./get-post-owner-user-id.sh'], shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
    #byte_output = p.communicate()[0]

    byte_output = subprocess.check_output(cmd)
    #print(byte_output)
    out_list = byte_output.decode('ascii','ignore').split('\n')
    out_list.remove('')
    return out_list

def prune_attributes(filename,outname,ftype):
    pflag = 0   # Flag to enable verbose printing
    newFiles = 0    # Flag to read from new cleaned up files

    scriptPath = os.path.dirname(os.path.realpath(__file__)) + '/../scripts/'
    if ftype=='post':
        ## Get list for postid:post_type:ownerid:parentid(onlyforans):score:AcceptedAnswerId:CreationDate:CAnswerCount
        alist = get_list([scriptPath + 'get-post-attrib.sh', filename])

        if pflag == 1:
            print(alist)

    if ftype=='user':
        ## Get list for Userid:displayname:Reputation:UpVotes:DownVotes
        if newFiles == 1:
            alist = get_list([scriptPath + 'get-newuser-upvotes.sh', filename])
        else:
            alist = get_list([scriptPath + 'get-user-upvotes.sh', filename])
        ## Insert a Dummy user with Id '-2'
        #alist.append('-2:Dummy:0')
        if pflag == 1:
            print(alist)

    ### Get list for VoteId:PostId:VoteTypeId:CreationDate
    #if lappy == 1:
    #    if newFiles == 1:
    #        vlist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-newuser-id-name.sh')
    #        print "change file"
    #    else:
    #        vlist = get_list('/home/arjun/Desktop/Cornell_courses/mengproject/scripts/get-vote-full.sh')
    #else:
    #    if newFiles == 1:
    #        vlist = get_list('/home/molnargroup/Music/project/scripts/get-newuser-id-name.sh')
    #        print "change file"
    #    else:
    #        vlist = get_list('/home/molnargroup/Music/project/scripts/get-user-id-name.sh')
    #        print "change file"

    #print "Data Loaded!!!"
    #print "Processing..."

    # Open new files for writing
    if outname != None:
        fname = outname
        wu = open(fname, 'a')
    else:
        fname = 'prune-'+ filename + '.csv'
        wu = open(fname, 'w')
    for i in xrange(len(alist)):
        wu.write(alist[i])
        wu.write('\n')

    return fname
