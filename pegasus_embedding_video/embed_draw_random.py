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

from pegasus_graph import P6
from matplotlib import pyplot as plt, colors as mpl_color
import networkx as nx, dwave_networkx as dnx, minorminer

nodes = 80
edge_probability = 0.1
G = nx.gnp_random_graph(nodes, edge_probability, seed = 0)

nx.draw(G)

emb = minorminer.find_embedding(G, P6, random_seed = 1)

dnx.draw_pegasus_embedding(P6, emb, G)
