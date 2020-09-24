from pegasus_graph import P16
from matplotlib import pyplot as plt
import networkx as nx, dwave_networkx as dnx

from minorminer import busclique

clique_cache = busclique.busgraph_cache(P16)
clique_embedding = clique_cache.largest_clique()

K = nx.complete_graph(len(clique_embedding))

dnx.draw_pegasus_embedding(P16, clique_embedding, K)