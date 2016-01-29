import numpy as np
import re
def dataCleanup(validUser):
    ## Open files as read only
    p = open('Posts.xml', 'r')
    u = open('Users.xml', 'r')
    # Open new files for writing
    wp = open('newPosts.xml', 'w')
    wu = open('newUsers.xml', 'w')
    # Cleaning User file
    # Write Header
    writeHeadU(wu)
    for line in u:
        m = re.match(r'.* Id="(.*?)" .*', line)
        if m != None and int(m.group(1)) in validUser:
            # write valid lines
            wu.write(line)
    # Write Footer
    writeFootU(wu)

    # Cleaning Post file
    # Write Header
    writeHeadP(wp)
    for line in p:
        m = re.match(r'.* OwnerUserId="(.*?)" .*', line)
        if m != None and int(m.group(1)) in validUser:
            # write valid lines
            wp.write(line)
    # Write Footer
    writeFootP(wp)

    # Close all files
    p.close()
    u.close()
    wp.close()
    wu.close()

def writeHeadU(w):
    w.write('<?xml version="1.0" encoding="utf-8"?>\n<users>\n')

def writeFootU(w):
    w.write('</users>\n')

def writeHeadP(w):
    w.write('<?xml version="1.0" encoding="utf-8"?>\n<posts>\n')

def writeFootP(w):
    w.write('</posts>\n')

# Tester
#dataCleanup(np.array([1,3,5,7,9]))
