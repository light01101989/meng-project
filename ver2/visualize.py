import numpy as np
import matplotlib.pyplot as plt
from colour import Color
import pdb

def visualize(voteHist):
    # color dictionary
    #pdb.set_trace()
    color = {}
    allAnsList = voteHist[-1][-1]
    for i in allAnsList:
        color[i] = (tuple(np.random.rand(3)))

    # Plot all the upvotes
    for vote in voteHist:
        markerline, stemlines, baseline = plt.stem(len(vote[1])-np.random.rand(1),[0.5])
        plt.setp(markerline, markerfacecolor=color[vote[0]])
        plt.setp(stemlines, color=color[vote[0]])

    markerline, stemlines, baseline = plt.stem(allAnsList,np.ones_like(allAnsList))
    plt.setp(stemlines, color='k')
    plt.setp(markerline, 'markerfacecolor', 'b')
    plt.setp(baseline, 'color', 'r', 'linewidth', 2)
    plt.xlim([allAnsList[0]-1,allAnsList[-1]+2])
    plt.ylim([-1,2])
    plt.show()

def visualizeScat(voteHist):
    np.random.seed(11)
    # color dictionary
    color = {}
    allAnsList = voteHist[-1][-1]

    for i in allAnsList:
        color[i] = (tuple(np.random.rand(3)))
        # Plot a stem for each answer
        markerline, stemlines, baseline = plt.stem([i+1],[allAnsList[i]+1], '-s', label='Answer: %d' % (i+1))
        plt.setp(stemlines, color=color[i])
        plt.setp(baseline, 'color', 'r', 'linewidth', 9)

    legend = plt.legend(loc='upper left')
    # Set limit on x axis
    plt.xlim([allAnsList[0],allAnsList[-1]+2])
    plt.ylim([allAnsList[0],allAnsList[-1]+2])

    # Plot all the upvotes
    for vote in voteHist:
        plt.scatter(len(vote[1])+np.random.rand(1),[vote[0]+1],c=color[vote[0]])

    plt.xlabel("Events", size=10, style='italic')
    plt.ylabel("Answers", size=10, style='italic')
    plt.title("Timeline of UpVote events")

    plt.grid('on')
    plt.show()

def barPlot(estTheta):
    # Find the min
    estThetaArr = np.array(estTheta)
    estThetaArr -= estThetaArr.min()
    plt.bar(np.array(xrange(len(estThetaArr)))+0.6, estThetaArr)
    plt.show()

def testVisualize():
    voteHist = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
    voteHist1 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
    #visualize(voteHist1)
    visualizeScat(voteHist)
    estTheta = [ 0.8755336,  -0.48721896,  0.18306973,  0.64801148, -0.78567085, -0.43377995]
    barPlot(estTheta)

