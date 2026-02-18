import networkx as nx
import matplotlib.pyplot as plt

from binary_spanning_tree import binary_spanning_tree
from simple_routing import simple_routing
from broadcasting import broadcasting


def plot_graph(G, title):
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.title(title)
    plt.show()


if __name__ == "__main__":

    n = 3

    print("\n==============================")
    print(" Execução dos Algoritmos ")
    print("==============================")

    # 1️⃣ Binary Spanning Tree
    bst = binary_spanning_tree(n)
    plot_graph(bst, "Binary Spanning Tree")

    # 2️⃣ Simple Routing
    source = (0, 0, 0)
    target = (1, 1, 0)
    simple_routing(n, source, target)

    # 3️⃣ Broadcasting
    broadcasting(n, source)
