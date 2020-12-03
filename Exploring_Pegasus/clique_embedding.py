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
import networkx as nx
import dwave_networkx as dnx
from minorminer.busclique import find_clique_embedding
from dwave.system.samplers import DWaveSampler

import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

N = int(sys.argv[1])
G = nx.complete_graph(N)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))

# Draw the QUBO as a networkx graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, font_size=10, node_size=100, node_color='cyan', ax=axes[0])

# Embed the graph on Chimera
dwave_sampler_chimera = DWaveSampler(solver={'topology__type': 'chimera'})
chimera_edges = dwave_sampler_chimera.edgelist
chimera_graph = dnx.chimera_graph(16, edge_list=chimera_edges)
clique_embedding_chimera = find_clique_embedding(N, chimera_graph)

# Draw the graph embedded on Chimera
dnx.draw_chimera_embedding(chimera_graph, clique_embedding_chimera, embedded_graph=G, unused_color=None, ax=axes[1])

# Embed the graph on Pegasus
dwave_sampler_pegasus = DWaveSampler(solver={'topology__type': 'pegasus'})
pegasus_edges = dwave_sampler_pegasus.edgelist
pegasus_graph = dnx.pegasus_graph(16, edge_list=pegasus_edges)
clique_embedding_pegasus = find_clique_embedding(N, pegasus_graph)

# Draw the graph embedded on Pegasus
dnx.draw_pegasus_embedding(pegasus_graph, clique_embedding_pegasus, embedded_graph=G, unused_color=None, ax=axes[2])
plt.savefig('clique_embedding')
