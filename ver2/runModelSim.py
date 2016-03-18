import simulation
import numpy as np
import visualize

voteHist0 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [0, [0, 1, 2, 3, 4, 5]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [2, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [3, [0, 1, 2, 3, 4, 5]], [4, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
visualize.visualizeScat(voteHist0)
visualize.barPlot(simulation.runModel(voteHist0,6))
voteHist1 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
visualize.visualizeScat(voteHist1)
visualize.barPlot(simulation.runModel(voteHist1,6))
voteHist2 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]
voteHist3 = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [0, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3]], [1, [0, 1, 2, 3, 4]], [1, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [3, [0, 1, 2, 3, 4]], [4, [0, 1, 2, 3, 4]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]], [5, [0, 1, 2, 3, 4, 5]]]

print simulation.runModel(voteHist0,6)
print simulation.runModel(voteHist1,6)
print simulation.runModel(voteHist2,6)
print simulation.runModel(voteHist3,6)