import networkx as nx
import matplotlib.pyplot as plt


def hypercube_neighbor(v, k):
    """
    Retorna o vizinho de v na dimensão k
    (flip do bit k)
    """
    return v ^ (1 << k)


def sequential_communication_schedule(d, iterations=8):
    """
    Gera agenda de comunicação sequencial
    """
    n = 2 ** d

    print(f"\nHipercubo {d}D com {n} nós")
    print("Nós:", list(range(n)))

    schedule = []

    i = 0

    for step in range(iterations):

        print(f"\n--- Iteração {step} ---")
        dimension = i % d
        print(f"Dimensão ativa: {dimension}")

        step_pairs = []

        for v in range(n):
            neighbor = hypercube_neighbor(v, dimension)

            # evita duplicar pares
            if v < neighbor:
                step_pairs.append((v, neighbor))
                print(f"Nó {v} sincroniza com {neighbor}")

        schedule.append(step_pairs)

        i += 1

    return schedule


def plot_hypercube(d):
    """
    Plota o hipercubo d-dimensional (projeção 2D)
    """
    n = 2 ** d
    G = nx.Graph()

    for v in range(n):
        for k in range(d):
            neighbor = hypercube_neighbor(v, k)
            if v < neighbor:
                G.add_edge(v, neighbor)

    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, with_labels=True)
    plt.title(f"Hypercube {d}D")
    plt.show()


# ==========================
# EXEMPLO DE EXECUÇÃO
# ==========================

if __name__ == "__main__":

    d = 3  # hipercubo 3D
    iterations = 6

    schedule = sequential_communication_schedule(d, iterations)

    print("\nAgenda completa:")
    for step, pairs in enumerate(schedule):
        print(f"Iteração {step}: {pairs}")

    plot_hypercube(d)