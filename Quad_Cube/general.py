import matplotlib.pyplot as plt


# =========================================
# Algorithm 7 – The General Algorithm
# =========================================

def algorithm7(k, t):
    assert k >= 3, "k deve ser ≥ 3"

    m = 2 ** k - 3

    assert 0 <= t <= 2 ** k - 1, f"t deve estar entre 0 e {2 ** k - 1}"

    Z = []

    for a in range(2 ** m):
        for b in range(2 ** (m - k)):
            for c in range(2 ** k):
                for d in range(2 ** m):
                    base = (
                            (2 ** (3 * m + 2)) * a +
                            (2 ** (2 * m + k + 2)) * b +
                            (2 ** (2 * m + 2)) * c +
                            (2 ** (m + 2)) * d +
                            t  # parâmetro adicional do algoritmo geral
                    )

                    block = list(range(base, base + 2 ** (m + 2)))

                    Z.extend(block)

    return Z


# =========================================
# Plotagem (apenas um gráfico)
# =========================================

def plot_Z(Z):
    plt.figure()
    plt.hist(Z, bins=40)
    plt.xlabel("Índice")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Elementos de Z (Algorithm 7)")
    plt.show()


# =========================================
# Execução
# =========================================

if __name__ == "__main__":
    k = 3  # k ≥ 3
    t = 1  # 0 ≤ t ≤ 2^k - 1

    Z = algorithm7(k, t)

    print("Total de elementos em Z:", len(Z))

    plot_Z(Z)