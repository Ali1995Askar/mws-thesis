import time
from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_flow.dinitz_solver import DinitzSolver

from app.src.algorithm.max_flow.edmond_karp_solver import EdmondKarpSolver
from app.src.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from app.src.algorithm.max_matching.max_matching_solver import MaxMatchingSolver
from app.src.algorithm.max_matching.heuristics.monte_carlo_algo import MonteCarloAlgo
from app.src.algorithm.max_matching.heuristics.backtracking_algo import BackTrackingAlgo
from app.src.algorithm.max_matching.heuristics.simple_greedy_algo import SimpleGreedyAlgo
from app.src.algorithm.max_matching.heuristics.limit_min_degree_algo import LimitMinDegreeAlgo
from app.src.algorithm.max_matching.heuristics.static_min_degree_algo import StaticMinDegreeAlgo
from app.src.algorithm.max_matching.heuristics.dynamic_min_degree_algo import DynamicMinDegreeAlgo
from app.src.algorithm.max_matching.heuristics.randomized_rounding_algo import RandomizedRoundingAlgo

columns_name = [
    'NUM OF NODES',
    'Density',

    'Backtracking Algorithm Time',
    'Backtracking Algorithm Result',

    'Static Min Degree Time',
    'Static Min Degree Result',

    'Dynamic Min Degree Time',
    'Dynamic Min Degree Result',

    'Limit Min Degree Time',
    'Limit Min Degree Result',

    'Monte Carlo Time',
    'Monte Carlo Result',

    'Randomized Rounding Time',
    'Randomized Rounding Result',

    'Simple Greedy Time',
    'Simple Greedy Result',

    'Max Matching Value'
]
nodes_range = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

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
    0.05,
    # 0.1,
    # 0.18,
    # 0.25,
    # 0.36,
    # 0.42,
    # 0.48,
    # 0.56,
    # 0.62,
    # 0.68,
    # 0.72,
    # 0.78,
    # 0.82,
    # 0.88,
    # 0.92,
    # 0.98,
    # 1
]

if __name__ == '__main__':
    bipartite_graph = BipartiteGraph()
    max_matching = MaxMatchingSolver()

    bipartite_graph.build_manually(
        nodes=[1, 2, 3, 4, 5, 6],
        edges=[
            (1, 4),
            (1, 6),
            (2, 5),
            (3, 5),
            (3, 4),
        ],

    )
    bipartite_graph.split_nodes()
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

    max_matching = MaxMatchingSolver()
    max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
    max_matching.set_solver(solver=FordFulkersonSolver)
    max_matching.reduce_to_max_flow()
    max_matching.find_max_matching()

    row = [

        len(backtracking_algo_result),
        backtracking_algo_time,

        len(static_min_degree_result),
        static_min_degree_time,

    ]
    print(row)

    # create_csv(f'{num_of_nodes}_heuristic_matching.csv', columns=columns_name, data=rows)
