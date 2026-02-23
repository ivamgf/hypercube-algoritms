import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import itertools


def virtual_node_similarity(vn1, vn2, S):
    """
    Soma das similaridades entre todos os pares (u,v)
    u ∈ vn1, v ∈ vn2
    """
    sim = 0
    for u in vn1:
        for v in vn2:
            sim += S[u, v]
    return sim


def max_similarity_hypercube(S):
    """
    Constrói um hipercubo max-similarity a partir da matriz S.
    S deve ser uma matriz n x n, onde n = 2^d
    """
    n = S.shape[0]
    d = int(np.log2(n))

    # Inicialização
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # Cada nó começa como um virtual node unitário
    virtual_nodes = [{i} for i in range(n)]

    for dim in range(d):
        print(f"\n--- Construindo dimensão {dim} ---")

        # Grafo completo entre virtual nodes
        VG = nx.Graph()

        for i, j in itertools.combinations(range(len(virtual_nodes)), 2):
            sim = virtual_node_similarity(
                virtual_nodes[i],
                virtual_nodes[j],
                S
            )
            VG.add_edge(i, j, weight=sim)

        # Blossom (maximum weight matching)
        matching = nx.algorithms.matching.max_weight_matching(
            VG, maxcardinality=True
        )

        print("Matching encontrado:", matching)

        new_virtual_nodes = []

        # Para cada par do matching
        for i, j in matching:
            vn1 = virtual_nodes[i]
            vn2 = virtual_nodes[j]

            # Conectar todos os pares (u,v)
            for u in vn1:
                for v in vn2:
                    G.add_edge(u, v)

            # Criar novo virtual node
            new_virtual_nodes.append(vn1.union(vn2))

        virtual_nodes = new_virtual_nodes

    return G


def plot_hypercube(G):
    """
    Plota o grafo usando layout 2D
    """
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, with_labels=True)
    plt.title("Max-Similarity Hypercube")
    plt.show()


# ================================
# EXEMPLO DE EXECUÇÃO
# ================================

if __name__ == "__main__":

    # Exemplo: hipercubo 3D → n = 8 nós
    n = 8

    # Matriz de similaridade aleatória simétrica
    np.random.seed(42)
    S = np.random.rand(n, n)
    S = (S + S.T) / 2
    np.fill_diagonal(S, 0)

    print("Matriz de Similaridade S:\n", S)

    G = max_similarity_hypercube(S)

    print("\nArestas finais do hipercubo:")
    for edge in G.edges():
        print(edge)

    plot_hypercube(G)