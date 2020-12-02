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
import dwave_networkx as dnx, networkx as nx
from matplotlib import pyplot as plt, colors as mpl_color

from minorminer import layout

nodes = 200
degree = 3
C = nx.random_regular_graph(degree, nodes)

layout_args = {'random_seed': 1, 'return_layouts': True}

emb, (layout_C, _) = layout.find_embedding(C, P6, **layout_args)

nx.draw(C, pos = layout_C)

dnx.draw_pegasus_embedding(P6, emb, C)
