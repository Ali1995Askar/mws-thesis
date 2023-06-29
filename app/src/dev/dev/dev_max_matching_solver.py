import time

from app.src.dev.graph.bipartite_graph import BipartiteGraph
from app.src.dev.max_matching.heuristics.min_degree.dynamic import DynamicMinDegreeHeuristic
from app.src.dev.max_matching.heuristics.min_degree.limit import LimitMinDegreeHeuristic
from app.src.dev.max_matching.heuristics.min_degree.static import StaticMinDegreeHeuristic
from app.src.dev.max_matching.heuristics.optimized_algo import Optimization
from app.src.dev.max_matching.heuristics.random_greedy.randomized_rounding import RandomizedRoundingHeuristic
from app.src.dev.max_matching.heuristics.random_greedy.simple_greedy import SimpleGreedyHeuristic
from app.src.dev.max_matching.heuristics.random_greedy.monte_carlo import MonteCarloHeuristic
from src.dev.max_matching.max_matching_solver import MaxMatchingSolver

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
nodes_range = [
    30,
    500,
    # 1000,
    # 2000,
    # 3000,
    # 4000,
    # 5000
]

density_range = [
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
    solver = MaxMatchingSolver()
    for node in nodes_range:

        rows = []
        num_of_nodes = node

        for density in density_range:
            bipartite_graph.random_build(num_of_nodes=num_of_nodes, density=density)
            solver.set_bipartite_graph(bipartite_graph=bipartite_graph)
            solver.init_ford_fulkerson_solver()
            solver.init_heuristic_algorithm(heuristic_algorithm=Optimization)
            solver.reduce_to_max_flow()
            solver.build_initial_flow()

            start_time = time.time()
            solver.find_max_matching()
            end_time = time.time()
            mixin_time = end_time - start_time
            mixin_matching_value = solver.get_matching_value()
            s1 = []
            for u, v in solver.get_max_matching_edges():
                assert u in bipartite_graph.red_nodes
                assert v in bipartite_graph.blue_nodes
                assert bipartite_graph.has_edge_with_positive_capacity(u, v)
                assert u not in ['source', 'sink']
                assert v not in ['source', 'sink']
                s1.append(u)
            assert len(s1) == len(set(s1))
            #     s1.append(v)
            # Optimization Heuristic
            # optimization = Optimization(bipartite_graph=bipartite_graph)
            # start_time = time.time()
            # optimization_result = optimization.get_matching_edges()
            # end_time = time.time()
            # optimization_time = end_time - start_time

            # s1 = []
            # assert len(simple_greedy_result) == len(set(simple_greedy_result))
            # for u, v in simple_greedy_result:
            #     assert bipartite_graph.has_edge_with_positive_capacity(u, v)
            #     assert u in bipartite_graph.red_nodes
            #     assert v in bipartite_graph.blue_nodes
            #     assert u not in ['source', 'sink']
            #     assert v not in ['source', 'sink']
            #     assert u < v
            #     s1.append(u)
            #     s1.append(v)
            # assert len(s1) == len(set(s1))

            row = [
                num_of_nodes,
                density,
                mixin_time,
                mixin_matching_value,

                #
                # f'greedy {len(simple_greedy_result)}',
                # f'monte_carlo {len(monte_carlo_result)}',
                # f'randomized {len(randomized_result)}',
                #
                # f'static {len(static_min_degree_result)}',
                # f'limit {len(limit_min_degree_result)}',
                # f'dynamic {len(dynamic_min_degree_result)}',
                #
                # f'optimization {len(optimization_result)}',
                #
                # '==========> ',
                #
                # f'greedy {round(simple_greedy_time, 4)}',
                # f'monte_carlo {round(monte_carlo_time, 4)}',
                # f'randomized {round(randomized_time, 4)}',
                #
                # f'static {round(static_min_degree_time, 4)}',
                # f'limit {round(limit_min_degree_time, 4)}',
                # f'dynamic {round(dynamic_min_degree_time, 4)}',
                #
                # f'optimization {round(optimization_time, 4)}',

            ]
            print(row)
