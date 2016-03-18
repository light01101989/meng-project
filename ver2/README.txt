check_grad.py       ==>>        script to check the gradient 
preprocess.py       ==>>        Important script: preprocess the data and structure it into following form for each question-
                                voteHist = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [5, [0, 1, 2, 3, 4, 5]]]
simulation.py       ==>>        Main script to solve for theta parameters(contains all the optimization functions)
runTestSim.py       ==>>        Just a test script to run a test case from simulation and visualize
visualize.py        ==>>        Contains implementation of all visualization functions
runModelSim.py      ==>>        A test script which takes a particular voteHist and solve it with runModel in simulation script and visualizes data and output
