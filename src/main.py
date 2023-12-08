import sys

from algorithms.branch_and_bound import branch_and_bound
from algorithms.twice_around_the_tree import twice_around_the_tree
from algorithms.christofides import christofides_algorithm
from utils.drop_vertex import drop_vertices
from utils.load_graph import create_tsp_graph_from_file


if __name__ == "__main__":
    file_path = sys.argv[1]
    num_vertices_remove = int(sys.argv[2])

    tsp_graph = create_tsp_graph_from_file(file_path)

    tsp_graph = drop_vertices(tsp_graph, (len(tsp_graph.nodes) - num_vertices_remove))

    cost_tw, path_tw = twice_around_the_tree(tsp_graph)

    cost_chr, path_chr = christofides_algorithm(tsp_graph)

    cost, path = branch_and_bound(tsp_graph)

    print("Custo (twice around the tree):", cost_tw)
    print("Caminho:", path_tw)

    print('\n')

    print("Custo (christofides):", cost_chr)
    print("Caminho:", path_chr)

    print('\n')

    print("Custo:", cost)
    print("Caminho:", path)
