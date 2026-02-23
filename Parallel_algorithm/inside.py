import matplotlib.pyplot as plt
import networkx as nx


# =============================
# Função Check reutilizada
# =============================

def check(A, B):
    a = A.bit_length()
    b = B.bit_length()

    while a != b:
        A = A * 2
        a = A.bit_length()

    return A < B


# =============================
# Função auxiliar intervalo
# =============================

def in_interval(A, B):
    a = A.bit_length()
    b = B.bit_length()

    if a > b:
        return False

    shift = b - a
    lower = A << shift
    upper = lower + (1 << shift) - 1

    return lower <= B <= upper


# =============================
# Inside Algorithm
# =============================

def inside_routing(A, B, n):

    path = [A]
    a = A.bit_length()
    b = B.bit_length()

    if A == 0:
        A = 2 ** (n - 1)
        path.append(A)

        while A < B * (2 ** (n - b)):
            A += 1
            path.append(A)

        while A.bit_length() > b:
            A //= 2
            path.append(A)

        return path

    # Caso geral
    if not in_interval(A, B):

        if check(A, B):
            # expandir com 1
            while A.bit_length() < n:
                A = A * 2 + 1
                path.append(A)

            while A < B * (2 ** (n - b)):
                A += 1
                path.append(A)

        else:
            # expandir com 0
            while A.bit_length() < n:
                A = A * 2
                path.append(A)

            limit = B * (2 ** (n - b)) + (2 ** (n - b)) - 1

            while A > limit:
                A -= 1
                path.append(A)

    else:

        shift = b - a
        lower = A << shift
        mid = lower + (1 << (shift - 1)) - 1 if shift > 0 else lower

        if lower <= B <= mid:

            A = A * 2 + 1
            path.append(A)

            while A.bit_length() < n:
                A = A * 2
                path.append(A)

            limit = B * (2 ** (n - b)) + (2 ** (n - b)) - 1

            while A > limit:
                A -= 1
                path.append(A)

        else:

            A = A * 2
            path.append(A)

            while A.bit_length() < n:
                A = A * 2 + 1
                path.append(A)

            while A < B * (2 ** (n - b)):
                A += 1
                path.append(A)

    # Contração final
    while A.bit_length() > b:
        A //= 2
        path.append(A)

    return path


# =============================
# Plot
# =============================

def plot_inside_path(path):

    G = nx.Graph()

    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(G, pos, with_labels=True,
            node_color="orange",
            node_size=1200,
            width=2)
    plt.title("Inside Routing Path")
    plt.show()


# =============================
# TESTE
# =============================

if __name__ == "__main__":

    A = 5
    B = 11
    n = 4   # dimensão máxima

    print(f"Inside Routing de {A} para {B} (n={n})")

    path = inside_routing(A, B, n)

    print("Caminho:")
    print(" → ".join(map(str, path)))

    plot_inside_path(path)