import simulation
import numpy as np
import pickle
from scipy import optimize
import argparse

# Run here
parser = argparse.ArgumentParser(description='Script to load dataStructures and perform optimization using gradient descent. Need to call from datasets/<xyz>/ directory')
parser.add_argument('-l','--lbfgs', help='Flag to use fmin_l_bfgs_b for optimization', required=False,action='store_true')
parser.add_argument('-a','--adagrad', help='Flag to use adagrad for optimization', required=False,action='store_true')
parser.add_argument('-c','--checkgrad', help='Flag to use check gradient', required=False,action='store_true')
args = parser.parse_args()

if args.lbfgs or args.adagrad or args.checkgrad:
    # Load data structures
    f1 = open('dataStructures/uaidx.pkl','rb')
    uaidx = pickle.load(f1)
    f1.close()
    f1 = open('dataStructures/qaidx.pkl','rb')
    qaidx = pickle.load(f1)
    f1.close()
    f1 = open('dataStructures/uphiidx.pkl','rb')
    uphiidx = pickle.load(f1)
    f1.close()
    f1 = open('dataStructures/qvHist.pkl','rb')
    qvHist = pickle.load(f1)
    f1.close()
    f1 = open('dataStructures/numParameters.pkl','rb')
    numPar = pickle.load(f1)
    f1.close()

    #initialVal = np.ones(numPar)*0.1
    np.random.seed(1)
    initialVal = np.random.randn(numPar)*0.1

# Run model
if args.lbfgs:
    print "Running LBFGS..."
    sol, f, d = optimize.fmin_l_bfgs_b(simulation.objFuncUser, initialVal, args=(uaidx, qaidx, uphiidx, qvHist), disp=0)
    #print sol

    f1 = open("sol_bfgs_randinit.pkl", 'wb')
    pickle.dump(sol,f1)
    f1.close()

if args.adagrad:
    print "Running AdaGrad..."
    sol = simulation.adaGradUser(initialVal, uaidx, qaidx, uphiidx, qvHist)
    print sol
    f1 = open("sol_adagrad_randinit.pkl", 'wb')
    pickle.dump(sol,f1)
    f1.close()

if args.checkgrad:
    # Check Grad
    print "Gradient Delta: ",optimize.check_grad(simulation.objFuncUser,simulation.objFuncUserGrad,np.random.randn(numPar),uaidx, qaidx, uphiidx, qvHist)

# Formatted Output
if args.lbfgs or args.adagrad:
# Dump learned user paramter with user ids
    #f1 = open('sol_bfgs_randinit.pkl','rb')
    #sol = pickle.load(f1)
    #f1.close()

    ufile = open('filterFiles/filterUsers.csv', 'r')
    ffile = open('filterFiles/filterFlags.txt', 'r')
    p = ffile.readline().split(':')[1].rstrip()
    u = ffile.readline().split(':')[1].rstrip()
    outfile = open("user_solved_p"+p+"u"+u+".csv", 'wb')

    # Header
    outfile.write("id,name,Reputation,UpVotes,DownVotes,ModelScore\n")

    for user in ufile:
        uid = user.split(':')
        uid[-1] = uid[-1].strip()
        uid.append(str(sol[uphiidx[uid[0]]])+'\n')

        dump = ','.join(uid)
        outfile.write(dump)
        ## Get list for Userid:displayname:Reputation:UpVotes:DownVotes
        #np.savetxt(outfile, dump, header="id,name,Reputation,UpVotes,DownVotes,ModelScore", comments='', delimiter = ',')

    fakeuser = "-2:Fake:0:0:0\n"
    uid = fakeuser.split(':')
    uid[-1] = uid[-1].strip()
    uid.append(str(sol[uphiidx[uid[0]]])+'\n')

    dump = ','.join(uid)
    outfile.write(dump)

    outfile.close()
    ufile.close()
    ffile.close()

