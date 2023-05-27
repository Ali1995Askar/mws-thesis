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

            # Limit Min Degree
            limit = LimitMinDegreeAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            limit_min_degree_result = limit.find_matching_edges()
            end_time = time.time()
            limit_min_degree_time = end_time - start_time

            # Monte Carlo
            monte_carlo = MonteCarloAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            monte_carlo_result = monte_carlo.find_matching_edges()
            end_time = time.time()
            monte_carlo_time = end_time - start_time

            # Randomized Rounding
            randomized_rounding = RandomizedRoundingAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            randomized_rounding_result = randomized_rounding.find_matching_edges()
            end_time = time.time()
            randomized_rounding_time = end_time - start_time

            # Randomized Rounding
            simple_greedy = SimpleGreedyAlgo(bipartite_graph=bipartite_graph)
            start_time = time.time()
            simple_greedy_result = simple_greedy.find_matching_edges()
            end_time = time.time()
            simple_greedy_time = end_time - start_time

            max_matching = MaxMatchingSolver()
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
            max_matching.set_solver(solver=FordFulkersonSolver)
            max_matching.reduce_to_max_flow()
            max_matching.find_max_matching()

            bipartite_graph.split_nodes()
            #
            s1 = []
            s2 = []
            s3 = []
            s4 = []
            s5 = []
            s6 = []
            assert len(backtracking_algo_result) == len(set(backtracking_algo_result))
            for u, v in backtracking_algo_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)
            assert len(s1) == len(set(s1))
            #
            for u, v in static_min_degree_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s2.append(u)
                s2.append(v)
            assert len(s2) == len(set(s2))

            for u, v in dynamic_min_degree_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s3.append(u)
                s3.append(v)
            assert len(s2) == len(set(s2))

            for u, v in limit_min_degree_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s4.append(u)
                s4.append(v)
            assert len(s4) == len(set(s4))

            for u, v in randomized_rounding_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s5.append(u)
                s5.append(v)
            assert len(s5) == len(set(s5))

            for u, v in simple_greedy_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                s6.append(u)
                s6.append(v)
            assert len(s6) == len(set(s6))

            row = [
                num_of_nodes,
                density,

                len(backtracking_algo_result),
                backtracking_algo_time,

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
