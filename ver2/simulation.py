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
    #voteHist = args[0]     # FIXME when called by check_grad/adaGrad
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
    #return out             # FIXME when called by check_grad

# Takes in voteHistory
# Returns both function value and gradient
# FIXME:Same as above(because of args issue)
def objFunc2Ada(thetaVec, *args):
    voteHist = args[0]     # FIXME when called by check_grad/adaGrad
    #voteHist = args         # when called by fmin_l_bfgs_b
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
    #return out             # FIXME when called by check_grad

# Written just for check_grad
def objFunc2Grad(thetaVec, *args):
    voteHist = args[0]       # when called by check_grad
    #voteHist = args         # when called by fmin_l_bfgs_b
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
    p3 = logsumexp(thetaVec[curVote[1]])
    return -p1+p3

# Main function
def objFunc2CoreGrad(thetaVec, curVote):
    tmp = np.zeros_like(thetaVec)
    tmp[curVote[0]] = 1
    p1 = tmp
    #curTheta = thetaVec[0:curVote[1].size]
    curTheta = thetaVec[curVote[1]]
    p3 =  np.zeros_like(thetaVec)
    p3[curVote[1]] = np.exp(curTheta)/np.sum(np.exp(curTheta))
    return -p1+p3

def adaGrad(initialGuess, voteHist):
    initialLR = 0.5
    accumGrad = np.zeros_like(initialGuess)
    bound = 0.00001
    funcVal, grad = objFunc2Ada(initialGuess, voteHist)
    out = initialGuess
    cnt = 0
    # while not converged
    while np.linalg.norm(grad) > bound:
        funcVal, grad = objFunc2Ada(out, voteHist)
        accumGrad += np.square(grad)
        adjGrad = grad/np.sqrt(accumGrad)
        out = out - initialLR*adjGrad
        cnt += 1
    print "numIteration: ",cnt
    return out

##########################################################################
## Objective function with User parameter also included                 ##
##########################################################################
def genHist(N, cDist):
    np.random.seed(110)
    vote = np.array([])
    # Generate a bunch of clickers(users choices)
    for i in range(N):
        cvote = np.random.rand(1)
        vote = np.append(vote,cvote)
        dvote = np.digitize(vote, cDist)
        #voteHist = [[v,np.ones_like(Theta)] for v in dvote]
        voteHist = [[v,list(xrange(cDist.size))] for v in dvote]

    return voteHist

def objFuncUser(thetaVec, *args):
    # get from args
    uaidx = args[0]
    qaidx = args[1]
    uphiidx = args[2]
    qvHist = args[3]

    grad = np.zeros_like(thetaVec)

    # get term 1: P(clicks|theta)
    t1 = 0
    for key in qvHist:
        t1o, t1g = term1(thetaVec[qaidx[key]], qvHist[key])
        #t1 += term1(thetaVec[qaidx[key]], qvHist[key])
        t1 += t1o
        grad[qaidx[key]] += t1g

    # get term 2: P(theta|Phi)
    # get term 3: P(Phi)
    # FIXME: Does sigma/constant matter?
    t2 = 0
    t3 = 0
    for key in uaidx:
        t2 += np.sum(np.square(thetaVec[uaidx[key]] - thetaVec[uphiidx[key]]))
        grad[uaidx[key]] += 2*(thetaVec[uaidx[key]] - thetaVec[uphiidx[key]])
        grad[uphiidx[key]] += np.sum(-2*(thetaVec[uaidx[key]] - thetaVec[uphiidx[key]]))
        t3 += np.square(thetaVec[uphiidx[key]])
        grad[uphiidx[key]] += 2*thetaVec[uphiidx[key]]

    # Final output
    out = t1+t2+t3
    return out,grad
    #return out

