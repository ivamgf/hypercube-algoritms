# hypercube_visualization.py
# Visualização do grafo hipercubo Q_d com pandas + matplotlib

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def tuple_to_bitstring(t):
    """Converte uma tupla de 0/1 em string binária, ex: (0,1,0) -> '010'."""
    return "".join(str(x) for x in t)

def build_hypercube(d):
    """Cria o grafo hipercubo Q_d com rótulos de nós em bitstrings."""
    G = nx.hypercube_graph(d)
    mapping = {node: tuple_to_bitstring(node) for node in G.nodes()}
    return nx.relabel_nodes(G, mapping)

def hypercube_to_dataframes(G):
    """Retorna (edges_df, adjacency_df) do grafo G."""
    edges = pd.DataFrame(sorted(list(G.edges())), columns=["source", "target"])
    adjacency_df = nx.to_pandas_adjacency(G, dtype=int)
    return edges, adjacency_df

def visualize_graph(G, d):
    """Mostra visualização do grafo hipercubo usando networkx + matplotlib."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42, dim=2)  # disposição em 2D
    nx.draw(
        G, pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=9,
        font_color="black",
        edge_color="gray",
        font_weight="bold"
    )
    plt.title(f"Grafo Hipercubo Q_{d}", fontsize=14)
    plt.show()

def main():
    d = 3  # altere a dimensão do hipercubo aqui

    # Construir grafo
    G = build_hypercube(d)

    # Converter para DataFrames
    edges_df, adjacency_df = hypercube_to_dataframes(G)

    # Mostrar DataFrames
    print(f"\nHypercube Q_{d} - Vértices: {G.number_of_nodes()}, Arestas: {G.number_of_edges()}\n")
    print("Lista de arestas:")
    print(edges_df)
    print("\nMatriz de adjacência:")
    print(adjacency_df)

    # Visualizar
    visualize_graph(G, d)

if __name__ == "__main__":
    main()
