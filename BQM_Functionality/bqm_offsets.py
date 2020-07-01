# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# --------------------------------------------------------------------------#

# This program demonstrates a basic Ocean program that creates a
# BinaryQuadraticModel with a non-zero offset to store a constant term. 

# --------------------------------------------------------------------------#

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