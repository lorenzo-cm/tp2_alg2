import sys

sys.path.append('src')

from pathlib import Path

from algorithms.twice_around_the_tree import twice_around_the_tree
from algorithms.christofides import christofides_algorithm
from utils.load_graph import create_tsp_graph_from_file
from utils.utils import timer
from utils.tsp_results import tsp_results

@timer
def run(file):
    tsp_graph = create_tsp_graph_from_file('data/instances/' + file.name)

    cost_tw, path_tw = twice_around_the_tree(tsp_graph)

    cost_chr, path_chr = christofides_algorithm(tsp_graph)

    filename_parts = file.name.split('.')

    real_cost = tsp_results[filename_parts[0]]
    
    print('\n')
    print('-' * 50)
    print(f'File name: {file.name}')
    print(f"Cost (twice around the tree): {cost_tw}")
    print(f"Cost (christofides): {cost_chr}")
    print('\n')
    print(f"Real cost: {real_cost}")
    print(f"Performance twice around the tree: {cost_tw * 100 / real_cost}%")
    print(f"Performance christofides: {cost_chr * 100 / real_cost}%")
    print('-' * 50)
    print('\n')


if __name__ == '__main__':

    folder_path = Path('data/instances')

    for file in folder_path.iterdir():
        if file.suffix == '.tsp':
            run(file)

