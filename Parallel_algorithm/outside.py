import matplotlib.pyplot as plt
import networkx as nx


# =====================================
# Reutilizando Check
# =====================================

def check(A, B):
    a = A.bit_length()
    b = B.bit_length()

    while a != b:
        A *= 2
        a = A.bit_length()

    return A < B


# =====================================
# Verifica intervalo de subárvore
# =====================================

def in_interval(A, B):
    a = A.bit_length()
    b = B.bit_length()

    if a > b:
        return False

    shift = b - a
    lower = A << shift
    upper = lower + (1 << shift) - 1

    return lower <= B <= upper


# =====================================
# Outside Routing
# =====================================

def outside_routing(A, B, n):

    path = [A]
    a = A.bit_length()
    b = B.bit_length()

    # ============================
    # Caso A = 0
    # ============================
    if A == 0:
        A = 2 ** (n - 1)
        path.append(A)

        limit = B * (2 ** (n - b)) + (2 ** (n - b)) - 1

        while A > limit:
            A -= 1
            path.append(A)

        while A.bit_length() > b:
            A //= 2
            path.append(A)

        return path

    # ============================
    # Caso fora do intervalo
    # ============================
    if not in_interval(A, B):

        if check(A, B):

            # descer preenchendo 0
            while A.bit_length() < n:
                A = A * 2
                path.append(A)

            # ir até borda inferior
            while A > 2 ** (n - 1):
                A -= 1
                path.append(A)

            # reset estrutural
            A = 2 ** (n - 1)
            path.append(A)

            limit = B * (2 ** (n - b)) + (2 ** (n - b)) - 1

            while A > limit:
                A -= 1
                path.append(A)

        else:

            # descer preenchendo 1
            while A.bit_length() < n:
                A = A * 2 + 1
                path.append(A)

            # ir até borda superior
            while A < 2 ** n - 1:
                A += 1
                path.append(A)

            # reset estrutural
            A = 2 ** (n - 1)
            path.append(A)

            while A < B * (2 ** (n - b)):
                A += 1
                path.append(A)

    # ============================
    # Caso dentro do intervalo
    # ============================
    else:

        shift = b - a
        lower = A << shift
        mid = lower + (1 << (shift - 1)) - 1 if shift > 0 else lower

        # subir até raiz
        while A > 0:
            A //= 2
            path.append(A)

        A = 2 ** (n - 1)
        path.append(A)

        if B <= mid:

            while A < B * (2 ** (n - b)):
                A += 1
                path.append(A)

        else:

            limit = B * (2 ** (n - b)) + (2 ** (n - b)) - 1

            while A > limit:
                A -= 1
                path.append(A)

    # ============================
    # Contração final
    # ============================
    while A.bit_length() > b:
        A //= 2
        path.append(A)

    return path


# =====================================
# Plot
# =====================================

def plot_outside_path(path):

    G = nx.Graph()

    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(G, pos,
            with_labels=True,
            node_color="lightgreen",
            node_size=1200,
            width=2)

    plt.title("Outside Routing Path")
    plt.show()


# =====================================
# TESTE
# =====================================

if __name__ == "__main__":

    A = 6
    B = 11
    n = 4

    print(f"Outside Routing de {A} para {B} (n={n})")

    path = outside_routing(A, B, n)

    print("Caminho:")
    print(" → ".join(map(str, path)))

    plot_outside_path(path)