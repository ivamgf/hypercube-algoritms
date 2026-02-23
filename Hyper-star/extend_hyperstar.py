import itertools
import networkx as nx
import matplotlib.pyplot as plt


# =====================================================
# Geração Hyper-Star HS(n,k)
# =====================================================

def generate_hyperstar(n, k):

    G = nx.Graph()

    vertices = []
    for bits in itertools.product([0, 1], repeat=n):
        if sum(bits) == k:
            vertices.append(bits)

    for v in vertices:
        G.add_node(v)

    for v in vertices:
        for i in range(1, n):
            if v[0] != v[i]:
                new_v = list(v)
                new_v[0], new_v[i] = new_v[i], new_v[0]
                new_v = tuple(new_v)
                if new_v in G:
                    G.add_edge(v, new_v)

    return G


# =====================================================
# Verificação Hyper-Star estrutural
# =====================================================

def is_hyperstar(G):

    for v in G.nodes:
        valid = True

        for u in G.nodes:
            if u == v:
                continue

            if not G.has_edge(u, v):
                valid = False
                break

        if valid:
            return True

    return False


# =====================================================
# Remover isomorfos
# =====================================================

def remove_isomorphic(graph_list):

    unique_graphs = []

    for g in graph_list:
        is_new = True
        for ug in unique_graphs:
            if nx.is_isomorphic(g, ug):
                is_new = False
                break
        if is_new:
            unique_graphs.append(g)

    return unique_graphs


# =====================================================
# Algorithm 3 – ExtendHyperStars
# =====================================================

def extend_hyperstars(H, Si):

    Si_next = []

    for S in Si:

        for v in set(H.nodes) - set(S):

            T = set(S)
            T.add(v)

            subgraph = H.subgraph(T).copy()

            if nx.is_connected(subgraph) and is_hyperstar(subgraph):
                Si_next.append(subgraph)

    # remover isomorfos
    Si_next = remove_isomorphic(Si_next)

    return Si_next


# =====================================================
# Plot
# =====================================================

def plot_graph(G, title="Graph"):

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(G, pos, with_labels=False, node_size=500)

    labels = {v: ''.join(map(str, v)) for v in G.nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    plt.title(title)
    plt.show()


# =====================================================
# TESTE
# =====================================================

if __name__ == "__main__":

    n = 4
    k = 2

    H = generate_hyperstar(n, k)

    print("Hyper-Star original:")
    plot_graph(H, "Hyper-Star HS(4,2)")

    # Começamos com conjuntos unitários
    Si = [{v} for v in H.nodes]

    print("Executando ExtendHyperStars...")

    Si_next = extend_hyperstars(H, Si)

    print("Número de extensões encontradas:", len(Si_next))

    for i, g in enumerate(Si_next):
        plot_graph(g, f"Extensão Hyper-Star {i+1}")