import random
import networkx as nx
import matplotlib.pyplot as plt


def generate_hypercube(n):
    print(f"\nGerando hipercubo Q_{n} ...")
    G = nx.hypercube_graph(n)
    print(f"Total de vértices: {len(G.nodes())}")
    print(f"Total de arestas: {len(G.edges())}")
    return G


def compute_m_paths(G, k, m):
    print(f"\nGerando {m} caminhos de tamanho {k} ...")
    paths = []
    nodes = list(G.nodes())

    for i in range(m):
        start = random.choice(nodes)
        path = [start]

        while len(path) < k:
            neighbors = list(G.neighbors(path[-1]))
            neighbors = [v for v in neighbors if v not in path]

            if not neighbors:
                break

            next_node = random.choice(neighbors)
            path.append(next_node)

        if len(path) == k:
            print(f"Caminho {i+1}: {path}")
            paths.append(path)

    return paths


def compute_endpoints(paths):
    K = [(path[0], path[-1]) for path in paths]
    print("\nEndpoints (K):")
    for pair in K:
        print(pair)
    return K


def build_path_graph(n, k, m):
    Qn = generate_hypercube(n)
    paths = compute_m_paths(Qn, k, m)
    K = compute_endpoints(paths)

    P = nx.Graph()

    for path in paths:
        nx.add_path(P, path)

    print(f"\nGrafo P possui {len(P.nodes())} vértices e {len(P.edges())} arestas.")

    return P, K


def plot_graph(G, title="Grafo"):
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.title(title)
    plt.show()
