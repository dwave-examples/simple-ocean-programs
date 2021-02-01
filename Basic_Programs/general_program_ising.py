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

# This program demonstrates a basic Ocean program that runs an Ising problem
# on the D-Wave QPU.

# --------------------------------------------------------------------------#

# Import the functions and packages that are used
from dwave.system import EmbeddingComposite, DWaveSampler

# Define the problem as two Python dictionaries:
#   h for linear terms, J for quadratic terms
h = {}
J = {('A','K'): -0.5,
    ('B','C'): -0.5, 
    ('A','C'): 0.5}

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J,
                                 num_reads = 10,
                                 label='Example - Simple Ocean Programs: Ising')
print(sampleset)
