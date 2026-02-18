import numpy as np
from scipy.optimize import linprog


def papr_heuristic(c_sequence, a, b, mu):
    """
    Heuristic to Find a Low PAPR Mapping

    Parameters
    ----------
    c_sequence : array-like
        Mensagem {c} = (c0,...,cN−1)
    a, b : arrays
        {(ai, bi)} para i = 1,...,2k
    mu : função
        Mapeamento μ(ci) -> vi

    Returns
    -------
    P_opt : matriz de permutação aproximada
    mapping_function : função f
    """

    N = len(c_sequence)
    k2 = len(a)  # 2k

    # Gerar vetores v e w
    v = np.array([mu(ci) for ci in c_sequence])
    w = np.array([a[i]**2 + b[i]**2 for i in range(k2)])

    # Produto externo para objetivo linear
    # max v^T P w  -> linearização
    C = np.outer(v, w)

    # Como linprog minimiza, usamos -C
    c_obj = -C.flatten()

    # Restrições de matriz bistocástica
    A_eq = []
    b_eq = []

    # Soma das linhas = 1
    for i in range(N):
        row = np.zeros((N, k2))
        row[i, :] = 1
        A_eq.append(row.flatten())
        b_eq.append(1)

    # Soma das colunas = 1
    for j in range(k2):
        col = np.zeros((N, k2))
        col[:, j] = 1
        A_eq.append(col.flatten())
        b_eq.append(1)

    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)

    # Limites P >= 0
    bounds = [(0, 1) for _ in range(N * k2)]

    # Resolver LP
    result = linprog(
        c=c_obj,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs"
    )

    if not result.success:
        raise ValueError("Linear programming failed")

    P_opt = result.x.reshape((N, k2))

    # Aproximação para matriz de permutação
    P_binary = np.zeros_like(P_opt)
    for i in range(N):
        j = np.argmax(P_opt[i])
        P_binary[i, j] = 1

    # Função de mapeamento final
    def mapping_function(bits):
        """
        f([b0,...,bk−1]) = aj + i bj
        """
        index = int("".join(str(bit) for bit in bits), 2)
        j = np.argmax(P_binary[index])
        return a[j] + 1j * b[j]

    return P_binary, mapping_function
