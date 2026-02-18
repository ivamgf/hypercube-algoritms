from hypercube import hypercube
import numpy as np

if __name__ == "__main__":

    # Exemplo: matriz de distâncias do hipercubo Q2
    D = np.array([
        [0, 1, 1, 2],
        [1, 0, 2, 1],
        [1, 2, 0, 1],
        [2, 1, 1, 0]
    ])

    result = hypercube(D)

    if result == 1:
        print("\nD é matriz de distâncias de um hipercubo.")
    else:
        print("\nD NÃO é matriz de distâncias de um hipercubo.")
