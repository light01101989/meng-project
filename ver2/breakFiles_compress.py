#!usr/bin/python
import subprocess
import pprint
import numpy as np
import matplotlib.pyplot as plt
import operator
from datetime import datetime
import os.path
import pdb
import prune_attributes as pa

# NOTE: Need to call from datasets/<xyz>/ directory
# Break file into parts
def breakFile(filename):
    subprocess.check_output(["awk", "BEGIN{getline f;getline ff;}NR%500000==3{x=\"FF\"++i;a[i]=x;print f>x;print ff>x}{print > x}END{for(j=1;j<i;j++)print> a[j];}" ,filename])

def compressUsers():
    # Break file into parts
    breakFile("Users.xml")

    # number of files to be parsed
    temp = subprocess.check_output(["wc", "-l" ,"Users.xml"])
    numlines = int(temp.split(" ")[0])
    numFiles = (numlines-3)/500000 + 1

    # parse each file one by one and dump
    outfile = "final-Users.csv"
    if os.path.isfile(outfile) == True:
        subprocess.check_output(["rm", outfile])
    for i in xrange(numFiles):
        filename = "FF"+ str(i+1)
        print filename
        fname = pa.prune_attributes(filename,outfile,'user')
        # combine all the files
        #subprocess.check_output(["cat", fname, ">>", "final-Users.csv"])

    print fname
    # Remove the temporary files

def compressPosts():
    # Break file into parts
    breakFile("Posts.xml")

    # number of files to be parsed
    #temp = subprocess.check_output(["wc", "-l" ,"Posts.xml"])
    #numlines = int(temp.split(" ")[0])
    # FIXME: Hardcoding to save time
    numlines = 29499662
    numFiles = (numlines-3)/500000 + 1

    # parse each file one by one and dump
    outfile = "final-Posts.csv"
    if os.path.isfile(outfile) == True:
        subprocess.check_output(["rm", outfile])
    for i in xrange(numFiles):
        filename = "FF"+ str(i+1)
        print filename
        fname = pa.prune_attributes(filename,outfile,'post')
        # combine all the files
        #subprocess.check_output(["cat", fname, ">>", "final-Users.csv"])

    print fname
    # Remove the temporary files

# Run here
compressPosts()
