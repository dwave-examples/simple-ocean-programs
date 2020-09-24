from pegasus_graph import P6
from matplotlib import pyplot as plt, colors as mpl_color
import networkx as nx, dwave_networkx as dnx, minorminer

nodes = 80
edge_probability = 0.1
G = nx.gnp_random_graph(nodes, edge_probability, seed = 0)

nx.draw(G)

emb = minorminer.find_embedding(G, P6, random_seed = 1)

dnx.draw_pegasus_embedding(P6, emb, G)