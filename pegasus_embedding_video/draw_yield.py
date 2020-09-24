from pegasus_graph import P6
from matplotlib import pyplot as plt
import dwave_networkx as dnx

dnx.draw_pegasus_yield(P6, node_size = 80)

dnx.draw_pegasus(P6, node_size = 80)