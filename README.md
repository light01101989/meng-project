# Master of Engineering project at Cornell.
## Title: Automatic Assessment Generation via Machine Learning using StackOverflow Dataset.

### Description of Main scripts present in ver2 folder

1. **check_grad.py**       ==>        script to check the gradient
2. **preprocess.py**       ==>        Important script: preprocess the data and structure it into following form for each question-
  * voteHist = [[0, [0, 1, 2, 3]], [0, [0, 1, 2, 3, 4]], [2, [0, 1, 2, 3]], [5, [0, 1, 2, 3, 4, 5]]]
3. **simulation.py**       ==>        Main script to solve for theta parameters(contains all the optimization functions)
4. **runTestSim.py**       ==>        Just a test script to run a test case from simulation and visualize
5. **visualize.py**        ==>        Contains implementation of all visualization functions
6. **runModelSim.py**      ==>        A test script which takes a particular voteHist and solve it with runModel in simulation script and visualizes data and output

### Dataset
