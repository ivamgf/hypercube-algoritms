import matplotlib.pyplot as plt
import networkx as nx


def gray_cycle(n):
    """
    Gera ciclo Hamiltoniano (Gray code) do hipercubo nD
    """
    return [i ^ (i >> 1) for i in range(2**n)]


def plot_cycle(n, cycle):

    G = nx.Graph()
    nodes = range(2 ** n)

    # cria hipercubo
    for v in nodes:
        for k in range(n):
            neighbor = v ^ (1 << k)
            if v < neighbor:
                G.add_edge(v, neighbor)

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(G, pos, with_labels=True, node_color='lightgray')

    # fechar ciclo (último volta para o primeiro)
    edges = [(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle))]
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=2)

    plt.title(f"Hamiltonian Cycle (Gray Code) in {n}D Hypercube")
    plt.show()


# ==========================
# TESTE
# ==========================

if __name__ == "__main__":

    n = 3

    cycle = gray_cycle(n)

    print("Ciclo Hamiltoniano:")
    print(cycle)

    plot_cycle(n, cycle)