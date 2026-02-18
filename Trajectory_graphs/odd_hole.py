def find_odd_hole(P, k):
    print(f"\nProcurando ciclo ímpar de tamanho {k} ...")

    if k % 2 == 0:
        print("k precisa ser ímpar.")
        return None

    for node in P.nodes():
        stack = [(node, [node])]

        while stack:
            current, path = stack.pop()

            if len(path) == k:
                if path[0] in P.neighbors(current):
                    print(f"\nCiclo ímpar encontrado: {path}")
                    return path
                continue

            for neighbor in P.neighbors(current):
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))

    print("Nenhum ciclo ímpar encontrado.")
    return None
