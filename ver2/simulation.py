import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import logsumexp
from scipy import optimize
from scipy.stats import kendalltau
import pdb

# Takes in cumulative voteCount at the end
def objFunc(thetaVec, *args):
    voteCount = args
    p1 = np.sum(voteCount*thetaVec)
    p2 = np.sum(np.square(thetaVec))
    p3 = np.sum(voteCount)*logsumexp(thetaVec)
    out = -p1+p2+p3
    return out

# Takes in voteHistory
# Returns both function value and gradient
def objFunc2(thetaVec, *args):
    #voteHist = args[0]     # FIXME when called by check_grad
    voteHist = args         # when called by fmin_l_bfgs_b
    out = 0
    grad = np.zeros_like(thetaVec)
    for i in range(len(voteHist)):
        out += objFunc2Core(thetaVec, voteHist[i])
        grad += objFunc2CoreGrad(thetaVec, voteHist[i])

    p2 = np.sum(np.square(thetaVec))
    p2g = 2*thetaVec
    out = out+p2
    grad = grad+p2g
    return out,grad
    #print "out",out
    #return out

# Written just for check_grad
def objFunc2Grad(thetaVec, *args):
    #voteHist = args[0]     # when called by check_grad
    voteHist = args         # when called by fmin_l_bfgs_b
    out = 0
    grad = np.zeros_like(thetaVec)
    for i in range(len(voteHist)):
        out += objFunc2Core(thetaVec, voteHist[i])
        grad += objFunc2CoreGrad(thetaVec, voteHist[i])

    p2 = np.sum(np.square(thetaVec))
    p2g = 2*thetaVec
    out = out+p2
    grad = grad+p2g
    #print "grad", grad
    return grad

# Main function
def objFunc2Core(thetaVec, curVote):
    tmp = np.zeros_like(thetaVec)
    tmp[curVote[0]] = 1
    p1 = np.sum(tmp*thetaVec)
    #p3 = logsumexp(thetaVec[0:curVote[1].size])
    p3 = logsumexp(thetaVec[0:len(curVote[1])])
    return -p1+p3

# Main function
def objFunc2CoreGrad(thetaVec, curVote):
    tmp = np.zeros_like(thetaVec)
    tmp[curVote[0]] = 1
    p1 = tmp
    #curTheta = thetaVec[0:curVote[1].size]
    curTheta = thetaVec[0:len(curVote[1])]
    p3 =  np.zeros_like(thetaVec)
    p3[curVote[1]] = np.exp(curTheta)/np.sum(np.exp(curTheta))
    return -p1+p3

# Simulate N new clicks from every iteration
def simulateClicks(N, cDist):
    # Generate a bunch of clickers(users choices)
    vote = np.random.rand(N)
    vote = np.digitize(vote, cDist)
    voteCount = np.histogram(vote, bins=cDist.size, range=(0,cDist.size))[0]
    #print "Votes for each answer:"
    #print voteCount
    
    # Optimization
    initialVal = np.ones(10)*0.1
    #initialVal = np.random.randn(10)
    sol, f, d = optimize.fmin_l_bfgs_b(objFunc, initialVal, approx_grad=1, args=(voteCount), disp=0)
    #print "Solution:", sol
    return sol

# Generate one new click and append to previous N-1 clicks to form N clicks
def simulateClicks2(N, cDist, Theta):
    np.random.seed(110)
    vote = np.array([])
    kTau = np.zeros(N)
    # Generate a bunch of clickers(users choices)
    for i in range(N):
        cvote = np.random.rand(1)
        vote = np.append(vote,cvote)
        dvote = np.digitize(vote, cDist)
        voteCount = np.histogram(dvote, bins=cDist.size, range=(0,cDist.size))[0]
        #print "Votes for each answer:"
        #print voteCount
        
        # Optimization
        initialVal = np.ones(10)*0.1
        #initialVal = np.random.randn(10)
        sol, f, d = optimize.fmin_l_bfgs_b(objFunc, initialVal, approx_grad=1, args=(voteCount), disp=0)
        kTau[i] = kendalltau(Theta, sol)[0]
    return kTau

def simClicksTime(N, cDist, Theta):
    np.random.seed(110)
    vote = np.array([])
    kTau = np.zeros(N)
    # Generate a bunch of clickers(users choices)
    for i in range(N):
        cvote = np.random.rand(1)
        vote = np.append(vote,cvote)
        dvote = np.digitize(vote, cDist)
        #voteHist = [[v,np.ones_like(Theta)] for v in dvote]
        voteHist = [[v,list(xrange(Theta.size))] for v in dvote]

        # Optimization
        initialVal = np.ones(10)*0.1
        #initialVal = np.random.randn(10)
        #print optimize.check_grad(objFunc2,objFunc2Grad,np.random.randn(10),voteHist)
        #sol, f, d = optimize.fmin_l_bfgs_b(objFunc2, initialVal, approx_grad=1, args=(voteHist), disp=0)
        sol, f, d = optimize.fmin_l_bfgs_b(objFunc2, initialVal, args=(voteHist), disp=0)
        kTau[i] = kendalltau(Theta, sol)[0]
    return kTau

def runModel(voteHist,numAns):
    initialVal = np.ones(numAns)*0.1
    #initialVal = np.random.randn(numAns)
    # Optimization
    sol, f, d = optimize.fmin_l_bfgs_b(objFunc2, initialVal, args=voteHist, disp=0)
    return sol

def runTest():
    sd = 110
    np.random.seed(sd)
    # Generate sample Theta's which tells the relative goodness of answers
    # Suppose there are 10 answers
    Theta = np.random.randn(10)
    
    # pDensity
    pDens = np.exp(Theta)/np.sum(np.exp(Theta))
    cDist = np.cumsum(pDens)
    aNum = np.ones(10)
    aNum[0] = 0
    aNum = np.cumsum(aNum)
    plt.bar(aNum, pDens)
    plt.plot(aNum, cDist)
    plt.title('PDensityF/CDistributionF')
    print "Close the figure to run simulation"
    plt.savefig('PDF-sd%d.png'%sd)
    plt.show()
    
    N = 200
    kTau = np.zeros(N)
    for i in range(N):
        ThetaEst = simulateClicks(i+1, cDist)
        kTau[i] = kendalltau(Theta, ThetaEst)[0]
    
    kTau2 = simulateClicks2(N, cDist, Theta)
    kTau3 = simClicksTime(N, cDist, Theta)
    plt.plot(range(1, N+1),kTau, 'b')
    plt.plot(range(1, N+1),kTau2,'k')
    plt.plot(range(1, N+1),kTau3,'r')
    plt.title('KendallTau')
    plt.xlabel('Number of clicks(N)')
    plt.savefig('KTau-sd%d.png'%sd)
    plt.show()
