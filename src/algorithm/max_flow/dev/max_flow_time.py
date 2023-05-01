import random
import time

import networkx

from src.algorithm.max_flow.ford_fulkerson import FordFulkersonAlgorithm
from src.graph.bipartite_graph import BipartiteGraph
from src.algorithm.max_matching.max_matching import MaxMatching
# from src.algorithm.max_flow.core.edmonds_karp import edmonds_karp
from src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from src.algorithm.max_flow.edmond_karp_algorithm import EdmondsKarpAlgorithm

from networkx.algorithms.flow import edmonds_karp

from utils.utils import create_csv

columns_name = [
    'NUM OF NODES',
    'Density',
    'Ford-Fulkerson Result',
    'Ford-Fulkerson Execution Time',
    'Edmond-Karp Result',
    'Edmond-Karp Execution Time',
    'Dinitz Result',
    'Dinitz Execution Time',
    'Max Matching Value'
]
nodes_range = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
density_range = [0.009,
                 0.01,
                 0.015,
                 0.04,
                 0.09,
                 0.1,
                 0.16,
                 0.26,
                 0.32,
                 0.4,
                 0.44,
                 0.5,
                 0.56,
                 0.62,
                 0.68,
                 0.74,
                 0.8,
                 0.84,
                 0.89,
                 0.92,
                 0.98,
                 1]

if __name__ == '__main__':
    bipartite_graph = BipartiteGraph()
    max_matching = MaxMatching()

    for node in nodes_range:
        rows = []
        for density in density_range:
            bipartite_graph.random_build(num_of_nodes=node, density=density)
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)

            max_matching.set_algorithm(algorithm=FordFulkersonAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            ford_fulkerson_algorithm_execution_time = end_time - start_time
            ford_fulkerson_algorithm_value = max_matching.max_matching_value

            max_matching.set_algorithm(algorithm=EdmondsKarpAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            edmond_algorithm_execution_time = end_time - start_time
            edmond_algorithm_value = max_matching.max_matching_value

            max_matching.set_algorithm(algorithm=DinitzAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            dinitz_algorithm_execution_time = end_time - start_time
            dinitz_algorithm_value = max_matching.max_matching_value
            R = edmonds_karp(max_matching.get_temp_graph(), 'source', 'sink')
            row = [
                node,
                density,
                ford_fulkerson_algorithm_value,
                ford_fulkerson_algorithm_execution_time,
                edmond_algorithm_value,
                edmond_algorithm_execution_time,
                dinitz_algorithm_value,
                dinitz_algorithm_execution_time,
                R.graph['flow_value']
            ]
            print(row)
            rows.append(row)
        create_csv(f'{node}.csv', columns=columns_name, data=rows)
