import itertools
import networkx as nx
import matplotlib.pyplot as plt


# =====================================================
# Construção da Hyper-Star HS(n, k)
# =====================================================

def generate_hyperstar(n, k):

    G = nx.Graph()

    # gera todos os vértices com exatamente k bits 1
    vertices = []
    for bits in itertools.product([0, 1], repeat=n):
        if sum(bits) == k:
            vertices.append(bits)

    # adiciona vértices
    for v in vertices:
        G.add_node(v)

    # adiciona arestas (troca posição 0 com i)
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
# Algorithm 1 – DecompositionHyperStar
# =====================================================

def decomposition_hyperstar(H):

    G = H.copy()
    components = []

    while len(G.nodes) > 0:

        # δ(G) = grau mínimo
        min_degree = min(dict(G.degree()).values())

        # escolhe vértice com grau mínimo
        for v in G.nodes:
            if G.degree(v) == min_degree:
                start = v
                break

        # encontra conjunto S conectado com grau mínimo
        S = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in S and G.degree(node) == min_degree:
                S.add(node)
                for neighbor in G.neighbors(node):
                    if G.degree(neighbor) == min_degree:
                        stack.append(neighbor)

        # Hi = fecho de S (subgrafo induzido)
        Hi = G.subgraph(S).copy()
        components.append(Hi)

        # remove S do grafo
        G.remove_nodes_from(S)

    return components


# =====================================================
# Plotagem
# =====================================================

def plot_graph(G, title="Graph"):

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(
        G,
        pos,
        with_labels=False,
        node_size=500,
    )

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

    print(f"Gerando Hyper-Star HS({n},{k})")

    H = generate_hyperstar(n, k)

    print("Plotando Hyper-Star original...")
    plot_graph(H, "Hyper-Star HS(4,2)")

    print("Executando DecompositionHyperStar...")
    components = decomposition_hyperstar(H)

    print(f"Número de componentes encontrados: {len(components)}")

    for i, comp in enumerate(components):
        plot_graph(comp, f"Componente H{i+1}")