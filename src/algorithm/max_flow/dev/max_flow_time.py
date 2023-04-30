import random
import time

import networkx
from src.graph.bipartite_graph import BipartiteGraph
from src.algorithm.max_matching.max_matching import MaxMatching
# from src.algorithm.max_flow.core.edmonds_karp import edmonds_karp
from src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from src.algorithm.max_flow.edmond_karp_algorithm import EdmondsKarpAlgorithm

from networkx.algorithms.flow import edmonds_karp

from utils.utils import timed_execution, create_csv

if __name__ == '__main__':
    nodes_range = [node_num for node_num in range(1000, 12800, 400)]
    density_range = [density / 100 for density in range(2, 100, 3)]

    columns_name = [
        'NUM OF NODES',
        'Density',
        'Dinitz Result',
        'Edmond-Karp Result',
        'Dinitz Execution Time',
        'Edmond-Karp Execution Time',
        'MaxMatching'
    ]

    bipartite_graph = BipartiteGraph()
    dinitz = MaxMatching()
    edmond = MaxMatching()

    sparse = [value for value in density_range if value < 0.5]
    density = [value for value in density_range if value > 0.5]

    sparse_rows = []
    density_rows = []

    for i in range(30):
        node_num = nodes_range[i]
        density_value = sparse[i]
        bipartite_graph.fast_way(num_of_nodes=node_num, density=density_value)

        edmond.set_bipartite_graph(bipartite_graph=bipartite_graph)
        edmond.reduce_to_max_flow()
        edmond.set_algorithm(algorithm=EdmondsKarpAlgorithm)
        start_time = time.time()
        edmond.find_max_matching()
        end_time = time.time()
        edmond_algorithm_execution_time = end_time - start_time
        edmond_algorithm_value = edmond.max_matching_value

        dinitz.set_bipartite_graph(bipartite_graph=bipartite_graph)
        dinitz.reduce_to_max_flow()
        dinitz.set_algorithm(algorithm=DinitzAlgorithm)
        start_time = time.time()
        dinitz.find_max_matching()
        end_time = time.time()
        dinitz_algorithm_execution_time = end_time - start_time
        dinitz_algorithm_value = dinitz.max_matching_value

        edmonds_karp_max_flow = edmonds_karp(dinitz.get_temp_graph(), "source", "sink")

        row = [
            node_num,
            density_value,
            dinitz_algorithm_value,
            dinitz_algorithm_execution_time,
            edmond_algorithm_value,
            edmond_algorithm_execution_time,
            edmonds_karp_max_flow.graph['flow_value']
        ]
      
        sparse_rows.append(row)

    for i in range(30):
        node_num = nodes_range[i]
        density_value = density[i]
        bipartite_graph.fast_way(num_of_nodes=node_num, density=density_value)

        edmond.set_bipartite_graph(bipartite_graph=bipartite_graph)
        edmond.reduce_to_max_flow()
        edmond.set_algorithm(algorithm=EdmondsKarpAlgorithm)
        start_time = time.time()
        edmond.find_max_matching()
        end_time = time.time()
        edmond_algorithm_execution_time = end_time - start_time
        edmond_algorithm_value = edmond.max_matching_value

        dinitz.set_bipartite_graph(bipartite_graph=bipartite_graph)
        dinitz.reduce_to_max_flow()
        dinitz.set_algorithm(algorithm=DinitzAlgorithm)
        start_time = time.time()
        dinitz.find_max_matching()
        end_time = time.time()
        dinitz_algorithm_execution_time = end_time - start_time
        dinitz_algorithm_value = dinitz.max_matching_value

        edmonds_karp_max_flow = edmonds_karp(dinitz.get_temp_graph(), "source", "sink")
        row = [
            node_num,
            density_value,
            dinitz_algorithm_value,
            dinitz_algorithm_execution_time,
            edmond_algorithm_value,
            edmond_algorithm_execution_time,
            edmonds_karp_max_flow.graph['flow_value']
        ]

        density_rows.append(row)

    create_csv('sparse.csv', columns_name, sparse_rows)
    create_csv('density.csv', columns_name, density_rows)
