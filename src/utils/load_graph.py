import networkx as nx

from utils.utils import euclidean_distance

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