import time

from app.src.algorithm.max_matching.heuristics.dynamic_min_degree import DynamicMinDegree
from app.src.algorithm.max_matching.heuristics.limit_min_degree import LimitMinDegree
from app.src.algorithm.max_matching.heuristics.monte_carlo import MonteCarlo
from app.src.algorithm.max_matching.heuristics.randomized_rounding import RandomizedRounding
from app.src.algorithm.max_matching.heuristics.simple_greedy import SimpleGreedy
from app.src.algorithm.max_matching.heuristics.static_min_degree import StaticMinDegree
from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_matching.max_matching import MaxMatching
from app.src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from app.src.algorithm.max_flow.edmond_karp_algorithm import EdmondKarpAlgorithm
from app.src.algorithm.max_flow.ford_fulkerson_algorithm import FordFulkersonAlgorithm

static_min_degree = 1
dynamic_min_degree = 1
limit_min_degree = 1

monte_carlo = 1
randomized_rounding = 1
simple_greedy = 1

columns_name = [
    'NUM OF NODES',
    'Density',

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

            # Dynamic Min Degree
            static = StaticMinDegree(bipartite_graph=bipartite_graph)
            start_time = time.time()
            static_min_degree_result = static.find_matching_edges()
            end_time = time.time()
            static_min_degree_time = end_time - start_time

            # Dynamic Min Degree
            dynamic = DynamicMinDegree(bipartite_graph=bipartite_graph)
            start_time = time.time()
            dynamic_min_degree_result = dynamic.find_matching_edges()
            end_time = time.time()
            dynamic_min_degree_time = end_time - start_time

            # Limit Min Degree
            limit = LimitMinDegree(bipartite_graph=bipartite_graph)
            start_time = time.time()
            limit_min_degree_result = limit.find_matching_edges()
            end_time = time.time()
            limit_min_degree_time = end_time - start_time

            # Monte Carlo
            monte_carlo = MonteCarlo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            monte_carlo_result = monte_carlo.find_matching_edges()
            end_time = time.time()
            monte_carlo_time = end_time - start_time

            # Randomized Rounding
            randomized_rounding = RandomizedRounding(bipartite_graph=bipartite_graph)
            start_time = time.time()
            randomized_rounding_result = randomized_rounding.find_matching_edges()
            end_time = time.time()
            randomized_rounding_time = end_time - start_time

            # Randomized Rounding
            simple_greedy = SimpleGreedy(bipartite_graph=bipartite_graph)
            start_time = time.time()
            simple_greedy_result = simple_greedy.find_matching_edges()
            end_time = time.time()
            simple_greedy_time = end_time - start_time

            max_matching = MaxMatching()
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
            max_matching.set_algorithm(algorithm=FordFulkersonAlgorithm)
            max_matching.reduce_to_max_flow()
            max_matching.find_max_matching()

            row = [
                num_of_nodes,
                density,

                len(static_min_degree_result),
                static_min_degree_time,

                len(dynamic_min_degree_result),
                dynamic_min_degree_time,

                len(limit_min_degree_result),
                limit_min_degree_time,

                len(monte_carlo_result),
                monte_carlo_time,

                len(randomized_rounding_result),
                randomized_rounding_time,

                len(simple_greedy_result),
                simple_greedy_time,

                max_matching.max_matching_value
            ]
            print(row)
            rows.append(row)
        create_csv(f'{num_of_nodes}_heuristic_matching.csv', columns=columns_name, data=rows)
