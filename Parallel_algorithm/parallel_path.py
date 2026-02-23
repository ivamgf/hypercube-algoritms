import matplotlib.pyplot as plt
import networkx as nx
from simple_routing import simple_routing


def check(A, B):
    """
    Implementação do Check(A, a)
    """
    a = A.bit_length()
    b = B.bit_length()

    while a != b:
        A = A * 2
        a = A.bit_length()

    return A < B


def parallel_path(A, B):
    """
    Parallel Path Algorithm
    """
    if check(A, B):
        path = simple_routing(A, B)
    else:
        path = simple_routing(B, A)
        path = path[::-1]

    return path


def plot_parallel_path(path):
    """
    Plota o caminho paralelo em uma árvore binária implícita
    """
    G = nx.Graph()

    # adiciona apenas nós e arestas do caminho
    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=1200,
        width=2
    )
    plt.title("Parallel Path Routing")
    plt.show()


# ==========================
# TESTE
# ==========================

if __name__ == "__main__":

    A = 13
    B = 25

    print(f"Parallel Path de {A} para {B}")

    path = parallel_path(A, B)

    print("Caminho encontrado:")
    print(" → ".join(map(str, path)))

    plot_parallel_path(path)