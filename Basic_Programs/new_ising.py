from dwave.system import EmbeddingComposite, FixedEmbeddingComposite, DWaveSampler

import random
import numpy as np
import os
import math as math
import dimod

#project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(project_dir)

params = np.loadtxt(open("/workspace/simple-ocean-programs/Basic_Programs/params_1.csv", "rb"), delimiter=",", skiprows=0)

d = 9
n = 1
T = 5

h = {}
for i in range(d):
    #h.add(i,params(i,n))
    h[i] = params[i,n]*T/2
gamma = {}
for i in range(d):
    #h.add(i,params(d+i,n))
    gamma[i] = T*(math.exp((params[d+i,n]**2)))
J = {}
c = 0
for i in range(d-1):
    for j in range(i+1,d-1):
        #J.add((i,j),params(d*2+c,n))
        J[(i,j)] = params[d*2+c,n]*T
        c = c + 1

#h = {1: 0.2,
#    2: -0.2}
#J = {(1,2): -0.5,
#    (3,4): -0.5, 
#    (1,4): 0.5}    

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J,
                                 num_reads = 10,
                                 label='qbm samples : MNIST')

mat = dimod.as_samples(sampleset)
mat = mat[0]

params = np.savetxt(open("/workspace/simple-ocean-programs/Basic_Programs/samples_1_1.csv", "w"), mat, delimiter=",")

print(sampleset)
print(mat)



# test alteration
