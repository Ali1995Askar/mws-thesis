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
    # 2000,
    # 3000,
    # 4000,
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

            # Modified Greedy Heuristic
            modified_greedy = ModifiedGreedy(bipartite_graph=bipartite_graph)
            start_time = time.time()
            modified_greedy_result = modified_greedy.get_matching_edges()
            end_time = time.time()
            modified_greedy_time = end_time - start_time

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
            assert len(modified_greedy_result) == len(set(modified_greedy_result))
            for u, v in modified_greedy_result:
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

                len(modified_greedy_result),
                round(modified_greedy_time, 5),

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
            print(row[:3], '===>', row[3::])
            rows.append(row)
        create_csv(filename=f'heuristic_{num_of_nodes}.csv', columns=columns_name, data=rows)

# [4000, 0.0001, 328] ===> [328, 0.00098, 328, 0.01097, 328, 1.31835, 328, 1.27442, 326, 0.00092, 172, 0.001, 327, 0.00598]
# [4000, 0.0002, 597] ===> [596, 0.001, 596, 0.00257, 597, 2.56114, 597, 2.37927, 588, 0.001, 308, 0.001, 587, 0.00897]
# [4000, 0.0003, 777] ===> [773, 0.00091, 773, 0.00199, 777, 2.19254, 777, 2.17757, 750, 0.00096, 427, 0.001, 750, 0.00691]
# [4000, 0.0004, 948] ===> [943, 0.00197, 940, 0.003, 948, 2.68405, 948, 2.78136, 907, 0.00312, 507, 0.00099, 908, 0.00908]
# [4000, 0.0005, 1090] ===> [1075, 0.001, 1069, 0.00297, 1090, 2.66426, 1090, 2.72945, 1025, 0.00112, 585, 0.001, 1025, 0.00997]
# [4000, 0.0006, 1201] ===> [1182, 0.00199, 1173, 0.00199, 1201, 2.67214, 1201, 2.69004, 1114, 0.001, 628, 0.001, 1114, 0.00997]
# [4000, 0.0007, 1284] ===> [1261, 0.00299, 1250, 0.00598, 1284, 3.12208, 1284, 3.16229, 1160, 0.00199, 671, 0.001, 1169, 0.02098]
# [4000, 0.0008, 1392] ===> [1355, 0.00299, 1332, 0.00399, 1392, 3.17848, 1392, 2.51713, 1261, 0.001, 733, 0.001, 1256, 0.00997]
# [4000, 0.0009, 1486] ===> [1445, 0.00299, 1409, 0.03287, 1486, 2.94405, 1486, 2.83291, 1334, 0.00198, 742, 0.00199, 1331, 0.01196]
# [4000, 0.001, 1571] ===> [1512, 0.00189, 1483, 0.00299, 1571, 1.99396, 1571, 1.99649, 1378, 0.00199, 785, 0.00199, 1387, 0.01098]
# [4000, 0.002, 1961] ===> [1826, 0.00299, 1782, 0.00407, 1928, 1.17638, 1928, 1.13827, 1646, 0.00199, 945, 0.001, 1669, 0.01395]
# [4000, 0.003, 1995] ===> [1932, 0.00299, 1857, 0.00399, 1966, 1.01002, 1966, 1.01416, 1774, 0.00259, 993, 0.001, 1787, 0.01694]
# [4000, 0.004, 1999] ===> [1970, 0.00419, 1894, 0.00399, 1985, 1.04065, 1985, 1.09368, 1844, 0.001, 970, 0.00098, 1837, 0.02193]
# [4000, 0.005, 2000] ===> [1984, 0.00399, 1915, 0.00598, 1980, 1.05029, 1980, 1.05993, 1867, 0.00199, 1016, 0.001, 1861, 0.02194]
# [4000, 0.006, 2000] ===> [1986, 0.00399, 1920, 0.00497, 1986, 1.0849, 1986, 1.17076, 1888, 0.00199, 1011, 0.001, 1896, 0.02798]
# [4000, 0.007, 2000] ===> [1990, 0.004, 1943, 0.00598, 1986, 1.37829, 1986, 1.26846, 1914, 0.00199, 995, 0.001, 1914, 0.11063]
# [4000, 0.008, 2000] ===> [1994, 0.00299, 1942, 0.00498, 1995, 1.13327, 1995, 1.24365, 1904, 0.00199, 1008, 0.001, 1913, 0.03289]
# [4000, 0.009, 2000] ===> [1995, 0.004, 1942, 0.00498, 1995, 1.25355, 1995, 1.15103, 1922, 0.00199, 1007, 0.001, 1930, 0.03886]
# [4000, 0.01, 2000] ===> [1995, 0.00399, 1949, 0.00498, 1994, 1.19376, 1994, 1.21439, 1928, 0.00144, 981, 0.001, 1946, 0.03994]
# [4000, 0.02, 2000] ===> [2000, 0.00399, 1975, 0.00498, 1967, 0.50694, 1998, 1.56726, 1969, 0.00299, 1018, 0.00199, 1966, 0.07762]
# [4000, 0.03, 2000] ===> [2000, 0.00498, 1981, 0.01296, 1984, 0.76349, 1999, 1.92275, 1984, 0.00408, 988, 0.00199, 1979, 0.10854]
# [4000, 0.04, 2000] ===> [2000, 0.00797, 1987, 0.01794, 1986, 1.12107, 2000, 2.29146, 1986, 0.00524, 984, 0.00199, 1985, 0.1465]
# [4000, 0.05, 2000] ===> [2000, 0.00596, 1990, 0.02313, 1988, 1.77283, 1998, 2.97113, 1988, 0.00498, 995, 0.00299, 1990, 0.18009]
# [4000, 0.06, 2000] ===> [2000, 0.00632, 1989, 0.00997, 1991, 1.77001, 2000, 4.7662, 1991, 0.00498, 1000, 0.00243, 1991, 0.23703]
# [4000, 0.07, 2000] ===> [2000, 0.00698, 1991, 0.0322, 1989, 2.11738, 1999, 3.48599, 1989, 0.00766, 976, 0.00299, 1992, 0.30889]
# [4000, 0.08, 2000] ===> [2000, 0.00545, 1995, 0.03688, 1991, 2.81318, 2000, 4.25659, 1991, 0.00797, 1009, 0.00563, 1994, 0.47277]
# [4000, 0.09, 2000] ===> [2000, 0.00598, 1993, 0.03598, 1990, 2.40823, 1999, 3.57393, 1990, 0.00598, 997, 0.00199, 1992, 0.28505]
# [4000, 0.1, 2000] ===> [2000, 0.00607, 1992, 0.03796, 1992, 2.51315, 1999, 3.57659, 1992, 0.00496, 993, 0.00199, 1995, 0.29567]
# [4000, 0.18, 2000] ===> [2000, 0.00805, 1997, 0.01595, 1995, 4.92939, 2000, 6.30961, 1995, 0.00698, 1022, 0.00399, 1998, 0.59495]
# [4000, 0.2, 2000] ===> [2000, 0.00794, 1999, 0.06913, 1997, 5.34737, 2000, 6.97868, 1997, 0.00698, 987, 0.00399, 1999, 0.79481]
# [4000, 0.28, 2000] ===> [2000, 0.02192, 1998, 0.03947, 1998, 14.21786, 2000, 16.3504, 1998, 0.01496, 983, 0.00797, 1999, 1.74125]
# [4000, 0.3, 2000] ===> [2000, 0.01765, 1998, 0.16209, 1998, 13.54099, 2000, 16.20662, 1998, 0.0162, 1058, 0.01552, 1999, 1.66434]
# [4000, 0.38, 2000] ===> [2000, 0.01593, 1999, 0.0508, 1999, 16.70076, 2000, 23.28882, 1999, 0.01694, 973, 0.02154, 1999, 1.40516]
# [4000, 0.4, 2000] ===> [2000, 0.01396, 1999, 0.20005, 2000, 14.48694, 2000, 23.38951, 2000, 0.02484, 975, 0.02684, 1999, 1.97459]
# [4000, 0.48, 2000] ===> [2000, 0.02331, 1999, 0.24937, 1998, 18.02928, 2000, 20.66849, 1998, 0.01725, 1014, 0.03114, 2000, 2.84516]
# [4000, 0.5, 2000] ===> [2000, 0.01495, 1999, 0.04138, 1999, 18.13476, 2000, 23.366, 1999, 0.01802, 1028, 0.02155, 2000, 2.27169]
# [4000, 0.58, 2000] ===> [2000, 0.03695, 1999, 0.05178, 1999, 21.38737, 2000, 28.16495, 1999, 0.06641, 941, 0.07707, 2000, 1.93816]
# [4000, 0.6, 2000] ===> [2000, 0.04114, 2000, 0.07322, 2000, 34.13669, 2000, 27.17966, 2000, 0.06869, 1016, 0.02155, 2000, 2.67288]
# [4000, 0.68, 2000] ===> [2000, 0.06124, 2000, 0.07051, 1999, 29.55591, 2000, 34.46184, 1999, 0.05663, 1019, 0.02343, 2000, 2.26841]
# [4000, 0.7, 2000] ===> [2000, 0.086, 2000, 0.06217, 2000, 38.04498, 2000, 35.33359, 2000, 0.09932, 1032, 0.03273, 2000, 2.53835]
# [4000, 0.78, 2000] ===> [2000, 0.03458, 2000, 0.06797, 1999, 30.4496, 2000, 37.14268, 1999, 0.2497, 999, 0.01903, 2000, 3.14241]
# [4000, 0.8, 2000] ===> [2000, 0.02798, 2000, 0.34642, 2000, 35.30744, 2000, 37.43941, 2000, 0.04255, 975, 0.03435, 2000, 4.16661]
# [4000, 0.88, 2000] ===> [2000, 0.0223, 2000, 0.06863, 2000, 29.32982, 2000, 35.02812, 2000, 0.03807, 979, 0.01918, 2000, 4.33512]
# [4000,0.9,2000,2000,0.02493,2000,0.34584,2000,28.94743,2000,35.7784,2000,0.03181,994,0.02791,2000,3.37042]
# [4000,0.98,2000,2000,0.03977,2000,0.38996,2000,31.3448,2000,33.45249,2000,0.03289,1002,0.01905,2000,4.31258]
#############################################################################################################

