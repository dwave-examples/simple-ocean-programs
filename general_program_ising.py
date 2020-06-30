# This program demonstrates a basic Ocean program that runs an Ising problem on the D-Wave QPU. In this example we use Ocean's `EmbeddingComposite` to determine the best placement of our problem onto the physical hardware.

# Program Characteristics:

# - Model: Ising
# - Sampler: D-Wave QPU with EmbeddingComposite

# This Ising problem is formulated/developed here: https://docs.dwavesys.com/docs/latest/c_pf_3.html#social-networks-friends-and-enemies

# -------------------------------------------------------#

# First we import the functions and packages that we will use in this program.
from dwave.system import EmbeddingComposite, DWaveSampler

# Now we can define our problem as two Python dictionaries.
# Dictionary for linear terms
h = {} 

# Dictionary for quadratic terms
J = {('A','K'): -0.5, ('B','C'): -0.5, ('A','C'): 0.5} 

# Next we define the sampler that we want to use to run our problem.
sampler = EmbeddingComposite(DWaveSampler())

# Finally we run our problem and print out the results.
sampleset = sampler.sample_ising(h, J, num_reads = 10)
print(sampleset)