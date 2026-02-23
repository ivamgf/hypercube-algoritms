import matplotlib.pyplot as plt


# =========================================
# Algorithm 2 – Main Scheme
# =========================================

def main_scheme(k):
    assert k >= 3, "k deve ser ≥ 3"

    m = 2 ** k - 3

    Z = []

    # Tamanho total do espaço
    total_vertices = 2 ** (4 * m + 2)

    for a in range(2 ** m):

        Pa_base = (2 ** (3 * m + 2)) * a

        for b in range(2 ** (m - k)):

            Qa_base = Pa_base + (2 ** (2 * m + k + 2)) * b

            for c in range(2 ** k):

                Ra_base = Qa_base + (2 ** (2 * m + 2)) * c

                for d in range(2 ** m):
                    Ta_base = Ra_base + (2 ** (m + 2)) * d

                    # bloco elementar
                    block = list(range(Ta_base, Ta_base + 2 ** (m + 2)))

                    Z.extend(block)

    return Z


# =========================================
# Plotagem
# =========================================

def plot_results(Z):
    plt.figure()
    plt.hist(Z, bins=20)
    plt.xlabel("Índice dos Vértices")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Elementos do Conjunto Z")
    plt.show()


# =========================================
# Execução
# =========================================

if __name__ == "__main__":
    k = 3  # pode alterar (≥3)

    Z = main_scheme(k)

    print("Total de elementos em Z:", len(Z))

    plot_results(Z)