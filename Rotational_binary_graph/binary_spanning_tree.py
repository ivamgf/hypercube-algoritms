import networkx as nx


def binary_spanning_tree(n):
    """
    Constrói uma árvore geradora binária (BST)
    a partir de um hipercubo Q_n.
    """

    print(f"\nConstruindo Binary Spanning Tree para Q_{n}")

    Q = nx.hypercube_graph(n)
    T = nx.Graph()

    root = tuple([0] * n)
    visited = {root}
    queue = [root]

    while queue:
        u = queue.pop(0)
        for v in Q.neighbors(u):
            if v not in visited:
                T.add_edge(u, v)
                visited.add(v)
                queue.append(v)

    print("BST construída.")
    print("Vértices:", len(T.nodes()))
    print("Arestas:", len(T.edges()))

    return T
