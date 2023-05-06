import time
from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_matching.max_matching import MaxMatching
from app.src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from app.src.algorithm.max_flow.edmond_karp_algorithm import EdmondKarpAlgorithm
from app.src.algorithm.max_flow.ford_fulkerson_algorithm import FordFulkersonAlgorithm

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

density_range = [
    0.0001,
    0.0009,
    0.009,
    0.05,
    0.1,
    0.18,
    0.25,
    0.36,
    0.42,
    0.48,
    0.56,
    0.62,
    0.68,
    0.72,
    0.78,
    0.82,
    0.88,
    0.92,
    0.98,
    1
]

if __name__ == '__main__':
    bipartite_graph = BipartiteGraph()
    max_matching = MaxMatching()

    for node in nodes_range:
        rows = []
        num_of_nodes = node
        for density in density_range:
            bipartite_graph.random_build(num_of_nodes=num_of_nodes, density=density)
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)

            max_matching.set_algorithm(algorithm=FordFulkersonAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            ford_fulkerson_algorithm_execution_time = end_time - start_time
            ford_fulkerson_algorithm_value = max_matching.max_matching_value

            max_matching.set_algorithm(algorithm=EdmondKarpAlgorithm)
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
                num_of_nodes,
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
        create_csv(f'edmond_{num_of_nodes}.csv', columns=columns_name, data=rows)


