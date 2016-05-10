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
parser.add_argument('-k','--kfold', help='Number of folds to train on. k=1 is special case where it just trains on one training set made up of full data.',required=True,type=int)
args = parser.parse_args()

# k-fold cross validation
k = args.kfold
for fold in xrange(k):
    d = "dataStructures_fold%d" % fold
    print "Processing " + d
    if args.lbfgs or args.adagrad or args.checkgrad:
        # Load data structures
        f1 = open(d+'/uaidx.pkl','rb')
        uaidx = pickle.load(f1)
        f1.close()
        f1 = open(d+'/qaidx.pkl','rb')
        qaidx = pickle.load(f1)
        f1.close()
        f1 = open(d+'/uphiidx.pkl','rb')
        uphiidx = pickle.load(f1)
        f1.close()
        f1 = open(d+'/qvHist.pkl','rb')
        qvHist = pickle.load(f1)
        f1.close()
        f1 = open(d+'/numParameters.pkl','rb')
        numPar = pickle.load(f1)
        f1.close()

        #initialVal = np.ones(numPar)*0.1
        np.random.seed(1)
        initialVal = np.random.randn(numPar)*0.1

    # Run model
    if args.lbfgs:
        print "Running LBFGS..."
        sol, f, infodict = optimize.fmin_l_bfgs_b(simulation.objFuncUser, initialVal, args=(uaidx, qaidx, uphiidx, qvHist), disp=0)
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
        # User to learned Phi value
        uphival = {}
        for user in uphiidx:
            uphival[user] = sol[uphiidx[user]]

        # Dump it
        f1 = open(d+"/uphival.pkl", 'wb')
        pickle.dump(uphival,f1)
        f1.close()

        # Dump learned user paramter with user ids
        ufile = open('filterFiles/filterUsers.csv', 'r')
        ffile = open('filterFiles/filterFlags.txt', 'r')
        p = ffile.readline().split(':')[1].rstrip()
        u = ffile.readline().split(':')[1].rstrip()
        outfile = open("user_solved_"+str(fold)+"_p"+p+"u"+u+".csv", 'wb')

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

