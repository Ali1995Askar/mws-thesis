import time
from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_flow.dinitz_solver import DinitzSolver
from app.src.algorithm.max_flow.edmond_karp_solver import EdmondKarpSolver
from app.src.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from app.src.algorithm.max_matching.max_matching_solver import MaxMatchingSolver

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
nodes_range = [

    1000,
    1500,
    2000,
    2500,
    3000,
    3500,
    4000,
    4500,
    5000,
    5500,
    6000,
    6500,
    7000,
    7500,
    8000,
    8500,
    9000,
    9500,
    10000
]

density_range = [
    0.0001,
    0.0002,
    0.0004,
    0.0007,
    0.001,
    0.003,
    0.005,
    0.008,
    0.01,
    0.02,
    0.05,
    0.07,
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
    max_matching = MaxMatchingSolver()

    for node in nodes_range:
        rows = []
        num_of_nodes = node
        for density in density_range:
            bipartite_graph.random_build(num_of_nodes=num_of_nodes, density=density)
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
            max_matching.reduce_to_max_flow()

            # FordFulkerson Algorithm
            max_matching.set_solver(solver=FordFulkersonSolver)
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            ford_fulkerson_algorithm_execution_time = end_time - start_time
            ford_fulkerson_algorithm_value = max_matching.max_matching_value

            # EdmondKarp Algorithm
            max_matching.set_solver(solver=EdmondKarpSolver)
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            edmond_algorithm_execution_time = end_time - start_time
            edmond_algorithm_value = max_matching.max_matching_value

            # Dinitz Algorithm
            max_matching.set_solver(solver=DinitzSolver)
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            dinitz_algorithm_execution_time = end_time - start_time
            dinitz_algorithm_value = max_matching.max_matching_value

            R = edmonds_karp(max_matching.temp_graph.graph, 'source', 'sink')

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
        create_csv(f'{num_of_nodes}_max_flow.csv', columns=columns_name, data=rows)
