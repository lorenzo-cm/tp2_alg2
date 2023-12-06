import numpy as np
import networkx as nx
import heapq

def branch_and_bound(G):
    # Função auxiliar para calcular o custo de um caminho
    def path_cost(path):
        return sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))

    # Função auxiliar para calcular um limite inferior para um caminho parcial
    def lower_bound(path):
        return path_cost(path)  # MUDAR

    # Inicialização
    best_cost = float('inf')
    best_path = None
    heap = []

    # Adiciona o caminho inicial na heap
    initial_path = [next(iter(G.nodes))]  # Supondo que o nó '1' é o ponto de partida
    heapq.heappush(heap, (lower_bound(initial_path), initial_path))

    while heap:
        _, path = heapq.heappop(heap)

        if len(path) == G.number_of_nodes():
            # Verifica se encontrou um caminho completo
            complete_path = path + [path[0]]  # Retorna ao ponto de partida
            cost = path_cost(complete_path)
            if cost < best_cost:
                best_cost, best_path = cost, complete_path
        else:
            # Explora os vizinhos do último nó no caminho
            for neighbor in G.neighbors(path[-1]):
                if neighbor not in path:  # Evita ciclos
                    new_path = path + [neighbor]
                    bound = lower_bound(new_path)
                    if bound < best_cost:
                        heapq.heappush(heap, (bound, new_path))

    return best_cost, best_path