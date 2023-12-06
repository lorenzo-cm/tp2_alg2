import sys

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

from branch_and_bound import branch_and_bound
from twice_around_the_tree import twice_around_the_tree
from christofides import christofides_algorithm
from drop_vertex import drop_vertices

def euclidean_distance(coord1, coord2):
    """Calcula a distância euclidiana entre dois pontos."""
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_tsp_graph_from_file(file_path):
    """
    Cria um grafo NetworkX para o problema TSP a partir de um arquivo de coordenadas.

    Args:
    file_path (str): Caminho para o arquivo contendo os dados do TSP.

    Returns:
    networkx.Graph: Grafo representando o problema TSP.
    """
    G = nx.Graph()

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Encontra a seção onde as coordenadas dos nós começam
    start = lines.index("NODE_COORD_SECTION\n") + 1
    end = lines.index("EOF\n", start)
    coord_lines = lines[start:end]

    coords = {}
    for line in coord_lines:
        parts = line.split()
        coords[parts[0]] = (float(parts[1]), float(parts[2]))

    # Adiciona os nós com suas coordenadas
    for node, coord in coords.items():
        G.add_node(node, coord=coord)

    # Adiciona as arestas com pesos baseados na distância euclidiana
    for node1, coord1 in coords.items():
        for node2, coord2 in coords.items():
            if node1 != node2:
                distance = euclidean_distance(coord1, coord2)
                G.add_edge(node1, node2, weight=distance)

    return G


if __name__ == "__main__":
    file_path = sys.argv[1]

    tsp_graph = create_tsp_graph_from_file(file_path)

    tsp_graph = drop_vertices(tsp_graph, 52-10)

    # cost_tw, path_tw = twice_around_the_tree(tsp_graph)

    # cost_chr, path_chr = christofides_algorithm(tsp_graph)

    cost, path = branch_and_bound(tsp_graph)

    print("Custo:", cost)
    print("Caminho:", path)
