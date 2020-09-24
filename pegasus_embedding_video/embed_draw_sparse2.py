from pegasus_graph import P16, P6
import minorminer.layout as mml, dwave_networkx as dnx, networkx as nx
from matplotlib import pyplot as plt, colors as mpl_color

if False:
    n = 200
    C = nx.random_regular_graph(3, n)

    emb, (layout_C, layout_P) = mml.find_embedding(C, P6, random_seed = 1,
                                                     return_layouts = True,
                                                     threads = 3)

    plt.figure(figsize=(20, 20))

    nx.draw(C)

    plt.savefig("sparse_graph.png")
    plt.close()

    plt.figure(figsize=(20, 20))
    dnx.draw_pegasus_embedding(P6, emb, C)
    plt.savefig("sparse_embedded.png")
    plt.close()


n = 850
C = nx.random_regular_graph(3, n)

emb, (layout_C, layout_P) = mml.find_embedding(C, P16, random_seed = 2,
                                                 return_layouts = True, layout = (None, None),
                                                 threads = 3, verbose = 2, interactive = True, tries = 30, max_no_improvement = 10000, timeout = 10000000)

plt.figure(figsize=(20, 20))

nx.draw(C)

plt.savefig("sparse_graph_big.png")
plt.close()

plt.figure(figsize=(20, 20))
dnx.draw_pegasus_embedding(P16, emb, C)
plt.savefig("sparse_embedded_big.png")
plt.close()
from double_plot import double_plot
double_plot(C, P16, emb, 'sparse_doubleplot2.png',
            [{'node_size': 70, 'pos': layout_C},
             {'node_size': 30}])
