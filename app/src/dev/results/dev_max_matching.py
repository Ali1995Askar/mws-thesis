import time
from app.utils.utils import create_csv
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.solvers.max_matching.max_matching_solver import MaxMatchingSolver
from app.src.solvers.max_matching.heuristics.modified_greedy import ModifiedGreedy
from app.src.solvers.max_matching.heuristics.min_degree.limit import LimitMinDegreeHeuristic
from app.src.solvers.max_matching.heuristics.min_degree.static import StaticMinDegreeHeuristic
from app.src.solvers.max_matching.heuristics.min_degree.dynamic import DynamicMinDegreeHeuristic
from app.src.solvers.max_matching.heuristics.random_greedy.monte_carlo import MonteCarloHeuristic
from app.src.solvers.max_matching.heuristics.random_greedy.simple_greedy import SimpleGreedyHeuristic
from app.src.solvers.max_matching.heuristics.random_greedy.randomized_rounding import RandomizedRoundingHeuristic

columns_name = [
    'NUM OF NODES',
    'Density',
    'Max Matching Value',

    'Modified Greedy Result',
    'Optimized Greedy Time',

    'Static Min Degree Result',
    'Static Min Degree Time',

    'Limit Min Degree Result',
    'Limit Min Degree Time',

    'Dynamic Min Degree Result',
    'Dynamic Min Degree Time',

    'Simple Greedy Result',
    'Simple Greedy Time',

    'Rounding Result',
    'Rounding Time',

    'Monte Carlo Result',
    'Monte Carlo Time',

]

nodes_range = [
    # 500,
    # 1000,
    2000,
    4000,
    5000
]

density_range = [
    0.0001,
    0.0002,
    0.0003,
    0.0004,
    0.0005,
    0.0006,
    0.0007,
    0.0008,
    0.0009,

    0.001,
    0.002,
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
    0.08,
    0.09,

    0.1,
    0.18,

    0.2,
    0.28,

    0.3,
    0.38,

    0.4,
    0.48,

    0.5,
    0.58,

    0.6,
    0.68,

    0.7,
    0.78,

    0.8,
    0.88,

    0.9,
    0.98,

]

if __name__ == '__main__':
    bipartite_graph = BipartiteGraph()

    for node in nodes_range:
        rows = []
        num_of_nodes = node

        for density in density_range:
            bipartite_graph.random_build(num_of_nodes=num_of_nodes, density=density)

            max_matching = MaxMatchingSolver()
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
            max_matching.init_ford_fulkerson_solver()
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            first_time = end_time - start_time

            # Limit Min Degree Heuristic
            limit = SimpleGreedyHeuristic(bipartite_graph=bipartite_graph)
            start_time = time.time()
            limit_min_degree_result = limit.get_matching_edges()
            end_time = time.time()
            second_time = end_time - start_time

            max_matching_2 = MaxMatchingSolver()
            max_matching_2.set_bipartite_graph(bipartite_graph=bipartite_graph)
            max_matching_2.init_ford_fulkerson_solver()
            max_matching_2.reduce_to_max_flow()
            max_matching_2.init_heuristic_algorithm(SimpleGreedyHeuristic)
            max_matching_2.build_initial_flow()
            start_time = time.time()
            max_matching_2.find_max_matching()
            end_time = time.time()
            third_time = end_time - start_time

            row = [
                num_of_nodes,
                density,
                max_matching.get_matching_value(),
                first_time,
                second_time,
                third_time,
                max_matching_2.get_matching_value(),

            ]

            print(row)
