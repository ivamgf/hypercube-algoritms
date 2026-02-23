import matplotlib.pyplot as plt


# =========================================
# Algorithm 5 – Innermost Three Loops
# =========================================

def algorithm5(k):
    assert k >= 3, "k deve ser ≥ 3"

    m = 2 ** k - 3

    S = []

    for b in range(2 ** (m - k)):
        for c in range(2 ** k):
            for d in range(2 ** m):
                base = (
                        (2 ** (2 * m + k + 2)) * b +
                        (2 ** (2 * m + 2)) * c +
                        (2 ** (m + 2)) * d
                )

                block = list(range(base, base + 2 ** (m + 2)))

                S.extend(block)

    return S


# =========================================
# Plotagem (apenas um gráfico)
# =========================================

def plot_S(S):
    plt.figure()
    plt.hist(S, bins=30)
    plt.xlabel("Índice")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Elementos de S (Algorithm 5)")
    plt.show()


# =========================================
# Execução
# =========================================

if __name__ == "__main__":
    k = 3  # k ≥ 3

    S = algorithm5(k)

    print("Total de elementos em S:", len(S))

    plot_S(S)