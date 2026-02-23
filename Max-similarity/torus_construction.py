import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import math


def construct_rings(S):
    """
    Constrói m anéis de tamanho m maximizando similaridade local
    """
    n = S.shape[0]
    m = int(math.sqrt(n))

    G = nx.Graph()
    G.add_nodes_from(range(n))

    unmatched = set(range(n))
    rings = []

    for i in range(m):
        print(f"\n--- Construindo Ring {i+1} ---")

        # Escolhe nó inicial aleatório
        u = random.choice(list(unmatched))
        unmatched.remove(u)

        ring = [u]

        for j in range(1, m):
            # encontra nó não pareado com maior similaridade
            v = max(unmatched, key=lambda x: S[u, x])
            ring.append(v)
            unmatched.remove(v)
            G.add_edge(u, v)
            u = v

        # fecha o anel
        G.add_edge(ring[-1], ring[0])

        print("Ring:", ring)
        rings.append(ring)

    return G, rings


def match_rings(G, rings, S):
    """
    Conecta os anéis formando um toro 2D
    """
    m = len(rings)

    print("\n--- Conectando Rings (Ring of Rings) ---")

    # conecta Ri com Ri+1
    for i in range(m):
        ring1 = rings[i]
        ring2 = rings[(i + 1) % m]

        for u, v in zip(ring1, ring2):
            G.add_edge(u, v)

        print(f"Conectado Ring {i+1} com Ring {(i+2 if i+1<m else 1)}")

    return G


def max_similarity_torus(S):
    """
    Constrói toro 2D max-similarity
    """
    n = S.shape[0]
    m = int(math.sqrt(n))

    if m * m != n:
        raise ValueError("n deve ser quadrado perfeito")

    print(f"\nConstruindo toro 2D com m = {m}")

    G, rings = construct_rings(S)
    G = match_rings(G, rings, S)

    return G


def plot_torus(G):
    """
    Plota o grafo usando layout spring
    """
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, with_labels=True)
    plt.title("Max-Similarity 2D Torus")
    plt.show()


# ==========================
# EXEMPLO DE EXECUÇÃO
# ==========================

if __name__ == "__main__":

    # Exemplo: toro 3x3 → n = 9
    n = 9

    np.random.seed(42)
    random.seed(42)

    S = np.random.rand(n, n)
    S = (S + S.T) / 2
    np.fill_diagonal(S, 0)

    print("Matriz de Similaridade S:\n", S)

    G = max_similarity_torus(S)

    print("\nArestas finais do Toro:")
    for edge in G.edges():
        print(edge)

    plot_torus(G)