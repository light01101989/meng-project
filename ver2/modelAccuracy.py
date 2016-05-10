#!usr/bin/python
import subprocess
import numpy as np
import pickle
import argparse
import pdb

parser = argparse.ArgumentParser(description='Script for testing/making prediction on validation set. Should be called from datasets/<xyz> directory')
parser.add_argument('-k','--kfold', help='Number of folds to run prediction. k=1 is not valid.',required=True,type=int)
args = parser.parse_args()

# Load the general dataStructures
dgen = "dataStructures_gen"
f1 = open(dgen+'/qla.pkl','rb')
qla = pickle.load(f1)
f1.close()
f1 = open(dgen+'/qvHist.pkl','rb')
qvHist = pickle.load(f1)
f1.close()
f1 = open(dgen+'/atu.pkl','rb')
atu = pickle.load(f1)
f1.close()

accuracy = {}
randaccuracy = {}
probaccuracy = {}
# Prediction
for fold in xrange(args.kfold):
    d = "dataStructures_fold%d" % fold
    print "Predicting validation set in " + d

    # Load validation set
    f1 = open(d+'/valset.pkl','rb')
    valset = pickle.load(f1)
    f1.close()

    # Load user to phival dict
    f1 = open(d+'/uphival.pkl','rb')
    uphival = pickle.load(f1)
    f1.close()

    correct = 0.0
    randcorrect = 0.0
    total = 0.0
    qAcc = {}
    for ques in valset:
        vHist = qvHist[ques]
        la = qla[ques]

        # Make corresponding user list to la
        # Insert one invalid entry for fake answer
        user = ['-10']
        for ans in la:
            user.append(atu[ans])

        philist = []
        for eachuser in user:
            if eachuser in uphival:
                philist.append(uphival[eachuser])
            else:
                philist.append(-100)
        philist = np.array(philist)

        actualcount = np.zeros(philist.shape[0])
        for eachvote in vHist:
            click = eachvote[0]
            choice = eachvote[1]

            # FIXME: Downvotes, will always get them wrong
            # therefore, not counting
            if click == 0:
                continue

            # Absolute Prediction
            if click == np.argmax(philist[choice]):
                correct += 1

            # Random prediction
            randpred = np.random.randint(0,high=philist[choice].shape[0])
            if click == randpred:
                randcorrect += 1

            # Probabilistic Prediction
            actualcount[click]+=1

            total+=1

        # Probabilistic Prediction
        predprob = np.exp(philist)/np.sum(np.exp(philist))
        predcount = np.round(np.sum(actualcount)*predprob)
        numErr = np.sum(np.abs(predcount-actualcount))
        if np.sum(actualcount) != 0:
            qAcc[ques] = 1.0 - float(numErr)/np.sum(actualcount)

    accuracy[fold] = correct/total
    print accuracy[fold]
    randaccuracy[fold] = randcorrect/total
    print randaccuracy[fold]
    probaccuracy[fold] = np.mean(np.array(qAcc.values()))
    print probaccuracy[fold]

# Final accuracy
finalAcc = np.mean(np.array(accuracy.values()))
finalRandAcc = np.mean(np.array(randaccuracy.values()))
finalProbAcc = np.mean(np.array(probaccuracy.values()))
print "Final Accuracy..."
print "Our Model: %f" % finalAcc
print "Random Prediction: %f" % finalRandAcc
print "Probabilistic Prediction: %f" % finalProbAcc


