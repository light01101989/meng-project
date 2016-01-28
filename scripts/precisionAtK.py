import numpy as np
import math

def precisionAtK(rank1, rank2, numBins):
    binSize = rank1.size/numBins;

    precision = []
    cutOffList = []
    for i in range(numBins):
        cutOff = math.floor((i+1)*binSize);
        cutOffList.append(cutOff)
        #print(cutOff)

        # take first cutOff elements from both rank arrays
        subRank1 = rank1[np.arange(cutOff)]
        subRank2 = rank2[np.arange(cutOff)]
        # sort rank2
        sortedSubRank2 = np.sort(subRank2, kind='mergesort')
        # do cutOff number of binary searches in rank2 from elements in rank1
        match = 0
        for uId in subRank1:
            if binarySearch(uId, sortedSubRank2):
                # increment counter
                match += 1

        # number of match divided by cutOff is precisionAtK
        precision.append(match/cutOff)

    return (precision, cutOffList)


def binarySearch(uId, sortedSubRank2):
    idx = np.searchsorted(sortedSubRank2, uId)
    if idx != sortedSubRank2.size and uId == sortedSubRank2[idx]:
        # match found
        return True
    else:
        return False
