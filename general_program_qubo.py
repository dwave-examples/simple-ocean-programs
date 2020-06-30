# This program demonstrates a basic Ocean program that runs a QUBO problem on the D-Wave QPU. In this example we use Ocean's `EmbeddingComposite` to determine the best placement of our problem onto the physical hardware.

# Program Characteristics:

# - Model: QUBO
# - Sampler: D-Wave QPU with EmbeddingComposite

# This QUBO problem is formulated/developed here: https://docs.dwavesys.com/docs/latest/c_pf_3.html#social-networks-friends-and-enemies

# -------------------------------------------------------#

# First we import the functions and packages that we will use in this program.
from dwave.system import EmbeddingComposite, DWaveSampler

# Now we can define our problem as a Python dictionary.
Q = {('B','B'): 1, ('K','K'): 1, ('A','C'): 2, ('A','K'): -2, ('B','C'): -2}

# Next we define the sampler that we want to use to run our problem.
sampler = EmbeddingComposite(DWaveSampler())

# Finally we run our problem and print out the results.
sampleset = sampler.sample_qubo(Q, num_reads = 10)
print(sampleset)