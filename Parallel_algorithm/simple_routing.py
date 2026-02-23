import matplotlib.pyplot as plt
import networkx as nx


def is_prefix(S, D):
    """
    Verifica se S é prefixo binário de D
    """
    a = S.bit_length()
    b = D.bit_length()

    if a > b:
        return False

    # remove últimos (b-a) bits de D
    return (D >> (b - a)) == S


def simple_routing(S, D):

    if S == 0:
        S = 1

    path = [S]

    # ======================
    # FASE 1 — SUBIR
    # ======================
    while not is_prefix(S, D):
        S = S // 2
        path.append(S)

    # ======================
    # FASE 2 — DESCER
    # ======================
    while S != D:

        left_child = S * 2
        right_child = S * 2 + 1

        if is_prefix(left_child, D):
            S = left_child
        else:
            S = right_child

        path.append(S)

    return path


def plot_routing_path(path):

    G = nx.Graph()

    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(G, pos, with_labels=True)
    plt.title("Simple Routing Path")
    plt.show()


# ==========================
# TESTE
# ==========================

if __name__ == "__main__":

    S = 13
    D = 25

    print(f"Roteamento de {S} para {D}")

    path = simple_routing(S, D)

    print("Caminho encontrado:")
    print(" → ".join(map(str, path)))

    plot_routing_path(path)