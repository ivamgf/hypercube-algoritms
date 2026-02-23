import matplotlib.pyplot as plt


# =========================================
# Algorithm 3 – Innermost Two Loops
# =========================================

def innermost_two_loops(k):
    assert k >= 3, "k deve ser ≥ 3"

    m = 2 ** k - 3

    S = []

    for c in range(2 ** k):
        for d in range(2 ** m):
            base = (2 ** (2 * m + 2)) * c + (2 ** (m + 2)) * d

            block = list(range(base, base + 2 ** (m + 2)))

            S.extend(block)

    return S


# =========================================
# Plotagem
# =========================================

def plot_S(S):
    plt.figure()
    plt.hist(S, bins=20)
    plt.xlabel("Índice")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Elementos de S")
    plt.show()


# =========================================
# Execução
# =========================================

if __name__ == "__main__":
    k = 3  # pode alterar (≥3)

    S = innermost_two_loops(k)

    print("Total de elementos em S:", len(S))

    plot_S(S)