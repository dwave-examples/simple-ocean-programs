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

import sys
import numpy as np
import networkx as nx
import dwave_networkx as dnx
from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler

import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

# Form the biclique
args = sys.argv
if len(args) <= 1:
    print("\nNo input provided. Please provide an integer.")
    exit(1)

try:
    N = int(args[1])
except:
    print("\nIncorrect input argument. Please provide an integer.\n")
    exit(1)

nodes1 = np.arange(N)
nodes2 = [chr(i + ord('a')) for i in range(N)]
B = nx.Graph()
B.add_nodes_from(nodes1, bipartite=0)
B.add_nodes_from(nodes2, bipartite=1)
for node1 in nodes1:
    for node2 in nodes2:
        B.add_edge(node1, node2)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))

# Draw the QUBO as a networkx graph
pos = nx.spring_layout(B)
nx.draw_networkx(B, pos=pos, font_size=10, node_size=100, node_color='cyan', ax=axes[0])

# Embed the graph on Chimera
dwave_sampler_chimera = DWaveSampler(solver={'topology__type': 'chimera'})
chimera_edges = dwave_sampler_chimera.edgelist
chimera_graph = dnx.chimera_graph(16, edge_list=chimera_edges)
embedding_chimera = find_embedding(B, chimera_graph)

# Draw the graph embedded on Chimera
dnx.draw_chimera_embedding(chimera_graph, embedding_chimera, embedded_graph=B, unused_color=None, ax=axes[1])

# Embed the graph on Pegasus
dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
pegasus_edges = dwave_sampler_pegasus.edgelist
pegasus_graph = dnx.pegasus_graph(16, edge_list=pegasus_edges)
embedding_pegasus = find_embedding(B, pegasus_graph)

# Draw the graph embedded on Pegasus
dnx.draw_pegasus_embedding(pegasus_graph, embedding_pegasus, embedded_graph=B, unused_color=None, ax=axes[2])
plt.savefig('biclique_embedding')
