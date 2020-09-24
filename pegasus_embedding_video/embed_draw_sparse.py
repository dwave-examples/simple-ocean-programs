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