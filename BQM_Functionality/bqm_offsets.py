# -------------------------------------------------------#

# First we import the functions and packages that we will use in this program.
from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel

# Now we can define our problem as a Python dictionary and convert it to a BQM.
Q = {('B','B'): 1, 
    ('K','K'): 1, 
    ('A','C'): 2, 
    ('A','K'): -2, 
    ('B','C'): -2}
    
bqm = BinaryQuadraticModel.from_qubo(Q, offset=1.0)

# Next we define the sampler that we want to use to run our problem.
sampler = EmbeddingComposite(DWaveSampler())

# Finally we run our problem and print out the results.
sampleset = sampler.sample(bqm, num_reads = 10)
print("QUBO samples:")
print(sampleset)

# Now we can convert our problem to an Ising model and run the problem on our sampler.
bqm.change_vartype('SPIN')
sampleset = sampler.sample(bqm, num_reads = 10)
print("\nIsing samples:")
print(sampleset)