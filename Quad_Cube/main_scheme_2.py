import matplotlib.pyplot as plt


# =========================================
# Algorithm 6 – Main Scheme (Miniature Form)
# =========================================

def algorithm6(k):
    assert k >= 3, "k deve ser ≥ 3"

    m = 2 ** k - 3
    Z = []

    for a in range(2 ** m):
        for b in range(2 ** (m - k)):
            for c in range(2 ** k):
                for d in range(2 ** m):
                    base = (
                            (2 ** (3 * m + 2)) * a +
                            (2 ** (2 * m + k + 2)) * b +
                            (2 ** (2 * m + 2)) * c +
                            (2 ** (m + 2)) * d
                    )

                    block = list(range(base, base + 2 ** (m + 2)))

                    Z.extend(block)

    return Z


# =========================================
# Plotagem (um único gráfico)
# =========================================

def plot_Z(Z):
    plt.figure()
    plt.hist(Z, bins=40)
    plt.xlabel("Índice")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Elementos de Z (Algorithm 6)")
    plt.show()


# =========================================
# Execução
# =========================================

if __name__ == "__main__":
    k = 3  # k ≥ 3 (valores maiores crescem exponencialmente)

    Z = algorithm6(k)

    print("Total de elementos em Z:", len(Z))

    plot_Z(Z)