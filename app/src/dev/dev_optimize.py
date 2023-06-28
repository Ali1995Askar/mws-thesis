import time

from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph

from app.src.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from app.src.algorithm.max_matching.max_matching_solver import MaxMatchingSolver
from app.src.algorithm.max_matching.heuristics.monte_carlo_algo import MonteCarloAlgo
from app.src.algorithm.max_matching.heuristics.backtracking_algo import BackTrackingAlgo
from app.src.algorithm.max_matching.heuristics.simple_greedy_algo import SimpleGreedyAlgo
from app.src.algorithm.max_matching.heuristics.limit_min_degree_algo import LimitMinDegreeAlgo
from app.src.algorithm.max_matching.heuristics.static_min_degree_algo import StaticMinDegreeAlgo
from app.src.algorithm.max_matching.heuristics.dynamic_min_degree_algo import DynamicMinDegreeAlgo
from app.src.algorithm.max_matching.heuristics.randomized_rounding_algo import RandomizedRoundingAlgo
from src.algorithm.max_matching.heuristics.optimized_algo import OptimizedAlgo

columns_name = [
    'NUM OF NODES',
    'Density',
    'Max Matching Value',

    'Backtracking Algorithm Result',
    'Backtracking Algorithm Time',

    'Static Min Degree Result',
    'Static Min Degree Time',

    'Dynamic Min Degree Result',
    'Dynamic Min Degree Time',

    'Limit Min Degree Result',
    'Limit Min Degree Time',

    'Simple Greedy Result',
    'Simple Greedy Time',

    'Monte Carlo Result',
    'Monte Carlo Time',

    'Rounding Result',
    'Rounding Time',

]
nodes_range = [200, 400, 600, 700, 900]

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
    0.006,
    0.007,
    0.008,
    0.009,
    0.01,
    0.02,
    0.03,
    0.04,
    0.05,
    0.06,
    0.07,
    0.09,
    0.1,
    0.18,
    0.25,
    0.36,
    0.4,
    0.42,
    0.44,
    0.48,
    0.52,
    0.56,
    0.62,
    0.68,
    0.72,

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

            # Backtracking Algorithm
            backtracking_algo = BackTrackingAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            backtracking_algo_result = backtracking_algo.find_matching_edges()
            end_time = time.time()
            backtracking_algo_time = end_time - start_time

            # Static Min Degree
            static = StaticMinDegreeAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            static_min_degree_result = static.find_matching_edges()
            end_time = time.time()
            static_min_degree_time = end_time - start_time

            # Dynamic Min Degree
            dynamic = DynamicMinDegreeAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            dynamic_min_degree_result = dynamic.find_matching_edges()
            end_time = time.time()
            dynamic_min_degree_time = end_time - start_time

            # OptimizedAlgo
            optimized = OptimizedAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            optimized_result = optimized.find_matching_edges()
            end_time = time.time()
            optimized_time = end_time - start_time
            row = [
                num_of_nodes,
                density,

                len(optimized_result),
                len(backtracking_algo_result),
                len(dynamic_min_degree_result),
                len(static_min_degree_result),
                '=======================================================',
                round(optimized_time, 3),
                round(backtracking_algo_time, 3),
                round(dynamic_min_degree_time, 3),
                round(static_min_degree_time, 3),

            ]
            print(row)
            rows.append(row)
        # create_csv(f'{num_of_nodes}_heuristic_matching.csv', columns=columns_name, data=rows)
