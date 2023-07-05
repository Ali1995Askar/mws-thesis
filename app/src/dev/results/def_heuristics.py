import time

from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.problems.max_matching.heuristics.min_degree.dynamic import DynamicMinDegreeHeuristic
from app.src.problems.max_matching.heuristics.min_degree.limit import LimitMinDegreeHeuristic
from app.src.problems.max_matching.heuristics.min_degree.static import StaticMinDegreeHeuristic
from app.src.problems.max_matching.heuristics.optimized_algo import Optimization
from app.src.problems.max_matching.heuristics.random_greedy.randomized_rounding import RandomizedRoundingHeuristic
from app.src.problems.max_matching.heuristics.random_greedy.simple_greedy import SimpleGreedyHeuristic
from app.src.problems.max_matching.heuristics.random_greedy.monte_carlo import MonteCarloHeuristic
from app.src.problems.max_matching.max_matching_solver import MaxMatchingSolver
from app.utils.utils import create_csv

columns_name = [
    'NUM OF NODES',
    'Density',
    'Max Matching Value',

    'Optimized Greedy Algorithm Result',
    'Optimized Greedy Algorithm Time',

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
    #
    # 500,
    # 1000,
    # 2000,
    # 3000,
    # 4000,
    5000
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
    0.78,
    0.82,
    0.88,
    0.92,
    0.98,
    1,

]

if __name__ == '__main__':
    bipartite_graph = BipartiteGraph()

    for node in nodes_range:
        rows = []
        num_of_nodes = node

        for density in density_range:
            bipartite_graph.random_build(num_of_nodes=num_of_nodes, density=density)

            # Optimization Heuristic
            optimization = Optimization(bipartite_graph=bipartite_graph)
            start_time = time.time()
            optimization_result = optimization.get_matching_edges()
            end_time = time.time()
            optimization_time = end_time - start_time

            # Static Min Degree Heuristic
            static = StaticMinDegreeHeuristic(bipartite_graph=bipartite_graph)
            start_time = time.time()
            static_min_degree_result = static.get_matching_edges()
            end_time = time.time()
            static_min_degree_time = end_time - start_time

            # Limit Min Degree Heuristic
            limit = LimitMinDegreeHeuristic(bipartite_graph=bipartite_graph)
            start_time = time.time()
            limit_min_degree_result = limit.get_matching_edges()
            end_time = time.time()
            limit_min_degree_time = end_time - start_time

            # Dynamic Min Degree Heuristic
            dynamic = DynamicMinDegreeHeuristic(bipartite_graph=bipartite_graph)
            start_time = time.time()
            dynamic_min_degree_result = dynamic.get_matching_edges()
            end_time = time.time()
            dynamic_min_degree_time = end_time - start_time

            # Simple Greedy Heuristic
            simple_greedy = SimpleGreedyHeuristic(bipartite_graph=bipartite_graph)
            start_time = time.time()
            simple_greedy_result = simple_greedy.get_matching_edges()
            end_time = time.time()
            simple_greedy_time = end_time - start_time

            # Randomized Rounding Heuristic
            randomized = RandomizedRoundingHeuristic(bipartite_graph=bipartite_graph)
            start_time = time.time()
            randomized_result = randomized.get_matching_edges()
            end_time = time.time()
            randomized_time = end_time - start_time

            # Monte Carlo Heuristic
            monte_carlo = MonteCarloHeuristic(bipartite_graph=bipartite_graph)
            start_time = time.time()
            monte_carlo_result = monte_carlo.get_matching_edges()
            end_time = time.time()
            monte_carlo_time = end_time - start_time

            s1 = []
            assert len(simple_greedy_result) == len(set(simple_greedy_result))
            for u, v in simple_greedy_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)
            assert len(s1) == len(set(s1))

            s1 = []
            assert len(static_min_degree_result) == len(set(static_min_degree_result))
            for u, v in static_min_degree_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)
            assert len(s1) == len(set(s1))

            s1 = []
            assert len(dynamic_min_degree_result) == len(set(dynamic_min_degree_result))
            for u, v in dynamic_min_degree_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)
            assert len(s1) == len(set(s1))

            s1 = []
            assert len(limit_min_degree_result) == len(set(limit_min_degree_result))
            for u, v in limit_min_degree_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)

            s1 = []
            assert len(monte_carlo_result) == len(set(monte_carlo_result))
            for u, v in monte_carlo_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)

            s1 = []
            assert len(randomized_result) == len(set(randomized_result))
            for u, v in randomized_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)

            s1 = []
            assert len(optimization_result) == len(set(optimization_result))
            for u, v in optimization_result:
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                assert u < v
                s1.append(u)
                s1.append(v)

            max_matching = MaxMatchingSolver()
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)
            max_matching.init_ford_fulkerson_solver()
            max_matching.reduce_to_max_flow()
            max_matching.find_max_matching()

            row = [
                num_of_nodes,
                density,
                max_matching.get_matching_value(),

                len(optimization_result),
                round(optimization_time, 5),

                len(static_min_degree_result),
                round(static_min_degree_time, 5),

                len(limit_min_degree_result),
                round(limit_min_degree_time, 5),

                len(dynamic_min_degree_result),
                round(dynamic_min_degree_time, 5),

                len(simple_greedy_result),
                round(simple_greedy_time, 5),

                len(randomized_result),
                round(randomized_time, 5),

                len(monte_carlo_result),
                round(monte_carlo_time, 5),

            ]
            print(row)
            rows.append(row)
        create_csv(filename=f'heuristic_{num_of_nodes}_2.csv', columns=columns_name, data=rows)

# [5000, 0.4, 2500, 2499, 0.03, 2499, 0.2522, 1242, 0.0319, 2498, 0.033, 2500, 20.1529, 2499, 16.8329, 2500, 0.0423]
# [5000, 0.42, 2500, 2500, 0.0179, 2500, 0.0548, 1246, 0.01, 2499, 0.0284, 2500, 24.9447, 2500, 22.4043, 2500, 0.0359]
# [5000, 0.44, 2500, 2498, 0.0326, 2498, 0.1945, 1294, 0.0609, 2499, 0.0788, 2500, 36.2585, 2498, 32.4378, 2500, 0.0403]
# [5000, 0.48, 2500, 2499, 0.0352, 2499, 0.1077, 1299, 0.0189, 2499, 0.0478, 2500, 38.1094, 2499, 34.9218, 2500, 0.0372]
# [5000, 0.52, 2500, 2498, 0.028, 2498, 0.2059, 1253, 0.0249, 2499, 0.0593, 2500, 41.844, 2498, 36.1722, 2500, 0.0294]
# [5000, 0.56, 2500, 2500, 0.0574, 2500, 0.7664, 1248, 0.0223, 2499, 0.1359, 2500, 44.8532, 2500, 39.7203, 2500, 0.0699]
# [5000, 0.62, 2500, 2500, 0.0807, 2500, 0.551, 1233, 0.0323, 2500, 0.697, 2500, 58.9613, 2500, 48.3803, 2500, 0.0677]
# [5000, 0.68, 2500, 2499, 0.0788, 2499, 0.2251, 1241, 0.0369, 2500, 0.1431, 2500, 60.8774, 2499, 55.3816, 2500, 0.0595]
# [5000, 0.72, 2500, 2499, 0.1497, 2499, 0.2703, 1211, 0.0269, 2499, 0.8899, 2500, 67.5356, 2499, 59.0381, 2500, 0.066]
