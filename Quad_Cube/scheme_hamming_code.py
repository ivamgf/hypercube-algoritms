import itertools
import numpy as np
import matplotlib.pyplot as plt


# ================================
# Utilidades
# ================================

def parity(bits):
    return sum(bits) % 2


def int_to_bin_vector(x, n):
    return np.array(list(map(int, format(x, f'0{n}b'))))


def generate_vertices(n):
    return [int_to_bin_vector(i, n) for i in range(2 ** n)]


# ================================
# Construção da matriz H de Hamming
# ================================

def generate_hamming_matrix(k):
    """
    Gera a matriz de verificação H
    dimensão: k x (2^k - 1)
    """
    n = 2 ** k - 1
    H = []

    for i in range(1, n + 1):
        col = list(map(int, format(i, f'0{k}b')))
        H.append(col)

    return np.array(H).T  # dimensão k x n


# ================================
# Construção dos códigos
# ================================

def construct_hamming_partition(k):
    n = 2 ** k - 1

    # Caso base k=2
    if k == 2:
        return [
            ["000", "111"],
            ["001", "110"],
            ["010", "101"],
            ["011", "100"]
        ]

    H = generate_hamming_matrix(k)
    vertices = generate_vertices(n)

    # Síndrome de cada vetor
    partition = {}
    for v in vertices:
        syndrome = tuple(np.mod(H @ v, 2))
        if syndrome not in partition:
            partition[syndrome] = []
        partition[syndrome].append("".join(map(str, v)))

    # Converte para lista ordenada
    codes = list(partition.values())

    return codes


# ================================
# Plotagem
# ================================

def plot_partition(codes, k):
    sizes = [len(code) for code in codes]

    plt.figure()
    plt.bar(range(len(sizes)), sizes)
    plt.xlabel("Índice do Código (V_i)")
    plt.ylabel("Número de Palavras")
    plt.title(f"Partição de Q_n em Códigos de Hamming (k={k})")
    plt.show()


# ================================
# Execução
# ================================

if __name__ == "__main__":
    k = 3  # pode alterar (>=2)
    codes = construct_hamming_partition(k)

    print(f"n = {2 ** k - 1}")
    print(f"Número de códigos: {len(codes)}")
    print(f"Tamanho de cada código: {len(codes[0])}")

    plot_partition(codes, k)