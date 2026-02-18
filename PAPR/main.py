from papr import papr_heuristic
import numpy as np

if __name__ == "__main__":

    # Exemplo simples
    c_sequence = [0, 1, 2, 3]

    a = np.array([1, -1, 1, -1])
    b = np.array([1, 1, -1, -1])

    def mu(x):
        return x + 1

    P, f = papr_heuristic(c_sequence, a, b, mu)

    print("\nMatriz de permutação aproximada P:")
    print(P)

    print("\nExemplo de mapeamento:")
    print("bits [0,1] ->", f([0, 1]))
