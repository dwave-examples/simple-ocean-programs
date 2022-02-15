from dwave.system import EmbeddingComposite, FixedEmbeddingComposite, DWaveSampler

import random

#h = {}
#J = {('A','K'): -0.5,
#    ('B','C'): -0.5, 
#    ('A','C'): 0.5}

h = {1: 0.2,
    2: -0.2}
J = {(1,2): -0.5,
    (3,4): -0.5, 
    (1,4): 0.5}    

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J,
                                 num_reads = 10,
                                 label='Example - Simple Ocean Programs: Ising')
print(sampleset)

# test alteration
