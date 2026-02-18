import numpy as np


def hypercube(D):
    """
    Verifica se D é a matriz de distâncias de um hipercubo
    onde todas as arestas são úteis.

    Parameters
    ----------
    D : numpy.ndarray
        Matriz simétrica m×m
        - diagonal zero
        - entradas positivas fora da diagonal
        - satisfaz desigualdade triangular

    Returns
    -------
    H : int
        1 se D representa um hipercubo válido
        0 caso contrário
    """

    m = D.shape[1]

    # Verifica se m é potência de 2
    d = np.log2(m)
    if not d.is_integer():
        print("m não é potência de 2.")
        return 0

    d = int(d)
    H = 1

    T = np.zeros((m, m, m))
    IND = np.zeros((m, m), dtype=int)

    for i in range(m):

        # Construção da torre T(:,:,i)
        T[:, :, i] = D + np.ones((m, 1)) @ D[i, :].reshape(1, -1)

        # Matriz C: onde T(j,l,i) == D(j,i)
        C = (T[:, :, i] == D[:, i].reshape(-1, 1)).astype(int)

        # Soma das linhas
        R = np.sum(C, axis=1)

        # D_ij é indecomponível se R_j == 2
        IND[:, i] = (R == 2).astype(int)

        # Verificação: número de indecomponíveis deve ser d
        if np.sum(IND[:, i]) != d:
            print(f"Falha na verificação de grau no vértice {i}")
            H = 0
            return H

    # Verificação da condição (0,2)-graph
    for i in range(m):
        for j in range(i + 1, m):

            product = IND[:, i].T @ IND[:, j]

            if product not in [0, 2]:
                print(f"Falha na condição (0,2) entre {i} e {j}")
                H = 0
                return H

    return H
