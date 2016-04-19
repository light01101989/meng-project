import simulation
import visualize
import numpy as np
import matplotlib.pyplot as plt

simulation.runTestUser(50)
# Ktau plot for User(Phi) with number of users
#N=200
#kTau = np.zeros(N)
#for i in xrange(N):
#    print i
#    kTau[i] = simulation.runTestUser(i+1)
#plt.plot(range(1, N+1),kTau, 'b')
#plt.title('KendallTau')
#plt.xlabel('Number of clicks(N)')
#plt.savefig('KTau-User.png')
#plt.show()
#simulation.runTest()
#visualize.testVisualize()
