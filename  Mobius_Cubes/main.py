# main.py

import sys
import os

# Garante que a pasta atual esteja no path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import networkx as nx
import matplotlib.pyplot as plt

from alg_sp import SP, flip_bit


# ===============================
# Geração do Hipercubo
# ===============================

def generate_hypercube(n):

    G = nx.Graph()

    for i in range(2 ** n):
        G.add_node(i)

    for i in range(2 ** n):
        for j in range(n):
            neighbor = flip_bit(i, j)
            G.add_edge(i, neighbor)

    return G


# ===============================
# Plot
# ===============================

def plot_hypercube_with_path(G, path, n):

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nx.draw(
        G,
        pos,
        node_size=600,
        node_color="lightgray",
        with_labels=True,
        labels={v: format(v, f'0{n}b') for v in G.nodes},
    )

    edges_path = list(zip(path[:-1], path[1:]))

    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=path,
        node_color="red",
        node_size=700,
    )

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=edges_path,
        width=3,
    )

    plt.title("Shortest Path in Hypercube (SP Algorithm)")
    plt.show()


# ===============================
# MAIN
# ===============================

if __name__ == "__main__":

    n = 4
    s = 3
    t = 12

    G = generate_hypercube(n)

    path = SP(s, t, n)

    print("Caminho encontrado:")
    for v in path:
        print(format(v, f'0{n}b'))

    plot_hypercube_with_path(G, path, n)