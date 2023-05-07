import time
from app.utils.utils import create_csv
from networkx.algorithms.flow import edmonds_karp
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_matching.max_matching import MaxMatching
from app.src.algorithm.max_flow.dinitz_algorithm import DinitzAlgorithm
from app.src.algorithm.max_flow.edmond_karp_algorithm import EdmondKarpAlgorithm
from app.src.algorithm.max_flow.ford_fulkerson_algorithm import FordFulkersonAlgorithm

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
    # 500,
    # 1000,
    # 1500,
    # 2000,
    # 2500,
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
    1000
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
            print(bipartite_graph.graph)
            max_matching.set_bipartite_graph(bipartite_graph=bipartite_graph)

            # FordFulkerson Algorithm
            max_matching.set_algorithm(algorithm=FordFulkersonAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            ford_fulkerson_algorithm_execution_time = end_time - start_time
            ford_fulkerson_algorithm_value = max_matching.max_matching_value

            # EdmondKarp Algorithm
            max_matching.set_algorithm(algorithm=EdmondKarpAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            edmond_algorithm_execution_time = end_time - start_time
            edmond_algorithm_value = max_matching.max_matching_value

            # Dinitz Algorithm
            max_matching.set_algorithm(algorithm=DinitzAlgorithm)
            max_matching.reduce_to_max_flow()
            start_time = time.time()
            max_matching.find_max_matching()
            end_time = time.time()
            dinitz_algorithm_execution_time = end_time - start_time
            dinitz_algorithm_value = max_matching.max_matching_value

            R = edmonds_karp(max_matching.get_temp_graph(), 'source', 'sink')

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

# [3000, 0.0001, 198, 0.0372011661529541, 198, 0.06392836570739746, 198, 0.07407093048095703, 198]
# [3000, 0.0002, 352, 0.1040031909942627, 352, 0.18368268013000488, 352, 0.2120814323425293, 352]
# [3000, 0.0004, 588, 0.22624635696411133, 588, 0.48919224739074707, 588, 0.6068003177642822, 588]
# [3000, 0.0007, 862, 0.4985377788543701, 862, 1.2270710468292236, 862, 1.451869010925293, 862]
# [3000, 0.001, 1020, 0.8139092922210693, 1020, 2.307105541229248, 1020, 2.268625259399414, 1020]
# [3000, 0.003, 1478, 1.1132962703704834, 1478, 7.498203754425049, 1478, 5.263913154602051, 1478]
# [3000, 0.005, 1499, 1.031740427017212, 1499, 7.750374794006348, 1499, 6.098487615585327, 1499]
# [3000, 0.008, 1500, 1.2742373943328857, 1500, 11.604298114776611, 1500, 8.705273151397705, 1500]
# [3000, 0.01, 1500, 1.37418532371521, 1500, 10.662467002868652, 1500, 9.633539915084839, 1500]
# [3000, 0.05, 1500, 2.2319133281707764, 1500, 27.566731452941895, 1500, 32.68046712875366, 1500]
# [3000, 0.1, 1500, 3.0671274662017822, 1500, 40.65789270401001, 1500, 65.43306279182434, 1500]
# [3000, 0.18, 1500, 5.383186340332031, 1500, 89.54995799064636, 1500, 126.08210039138794, 1500]
# [3000, 0.25, 1500, 7.54013729095459, 1500, 116.82383966445923, 1500, 184.05621433258057, 1500]
# [3000, 0.36, 1500, 16.029949426651, 1500, 168.380117893219, 1500, 250.5087594985962, 1500]
# [3000, 0.42, 1500, 10.629196405410767, 1500, 149.63217663764954, 1500, 256.4830982685089, 1500]
