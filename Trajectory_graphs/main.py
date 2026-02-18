import networkx as nx
import matplotlib.pyplot as plt

# Importações dos módulos
from trajectory_graphs import build_path_graph, plot_graph
from odd_hole import find_odd_hole


if __name__ == "__main__":

    # Parâmetros do experimento
    n = 3
    k = 3
    m = 4

    print("\n==============================")
    print(" Execução do Experimento ")
    print("==============================")

    # Construção do grafo de caminhos
    P, K = build_path_graph(n, k, m)

    print("\nVértices do grafo P:")
    print(list(P.nodes()))

    print("\nArestas do grafo P:")
    print(list(P.edges()))

    print("\nEndpoints K:")
    print(K)

    # Plot do grafo de caminhos
    plot_graph(P, "Grafo de Caminhos no Hipercubo")

    # Busca por ciclo ímpar
    ciclo = find_odd_hole(P, k)

    if ciclo:
        print("\nConstruindo grafo do ciclo encontrado...")
        ciclo_grafo = nx.Graph()
        nx.add_path(ciclo_grafo, ciclo + [ciclo[0]])

        print("Vértices do ciclo:", ciclo)
        print("Arestas do ciclo:", list(ciclo_grafo.edges()))

        plot_graph(ciclo_grafo, "Ciclo Ímpar Encontrado")
    else:
        print("\nNenhum ciclo ímpar foi encontrado.")
