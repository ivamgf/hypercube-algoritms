import itertools
import networkx as nx
import matplotlib.pyplot as plt


# =====================================================
# Geração da Hyper-Star HS(n,k)
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
# Verificação H_diag(u,v)
# =====================================================

def has_Hdiag(G, u, v):
    """
    Verifica se existe aresta válida tipo Hyper-Star
    entre u e v (troca da posição 0 com outra).
    """

    if u == v:
        return True

    if len(u) != len(v):
        return False

    n = len(u)

    # verificar se são obtidos por troca da posição 0
    for i in range(1, n):
        candidate = list(u)
        candidate[0], candidate[i] = candidate[i], candidate[0]
        if tuple(candidate) == v:
            return True

    return False


# =====================================================
# Algorithm 2 – IsHyperStar(G)
# =====================================================

def is_hyperstar(G):

    found = False

    for v in G.nodes:

        flag = True

        for u in G.nodes:
            if u == v:
                continue

            if not has_Hdiag(G, u, v):
                flag = False
                break

        if flag:
            found = True
            break

    return found


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

    plot_graph(H, "Hyper-Star HS(4,2)")

    result = is_hyperstar(H)

    print("O grafo é Hyper-Star?", result)