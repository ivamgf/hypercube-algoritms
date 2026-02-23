import matplotlib.pyplot as plt


# =========================================
# Algorithm 4 – Innermost Two Loops (com parâmetro b)
# =========================================

def algorithm4(k, b):
    assert k >= 3, "k deve ser ≥ 3"

    m = 2 ** k - 3

    max_b = 2 ** (m - k) - 1
    assert 0 <= b <= max_b, f"b deve estar entre 0 e {max_b}"

    S = []

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
# Plotagem
# =========================================

def plot_S(S):
    plt.figure()
    plt.hist(S, bins=20)
    plt.xlabel("Índice")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Elementos de S (Algorithm 4)")
    plt.show()


# =========================================
# Execução
# =========================================

if __name__ == "__main__":
    k = 3  # k ≥ 3
    b = 0  # se b = 0, equivale ao Algorithm 3

    S = algorithm4(k, b)

    print("Total de elementos em S:", len(S))

    plot_S(S)