import dwave_networkx as dnx
from random import seed, sample

seed(5640)

P16_perfect = dnx.pegasus_graph(16)

mask_nodes = sample(list(P16_perfect), int(.96*len(P16_perfect)))

P16 = P16_perfect.subgraph(mask_nodes).copy()


P6_perfect = dnx.pegasus_graph(6)

mask_nodes = sample(list(P6_perfect), int(.96*len(P6_perfect)))

P6 = P6_perfect.subgraph(mask_nodes).copy()