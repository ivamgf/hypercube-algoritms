import networkx as nx

def broadcasting(n, source):
    """
    One-to-all broadcasting no hipercubo Q_n.
    Usa BFS para simular propagação.
    """

    print(f"\nBroadcasting a partir de {source}")

    Q = nx.hypercube_graph(n)

    visited = {source}
    queue = [source]
    steps = 0

    while queue:
        next_queue = []
        print(f"\nEtapa {steps}:")
        for u in queue:
            print("Transmitindo de:", u)
            for v in Q.neighbors(u):
                if v not in visited:
                    visited.add(v)
                    next_queue.append(v)
        queue = next_queue
        steps += 1

    print("\nBroadcast finalizado.")
    print("Total de nós alcançados:", len(visited))

    return visited