# Just for check grad
def objFuncUserGrad(thetaVec, *args):
    # get from args
    uaidx = args[0]
    qaidx = args[1]
    uphiidx = args[2]
    qvHist = args[3]

    grad = np.zeros_like(thetaVec)

    # get term 1: P(clicks|theta)
    t1 = 0
    #t1grad = 0
    for key in qvHist:
        t1o, t1g = term1(thetaVec[qaidx[key]], qvHist[key])
        #t1 += term1(thetaVec[qaidx[key]], qvHist[key])
        t1 += t1o
        grad[qaidx[key]] += t1g

    # get term 2: P(theta|Phi)
    # get term 3: P(Phi)
    # FIXME: Does sigma/constant matter?
    t2 = 0
    t3 = 0
    for key in uaidx:
        t2 += np.sum(np.square(thetaVec[uaidx[key]] - thetaVec[uphiidx[key]]))
        grad[uaidx[key]] += 2*(thetaVec[uaidx[key]] - thetaVec[uphiidx[key]])
        grad[uphiidx[key]] += np.sum(-2*(thetaVec[uaidx[key]] - thetaVec[uphiidx[key]]))
        t3 += np.square(thetaVec[uphiidx[key]])
        grad[uphiidx[key]] += 2*thetaVec[uphiidx[key]]

    # Final output
    #print t1+t2+t3
    out = t1+t2+t3
    return grad

def term1(thetaVec, *args):
    voteHist = args[0]
    out = 0
    grad = np.zeros_like(thetaVec)
    for i in range(len(voteHist)):
        out += objFunc2Core(thetaVec, voteHist[i])
        grad += objFunc2CoreGrad(thetaVec, voteHist[i])

    return out,grad

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
    #print sol
    #sol2 = adaGrad(initialVal, voteHist)
    #print sol2
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

def runTestUser(N):
    sd = 110
    np.random.seed(sd)
    # Generate sample Phi's which tells the relative goodness of users
    # Suppose there are 10 users
    nUser = 10
    Phi = np.random.randn(nUser)

    # convert it to probability density function
    # pDensity
    pDens = np.exp(Phi)/np.sum(np.exp(Phi))
    cDist = np.cumsum(pDens)
    #aNum = np.ones(nUser)
    #aNum[0] = 0
    #aNum = np.cumsum(aNum)
    #plt.bar(aNum, pDens)
    #plt.plot(aNum, cDist)
    #plt.title('PDensityF/CDistributionF')
    #print "Close the figure to run simulation"
    #plt.savefig('PDF-sd%d.png'%sd)
    #plt.show()

    # Generate sample Theta's which tells the relative goodness of answers
    # Suppose every user has generated 10 answers
    numAnsPuser = 10
    Theta = np.zeros((nUser,numAnsPuser))
    for i in range(nUser):
        Theta[i,:] = np.random.randn(numAnsPuser)

    Theta = Theta + Phi[np.newaxis].T

    #N = 200     # num of clicks

    # Prepare data structure to pass to objFuncUser
    totalAns = numAnsPuser*nUser
    qaidx = {}
    uaidx = {}
    qvHist = {}
    uphiidx = {}
    numQues = 10
    numAnsPques = 10
    #pdb.set_trace()
    for i in xrange(numQues):
        qaidx[i] = []
        qvHist[i] = []

    for i in xrange(nUser):
        uaidx[i] = []
        uphiidx[i] = totalAns+i

    for i in xrange(totalAns):
        qaidx[np.floor(i/numAnsPques)].append(i)
        uaidx[i%numAnsPques].append(i)

    print "qaidx",qaidx
    print "uaidx",uaidx
    print "uphiidx",uphiidx
    # generate clicks for each ques
    for i in xrange(numQues):
        pDens = np.exp(Theta[:,i])/np.sum(np.exp(Theta[:,i]))
        cDist = np.cumsum(pDens)
        qvHist[i] = genHist(N, cDist)

    print "qvHist",qvHist

    # optimize
    initialVal = np.ones(totalAns+nUser)*0.1
    #print "Error with User:"
    #print optimize.check_grad(objFuncUser,objFuncUserGrad,np.random.randn(totalAns+nUser),uaidx, qaidx, uphiidx, qvHist)
    #sol, f, d = optimize.fmin_l_bfgs_b(objFuncUser, initialVal, approx_grad=1, args=(uaidx, qaidx, uphiidx, qvHist), disp=1)
    sol, f, d = optimize.fmin_l_bfgs_b(objFuncUser, initialVal, args=(uaidx, qaidx, uphiidx, qvHist), disp=0)

    #print Phi
    #print sol
    #print kendalltau(Phi,sol[100:110])
    return kendalltau(Phi,sol[100:110])[0]
