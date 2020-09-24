from matplotlib import pyplot as plt, colors as mpl_color
import networkx as nx, dwave_networkx as dnx

def color(i, n):
    r, g, b = mpl_color.hsv_to_rgb((i/n, .25 + (i%4)/4, 1))
    return r, g, b, 1.

def double_plot(S, T, emb, filename, params):
    fig = plt.figure(figsize = (40, 20))
    axes = fig.subplots(nrows=1, ncols=2)
    
    n = len(S)
    colors = {v: color(i, n) for i, v in enumerate(S)}

    node_colors = list(colors[v] for v in S)

    if params[0].get('pos') is None:
        params[0]['pos'] = nx.kamada_kawai_layout(S)

    nx.draw(S,
            node_color = node_colors,
            ax = axes[0],
            **params[0])

    dnx.draw_pegasus_embedding(T, emb, S,
                               crosses = True, 
                               chain_colors = colors,
                               ax = axes[1],
                               **params[1])


    fig.tight_layout()
    plt.savefig(filename)
    plt.close()

def yield_double_plot(P, filename):
    fig = plt.figure(figsize = (40, 20))
    axes = fig.subplots(nrows=1, ncols=2)
    
    dnx.draw_pegasus_yield(P, node_size = 80, ax = axes[0])

    dnx.draw_pegasus(P, crosses = True, node_size = 80, node_color = "#f37820",
                     edge_color = "#17bebb", ax = axes[1])

    fig.tight_layout()
    plt.savefig(filename)
    plt.close()
    
if __name__ == '__main__':
    from pegasus_graph import P6, P16

    from embed_draw_random import G, emb as random_embedding

    double_plot(G, P6, random_embedding,
                'random_doubleplot.png',
                [{'node_size': 100}, {'node_size': 30}])

    from embed_draw_clique import K, clique_embedding

    double_plot(K, P16, clique_embedding, 'clique_doubleplot.png',
                [{'node_size': 100, 'pos': nx.circular_layout(K), 'width': 1, 
                 'edge_color': (0, 0, 0, .1)}, {'node_size': 10}])

    from embed_draw_sparse import C, layout_C, emb as sparse_embedding

    double_plot(C, P6, sparse_embedding, 'sparse_doubleplot.png',
                [{'node_size': 70, 'pos': layout_C},
                 {'node_size': 30}])

    fig = plt.figure(figsize = (20, 20))
    dnx.draw_pegasus(dnx.pegasus_graph(3), node_color = "#f37820",
                     edge_color = "#17bebb", crosses = True)
    plt.savefig("P3.png")
    plt.close()

    yield_double_plot(P6, "yield_doubleplot.png")
