import numpy as np

def countCumVotes(voteHist):
    cumsum = np.zeros_like(voteHist[-1][1])
    for i in xrange(len(voteHist)):
        cumsum[voteHist[i][0]] += 1
    return cumsum