# [5000, 0.0001, 508] ===> [508, 0.00201, 508, 0.00304, 508, 5.6674, 508, 4.85013, 504, 0.00111, 266, 0.001, 507, 0.01671]
# [5000, 0.0002, 864] ===> [863, 0.002, 863, 0.002, 864, 4.44887, 864, 7.75189, 839, 0.00321, 423, 0.00306, 848, 0.02422]
# [5000, 0.0003, 1134] ===> [1125, 0.004, 1120, 0.004, 1134, 10.17606, 1134, 11.46194, 1081, 0.00855, 604, 0.006, 1085, 0.0386]
# [5000, 0.0004, 1369] ===> [1360, 0.00209, 1353, 0.00503, 1369, 5.85628, 1369, 7.09482, 1289, 0.00101, 717, 0.001, 1280, 0.016]
# [5000, 0.0005, 1553] ===> [1533, 0.002, 1518, 0.005, 1553, 5.62017, 1553, 8.23424, 1442, 0.00278, 817, 0.001, 1452, 0.01524]
# [5000, 0.0006, 1698] ===> [1657, 0.003, 1635, 0.00515, 1698, 5.64425, 1698, 7.11555, 1547, 0.00208, 873, 0.002, 1531, 0.0126]
# [5000, 0.0007, 1835] ===> [1791, 0.004, 1754, 0.00498, 1835, 5.36358, 1835, 4.66213, 1654, 0.00202, 931, 0.001, 1656, 0.01498]
# [5000, 0.0008, 1939] ===> [1856, 0.004, 1826, 0.005, 1939, 4.50795, 1939, 4.48443, 1707, 0.00198, 953, 0.001, 1710, 0.01697]
# [5000, 0.0009, 2064] ===> [1963, 0.00302, 1924, 0.00622, 2064, 4.17797, 2064, 3.85413, 1799, 0.002, 1011, 0.00137, 1801, 0.015]
# [5000, 0.001, 2134] ===> [2006, 0.003, 1957, 0.003, 2133, 3.32184, 2133, 3.80918, 1824, 0.00252, 1071, 0.001, 1831, 0.01511]
# [5000, 0.002, 2473] ===> [2367, 0.004, 2290, 0.007, 2448, 2.33213, 2448, 2.22507, 2145, 0.00301, 1221, 0.002, 2163, 0.02329]
# [5000, 0.003, 2497] ===> [2446, 0.00771, 2357, 0.00665, 2477, 2.2637, 2477, 2.82338, 2293, 0.00411, 1267, 0.0042, 2294, 0.17745]
# [5000, 0.004, 2500] ===> [2471, 0.00292, 2385, 0.00678, 2473, 1.8151, 2473, 2.07698, 2336, 0.003, 1215, 0.00097, 2340, 0.03433]
# [5000, 0.005, 2500] ===> [2484, 0.00498, 2405, 0.00698, 2482, 2.19436, 2482, 2.06388, 2354, 0.00407, 1237, 0.001, 2361, 0.04153]
# [5000, 0.006, 2500] ===> [2491, 0.00792, 2429, 0.008, 2486, 2.18063, 2486, 2.09573, 2386, 0.00417, 1247, 0.00314, 2391, 0.04543]
# [5000, 0.007, 2500] ===> [2493, 0.00559, 2436, 0.00593, 2487, 2.11869, 2487, 2.1146, 2404, 0.004, 1250, 0.00301, 2410, 0.05423]
# [5000, 0.008, 2500] ===> [2493, 0.006, 2443, 0.008, 2492, 2.09553, 2492, 2.06898, 2416, 0.003, 1271, 0.003, 2412, 0.05052]
# [5000, 0.009, 2500] ===> [2496, 0.005, 2451, 0.006, 2494, 2.77371, 2494, 2.31405, 2424, 0.00308, 1279, 0.003, 2431, 0.053]
# [5000, 0.01, 2500] ===> [2498, 0.00499, 2452, 0.00797, 2437, 0.68475, 2491, 2.14187, 2435, 0.003, 1248, 0.0011, 2429, 0.0756]


# edges = self.bipartite_graph.graph.edges(data=True)
#
#       red_nodes = self.bipartite_graph.red_nodes
#       blue_nodes = self.bipartite_graph.blue_nodes
#
#       for u, v, d in edges:
#
#           if v in red_nodes and u in blue_nodes:
#               self.temp_graph.graph[u][v]['capacity'] = 0
#
#       #     if u in red_nodes:
#       #         self.temp_graph.add_edge('source', u)
#       #         self.temp_graph.add_edge(u, 'source', capacity=0)
#       #
#       #     if v in blue_nodes:
#       #         self.temp_graph.add_edge(v, 'sink')
#       #         self.temp_graph.add_edge('sink', v, capacity=0)
#       #
#       #     if u in blue_nodes:
#       #         self.temp_graph.add_edge(u, 'sink')
#       #         self.temp_graph.add_edge('sink', u, capacity=0)
#       #
#       #     if v in blue_nodes:
#       #         self.temp_graph.add_edge(v, 'sink')
#       #         self.temp_graph.add_edge('sink', v, capacity=0)
#       #
#       # source_red_edges = [('source', u) for u in red_nodes]
#       # self.temp_graph.graph.add_edges_from(source_red_edges, capacity=0)
