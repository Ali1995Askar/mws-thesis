import time

from app.src.algorithm.max_matching.heuristics.backtracking_algo import BackTrackingAlgo
from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from app.src.algorithm.max_matching.max_matching_solver import MaxMatchingSolver
from src.algorithm.max_matching.heuristics.dynamic_min_degree_algo import DynamicMinDegreeAlgo
from src.algorithm.max_matching.heuristics.static_min_degree_algo import StaticMinDegreeAlgo

columns_name = [
    'NUM OF NODES',
    'Density',
    'Ford-Fulkerson Execution Time',
    'Heuristic Execution Time',
    'Mixin Execution Time',
    'Matching Value',
    'Max Matching Value'
]
nodes_range = [
    500,
    1000,
    1500,
    2000,
    2500,
    3000,
    3500,
    4000,

]

density_range = [
    0.0001,
    0.0002,
    0.0004,
    0.0007,
    0.0009,
    0.001,
    0.003,
    0.004,
    0.005,
    0.007,
    0.009,
    0.01,
    0.02,
    0.03,
    0.05,
    0.06,
    0.07,
    0.08,
    0.09,
    0.1,
    0.18,
    0.25,
    0.36,
    0.38,
    0.4,
    0.42,
    0.44,
    0.46,
    0.48,
    0.52,
    0.56,
    0.62,
    0.68,
    0.72,
    0.78,
    0.82,
    0.85,
    0.88,
    0.92,
    0.94,
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
            bipartite_graph = BipartiteGraph()
            max_matching = MaxMatchingSolver()

            bipartite_graph.random_build(num_of_nodes=num_of_nodes, density=density)
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
            max_matching.reduce_to_max_flow()

            # FordFulkerson Algorithm
            max_matching.set_solver(solver=FordFulkersonSolver)
            max_matching.set_initial_flow(BackTrackingAlgo)
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            mixin_time = end_time - start_time
            mixin_matching_value = max_matching.max_matching_value

            # FordFulkerson StaticMinDegreeAlgo Algorithm
            max_matching.set_solver(solver=FordFulkersonSolver)
            max_matching.set_initial_flow(StaticMinDegreeAlgo)
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            mixin_time_2 = end_time - start_time
            mixin_matching_value_2 = max_matching.max_matching_value

            # FordFulkerson StaticMinDegreeAlgo Algorithm
            max_matching.set_solver(solver=FordFulkersonSolver)
            max_matching.set_initial_flow(DynamicMinDegreeAlgo)
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            mixin_time_3 = end_time - start_time
            mixin_matching_value_3 = max_matching.max_matching_value

            row = [
                num_of_nodes,
                density,
                round(mixin_time, 3),
                round(mixin_time_2, 3),
                round(mixin_time_3, 3),
            ]
            print(row)
            rows.append(row)
        # create_csv(f'{num_of_nodes}_mixin_matching.csv', columns=columns_name, data=rows)
