def simple_routing(n, source, target):
    """
    Roteamento simples no hipercubo.
    Caminha corrigindo bits diferentes.
    """

    print(f"\nSimple Routing de {source} para {target}")

    current = list(source)
    path = [tuple(current)]

    for j in range(n):
        if current[j] != target[j]:
            current[j] = target[j]
            path.append(tuple(current))

    print("Caminho encontrado:")
    for node in path:
        print(node)

    return path
