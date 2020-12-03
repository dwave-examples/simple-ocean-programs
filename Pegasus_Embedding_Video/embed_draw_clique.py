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

from pegasus_graph import P16
import networkx as nx, dwave_networkx as dnx
from minorminer import busclique

import matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

clique_cache = busclique.busgraph_cache(P16)
clique_embedding = clique_cache.largest_clique()

K = nx.complete_graph(len(clique_embedding))

dnx.draw_pegasus_embedding(P16, clique_embedding, K)
